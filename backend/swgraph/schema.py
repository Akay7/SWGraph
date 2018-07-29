from graphene_django import DjangoObjectType
import graphene

from film.models import Film as FilmModel
from people.models import People as PeopleModel
from planet.models import Planet as PlanetModel
from species.models import Species as SpeciesModel
from transport.models import (
    Transport as TransportModel,
    Starship as StarshipModel,
    Vehicle as VehicleModel
)


class FilmType(DjangoObjectType):
    class Meta:
        model = FilmModel


class PeopleType(DjangoObjectType):
    class Meta:
        model = PeopleModel


class PlanetType(DjangoObjectType):
    class Meta:
        model = PlanetModel


class SpeciesType(DjangoObjectType):
    class Meta:
        model = SpeciesModel


class TransportType(DjangoObjectType):
    class Meta:
        model = TransportModel


class StarshipType(DjangoObjectType):
    class Meta:
        model = StarshipModel


class VehicleType(DjangoObjectType):
    class Meta:
        model = VehicleModel


class Query(graphene.ObjectType):
    film = graphene.List(FilmType)
    people = graphene.List(PeopleType)
    planet = graphene.List(PlanetType)
    species = graphene.List(SpeciesType)
    transport = graphene.List(TransportType)
    starship = graphene.List(StarshipType)
    vehicle = graphene.List(VehicleType)

    def resolve_film(self, info):
        return FilmModel.objects.all()

    def resolve_people(self, info):
        return PeopleModel.objects.all()

    def resolve_planet(self, info):
        return PlanetModel.objects.all()

    def resolve_species(self, info):
        return SpeciesModel.objects.all()

    def resolve_transport(self, info):
        return TransportModel.objects.all()

    def resolve_starship(self, info):
        return StarshipModel.objects.all()

    def resolve_vehicle(self, info):
        return VehicleModel.objects.all()


schema = graphene.Schema(query=Query)
