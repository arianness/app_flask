
import unittest
import json
import os
from BANK.ext.database import db
from BANK.app import create_app
from BANK.modules import create_password
from BANK.models import Users, Roles


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.app = app.test_client()
        # db.init_app(app)
        app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_user(self):
        u = Users(name='jhon', email='jhon@example.com', role_id=1, password="")
        password = create_password()
        u.password = password
        db.session.add(u)
        db.session.commit()
        return password

    def create_role(self):
        role = Roles(description='description jhon role')
        db.session.add(role)
        db.session.commit()

    def get_header(self):
        return {
            'Accept': '*/*',
            'User-Agent': 'request',
            "Content-Type": "application/json",
            }

    def test_database(self):
        test = os.path.exists(os.path.join(BASE_DIR, 'test.db'))
        self.assertTrue(test)

    def test_index(self):
        test = self.app.test_client(self)
        response = test.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Challenge API')

    def test_create_role(self):
        self.create_role()
        role = Roles.query.filter_by(id=1).first()
        assert role.description == 'description jhon role'

    def test_create_user(self):
        password = self.create_user()
        user = Users.query.filter_by(id=1).first()
        assert user.name == 'jhon'
        assert user.password == password

    def test_api_get_user_role(self):
        self.create_role()
        self.create_user()
        user = db.session.query(Users.id).order_by(Users.id.desc()).first()
        response = self.app.get('/users/' + str(user.id))
        data = json.loads(response.get_data(as_text=True))
        data = data['msg']
        if 'description' in data.keys():
            data = data['description']
        self.assertEqual(data, 'description jhon role')

    def test_api_get_user_role_not_found(self):
        response = self.app.get('/users/222')
        data = json.loads(response.get_data(as_text=True))
        data = data['msg']
        if 'description' in data.keys():
            data = data['description']
        else:
            data = data['msg']
        self.assertEqual(data, 'Não encontrou resultado para este usuário.')

    def test_api_post_create_user(self):
        self.create_role()
        self.create_user()
        headers = self.get_header()
        data = {
                "name": "jane",
                "email": "jane@gmail.com",
                "password": "aAJsjud",
                "role": "description jane role"
            }
        data = json.dumps(data)
        response = self.app.post('/users', headers=headers, data=data)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_api_post_create_user_without_password(self):
        headers = self.get_header()
        data = {
                "name": "jane",
                "email": "jane@gmail.com",
                "role": "description jane role"
            }
        data = json.dumps(data)
        response = self.app.post('/users', headers=headers, data=data)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_api_post_create_user_without_role(self):
        headers = self.get_header()
        data = {
                "name": "jane",
                "email": "jane@gmail.com",
                "password": "aAJsjud",
            }
        data = json.dumps(data)
        response = self.app.post('/users', headers=headers, data=data)
        response = response.get_json()
        response = response['status']
        self.assertEqual(response, 'Não foi possivel criar o usuário.')


if __name__ == '__main__':
    unittest.main()
