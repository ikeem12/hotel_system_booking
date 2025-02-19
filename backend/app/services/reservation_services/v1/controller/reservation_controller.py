from flask_restful import Resource
from pydantic import ValidationError
from flask import request, make_response

from ..schema.reservation_schema import ReservationSchema
from app.core.response import ResponseHandler
from app.core.error_handler import handle_validation_error

class ReservationResource(Resource):
    def get(self):
        return {'reservations': 'GET'}

    def post(self):
        try:
            reservation = ReservationSchema(**request.json)
            return make_response(ResponseHandler.success_response(), 201)
        except ValidationError as e:
            return handle_validation_error(e.errors(include_url=False,include_context=False,include_input=False))