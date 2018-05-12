from flask_restful import Resource

from Middleware.Auth import auth2
from Model.GroupCourse import GroupCourse


class List(Resource):
    @auth2.login_required
    def get(self):
        groupcourses = GroupCourse.select()
        ls = [
            dict(
                id=d.id,
                group_number=d.group_number,
                term=d.term,
                Course_id=dict(
                    id=d.Course_id.id,
                    presentation=d.Course_id.presentation,
                    type=d.Course_id.type,
                    name=d.Course_id.name,
                    unit_number=d.Course_id.unit_number,
                    list_prerequisite=d.Course_id.list_prerequisite,
                ),
                professor_id=dict(
                    firstname=d.professor_id.firstname,
                    lastname=d.professor_id.lastname,
                ),
                Time_Course_id=dict(
                    id=d.Time_Course_id.id,
                    days=d.Time_Course_id.days,
                    time=d.Time_Course_id.time,
                    classes=d.Time_Course_id.classes,
                    rotatory=d.Time_Course_id.rotatory,
                    day_rotatory=d.Time_Course_id.day_rotatory,
                ),
                semester=d.semester,
                guest_semester=d.guest_semester,
                date_exam=d.date_exam,
                time_exam=d.time_exam,
                capacity=d.capacity,
                min_capacity=d.min_capacity
            ) for d in groupcourses
        ]
        return dict(schedule=ls)
