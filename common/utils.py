from typing import Any
from rest_framework.response import Response


def success_response(data: Any, status: int) -> Response:
    """요청 성공

    요청이 성공했을 보내는 응답

    Args:
        data (Any): 전송하고자 하는 데이터
        status (int): status code

    Returns:
        Response: DRF의 Response 객체
    """
    return Response({"data": data, "message": "성공"}, status)


def error_response(error: Any, status: int) -> Response:
    """error_response 요청 실패

    요청이 실패했을때 보내는 응답

    Args:
        error (Any): error 객체
        status (int): status code

    Returns:
        Response: DRF의 Response 객체
    """
    return Response(error, status)
