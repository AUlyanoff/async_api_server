# Драйвер подключения к базе данных
## Описание

Основан на библиотеке асинхронного интерфейса выполнения запросов **asyncpg**

## Структура

```
parser
   |-entities.py
   |-parse_database.py
   |-parse_dbapi.py
   |-parser.py

procedures
   |-__init__.jinja2
   |-__init__.py
   |-base_procedure.py
   |-proc.signature.pickle
   |-procedure_list.jinja2
   |-procedure_list.py

core.py
exceptions.py
```

[parser.py](parser%2Fparser.py) - модуль получения параметров хранимых процедур из базы данных и DbAPI.  
Модуль [parser.py](parser%2Fparser.py) получает информацию о выходных/выходных параметрах ХП и их типах.  
`Далее будет реализована проверка сигнатур ХП относительно предыдущего состояния`  
Модуль [parse_dbapi.py](parser%2Fparse_dbapi.py) также получает информацию о составе полей процедур + состав ResultSet's 
(RefCursor)  

[parser.py](parser%2Fparser.py) запускает обе функции, формирует список процедур со всеми нужными параметрами и 
генерирует Python код используя шаблон [procedure_list.jinja2](procedures%2Fprocedure_list.jinja2) 
и файл [procedure_list.py](procedures%2Fprocedure_list.py)  

Все классы процедур наследуют интерфейс базового класса процедуры, определенного в 
[base_procedure.py](procedures%2Fbase_procedure.py), и являются т.н. _Callable Instances_ что 
позволяет использовать их как функции.

Логика взаимодействия непосредственно с базой данных находится в модуле [core.py](core.py)

Объект базы данных инициализируется в [__init__.py](__init__.py)

## Обновление списка и состава процедур

python3 parser.py

## Использование

### Инициализация
```
from database import db

db.set_config() # передача объекта конфигурации БД
await db.perform_connection() # установка соединения с БД, создание пула конектов
```

### вызовы процедур
#### 1. StandAlone
```python
from database import db

async with db.get_connection_from_pool() as conn:
    result, refcursor = db.sp_profile_imdm_get(conn, 102)
```
При нормальном завершении ХП commit вызывается автоматически.
Откатить можно так:
```python
from database import db

conn = db.connection_pool_dependency()
tr = conn.transaction()
tr.start()
try:
    result, refcursor = await db.sp_profile_imdm_get(conn, 102)
except Exception:
    tr.rollback()
tr.close()
conn.close()
```
Откатить можно и внутри контекстного менеджера.</br> 
Так же допустимо контекстный менеджер расположить внутри try-except.
#### 2. При использовании FastAPI
```python
from database import db, DBConnection
from fastapi import Request

@ios_router.put("/mdm")
async def mdm(request: Request, conn: DBConnection):
    result, refcursor = await db.sp_kit_imdm_get_next_command_for_ios(conn, 102)
```

**Важная ремарка**
В данной реализации аргументы процедур являются чисто позиционными  
Это означает что их нельзя передавать как keyword:
```python
# !!! НЕ СРАБОТАЕТ
result, refcursor = await db.sp_kit_imdm_get_next_command_for_ios(connection=conn, kit_id=102)
```

#### 3. Результаты
Процедуры, всегда возвращают tuple, в котором 0 значение - выходные параметры процедуры,  
а последующие - массивы значений ResultSets (если они есть)

Если у процедуры нет ResultSet, правильныое получение параметров выглядит следующим образом:
```python
res, = await db.sp_monitor_imdm_get_device_token(conn, 102)
```
У данной процедуры ResultSets отсутствуют, но запятая после res нужна чтобы в него попали параметры процедуры.  
Если у процедуры есть ResultSets, вызывать её нужно распаковав Tuple по числу её ResultSets
```python
result, refcursor = await db.sp_kit_imdm_get_next_command_for_ios(conn, 102)

res, ws, uids, policy = await db.sp_profile_imdm_get_ios_monitor_profile(conn, 102)
```
Например у первой процедуры ResultSet один, а у второй - 3  
P.S вторая процедура на данный момент единственная из процедур imdm, у которой больше одного ResultSet

Первый аргумент всегда является объектом `TRecord`  
`TRecord` - модифицированная версия объекта `asyncpg.Record`, ведущий себя также, как `NamedTuple`, то есть
позволяющий получать значения через `getattr` или оператор `.`

Последующие аргументы (если есть) - `list[TRecord]`

#### 4. Подсказки
Драйвер реализован таким образом, чтобы в нём работали TypeHints Pycharm, таким образом при вызове процедуры PyCharm
подсказывает имена параметров процедур, а также проверяет типы входных и выходных параметров, а также типы курсоров.

Фактически это - хак, который стал возможен благодаря динамической типизации  
Процедуры аннотированы с использованием `NamedTuple`, но при вызове ничего в него не конвертируют, а возвращают объекты
TRecord, которые ведут себя также, как `NamedTuple`.  
Это сделано для того, чтобы типы DBApi никак не влияли на работу самого драйвера, таким образом, если в DBApi содержится
ошибка в типах параметров, а БД возвращает всё верно, ничего не сломается




