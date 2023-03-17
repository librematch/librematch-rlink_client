import typing_extensions

from rlink_client.paths import PathValues
from rlink_client.apis.paths.community_external_proxysteamuserrequest import (
    CommunityExternalProxysteamuserrequest,
)
from rlink_client.apis.paths.community_leaderboard_get_personal_stat import (
    CommunityLeaderboardGetPersonalStat,
)
from rlink_client.apis.paths.community_leaderboard_get_recent_match_history import (
    CommunityLeaderboardGetRecentMatchHistory,
)
from rlink_client.apis.paths.community_advertisement_find_advertisements import (
    CommunityAdvertisementFindAdvertisements,
)
from rlink_client.apis.paths.community_leaderboard_get_avatar_stat_for_profile import (
    CommunityLeaderboardGetAvatarStatForProfile,
)
from rlink_client.apis.paths.community_achievement_get_achievements import (
    CommunityAchievementGetAchievements,
)
from rlink_client.apis.paths.community_achievement_get_available_achievements import (
    CommunityAchievementGetAvailableAchievements,
)
from rlink_client.apis.paths.community_news_get_news import CommunityNewsGetNews
from rlink_client.apis.paths.community_clan_find import CommunityClanFind
from rlink_client.apis.paths.community_clan_get_clan_info_full import (
    CommunityClanGetClanInfoFull,
)
from rlink_client.apis.paths.community_community_event_get_available_community_events import (
    CommunityCommunityEventGetAvailableCommunityEvents,
)
from rlink_client.apis.paths.community_item_get_inventory_by_profile_ids import (
    CommunityItemGetInventoryByProfileIDs,
)
from rlink_client.apis.paths.community_leaderboard_get_available_leaderboards import (
    CommunityLeaderboardGetAvailableLeaderboards,
)
from rlink_client.apis.paths.community_leaderboard_get_leaderboard2 import (
    CommunityLeaderboardGetLeaderboard2,
)
from rlink_client.apis.paths.game_account_find_profiles import (
    GameAccountFindProfiles,
)
from rlink_client.apis.paths.game_account_get_profile_name import (
    GameAccountGetProfileName,
)
from rlink_client.apis.paths.game_account_get_profile_property import (
    GameAccountGetProfileProperty,
)
from rlink_client.apis.paths.game_account_find_profiles_by_platform_id import (
    GameAccountFindProfilesByPlatformID,
)
from rlink_client.apis.paths.game_account_set_avatar_metadata import (
    GameAccountSetAvatarMetadata,
)
from rlink_client.apis.paths.game_account_set_language import (
    GameAccountSetLanguage,
)
from rlink_client.apis.paths.game_achievement_get_achievements import (
    GameAchievementGetAchievements,
)
from rlink_client.apis.paths.game_achievement_get_available_achievements import (
    GameAchievementGetAvailableAchievements,
)
from rlink_client.apis.paths.game_achievement_sync_stats import (
    GameAchievementSyncStats,
)
from rlink_client.apis.paths.game_advertisement_find_observable_advertisements import (
    GameAdvertisementFindObservableAdvertisements,
)
from rlink_client.apis.paths.game_advertisement_find_advertisements import (
    GameAdvertisementFindAdvertisements,
)
from rlink_client.apis.paths.game_advertisement_get_advertisements import (
    GameAdvertisementGetAdvertisements,
)
from rlink_client.apis.paths.game_advertisement_get_lan_advertisements import (
    GameAdvertisementGetLanAdvertisements,
)
from rlink_client.apis.paths.game_advertisement_host import (
    GameAdvertisementHost,
)
from rlink_client.apis.paths.game_advertisement_update import (
    GameAdvertisementUpdate,
)
from rlink_client.apis.paths.game_advertisement_join import (
    GameAdvertisementJoin,
)
from rlink_client.apis.paths.game_advertisement_start_observing import (
    GameAdvertisementStartObserving,
)
from rlink_client.apis.paths.game_advertisement_stop_observing import (
    GameAdvertisementStopObserving,
)
from rlink_client.apis.paths.game_advertisement_update_platform_lobby_id import (
    GameAdvertisementUpdatePlatformLobbyID,
)
from rlink_client.apis.paths.game_advertisement_update_state import (
    GameAdvertisementUpdateState,
)
from rlink_client.apis.paths.game_advertisement_update_tags import (
    GameAdvertisementUpdateTags,
)
from rlink_client.apis.paths.game_advertisement_leave import (
    GameAdvertisementLeave,
)
from rlink_client.apis.paths.game_automatch_get_automatch_map import (
    GameAutomatchGetAutomatchMap,
)
from rlink_client.apis.paths.game_automatch2_get_automatch_map import (
    GameAutomatch2GetAutomatchMap,
)
from rlink_client.apis.paths.game_automatch2_polling import (
    GameAutomatch2Polling,
)
from rlink_client.apis.paths.game_automatch2_stoppolling import (
    GameAutomatch2Stoppolling,
)
from rlink_client.apis.paths.game_automatch2_update_status import (
    GameAutomatch2UpdateStatus,
)
from rlink_client.apis.paths.game_challenge_get_challenge_progress import (
    GameChallengeGetChallengeProgress,
)
from rlink_client.apis.paths.game_challenge_get_challenge_progress_by_profile_id import (
    GameChallengeGetChallengeProgressByProfileID,
)
from rlink_client.apis.paths.game_challenge_get_challenges import (
    GameChallengeGetChallenges,
)
from rlink_client.apis.paths.game_challenge_update_progress_batched import (
    GameChallengeUpdateProgressBatched,
)
from rlink_client.apis.paths.game_chat_get_chat_channels import (
    GameChatGetChatChannels,
)
from rlink_client.apis.paths.game_chat_get_offline_messages import (
    GameChatGetOfflineMessages,
)
from rlink_client.apis.paths.game_chat_delete_offline_message import (
    GameChatDeleteOfflineMessage,
)
from rlink_client.apis.paths.game_clan_find import GameClanFind
from rlink_client.apis.paths.game_clan_get_clan import GameClanGetClan
from rlink_client.apis.paths.game_clan_get_clan_info_full import (
    GameClanGetClanInfoFull,
)
from rlink_client.apis.paths.game_clan_apply import GameClanApply
from rlink_client.apis.paths.game_clan_disband import GameClanDisband
from rlink_client.apis.paths.game_clan_create import GameClanCreate
from rlink_client.apis.paths.game_clan_update import GameClanUpdate
from rlink_client.apis.paths.game_cloud_get_file_url import GameCloudGetFileURL
from rlink_client.apis.paths.game_cloud_get_temp_credentials import (
    GameCloudGetTempCredentials,
)
from rlink_client.apis.paths.game_community_event_get_available_community_events import (
    GameCommunityEventGetAvailableCommunityEvents,
)
from rlink_client.apis.paths.game_community_event_get_event_challenge_progress import (
    GameCommunityEventGetEventChallengeProgress,
)
from rlink_client.apis.paths.game_community_event_get_event_stats import (
    GameCommunityEventGetEventStats,
)
from rlink_client.apis.paths.game_invitation_cancel_invitation import (
    GameInvitationCancelInvitation,
)
from rlink_client.apis.paths.game_invitation_extend_invitation import (
    GameInvitationExtendInvitation,
)
from rlink_client.apis.paths.game_item_get_inventory_by_profile_ids import (
    GameItemGetInventoryByProfileIDs,
)
from rlink_client.apis.paths.game_item_get_item_bundle_items_json import (
    GameItemGetItemBundleItemsJson,
)
from rlink_client.apis.paths.game_item_get_item_definitions_json import (
    GameItemGetItemDefinitionsJson,
)
from rlink_client.apis.paths.game_item_get_item_loadouts import (
    GameItemGetItemLoadouts,
)
from rlink_client.apis.paths.game_item_get_item_prices import (
    GameItemGetItemPrices,
)
from rlink_client.apis.paths.game_item_get_level_rewards_table_json import (
    GameItemGetLevelRewardsTableJson,
)
from rlink_client.apis.paths.game_item_get_personalized_sale_items import (
    GameItemGetPersonalizedSaleItems,
)
from rlink_client.apis.paths.game_item_get_scheduled_sale_and_items import (
    GameItemGetScheduledSaleAndItems,
)
from rlink_client.apis.paths.game_item_detach_items import GameItemDetachItems
from rlink_client.apis.paths.game_item_move_charges import GameItemMoveCharges
from rlink_client.apis.paths.game_item_move_item import GameItemMoveItem
from rlink_client.apis.paths.game_item_open_item_pack import (
    GameItemOpenItemPack,
)
from rlink_client.apis.paths.game_item_sign_items import GameItemSignItems
from rlink_client.apis.paths.game_item_update_item_attributes import (
    GameItemUpdateItemAttributes,
)
from rlink_client.apis.paths.game_leaderboard_get_recent_match_history import (
    GameLeaderboardGetRecentMatchHistory,
)
from rlink_client.apis.paths.game_leaderboard_get_available_leaderboards import (
    GameLeaderboardGetAvailableLeaderboards,
)
from rlink_client.apis.paths.game_leaderboard_get_leader_board import (
    GameLeaderboardGetLeaderBoard,
)
from rlink_client.apis.paths.game_leaderboard_get_party_stat import (
    GameLeaderboardGetPartyStat,
)
from rlink_client.apis.paths.game_leaderboard_get_personal_stat import (
    GameLeaderboardGetPersonalStat,
)
from rlink_client.apis.paths.game_leaderboard_get_recent_match_single_player_history import (
    GameLeaderboardGetRecentMatchSinglePlayerHistory,
)
from rlink_client.apis.paths.game_leaderboard_get_stat_groups_by_profile_ids import (
    GameLeaderboardGetStatGroupsByProfileIDs,
)
from rlink_client.apis.paths.game_leaderboard_get_stats_for_leaderboard_by_profile_name import (
    GameLeaderboardGetStatsForLeaderboardByProfileName,
)
from rlink_client.apis.paths.game_leaderboard_set_avatar_stat_values import (
    GameLeaderboardSetAvatarStatValues,
)
from rlink_client.apis.paths.game_login_logout import GameLoginLogout
from rlink_client.apis.paths.game_login_read_session import GameLoginReadSession
from rlink_client.apis.paths.game_login_platformlogin import (
    GameLoginPlatformlogin,
)
from rlink_client.apis.paths.game_news_get_news import GameNewsGetNews
from rlink_client.apis.paths.game_party_create_or_report_single_player import (
    GamePartyCreateOrReportSinglePlayer,
)
from rlink_client.apis.paths.game_party_report_match import GamePartyReportMatch
from rlink_client.apis.paths.game_playerreport_reportuser import (
    GamePlayerreportReportuser,
)
from rlink_client.apis.paths.game_party_send_match_chat import (
    GamePartySendMatchChat,
)
from rlink_client.apis.paths.game_party_finalize_replay_upload import (
    GamePartyFinalizeReplayUpload,
)
from rlink_client.apis.paths.game_party_peer_add import GamePartyPeerAdd
from rlink_client.apis.paths.game_party_peer_update import GamePartyPeerUpdate
from rlink_client.apis.paths.game_relationship_get_presence_data import (
    GameRelationshipGetPresenceData,
)
from rlink_client.apis.paths.game_relationship_get_relationships import (
    GameRelationshipGetRelationships,
)
from rlink_client.apis.paths.game_relationship_clear_relationship import (
    GameRelationshipClearRelationship,
)
from rlink_client.apis.paths.game_relationship_ignore import (
    GameRelationshipIgnore,
)
from rlink_client.apis.paths.game_relationship_set_presence import (
    GameRelationshipSetPresence,
)
from rlink_client.apis.paths.game_relationship_set_presence_property import (
    GameRelationshipSetPresenceProperty,
)

PathToApi = typing_extensions.TypedDict(
    "PathToApi",
    {
        PathValues.COMMUNITY_EXTERNAL_PROXYSTEAMUSERREQUEST: CommunityExternalProxysteamuserrequest,
        PathValues.COMMUNITY_LEADERBOARD_GET_PERSONAL_STAT: CommunityLeaderboardGetPersonalStat,
        PathValues.COMMUNITY_LEADERBOARD_GET_RECENT_MATCH_HISTORY: CommunityLeaderboardGetRecentMatchHistory,
        PathValues.COMMUNITY_ADVERTISEMENT_FIND_ADVERTISEMENTS: CommunityAdvertisementFindAdvertisements,
        PathValues.COMMUNITY_LEADERBOARD_GET_AVATAR_STAT_FOR_PROFILE: CommunityLeaderboardGetAvatarStatForProfile,
        PathValues.COMMUNITY_ACHIEVEMENT_GET_ACHIEVEMENTS: CommunityAchievementGetAchievements,
        PathValues.COMMUNITY_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS: CommunityAchievementGetAvailableAchievements,
        PathValues.COMMUNITY_NEWS_GET_NEWS: CommunityNewsGetNews,
        PathValues.COMMUNITY_CLAN_FIND: CommunityClanFind,
        PathValues.COMMUNITY_CLAN_GET_CLAN_INFO_FULL: CommunityClanGetClanInfoFull,
        PathValues.COMMUNITY_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS: CommunityCommunityEventGetAvailableCommunityEvents,
        PathValues.COMMUNITY_ITEM_GET_INVENTORY_BY_PROFILE_IDS: CommunityItemGetInventoryByProfileIDs,
        PathValues.COMMUNITY_LEADERBOARD_GET_AVAILABLE_LEADERBOARDS: CommunityLeaderboardGetAvailableLeaderboards,
        PathValues.COMMUNITY_LEADERBOARD_GET_LEADERBOARD2: CommunityLeaderboardGetLeaderboard2,
        PathValues.GAME_ACCOUNT_FIND_PROFILES: GameAccountFindProfiles,
        PathValues.GAME_ACCOUNT_GET_PROFILE_NAME: GameAccountGetProfileName,
        PathValues.GAME_ACCOUNT_GET_PROFILE_PROPERTY: GameAccountGetProfileProperty,
        PathValues.GAME_ACCOUNT_FIND_PROFILES_BY_PLATFORM_ID: GameAccountFindProfilesByPlatformID,
        PathValues.GAME_ACCOUNT_SET_AVATAR_METADATA: GameAccountSetAvatarMetadata,
        PathValues.GAME_ACCOUNT_SET_LANGUAGE: GameAccountSetLanguage,
        PathValues.GAME_ACHIEVEMENT_GET_ACHIEVEMENTS: GameAchievementGetAchievements,
        PathValues.GAME_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS: GameAchievementGetAvailableAchievements,
        PathValues.GAME_ACHIEVEMENT_SYNC_STATS: GameAchievementSyncStats,
        PathValues.GAME_ADVERTISEMENT_FIND_OBSERVABLE_ADVERTISEMENTS: GameAdvertisementFindObservableAdvertisements,
        PathValues.GAME_ADVERTISEMENT_FIND_ADVERTISEMENTS: GameAdvertisementFindAdvertisements,
        PathValues.GAME_ADVERTISEMENT_GET_ADVERTISEMENTS: GameAdvertisementGetAdvertisements,
        PathValues.GAME_ADVERTISEMENT_GET_LAN_ADVERTISEMENTS: GameAdvertisementGetLanAdvertisements,
        PathValues.GAME_ADVERTISEMENT_HOST: GameAdvertisementHost,
        PathValues.GAME_ADVERTISEMENT_UPDATE: GameAdvertisementUpdate,
        PathValues.GAME_ADVERTISEMENT_JOIN: GameAdvertisementJoin,
        PathValues.GAME_ADVERTISEMENT_START_OBSERVING: GameAdvertisementStartObserving,
        PathValues.GAME_ADVERTISEMENT_STOP_OBSERVING: GameAdvertisementStopObserving,
        PathValues.GAME_ADVERTISEMENT_UPDATE_PLATFORM_LOBBY_ID: GameAdvertisementUpdatePlatformLobbyID,
        PathValues.GAME_ADVERTISEMENT_UPDATE_STATE: GameAdvertisementUpdateState,
        PathValues.GAME_ADVERTISEMENT_UPDATE_TAGS: GameAdvertisementUpdateTags,
        PathValues.GAME_ADVERTISEMENT_LEAVE: GameAdvertisementLeave,
        PathValues.GAME_AUTOMATCH_GET_AUTOMATCH_MAP: GameAutomatchGetAutomatchMap,
        PathValues.GAME_AUTOMATCH2_GET_AUTOMATCH_MAP: GameAutomatch2GetAutomatchMap,
        PathValues.GAME_AUTOMATCH2_POLLING: GameAutomatch2Polling,
        PathValues.GAME_AUTOMATCH2_STOPPOLLING: GameAutomatch2Stoppolling,
        PathValues.GAME_AUTOMATCH2_UPDATE_STATUS: GameAutomatch2UpdateStatus,
        PathValues.GAME_CHALLENGE_GET_CHALLENGE_PROGRESS: GameChallengeGetChallengeProgress,
        PathValues.GAME_CHALLENGE_GET_CHALLENGE_PROGRESS_BY_PROFILE_ID: GameChallengeGetChallengeProgressByProfileID,
        PathValues.GAME_CHALLENGE_GET_CHALLENGES: GameChallengeGetChallenges,
        PathValues.GAME_CHALLENGE_UPDATE_PROGRESS_BATCHED: GameChallengeUpdateProgressBatched,
        PathValues.GAME_CHAT_GET_CHAT_CHANNELS: GameChatGetChatChannels,
        PathValues.GAME_CHAT_GET_OFFLINE_MESSAGES: GameChatGetOfflineMessages,
        PathValues.GAME_CHAT_DELETE_OFFLINE_MESSAGE: GameChatDeleteOfflineMessage,
        PathValues.GAME_CLAN_FIND: GameClanFind,
        PathValues.GAME_CLAN_GET_CLAN: GameClanGetClan,
        PathValues.GAME_CLAN_GET_CLAN_INFO_FULL: GameClanGetClanInfoFull,
        PathValues.GAME_CLAN_APPLY: GameClanApply,
        PathValues.GAME_CLAN_DISBAND: GameClanDisband,
        PathValues.GAME_CLAN_CREATE: GameClanCreate,
        PathValues.GAME_CLAN_UPDATE: GameClanUpdate,
        PathValues.GAME_CLOUD_GET_FILE_URL: GameCloudGetFileURL,
        PathValues.GAME_CLOUD_GET_TEMP_CREDENTIALS: GameCloudGetTempCredentials,
        PathValues.GAME_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS: GameCommunityEventGetAvailableCommunityEvents,
        PathValues.GAME_COMMUNITY_EVENT_GET_EVENT_CHALLENGE_PROGRESS: GameCommunityEventGetEventChallengeProgress,
        PathValues.GAME_COMMUNITY_EVENT_GET_EVENT_STATS: GameCommunityEventGetEventStats,
        PathValues.GAME_INVITATION_CANCEL_INVITATION: GameInvitationCancelInvitation,
        PathValues.GAME_INVITATION_EXTEND_INVITATION: GameInvitationExtendInvitation,
        PathValues.GAME_ITEM_GET_INVENTORY_BY_PROFILE_IDS: GameItemGetInventoryByProfileIDs,
        PathValues.GAME_ITEM_GET_ITEM_BUNDLE_ITEMS_JSON: GameItemGetItemBundleItemsJson,
        PathValues.GAME_ITEM_GET_ITEM_DEFINITIONS_JSON: GameItemGetItemDefinitionsJson,
        PathValues.GAME_ITEM_GET_ITEM_LOADOUTS: GameItemGetItemLoadouts,
        PathValues.GAME_ITEM_GET_ITEM_PRICES: GameItemGetItemPrices,
        PathValues.GAME_ITEM_GET_LEVEL_REWARDS_TABLE_JSON: GameItemGetLevelRewardsTableJson,
        PathValues.GAME_ITEM_GET_PERSONALIZED_SALE_ITEMS: GameItemGetPersonalizedSaleItems,
        PathValues.GAME_ITEM_GET_SCHEDULED_SALE_AND_ITEMS: GameItemGetScheduledSaleAndItems,
        PathValues.GAME_ITEM_DETACH_ITEMS: GameItemDetachItems,
        PathValues.GAME_ITEM_MOVE_CHARGES: GameItemMoveCharges,
        PathValues.GAME_ITEM_MOVE_ITEM: GameItemMoveItem,
        PathValues.GAME_ITEM_OPEN_ITEM_PACK: GameItemOpenItemPack,
        PathValues.GAME_ITEM_SIGN_ITEMS: GameItemSignItems,
        PathValues.GAME_ITEM_UPDATE_ITEM_ATTRIBUTES: GameItemUpdateItemAttributes,
        PathValues.GAME_LEADERBOARD_GET_RECENT_MATCH_HISTORY: GameLeaderboardGetRecentMatchHistory,
        PathValues.GAME_LEADERBOARD_GET_AVAILABLE_LEADERBOARDS: GameLeaderboardGetAvailableLeaderboards,
        PathValues.GAME_LEADERBOARD_GET_LEADER_BOARD: GameLeaderboardGetLeaderBoard,
        PathValues.GAME_LEADERBOARD_GET_PARTY_STAT: GameLeaderboardGetPartyStat,
        PathValues.GAME_LEADERBOARD_GET_PERSONAL_STAT: GameLeaderboardGetPersonalStat,
        PathValues.GAME_LEADERBOARD_GET_RECENT_MATCH_SINGLE_PLAYER_HISTORY: GameLeaderboardGetRecentMatchSinglePlayerHistory,
        PathValues.GAME_LEADERBOARD_GET_STAT_GROUPS_BY_PROFILE_IDS: GameLeaderboardGetStatGroupsByProfileIDs,
        PathValues.GAME_LEADERBOARD_GET_STATS_FOR_LEADERBOARD_BY_PROFILE_NAME: GameLeaderboardGetStatsForLeaderboardByProfileName,
        PathValues.GAME_LEADERBOARD_SET_AVATAR_STAT_VALUES: GameLeaderboardSetAvatarStatValues,
        PathValues.GAME_LOGIN_LOGOUT: GameLoginLogout,
        PathValues.GAME_LOGIN_READ_SESSION: GameLoginReadSession,
        PathValues.GAME_LOGIN_PLATFORMLOGIN: GameLoginPlatformlogin,
        PathValues.GAME_NEWS_GET_NEWS: GameNewsGetNews,
        PathValues.GAME_PARTY_CREATE_OR_REPORT_SINGLE_PLAYER: GamePartyCreateOrReportSinglePlayer,
        PathValues.GAME_PARTY_REPORT_MATCH: GamePartyReportMatch,
        PathValues.GAME_PLAYERREPORT_REPORTUSER: GamePlayerreportReportuser,
        PathValues.GAME_PARTY_SEND_MATCH_CHAT: GamePartySendMatchChat,
        PathValues.GAME_PARTY_FINALIZE_REPLAY_UPLOAD: GamePartyFinalizeReplayUpload,
        PathValues.GAME_PARTY_PEER_ADD: GamePartyPeerAdd,
        PathValues.GAME_PARTY_PEER_UPDATE: GamePartyPeerUpdate,
        PathValues.GAME_RELATIONSHIP_GET_PRESENCE_DATA: GameRelationshipGetPresenceData,
        PathValues.GAME_RELATIONSHIP_GET_RELATIONSHIPS: GameRelationshipGetRelationships,
        PathValues.GAME_RELATIONSHIP_CLEAR_RELATIONSHIP: GameRelationshipClearRelationship,
        PathValues.GAME_RELATIONSHIP_IGNORE: GameRelationshipIgnore,
        PathValues.GAME_RELATIONSHIP_SET_PRESENCE: GameRelationshipSetPresence,
        PathValues.GAME_RELATIONSHIP_SET_PRESENCE_PROPERTY: GameRelationshipSetPresenceProperty,
    },
)

path_to_api = PathToApi(
    {
        PathValues.COMMUNITY_EXTERNAL_PROXYSTEAMUSERREQUEST: CommunityExternalProxysteamuserrequest,
        PathValues.COMMUNITY_LEADERBOARD_GET_PERSONAL_STAT: CommunityLeaderboardGetPersonalStat,
        PathValues.COMMUNITY_LEADERBOARD_GET_RECENT_MATCH_HISTORY: CommunityLeaderboardGetRecentMatchHistory,
        PathValues.COMMUNITY_ADVERTISEMENT_FIND_ADVERTISEMENTS: CommunityAdvertisementFindAdvertisements,
        PathValues.COMMUNITY_LEADERBOARD_GET_AVATAR_STAT_FOR_PROFILE: CommunityLeaderboardGetAvatarStatForProfile,
        PathValues.COMMUNITY_ACHIEVEMENT_GET_ACHIEVEMENTS: CommunityAchievementGetAchievements,
        PathValues.COMMUNITY_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS: CommunityAchievementGetAvailableAchievements,
        PathValues.COMMUNITY_NEWS_GET_NEWS: CommunityNewsGetNews,
        PathValues.COMMUNITY_CLAN_FIND: CommunityClanFind,
        PathValues.COMMUNITY_CLAN_GET_CLAN_INFO_FULL: CommunityClanGetClanInfoFull,
        PathValues.COMMUNITY_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS: CommunityCommunityEventGetAvailableCommunityEvents,
        PathValues.COMMUNITY_ITEM_GET_INVENTORY_BY_PROFILE_IDS: CommunityItemGetInventoryByProfileIDs,
        PathValues.COMMUNITY_LEADERBOARD_GET_AVAILABLE_LEADERBOARDS: CommunityLeaderboardGetAvailableLeaderboards,
        PathValues.COMMUNITY_LEADERBOARD_GET_LEADERBOARD2: CommunityLeaderboardGetLeaderboard2,
        PathValues.GAME_ACCOUNT_FIND_PROFILES: GameAccountFindProfiles,
        PathValues.GAME_ACCOUNT_GET_PROFILE_NAME: GameAccountGetProfileName,
        PathValues.GAME_ACCOUNT_GET_PROFILE_PROPERTY: GameAccountGetProfileProperty,
        PathValues.GAME_ACCOUNT_FIND_PROFILES_BY_PLATFORM_ID: GameAccountFindProfilesByPlatformID,
        PathValues.GAME_ACCOUNT_SET_AVATAR_METADATA: GameAccountSetAvatarMetadata,
        PathValues.GAME_ACCOUNT_SET_LANGUAGE: GameAccountSetLanguage,
        PathValues.GAME_ACHIEVEMENT_GET_ACHIEVEMENTS: GameAchievementGetAchievements,
        PathValues.GAME_ACHIEVEMENT_GET_AVAILABLE_ACHIEVEMENTS: GameAchievementGetAvailableAchievements,
        PathValues.GAME_ACHIEVEMENT_SYNC_STATS: GameAchievementSyncStats,
        PathValues.GAME_ADVERTISEMENT_FIND_OBSERVABLE_ADVERTISEMENTS: GameAdvertisementFindObservableAdvertisements,
        PathValues.GAME_ADVERTISEMENT_FIND_ADVERTISEMENTS: GameAdvertisementFindAdvertisements,
        PathValues.GAME_ADVERTISEMENT_GET_ADVERTISEMENTS: GameAdvertisementGetAdvertisements,
        PathValues.GAME_ADVERTISEMENT_GET_LAN_ADVERTISEMENTS: GameAdvertisementGetLanAdvertisements,
        PathValues.GAME_ADVERTISEMENT_HOST: GameAdvertisementHost,
        PathValues.GAME_ADVERTISEMENT_UPDATE: GameAdvertisementUpdate,
        PathValues.GAME_ADVERTISEMENT_JOIN: GameAdvertisementJoin,
        PathValues.GAME_ADVERTISEMENT_START_OBSERVING: GameAdvertisementStartObserving,
        PathValues.GAME_ADVERTISEMENT_STOP_OBSERVING: GameAdvertisementStopObserving,
        PathValues.GAME_ADVERTISEMENT_UPDATE_PLATFORM_LOBBY_ID: GameAdvertisementUpdatePlatformLobbyID,
        PathValues.GAME_ADVERTISEMENT_UPDATE_STATE: GameAdvertisementUpdateState,
        PathValues.GAME_ADVERTISEMENT_UPDATE_TAGS: GameAdvertisementUpdateTags,
        PathValues.GAME_ADVERTISEMENT_LEAVE: GameAdvertisementLeave,
        PathValues.GAME_AUTOMATCH_GET_AUTOMATCH_MAP: GameAutomatchGetAutomatchMap,
        PathValues.GAME_AUTOMATCH2_GET_AUTOMATCH_MAP: GameAutomatch2GetAutomatchMap,
        PathValues.GAME_AUTOMATCH2_POLLING: GameAutomatch2Polling,
        PathValues.GAME_AUTOMATCH2_STOPPOLLING: GameAutomatch2Stoppolling,
        PathValues.GAME_AUTOMATCH2_UPDATE_STATUS: GameAutomatch2UpdateStatus,
        PathValues.GAME_CHALLENGE_GET_CHALLENGE_PROGRESS: GameChallengeGetChallengeProgress,
        PathValues.GAME_CHALLENGE_GET_CHALLENGE_PROGRESS_BY_PROFILE_ID: GameChallengeGetChallengeProgressByProfileID,
        PathValues.GAME_CHALLENGE_GET_CHALLENGES: GameChallengeGetChallenges,
        PathValues.GAME_CHALLENGE_UPDATE_PROGRESS_BATCHED: GameChallengeUpdateProgressBatched,
        PathValues.GAME_CHAT_GET_CHAT_CHANNELS: GameChatGetChatChannels,
        PathValues.GAME_CHAT_GET_OFFLINE_MESSAGES: GameChatGetOfflineMessages,
        PathValues.GAME_CHAT_DELETE_OFFLINE_MESSAGE: GameChatDeleteOfflineMessage,
        PathValues.GAME_CLAN_FIND: GameClanFind,
        PathValues.GAME_CLAN_GET_CLAN: GameClanGetClan,
        PathValues.GAME_CLAN_GET_CLAN_INFO_FULL: GameClanGetClanInfoFull,
        PathValues.GAME_CLAN_APPLY: GameClanApply,
        PathValues.GAME_CLAN_DISBAND: GameClanDisband,
        PathValues.GAME_CLAN_CREATE: GameClanCreate,
        PathValues.GAME_CLAN_UPDATE: GameClanUpdate,
        PathValues.GAME_CLOUD_GET_FILE_URL: GameCloudGetFileURL,
        PathValues.GAME_CLOUD_GET_TEMP_CREDENTIALS: GameCloudGetTempCredentials,
        PathValues.GAME_COMMUNITY_EVENT_GET_AVAILABLE_COMMUNITY_EVENTS: GameCommunityEventGetAvailableCommunityEvents,
        PathValues.GAME_COMMUNITY_EVENT_GET_EVENT_CHALLENGE_PROGRESS: GameCommunityEventGetEventChallengeProgress,
        PathValues.GAME_COMMUNITY_EVENT_GET_EVENT_STATS: GameCommunityEventGetEventStats,
        PathValues.GAME_INVITATION_CANCEL_INVITATION: GameInvitationCancelInvitation,
        PathValues.GAME_INVITATION_EXTEND_INVITATION: GameInvitationExtendInvitation,
        PathValues.GAME_ITEM_GET_INVENTORY_BY_PROFILE_IDS: GameItemGetInventoryByProfileIDs,
        PathValues.GAME_ITEM_GET_ITEM_BUNDLE_ITEMS_JSON: GameItemGetItemBundleItemsJson,
        PathValues.GAME_ITEM_GET_ITEM_DEFINITIONS_JSON: GameItemGetItemDefinitionsJson,
        PathValues.GAME_ITEM_GET_ITEM_LOADOUTS: GameItemGetItemLoadouts,
        PathValues.GAME_ITEM_GET_ITEM_PRICES: GameItemGetItemPrices,
        PathValues.GAME_ITEM_GET_LEVEL_REWARDS_TABLE_JSON: GameItemGetLevelRewardsTableJson,
        PathValues.GAME_ITEM_GET_PERSONALIZED_SALE_ITEMS: GameItemGetPersonalizedSaleItems,
        PathValues.GAME_ITEM_GET_SCHEDULED_SALE_AND_ITEMS: GameItemGetScheduledSaleAndItems,
        PathValues.GAME_ITEM_DETACH_ITEMS: GameItemDetachItems,
        PathValues.GAME_ITEM_MOVE_CHARGES: GameItemMoveCharges,
        PathValues.GAME_ITEM_MOVE_ITEM: GameItemMoveItem,
        PathValues.GAME_ITEM_OPEN_ITEM_PACK: GameItemOpenItemPack,
        PathValues.GAME_ITEM_SIGN_ITEMS: GameItemSignItems,
        PathValues.GAME_ITEM_UPDATE_ITEM_ATTRIBUTES: GameItemUpdateItemAttributes,
        PathValues.GAME_LEADERBOARD_GET_RECENT_MATCH_HISTORY: GameLeaderboardGetRecentMatchHistory,
        PathValues.GAME_LEADERBOARD_GET_AVAILABLE_LEADERBOARDS: GameLeaderboardGetAvailableLeaderboards,
        PathValues.GAME_LEADERBOARD_GET_LEADER_BOARD: GameLeaderboardGetLeaderBoard,
        PathValues.GAME_LEADERBOARD_GET_PARTY_STAT: GameLeaderboardGetPartyStat,
        PathValues.GAME_LEADERBOARD_GET_PERSONAL_STAT: GameLeaderboardGetPersonalStat,
        PathValues.GAME_LEADERBOARD_GET_RECENT_MATCH_SINGLE_PLAYER_HISTORY: GameLeaderboardGetRecentMatchSinglePlayerHistory,
        PathValues.GAME_LEADERBOARD_GET_STAT_GROUPS_BY_PROFILE_IDS: GameLeaderboardGetStatGroupsByProfileIDs,
        PathValues.GAME_LEADERBOARD_GET_STATS_FOR_LEADERBOARD_BY_PROFILE_NAME: GameLeaderboardGetStatsForLeaderboardByProfileName,
        PathValues.GAME_LEADERBOARD_SET_AVATAR_STAT_VALUES: GameLeaderboardSetAvatarStatValues,
        PathValues.GAME_LOGIN_LOGOUT: GameLoginLogout,
        PathValues.GAME_LOGIN_READ_SESSION: GameLoginReadSession,
        PathValues.GAME_LOGIN_PLATFORMLOGIN: GameLoginPlatformlogin,
        PathValues.GAME_NEWS_GET_NEWS: GameNewsGetNews,
        PathValues.GAME_PARTY_CREATE_OR_REPORT_SINGLE_PLAYER: GamePartyCreateOrReportSinglePlayer,
        PathValues.GAME_PARTY_REPORT_MATCH: GamePartyReportMatch,
        PathValues.GAME_PLAYERREPORT_REPORTUSER: GamePlayerreportReportuser,
        PathValues.GAME_PARTY_SEND_MATCH_CHAT: GamePartySendMatchChat,
        PathValues.GAME_PARTY_FINALIZE_REPLAY_UPLOAD: GamePartyFinalizeReplayUpload,
        PathValues.GAME_PARTY_PEER_ADD: GamePartyPeerAdd,
        PathValues.GAME_PARTY_PEER_UPDATE: GamePartyPeerUpdate,
        PathValues.GAME_RELATIONSHIP_GET_PRESENCE_DATA: GameRelationshipGetPresenceData,
        PathValues.GAME_RELATIONSHIP_GET_RELATIONSHIPS: GameRelationshipGetRelationships,
        PathValues.GAME_RELATIONSHIP_CLEAR_RELATIONSHIP: GameRelationshipClearRelationship,
        PathValues.GAME_RELATIONSHIP_IGNORE: GameRelationshipIgnore,
        PathValues.GAME_RELATIONSHIP_SET_PRESENCE: GameRelationshipSetPresence,
        PathValues.GAME_RELATIONSHIP_SET_PRESENCE_PROPERTY: GameRelationshipSetPresenceProperty,
    }
)
