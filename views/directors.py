from flask_restx import Resource, Namespace
from setup_db import db
from models import Director, DirectorSchema
from flask import abort

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(Director).all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:bid>')
class DirectorView(Resource):
    def get(self, bid):
        director = db.session.query(Director).get(bid)
        if not director:
            abort(404)
        return director_schema.dump(director), 200






