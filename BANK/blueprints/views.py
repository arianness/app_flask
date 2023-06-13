from flask import Flask, make_response, jsonify, request
from BANK.ext.database import db
from BANK.models import Users, Roles
from BANK.modules import create_password
import logging

def init_app(app):
    logging.basicConfig(filename='../app.log',
                        filemode='w')

    # Endpoint: return the user's role
    @app.route('/users/<user_id>', methods=['GET'])
    def get_role_user(user_id=0):
        try:
            filter = \
                db.session.query(Roles.description, Users.created_at).join(Users).filter(Users.id == user_id).first()
            if filter:
                msg = {"description": filter.description}
            else:
                msg = {"msg": "Não encontrou resultado para este usuário."}
        except Exception as error:
            logging.error('{}'.format(error))
            msg = {"msg": "Houve algum problema na busca: " + str(error)}

        return make_response(
            jsonify({"msg": msg})
        )


    # Endpoint: create new user
    @app.route('/users', methods=['POST'])
    def create_user():
        u = request.json
        if not 'password' in u.keys():
            u['password'] = create_password()
        try:
            db.session.add(Roles(u['role']))
            db.session.commit()
            role_id = db.session.query(Roles.id).order_by(Roles.id.desc()).first()
            role_id = int(role_id.id)
            db.session.add(Users(u['name'], u['email'], u['password'], role_id))
            db.session.commit()
            db.session.close()
            msg = {"status": "criado com sucesso!", "msg": u}
        except Exception as error:
            logging.error('{}'.format(error))
            msg = {"status": "Não foi possivel criar o usuário.", "error": str(error)}
        return make_response(
            jsonify(msg)
        )


    @app.route('/')
    def index():
        return 'Challenge API'