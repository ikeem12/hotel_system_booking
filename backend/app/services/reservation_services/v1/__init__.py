from flask import Blueprint
from flask_restful import Api

bp_rsv_svc_v1 = Blueprint('reservation_services_v1', __name__)
api = Api(bp_rsv_svc_v1)

from .controllers.reservation_controller import ReservationResource

api.add_resource(ReservationResource, '/reservations')