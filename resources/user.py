from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegistrater(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")

    parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")

    def post(self):
        data = UserRegistrater.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User was created successfullly.'}, 201
