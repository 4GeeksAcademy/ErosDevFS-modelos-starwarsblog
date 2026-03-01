from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    subscription: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    last_payment: Mapped[str] = mapped_column(nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="users")
    learnmore: Mapped[List["LearnMore"]] = relationship(back_populates="users")


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "subscription": self.subscription,
            "last_payment": self.last_payment
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    eyes_color: Mapped[str] = mapped_column(nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="characters")
    learnmore: Mapped[List["LearnMore"]] = relationship(back_populates="characters")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eyes_color": self.eyes_color
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    
    favorites: Mapped[List["Favorites"]] = relationship(back_populates="planets")
    learnmore: Mapped[List["LearnMore"]] = relationship(back_populates="planets")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain
            # do not serialize the password, its a security breach
        }
    

class Vehicles(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    manufacturer: Mapped[str] = mapped_column(nullable=False)
    
    favorites: Mapped[List["Favorites"]] = relationship(back_populates="vehicles")
    learnmore: Mapped[List["LearnMore"]] = relationship(back_populates="vehicles")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer
            # do not serialize the password, its a security breach
        }
    


class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    id_characters: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=False)
    id_planets: Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=False)
    id_vehicles: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["Users"] = relationship(back_populates="favorites")

    characters_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    characters: Mapped["Characters"] = relationship(back_populates="favorites")

    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    planets: Mapped["Planets"] = relationship(back_populates="favorites")

    vehicles_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"))
    vehicles: Mapped["Vehicles"] = relationship(back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "type": self.type,
            "id_characters": self.id_characters,
            "id_planets": self.id_planets,
            "id_vehicles": self.id_vehicles
            # do not serialize the password, its a security breach
        }
    

class LearnMore(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_characters: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=False)
    id_planets: Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=False)
    id_vehicles: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)


    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["Users"] = relationship(back_populates="learnmore")

    characters_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    characters: Mapped["Characters"] = relationship(back_populates="learnmore")

    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    planets: Mapped["Planets"] = relationship(back_populates="learnmore")

    vehicles_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"))
    vehicles: Mapped["Vehicles"] = relationship(back_populates="learnmore")

    def serialize(self):
        return {
            "id": self.id,
            "id_characters": self.id_characters,
            "id_planets": self.id_planets,
            "id_vehicles": self.id_vehicles,
            "description": self.description
            # do not serialize the password, its a security breach
        }