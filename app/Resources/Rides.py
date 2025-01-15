import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.Schema.Rides import RideSchema
from app.Models.Rides import Ride
from app.Models.db import db

blp = Blueprint("Rides", "rides", description="Operations on rides")

@blp.route("/rides")
class RidesResource(MethodView):
    @blp.response(200, RideSchema(many=True))
    def get(self):
        return Ride.query.all()

    @blp.arguments(RideSchema)
    @blp.response(201, RideSchema)
    def post(self, ride_data):
        ride = Ride(id=str(uuid.uuid4()), **ride_data)
        db.session.add(ride)
        db.session.commit()
        return ride

@blp.route("/rides/<string:ride_id>")
class RideResource(MethodView):
    @blp.response(200, RideSchema)
    def get(self, ride_id):
        ride = Ride.query.get_or_404(ride_id)
        return ride

    def delete(self, ride_id):
        ride = Ride.query.get_or_404(ride_id)
        db.session.delete(ride)
        db.session.commit()
        return {"message": "Ride deleted."}
