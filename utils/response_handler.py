# utils/response_handler.py
from fastapi.responses import JSONResponse
from fastapi import status


class ResponseHandler:
    @staticmethod
    def ok(data=None, message="Success"):
        return JSONResponse(
            content={"message": message, "data": data},
            status_code=status.HTTP_200_OK
        )

    @staticmethod
    def created(data=None, message="Resource created"):
        return JSONResponse(
            content={"message": message, "data": data},
            status_code=status.HTTP_201_CREATED
        )

    @staticmethod
    def accepted(data=None, message="Request accepted"):
        return JSONResponse(
            content={"message": message, "data": data},
            status_code=status.HTTP_202_ACCEPTED
        )

    @staticmethod
    def no_content(message="No content"):
        return JSONResponse(
            content={"message": message},
            status_code=status.HTTP_204_NO_CONTENT
        )

    # ---------- Client Errors ----------
    @staticmethod
    def bad_request(message="Bad request"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    @staticmethod
    def unauthorized(message="Unauthorized"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    @staticmethod
    def forbidden(message="Forbidden"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_403_FORBIDDEN
        )

    @staticmethod
    def not_found(message="Not found"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_404_NOT_FOUND
        )

    @staticmethod
    def conflict(message="Conflict"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_409_CONFLICT
        )

    @staticmethod
    def unprocessable_entity(message="Unprocessable entity"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    # ---------- Server Errors ----------
    @staticmethod
    def internal_error(message="Internal server error"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    @staticmethod
    def not_implemented(message="Not implemented"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_501_NOT_IMPLEMENTED
        )

    @staticmethod
    def bad_gateway(message="Bad gateway"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_502_BAD_GATEWAY
        )

    @staticmethod
    def service_unavailable(message="Service unavailable"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    @staticmethod
    def gateway_timeout(message="Gateway timeout"):
        return JSONResponse(
            content={"error": message},
            status_code=status.HTTP_504_GATEWAY_TIMEOUT
        )
