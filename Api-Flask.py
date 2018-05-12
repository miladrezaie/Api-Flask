from flask import Flask
from flask_restful import Api

from Controller import ChoiceCourseController, CourseController, LoginController, GroupCourseController

app = Flask(__name__)
api = Api(app)

api.add_resource(ChoiceCourseController.List, '/choicecourses', endpoint='choice_course_list')
api.add_resource(CourseController.List, '/list')
api.add_resource(LoginController.Login, '/login')

# api.add_resource(ChoiceCourseController.Delete, '/choicecourses', endpoint='delete_choice_courses')
api.add_resource(ChoiceCourseController.Store, '/choicecourse', endpoint='create_choice_course')
api.add_resource(ChoiceCourseController.Destroy, '/choicecourses/<int:choice_course_id>',endpoint='delete_choice_course')
api.add_resource(GroupCourseController.List, '/schedule', endpoint='schedule')




# api.add_resource(ChoiceCourseController, '/choicecourses', endpoint='choice_course_list')
# api.add_resource(ChoiceCourseController, '/choicecour')
# api.add_resource(ChoiceController, '/sas')
# api.add_resource(ChoiceController, '/a')
# api.add_resource(ChoiceController, '/dars')
# api.add_resource(ChoiceController, '/bb')


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, True)
    # app.run("127.0.0.1", 3000, True)
    #run True Debuge