# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_party_send_match_chat import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_PARTY_SEND_MATCH_CHAT
