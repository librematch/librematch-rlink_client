# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_chat_get_offline_messages import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_CHAT_GET_OFFLINE_MESSAGES