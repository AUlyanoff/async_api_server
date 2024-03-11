# -*- coding: utf-8 -*-
import json
import logging

import jsonschema
from fastapi import Request, HTTPException

from utils.json_utils import isjson
# from config_save import config
from utils.log.utils import trunc_str

logger = logging.getLogger(__name__)


class CheckJsonSchema:
    """Зависимость-валидатор запроса по json схеме
    Использовать в декораторе роута в массиве dependencies:
    dependencies=[Depends(CheckJsonSchema(schema_path=schema_path))]
    """
    def __init__(self, schema_path: str):
        """Передача параметров в зависимость
        :param schema_path: путь к json схеме
        """
        self.schema_path = schema_path

    async def __call__(self, req: Request) -> None:
        """Валидация запроса по json схеме
        :param req: запрос (передаёт FastApi)
        """
        api_path = req.url.path

        if not config.sowa:
            logger.debug("\n\t<~\t\tCheckJsonSchema - SOWA is OFF, validation skipped, ended")
            return

        body = await req.body()

        if not isjson(body):
            msg, status = "Request must be empty list [] or correct json", 420
            logger.error(f"\n\t<~\t\tCheckJsonSchema, error for API {api_path},HTTP={status}, {msg} - ended")
            raise HTTPException(status_code=status, detail={"error": msg})

        try:
            with open(self.schema_path, 'r', encoding='utf8') as schema_file:
                jsonschema.validate(await req.json(), json.load(schema_file))  # валидатор стороннего разработчика
            logger.debug("\n\t<~\t\tCheckJsonSchema (" + self.__call__.__doc__.split('\n')[0] + ") "
                         f"for {api_path} - ok, ended")
            return

        except jsonschema.ValidationError as err:
            msg, status = "Invalid request. Validation by JSON schema completed unsuccessfully", 400
            logger.error("\n\t<~\t\tCheckJsonSchema (" + self.__call__.__doc__.split('\n')[0] +
                         f") HTTP={status}, {msg}, ended"
                         f"\n\t\t\t" + trunc_str("Validate error: " +
                                                 str(err.validator) + " " +
                                                 str(list(err.absolute_path)[:]) + " " +
                                                 str(err.message) + " in " +
                                                 str(err.instance), delimiter="\n\t\t\t") +
                         f"\n\t\t\tJSON-schema {self.schema_path}")
            raise HTTPException(status_code=status, detail={"error": msg})

        except jsonschema.SchemaError as err:
            msg, status = "Request ignored. Validation skipped", 400
            logger.error(f"\n\t<~\t\tCheckJsonSchema HTTP={status}, {msg}, ended "
                         f"\nError in JSON-schema: {self.schema_path}, {err}")
            raise HTTPException(status_code=status, detail={"error": msg})

        except Exception as err:
            msg, status = "(validator error) json is not valid with json schema", 400
            logger.error(f"\n\t<~\t\tCheckJsonSchema HTTP={status}, {msg}, ended "
                         f"\nValidator crashed: {err}"
                         f"\n\tjson\t\t" + trunc_str(str(req.json()), delimiter="\n\t\t\t"))
            raise HTTPException(status_code=status, detail={"error": msg})
