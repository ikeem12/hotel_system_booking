from flask import make_response, jsonify

from .response import ResponseHandler

def register_error_handlers(app):

    @app.errorhandler(404)
    def handle_not_founnd_endpoint(error):
        response = ResponseHandler.error_response(
            type_error="NotFoundEnpoind",
            message="Recurso no encontrado"
        )
        return make_response(response, 404)



    @app.errorhandler(500)
    def handle_500_error(error):
        response = ResponseHandler.error_response(
            type_error="InternalServerError",
            message="Error interno del servidor"
        )
        return make_response(response, 500)



def handle_validation_error(error):
        response = ResponseHandler.error_response(
            type_error="ValidationError",
            message= [err["msg"] for err in error],
            details= [err["loc"] for err in error]
        )
        return make_response(response, 400)