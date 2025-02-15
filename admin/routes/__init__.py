from flask_restful import Api
from awards import AwardListResource, AwardResource, AwardUpdateResource
from event import EventResource, EventListResource, EventUpdateResource
from municipalities import MunicipalityListResource, MunicipalityResource, MunicipalityUpdateResource
from fighter import FighterResource, FighterListResource, FighterUpdateResource
from users import UserListResource, UserResource
from user_logs import UserLogListResource, UserLogResource

def register_api(api: Api):
    api.add_resource(AwardListResource, "/awards")
    api.add_resource(AwardResource, "/awards/<int:award_id>")
    api.add_resource(AwardUpdateResource, "/awards/<int:award_id>/update")
    api.add_resource(EventListResource, "/events")
    api.add_resource(EventResource, "/events/<int:event_id>")
    api.add_resource(EventUpdateResource, "/events/<int:event_id>/update")
    api.add_resource(MunicipalityListResource, "/municipalities")
    api.add_resource(MunicipalityResource, "/municipalities/<int:municipality_id>")
    api.add_resource(MunicipalityUpdateResource, "/municipalities/<int:municipality_id>/update")
    api.add_resource(FighterListResource, "/fighters")
    api.add_resource(FighterResource, "/fighters/<int:fighter_id>")
    api.add_resource(FighterUpdateResource, "/fighters/<int:fighter_id>/update")
    api.add_resource(UserListResource, "/users")
    api.add_resource(UserResource, "/users/<int:user_id>")
    api.add_resource(UserLogListResource, "/user_logs")
    api.add_resource(UserLogResource, "/user_logs/<int:log_id>")