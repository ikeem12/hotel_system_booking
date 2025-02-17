from flask_restful import Resource

class ReservationResource(Resource):
    def get(self):
        return {'reservations': 'GET'}

    def post(self):
        return {'reservations': 'POST'}
