from typing import Any
from rest_framework.response import Response


def SuccessResponse(data: Any, status: int) -> Response:
    return Response({"data": data, "message": "성공"}, status)


def ErrorResponse(error: Any, status: int) -> Response:
    return Response({"error": error, "message": "실패"}, status)
