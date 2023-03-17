# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_community_event_get_available_community_events import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS