class ResponseHandler:
    @staticmethod
    def success_response(data = None):
        return {
            "success": True,
            "data": data,
            "error": None
        }


    @staticmethod
    def error_response(type_error, message, details=None):
        return {
            "success": False,
            "data": None,
            "error": {
                "type": type_error,
                "message": message,
                "details": details
            }
        }