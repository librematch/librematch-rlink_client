# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_account_get_profile_property import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_ACCOUNT_GET_PROFILE_PROPERTY