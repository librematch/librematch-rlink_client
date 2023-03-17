# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_party_create_or_report_single_player import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_PARTY_CREATE_OR_REPORT_SINGLE_PLAYER
