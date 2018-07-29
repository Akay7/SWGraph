from graphene_django import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
import graphene
from graphene import relay

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
        filter_fields = {
            'title': ('exact', 'icontains',),
            'episode_id': ('exact',),
            'opening_crawl': ('exact', 'icontains',),
            'director': ('exact', 'icontains',),
            'producer': ('exact', 'icontains',),
            'release_date': ('exact', 'gte', 'lte', 'gt', 'lt',),
            'characters': ('exact', 'in',),
            'planets': ('exact', 'in',),
            'starships': ('exact', 'in',),
            'vehicles': ('exact', 'in',),
            'species': ('exact', 'in',),
        }
        interfaces = (relay.Node,)


class PeopleType(DjangoObjectType):
    class Meta:
        model = PeopleModel
        filter_fields = {
            'name': ('exact', 'icontains',),
            'height': ('exact', 'gte', 'lte', 'gt', 'lt',),
            'mass': ('exact', 'gte', 'lte', 'gt', 'lt',),
            'hair_color': ('exact', 'icontains',),
            'skin_color': ('exact', 'icontains',),
            'eye_color': ('exact', 'icontains',),
            'birth_year': ('exact', 'gte', 'lte', 'gt', 'lt',),
            'gender': ('exact', 'in',),
            'homeworld': ('exact', 'in',),
        }
        interfaces = (relay.Node,)


class PlanetType(DjangoObjectType):
    class Meta:
        model = PlanetModel
        filter_fields = {
            'name': ('exact', 'icontains',),
            'rotation_period': ('exact',),
            'orbital_period': ('exact',),
            'diameter': ('exact', 'icontains',),
            'climate': ('exact', 'icontains',),
            'gravity': ('exact', 'icontains',),
            'terrain': ('exact', 'icontains',),
            'surface_water': ('exact', 'icontains',),
            'population': ('exact', 'icontains',),
        }
        interfaces = (relay.Node,)


class SpeciesType(DjangoObjectType):
    class Meta:
        model = SpeciesModel
        filter_fields = {
            'name': ('exact', 'icontains',),
            'classification': ('exact', 'icontains',),
            'designation': ('exact', 'icontains',),
            'average_height': ('exact', 'gte', 'lte', 'gt', 'lt',),
            'skin_colors': ('exact', 'icontains',),
            'hair_colors': ('exact', 'icontains',),
            'eye_colors': ('exact', 'icontains',),
            'average_lifespan': ('exact', 'icontains',),
            'homeworld': ('exact',),
            'language': ('exact',),
            'people': ('exact',),
        }
        interfaces = (relay.Node,)


class TransportType(DjangoObjectType):
    class Meta:
        model = TransportModel
        interfaces = (relay.Node,)


class StarshipType(DjangoObjectType):
    class Meta:
        model = StarshipModel
        interfaces = (relay.Node,)


class VehicleType(DjangoObjectType):
    class Meta:
        model = VehicleModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    film = relay.Node.Field(FilmType)
    filmAll = DjangoFilterConnectionField(FilmType)
    people = relay.Node.Field(PeopleType)
    planet = relay.Node.Field(PlanetType)
    species = relay.Node.Field(SpeciesType)
    transport = relay.Node.Field(TransportType)
    starship = relay.Node.Field(StarshipType)
    vehicle = relay.Node.Field(VehicleType)

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
