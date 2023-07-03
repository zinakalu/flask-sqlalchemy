#Define the structure and behaviour(attributes) of the data that'll be stored in the database
#Each model class represents a table in the database, and the attributes of the class correspond to the columns of the table
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin #an instance of the Owner model(i.e a owner) is a python object that holds information about a particular user. But it can't be directly stored in a database or
#sent over a network, we need to serialize the owner; converting it into a format(i.e dictionaries or JSON) that can be easily sotred or transmitted


#create an instance of the SQLAlchemy class
db = SQLAlchemy()

# class Owner(db.Model):
#     __tablename__ = 'owners'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True)

#     pets = db.relationship('Pet', backref='owner')


#     def __repr__(self):
#         return f'<Pet Owner {self.name}>' 
class Owner(db.Model, SerializerMixin): #reconfigure each of our models to inherit from SerializerMixin
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    pets = db.relationship('Pet', backref='owner')

    serialize_rules = ('-pets',) #exlcudes the pets field when serializing an Owner object


    def __repr__(self):
        return f'<Pet Owner {self.name}>' 




# class Pet(db.Model):
#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     species = db.Column(db.String)

#     owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

#     def __repr__(self):
#         return f'<Pet {self.name}, {self.species}>'

class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    serialize_rules = ('-owner.pets',) #when a Pet object is serialized, this excludes the pets field of the related Owner object. This helps prevent a recursion loop. Used to specify fields that should be excluded from serialization

    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'


# owner = Owner(name='John Doe')
# db.session.add(owner)
# db.session.commit()

# pet = Pet(name="Neil", species="Husky")
# db.session.add(pet) #the variable name should match the instance created
# db.session.commit()

#IN FLASK SHELL:
#1) from models import *
#2) o1 = Owner.query.first() -> retireives the first instance of the Owner object from the database
#3) o1.to_dict() -> this serializes the Owner instance into a dictionary representation. {'name': 'Alexis Gonzalez', 'id': 1} -> the serialized Owner instance is returned as a dictionary with the keys 'name' and 'id'. 

#to_dict(): this method is provided by the SerializerMixin and can be called on an instance of the model class. It converts the model object and its attributes into a dictionary representation. Each attribute
#of the model becomes a key-value pair in the dictionary

#to_json(): this method is also provided by the SerializerMixin and can be called on an instance of the model class (doesn't have to be). It converts the model object into a JSON string representation. The JSON
#string will contain the serialized attributes of the model
