from flask_restful import Resource
from Middleware.Auth import auth2
from Model.Course import Course


class List(Resource):
    @auth2.login_required
    def get(self):
        courses = Course.select()
        ls = [dict(
            id=c.id,
            presentation=c.presentation,
            type=c.type,
            status_prerequisite=c.status_prerequisite,
            name=c.name,
            unit_number=c.unit_number,
            price=c.price,
            list_prerequisite=c.list_prerequisite,
        ) for c in courses]
        return dict(courses=ls)
