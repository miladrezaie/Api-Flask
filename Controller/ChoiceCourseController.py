from flask import g, request
from flask_restful import Resource

from Middleware.Auth import auth2
from Model.BaseModel import BaseModel
from Model.ChoiceCourse import ChoiceCourse


class List(Resource):
    @auth2.login_required
    def get(self):
        choice_courses = ChoiceCourse.select().where(ChoiceCourse.Student_student_number_id == g.user.student_number)
        ls = [
            dict(
                id=choice_course.id,
                Student_student_number=choice_course.Student_student_number_id.student_number,
                status=choice_course.status,
                status_pay=choice_course.status_pay,
                score=choice_course.score,
                semeter=choice_course.semeter,
            ) for choice_course in choice_courses
        ]
        return dict(courses=ls)


class Store(Resource):
    @auth2.login_required
    def post(self):
        request_json = request.get_json()
        choice_course = ChoiceCourse()
        # choicecourse.id = request_json['id']
        choice_course.Student_student_number_id = request_json['Student_student_number_id']
        choice_course.status = request_json['status']
        choice_course.status_pay = request_json['status_pay']
        choice_course.score = request_json['score']
        choice_course.semeter = request_json['semeter']
        choice_course.Group_Course_code_course_id = request_json['Group_Course_code_course_id']
        choice_course.save()
        return dict(
            status='sucessfull save'
        )


# class Delete(Resource):
#     @auth2.login_required
#     def delete(self):
#         ChoiceCourse.delete().where(ChoiceCourse.Student_student_number_id == g.user.student_number).execute()
#         return dict(
#             status='deleted sucessfull'
#         )


class Destroy(Resource):
    @auth2.login_required
    def delete(self, choice_course_id):
        try:
            choice_course = ChoiceCourse.get(id=choice_course_id)
        except ChoiceCourse.DoesNotExist:
            return None, 404
        choice_course.delete_instance()
        return dict(status='deleted sucessfull', id=choice_course_id ), 200
