from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Owner, Pet


#creates an instance of Flask class
app = Flask(__name__)

#Flask-SQLAlchemy uses the connection string to connect to the database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///furryfriends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


#create an instance of the migrate class
migrate= Migrate(app,db)



#configues this specific Flask application to use SQLAlchemy for database operations
db.init_app(app)


@app.route('/')
def index():
    response = make_response(
        '<h1>Welcome to the pet/owner directory!</h1>',
        200
    )
    return response


#how to...
@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()

    #if user puts into the url an id or username that doesn't exist
    if not pet:
        response_body = '<h1> 404 pet not found </h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f''' 
        <h1> Information for pet named: {pet.name} </h1>
        <h2> Pet Species is {pet.species} </h2>
        <h2> Pet Owner is {pet.owner.name} </h2>
    '''

    response = make_response(response_body, 200)
    return response



@app.route('/owners/<int:id>')
def owner_by_id(id):
    owner = Owner.query.filter(Owner.id == id).first()

    if not owner:
        response_body = '<h1>404 owner not found</h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f'<h1>Information for {owner.name}</h1>'

    pets = [pet for pet in owner.pets]

    if not pets: 
        response_body += f'<h2>Has no pets at this time.</h2>'

    else:
        for pet in pets:
            response_body += f'<h2> Has pet {pet.species} named {pet.name}. </h2>'
        
        response = make_response(response_body, 200)

        return response



#can start the server by running python app.py



if __name__ == '__main__':
    app.run(port=5555, debug=True)

