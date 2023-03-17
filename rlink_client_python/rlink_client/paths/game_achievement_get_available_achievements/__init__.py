# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_achievement_get_available_achievements import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS