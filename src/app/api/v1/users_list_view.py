import logging
from fastapi.responses import JSONResponse
from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncConnection
from database.core import get_conn


from app.api.v1.routes import v1
from app.api.v1.users_list_serv import get_users_list, serialize

logger = logging.getLogger(__name__)


@v1.post("/users/list")
async def users_list(request: Request, conn: AsyncConnection = Depends(get_conn)):
    """Возвращает список зарегистрированных юзеров"""
    api_path = request.url.path  # путь вызова API
    logger.debug(f"{api_path} ({users_list.__doc__}) started...")

    table_result = await get_users_list(conn)
    dict_result = serialize(table_result)

    response, status = {"data": dict_result}, 200
    _ll = f"{api_path}, HTTP={status} ended\n\tresponse={response}"
    logger.info(_ll) if status == 200 else logger.error(_ll)

    return JSONResponse(response, status_code=status)
