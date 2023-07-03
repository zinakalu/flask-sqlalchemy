#Here, we populate the database with data

from faker import Faker
from sqlalchemy.sql import func

from app import app
from models import db, Owner, Pet

#create an instance of the Faker class
fake = Faker()

with app.app_context():
    Pet.query.delete() #here we delete all the data we put when we used flask shell.
    Owner.query.delete() #initially we're starting the database off on a clean slate

    #Create owners
    for _ in range(10):
        owner = Owner(name=fake.name())
        db.session.add(owner)

    #Create pets
    for _ in range(20):
        pet = Pet(name=fake.name(), species=fake.random_element(['Chihuahua', 'German Shepherd', 'Golden Retriever', 'Poodle', 'Labrador Retriever', 'French Bulldog']))
        owner = Owner.query.order_by(func.random()).first() #get a random owner
        pet.owner = owner

        db.session.add(pet)
        db.session.commit()


#Then in the terminal run, python seed.py to populate the database