# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_leaderboard_get_stat_groups_by_profile_ids import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_LEADERBOARD_GET_STAT_GROUPS_BY_PROFILE_IDS