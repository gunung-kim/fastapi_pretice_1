from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["meetings"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["meetings"], redirect_slashes=False)
# 원래는 어떤 DB를 쓰는지 url에 표기 안하는게 좋움(edgedb,mysql)


@edgedb_router.post(
    "",
    description="Create a new meeting",
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post(
    "",
    description="Create a new meeting",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


# Dict 사용
# from fastapi import APIRouter
# from app.dtos.create_meeting_response import CreateMeetingResponse
#
# edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"],
#                           redirect_slashes=False)
# mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"],
#                          redirect_slashes=False)
#
#
# @edgedb_router.post(
#     "",
#     description="meeting을 생성합니다."
# )
# async def api_create_meeting_edgedb() -> dict[str, str]:
#     return {"url_code": "abc"}
#
#
# @mysql_router.post(
#     "",
#     description="meeting을 생성합니다."
# )
# async def api_create_meeting_mysql() -> CreateMeetingResponse:
#     return CreateMeetingResponse(url_code="abc")
#
