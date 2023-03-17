# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    COMMUNITY_EXTERNAL_PROXYSTEAMUSERREQUEST = (
        "/community/external/proxysteamuserrequest"
    )
    COMMUNITY_LEADERBOARD_GET_PERSONAL_STAT = (
        "/community/leaderboard/GetPersonalStat"
    )
    COMMUNITY_LEADERBOARD_GET_RECENT_MATCH_HISTORY = (
        "/community/leaderboard/getRecentMatchHistory"
    )
    COMMUNITY_ADVERTISEMENT_FIND_ADVERTISEMENTS = (
        "/community/advertisement/findAdvertisements"
    )
    COMMUNITY_LEADERBOARD_GET_AVATAR_STAT_FOR_PROFILE = (
        "/community/leaderboard/GetAvatarStatForProfile"
    )
    COMMUNITY_ACHIEVEMENT_GET_ACHIEVEMENTS = (
        "/community/achievement/getAchievements"
    )
    COMMUNITY_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS = (
        "/community/achievement/getAvailableAchievements"
    )
    COMMUNITY_NEWS_GET_NEWS = "/community/news/getNews"
    COMMUNITY_CLAN_FIND = "/community/clan/find"
    COMMUNITY_CLAN_GET_CLAN_INFO_FULL = "/community/clan/getClanInfoFull"
    COMMUNITY_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS = (
        "/community/CommunityEvent/getAvailableCommunityEvents"
    )
    COMMUNITY_ITEM_GET_INVENTORY_BY_PROFILE_IDS = (
        "/community/item/getInventoryByProfileIDs"
    )
    COMMUNITY_LEADERBOARD_GET_AVAILABLE_LEADERBOARDS = (
        "/community/leaderboard/getAvailableLeaderboards"
    )
    COMMUNITY_LEADERBOARD_GET_LEADERBOARD2 = (
        "/community/leaderboard/getLeaderboard2"
    )
    GAME_ACCOUNT_FIND_PROFILES = "/game/account/FindProfiles"
    GAME_ACCOUNT_GET_PROFILE_NAME = "/game/account/getProfileName"
    GAME_ACCOUNT_GET_PROFILE_PROPERTY = "/game/account/getProfileProperty"
    GAME_ACCOUNT_FIND_PROFILES_BY_PLATFORM_ID = (
        "/game/account/FindProfilesByPlatformID"
    )
    GAME_ACCOUNT_SET_AVATAR_METADATA = "/game/account/setAvatarMetadata"
    GAME_ACCOUNT_SET_LANGUAGE = "/game/account/setLanguage"
    GAME_ACHIEVEMENT_GET_ACHIEVEMENTS = "/game/Achievement/getAchievements"
    GAME_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS = (
        "/game/Achievement/getAvailableAchievements"
    )
    GAME_ACHIEVEMENT_SYNC_STATS = "/game/achievement/syncStats"
    GAME_ADVERTISEMENT_FIND_OBSERVABLE_ADVERTISEMENTS = (
        "/game/advertisement/findObservableAdvertisements"
    )
    GAME_ADVERTISEMENT_FIND_ADVERTISEMENTS = (
        "/game/advertisement/findAdvertisements"
    )
    GAME_ADVERTISEMENT_GET_ADVERTISEMENTS = (
        "/game/advertisement/getAdvertisements"
    )
    GAME_ADVERTISEMENT_GET_LAN_ADVERTISEMENTS = (
        "/game/advertisement/getLanAdvertisements"
    )
    GAME_ADVERTISEMENT_HOST = "/game/advertisement/host"
    GAME_ADVERTISEMENT_UPDATE = "/game/advertisement/update"
    GAME_ADVERTISEMENT_JOIN = "/game/advertisement/join"
    GAME_ADVERTISEMENT_START_OBSERVING = "/game/advertisement/startObserving"
    GAME_ADVERTISEMENT_STOP_OBSERVING = "/game/advertisement/stopObserving"
    GAME_ADVERTISEMENT_UPDATE_PLATFORM_LOBBY_ID = (
        "/game/advertisement/updatePlatformLobbyID"
    )
    GAME_ADVERTISEMENT_UPDATE_STATE = "/game/advertisement/updateState"
    GAME_ADVERTISEMENT_UPDATE_TAGS = "/game/advertisement/updateTags"
    GAME_ADVERTISEMENT_LEAVE = "/game/advertisement/leave"
    GAME_AUTOMATCH_GET_AUTOMATCH_MAP = "/game/automatch/getAutomatchMap"
    GAME_AUTOMATCH2_GET_AUTOMATCH_MAP = "/game/automatch2/getAutomatchMap"
    GAME_AUTOMATCH2_POLLING = "/game/automatch2/polling"
    GAME_AUTOMATCH2_STOPPOLLING = "/game/automatch2/stoppolling"
    GAME_AUTOMATCH2_UPDATE_STATUS = "/game/automatch2/updateStatus"
    GAME_CHALLENGE_GET_CHALLENGE_PROGRESS = (
        "/game/Challenge/getChallengeProgress"
    )
    GAME_CHALLENGE_GET_CHALLENGE_PROGRESS_BY_PROFILE_ID = (
        "/game/Challenge/getChallengeProgressByProfileID"
    )
    GAME_CHALLENGE_GET_CHALLENGES = "/game/Challenge/getChallenges"
    GAME_CHALLENGE_UPDATE_PROGRESS_BATCHED = (
        "/game/challenge/updateProgressBatched"
    )
    GAME_CHAT_GET_CHAT_CHANNELS = "/game/chat/getChatChannels"
    GAME_CHAT_GET_OFFLINE_MESSAGES = "/game/chat/getOfflineMessages"
    GAME_CHAT_DELETE_OFFLINE_MESSAGE = "/game/chat/deleteOfflineMessage"
    GAME_CLAN_FIND = "/game/clan/find"
    GAME_CLAN_GET_CLAN = "/game/clan/getClan"
    GAME_CLAN_GET_CLAN_INFO_FULL = "/game/clan/getClanInfoFull"
    GAME_CLAN_APPLY = "/game/clan/apply"
    GAME_CLAN_DISBAND = "/game/clan/disband"
    GAME_CLAN_CREATE = "/game/clan/create"
    GAME_CLAN_UPDATE = "/game/clan/update"
    GAME_CLOUD_GET_FILE_URL = "/game/cloud/getFileURL"
    GAME_CLOUD_GET_TEMP_CREDENTIALS = "/game/cloud/getTempCredentials"
    GAME_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS = (
        "/game/CommunityEvent/getAvailableCommunityEvents"
    )
    GAME_COMMUNITY_EVENT_GET_EVENT_CHALLENGE_PROGRESS = (
        "/game/CommunityEvent/getEventChallengeProgress"
    )
    GAME_COMMUNITY_EVENT_GET_EVENT_STATS = "/game/CommunityEvent/getEventStats"
    GAME_INVITATION_CANCEL_INVITATION = "/game/invitation/cancelInvitation"
    GAME_INVITATION_EXTEND_INVITATION = "/game/invitation/extendInvitation"
    GAME_ITEM_GET_INVENTORY_BY_PROFILE_IDS = (
        "/game/item/getInventoryByProfileIDs"
    )
    GAME_ITEM_GET_ITEM_BUNDLE_ITEMS_JSON = "/game/item/getItemBundleItemsJson"
    GAME_ITEM_GET_ITEM_DEFINITIONS_JSON = "/game/item/getItemDefinitionsJson"
    GAME_ITEM_GET_ITEM_LOADOUTS = "/game/item/getItemLoadouts"
    GAME_ITEM_GET_ITEM_PRICES = "/game/item/getItemPrices"
    GAME_ITEM_GET_LEVEL_REWARDS_TABLE_JSON = (
        "/game/item/getLevelRewardsTableJson"
    )
    GAME_ITEM_GET_PERSONALIZED_SALE_ITEMS = (
        "/game/item/getPersonalizedSaleItems"
    )
    GAME_ITEM_GET_SCHEDULED_SALE_AND_ITEMS = (
        "/game/item/getScheduledSaleAndItems"
    )
    GAME_ITEM_DETACH_ITEMS = "/game/item/detachItems"
    GAME_ITEM_MOVE_CHARGES = "/game/item/moveCharges"
    GAME_ITEM_MOVE_ITEM = "/game/item/moveItem"
    GAME_ITEM_OPEN_ITEM_PACK = "/game/item/openItemPack"
    GAME_ITEM_SIGN_ITEMS = "/game/item/signItems"
    GAME_ITEM_UPDATE_ITEM_ATTRIBUTES = "/game/item/updateItemAttributes"
    GAME_LEADERBOARD_GET_RECENT_MATCH_HISTORY = (
        "/game/Leaderboard/getRecentMatchHistory"
    )
    GAME_LEADERBOARD_GET_AVAILABLE_LEADERBOARDS = (
        "/game/Leaderboard/getAvailableLeaderboards"
    )
    GAME_LEADERBOARD_GET_LEADER_BOARD = "/game/Leaderboard/getLeaderBoard"
    GAME_LEADERBOARD_GET_PARTY_STAT = "/game/Leaderboard/getPartyStat"
    GAME_LEADERBOARD_GET_PERSONAL_STAT = "/game/Leaderboard/getPersonalStat"
    GAME_LEADERBOARD_GET_RECENT_MATCH_SINGLE_PLAYER_HISTORY = (
        "/game/Leaderboard/getRecentMatchSinglePlayerHistory"
    )
    GAME_LEADERBOARD_GET_STAT_GROUPS_BY_PROFILE_IDS = (
        "/game/Leaderboard/getStatGroupsByProfileIDs"
    )
    GAME_LEADERBOARD_GET_STATS_FOR_LEADERBOARD_BY_PROFILE_NAME = (
        "/game/Leaderboard/getStatsForLeaderboardByProfileName"
    )
    GAME_LEADERBOARD_SET_AVATAR_STAT_VALUES = (
        "/game/leaderboard/setAvatarStatValues"
    )
    GAME_LOGIN_LOGOUT = "/game/login/logout"
    GAME_LOGIN_READ_SESSION = "/game/login/readSession"
    GAME_LOGIN_PLATFORMLOGIN = "/game/login/platformlogin"
    GAME_NEWS_GET_NEWS = "/game/news/getNews"
    GAME_PARTY_CREATE_OR_REPORT_SINGLE_PLAYER = (
        "/game/party/createOrReportSinglePlayer"
    )
    GAME_PARTY_REPORT_MATCH = "/game/party/reportMatch"
    GAME_PLAYERREPORT_REPORTUSER = "/game/playerreport/reportuser"
    GAME_PARTY_SEND_MATCH_CHAT = "/game/party/sendMatchChat"
    GAME_PARTY_FINALIZE_REPLAY_UPLOAD = "/game/party/finalizeReplayUpload"
    GAME_PARTY_PEER_ADD = "/game/party/peerAdd"
    GAME_PARTY_PEER_UPDATE = "/game/party/peerUpdate"
    GAME_RELATIONSHIP_GET_PRESENCE_DATA = "/game/relationship/getPresenceData"
    GAME_RELATIONSHIP_GET_RELATIONSHIPS = "/game/relationship/getRelationships"
    GAME_RELATIONSHIP_CLEAR_RELATIONSHIP = (
        "/game/relationship/clearRelationship"
    )
    GAME_RELATIONSHIP_IGNORE = "/game/relationship/ignore"
    GAME_RELATIONSHIP_SET_PRESENCE = "/game/relationship/setPresence"
    GAME_RELATIONSHIP_SET_PRESENCE_PROPERTY = (
        "/game/relationship/setPresenceProperty"
    )
