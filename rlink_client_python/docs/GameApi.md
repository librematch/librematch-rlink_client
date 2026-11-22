# rlink_client.GameApi

All URIs are relative to *https://aoe-api.worldsedgelink.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**game_achievement_sync_stats**](GameApi.md#game_achievement_sync_stats) | **POST** /game/achievement/syncStats | Syncs achievement statistics
[**game_add_friend**](GameApi.md#game_add_friend) | **POST** /game/relationship/addfriend | Requests a friendship
[**game_add_profile_property**](GameApi.md#game_add_profile_property) | **POST** /game/account/addProfileProperty | Writes one profile property
[**game_advertisement_by_platform_session**](GameApi.md#game_advertisement_by_platform_session) | **GET** /game/advertisement/getAdvertisementByPlatformSessionID | Looks a lobby up by platform session id
[**game_advertisement_find_advertisements_get**](GameApi.md#game_advertisement_find_advertisements_get) | **GET** /game/advertisement/findAdvertisements | Searches visible joinable lobbies (GET)
[**game_advertisement_find_advertisements_post**](GameApi.md#game_advertisement_find_advertisements_post) | **POST** /game/advertisement/findAdvertisements | Searches visible joinable lobbies (POST)
[**game_advertisement_find_observable_get**](GameApi.md#game_advertisement_find_observable_get) | **GET** /game/advertisement/findObservableAdvertisements | Searches observable running games (GET)
[**game_advertisement_find_observable_post**](GameApi.md#game_advertisement_find_observable_post) | **POST** /game/advertisement/findObservableAdvertisements | Searches observable running games (POST)
[**game_advertisement_get_advertisements**](GameApi.md#game_advertisement_get_advertisements) | **GET** /game/advertisement/getAdvertisements | Lists the title&#39;s lobbies
[**game_advertisement_get_lan_advertisements_get**](GameApi.md#game_advertisement_get_lan_advertisements_get) | **GET** /game/advertisement/getLanAdvertisements | Lists the LAN lobbies (GET)
[**game_advertisement_get_lan_advertisements_post**](GameApi.md#game_advertisement_get_lan_advertisements_post) | **POST** /game/advertisement/getLanAdvertisements | Lists the LAN lobbies (POST)
[**game_advertisement_host**](GameApi.md#game_advertisement_host) | **POST** /game/advertisement/host | Creates and hosts a lobby advertisement
[**game_advertisement_join**](GameApi.md#game_advertisement_join) | **POST** /game/advertisement/join | Joins a lobby
[**game_advertisement_leave**](GameApi.md#game_advertisement_leave) | **POST** /game/advertisement/leave | Leaves a lobby
[**game_advertisement_start_observing**](GameApi.md#game_advertisement_start_observing) | **POST** /game/advertisement/startObserving | Starts observing a running game
[**game_advertisement_stop_observing**](GameApi.md#game_advertisement_stop_observing) | **POST** /game/advertisement/stopObserving | Stops observing a game
[**game_advertisement_update**](GameApi.md#game_advertisement_update) | **POST** /game/advertisement/update | Updates a lobby
[**game_advertisement_update_platform_lobby_id**](GameApi.md#game_advertisement_update_platform_lobby_id) | **POST** /game/advertisement/updatePlatformLobbyID | Stores the platform lobby id of the lobby
[**game_advertisement_update_platform_session_id**](GameApi.md#game_advertisement_update_platform_session_id) | **POST** /game/advertisement/updatePlatformSessionID | Stores the platform session id of the lobby
[**game_advertisement_update_state**](GameApi.md#game_advertisement_update_state) | **POST** /game/advertisement/updateState | Updates the lobby state
[**game_advertisement_update_tags**](GameApi.md#game_advertisement_update_tags) | **POST** /game/advertisement/updateTags | Replaces the lobby tags
[**game_apply_offline_achievement_updates**](GameApi.md#game_apply_offline_achievement_updates) | **POST** /game/achievement/applyOfflineUpdates | Applies offline achievement progress (no-op)
[**game_apply_offline_leaderboard_updates**](GameApi.md#game_apply_offline_leaderboard_updates) | **POST** /game/leaderboard/applyOfflineUpdates | Applies offline ladder progress
[**game_apply_to_clan**](GameApi.md#game_apply_to_clan) | **POST** /game/clan/apply | Applies to a clan
[**game_automatch_polling_get**](GameApi.md#game_automatch_polling_get) | **GET** /game/automatch2/polling | Enters and polls the matchmaking queue (GET)
[**game_automatch_polling_post**](GameApi.md#game_automatch_polling_post) | **POST** /game/automatch2/polling | Enters and polls the matchmaking queue (POST)
[**game_automatch_stop_polling_get**](GameApi.md#game_automatch_stop_polling_get) | **GET** /game/automatch2/stoppolling | Leaves the matchmaking queue (GET)
[**game_automatch_stop_polling_post**](GameApi.md#game_automatch_stop_polling_post) | **POST** /game/automatch2/stoppolling | Leaves the matchmaking queue (POST)
[**game_automatch_update_status_get**](GameApi.md#game_automatch_update_status_get) | **GET** /game/automatch2/updateStatus | Acknowledges the queue state (GET)
[**game_automatch_update_status_post**](GameApi.md#game_automatch_update_status_post) | **POST** /game/automatch2/updateStatus | Acknowledges the queue state (POST)
[**game_cancel_invitation**](GameApi.md#game_cancel_invitation) | **POST** /game/invitation/cancelInvitation | Cancels an invitation
[**game_clear_profile_property**](GameApi.md#game_clear_profile_property) | **POST** /game/account/clearProfileProperty | Deletes one profile property
[**game_clear_relationship**](GameApi.md#game_clear_relationship) | **POST** /game/relationship/clearRelationship | Deletes a relationship
[**game_cloud_get_file_url_get**](GameApi.md#game_cloud_get_file_url_get) | **GET** /game/cloud/getFileURL | Returns the download URLs of builtin assets (GET)
[**game_cloud_get_file_url_post**](GameApi.md#game_cloud_get_file_url_post) | **POST** /game/cloud/getFileURL | Returns the download URLs of builtin assets (POST)
[**game_cloud_get_temp_credentials**](GameApi.md#game_cloud_get_temp_credentials) | **GET** /game/cloud/getTempCredentials | Issues the SAS credential for a blob
[**game_community_event_get_event_challenge_progress**](GameApi.md#game_community_event_get_event_challenge_progress) | **GET** /game/CommunityEvent/getEventChallengeProgress | Challenge progress of an event
[**game_create_clan**](GameApi.md#game_create_clan) | **POST** /game/clan/create | Creates a clan
[**game_create_item_loadout**](GameApi.md#game_create_item_loadout) | **POST** /game/item/createItemLoadout | Creates an item loadout
[**game_delete_offline_message**](GameApi.md#game_delete_offline_message) | **POST** /game/chat/deleteOfflineMessage | Deletes a queued offline message
[**game_detach_items**](GameApi.md#game_detach_items) | **POST** /game/item/detachItems | Detaches items
[**game_disband_clan**](GameApi.md#game_disband_clan) | **POST** /game/clan/disband | Disbands a clan
[**game_equip_item_loadout**](GameApi.md#game_equip_item_loadout) | **POST** /game/item/equipItemLoadout | Equips an item loadout
[**game_extend_invitation**](GameApi.md#game_extend_invitation) | **POST** /game/invitation/extendInvitation | Invites a player to a lobby
[**game_find_clans**](GameApi.md#game_find_clans) | **GET** /game/clan/find | Searches clans 
[**game_find_profiles**](GameApi.md#game_find_profiles) | **GET** /game/account/FindProfiles | Searches profiles by alias
[**game_find_profiles_by_platform_id**](GameApi.md#game_find_profiles_by_platform_id) | **POST** /game/account/FindProfilesByPlatformID | Searches profiles by platform id
[**game_get_achievements**](GameApi.md#game_get_achievements) | **GET** /game/Achievement/getAchievements | Achievements of the caller 
[**game_get_automatch_map**](GameApi.md#game_get_automatch_map) | **GET** /game/automatch2/getAutomatchMap | Returns the matchmaking map pool
[**game_get_automatch_map_legacy**](GameApi.md#game_get_automatch_map_legacy) | **GET** /game/automatch/getAutomatchMap | Returns the matchmaking map pool (legacy path)
[**game_get_available_achievements**](GameApi.md#game_get_available_achievements) | **GET** /game/Achievement/getAvailableAchievements | Achievement catalogue
[**game_get_available_community_events**](GameApi.md#game_get_available_community_events) | **GET** /game/CommunityEvent/getAvailableCommunityEvents | Available community events
[**game_get_available_leaderboards**](GameApi.md#game_get_available_leaderboards) | **GET** /game/Leaderboard/getAvailableLeaderboards | Ladder catalogue
[**game_get_avatar_stat_leader_board**](GameApi.md#game_get_avatar_stat_leader_board) | **GET** /game/Leaderboard/getAvatarStatLeaderBoard | Avatar statistics ladder 
[**game_get_challenge_progress_by_profile_id**](GameApi.md#game_get_challenge_progress_by_profile_id) | **GET** /game/Challenge/getChallengeProgressByProfileID | Challenge progress of another profile
[**game_get_challenge_progress_get**](GameApi.md#game_get_challenge_progress_get) | **GET** /game/Challenge/getChallengeProgress | Challenge progress (GET)
[**game_get_challenge_progress_post**](GameApi.md#game_get_challenge_progress_post) | **POST** /game/Challenge/getChallengeProgress | Challenge progress (POST, legacy form)
[**game_get_challenges**](GameApi.md#game_get_challenges) | **GET** /game/Challenge/getChallenges | Challenge catalogue
[**game_get_chat_channels_get**](GameApi.md#game_get_chat_channels_get) | **GET** /game/chat/getChatChannels | Lists the chat channels (GET)
[**game_get_chat_channels_post**](GameApi.md#game_get_chat_channels_post) | **POST** /game/chat/getChatChannels | Lists the chat channels (POST)
[**game_get_clan**](GameApi.md#game_get_clan) | **GET** /game/clan/getClan | Clans by name
[**game_get_clan_info_full**](GameApi.md#game_get_clan_info_full) | **GET** /game/clan/getClanInfoFull | Full clan record
[**game_get_event_leaderboard**](GameApi.md#game_get_event_leaderboard) | **GET** /game/CommunityEvent/getEventLeaderboard | Event leaderboard 
[**game_get_event_stats**](GameApi.md#game_get_event_stats) | **GET** /game/CommunityEvent/getEventStats | Event statistics 
[**game_get_inventory_by_profile_ids**](GameApi.md#game_get_inventory_by_profile_ids) | **GET** /game/item/getInventoryByProfileIDs | Inventories and locations of profiles
[**game_get_item_bundle_items_json**](GameApi.md#game_get_item_bundle_items_json) | **GET** /game/item/getItemBundleItemsJson | Item bundle catalogue (signed, anonymous)
[**game_get_item_definitions_json**](GameApi.md#game_get_item_definitions_json) | **GET** /game/item/getItemDefinitionsJson | Item definition catalogue (signed)
[**game_get_item_loadouts**](GameApi.md#game_get_item_loadouts) | **GET** /game/item/getItemLoadouts | The item loadouts of the caller
[**game_get_item_prices**](GameApi.md#game_get_item_prices) | **GET** /game/item/getItemPrices | Item prices (empty catalogue)
[**game_get_leader_board**](GameApi.md#game_get_leader_board) | **GET** /game/Leaderboard/getLeaderBoard | Page of a ladder
[**game_get_level_rewards_table_json**](GameApi.md#game_get_level_rewards_table_json) | **GET** /game/item/getLevelRewardsTableJson | Level rewards table (signed)
[**game_get_news**](GameApi.md#game_get_news) | **GET** /game/news/getNews | News of the title
[**game_get_offline_messages**](GameApi.md#game_get_offline_messages) | **GET** /game/chat/getOfflineMessages | Polls the offline chat inbox
[**game_get_party_stat**](GameApi.md#game_get_party_stat) | **GET** /game/Leaderboard/getPartyStat | Ladder statistics of a party
[**game_get_personal_stat**](GameApi.md#game_get_personal_stat) | **GET** /game/Leaderboard/getPersonalStat | Personal ladder statistics
[**game_get_personalized_sale_items**](GameApi.md#game_get_personalized_sale_items) | **GET** /game/item/getPersonalizedSaleItems | Personalized sales
[**game_get_presence_data**](GameApi.md#game_get_presence_data) | **GET** /game/relationship/getPresenceData | Returns the presence definition catalogue
[**game_get_profile_name**](GameApi.md#game_get_profile_name) | **GET** /game/account/getProfileName | Returns profile rows by ids
[**game_get_profile_property**](GameApi.md#game_get_profile_property) | **GET** /game/account/getProfileProperty | Reads one profile property
[**game_get_recent_match_history_get**](GameApi.md#game_get_recent_match_history_get) | **GET** /game/Leaderboard/getRecentMatchHistory | Recent match history (GET)
[**game_get_recent_match_history_post**](GameApi.md#game_get_recent_match_history_post) | **POST** /game/Leaderboard/getRecentMatchHistory | Recent match history (POST, legacy form)
[**game_get_recent_match_single_player_history**](GameApi.md#game_get_recent_match_single_player_history) | **GET** /game/Leaderboard/getRecentMatchSinglePlayerHistory | Single-player match history (fixed empty answer)
[**game_get_relationships_get**](GameApi.md#game_get_relationships_get) | **GET** /game/relationship/getRelationships | Lists friends and recent players (GET)
[**game_get_relationships_post**](GameApi.md#game_get_relationships_post) | **POST** /game/relationship/getRelationships | Lists friends and recent players (POST)
[**game_get_scheduled_sale_and_items**](GameApi.md#game_get_scheduled_sale_and_items) | **GET** /game/item/getScheduledSaleAndItems | Scheduled sales
[**game_get_stat_groups_by_profile_ids**](GameApi.md#game_get_stat_groups_by_profile_ids) | **GET** /game/Leaderboard/getStatGroupsByProfileIDs | Stat groups of profiles
[**game_get_stats_for_leaderboard_by_profile_name**](GameApi.md#game_get_stats_for_leaderboard_by_profile_name) | **GET** /game/Leaderboard/getStatsForLeaderboardByProfileName | Ladder statistics by platform name
[**game_get_store_tokens**](GameApi.md#game_get_store_tokens) | **GET** /game/msstore/getStoreTokens | Returns the Microsoft Store tokens 
[**game_grant_achievement**](GameApi.md#game_grant_achievement) | **POST** /game/achievement/grantAchievement | Grants an achievement
[**game_ignore**](GameApi.md#game_ignore) | **POST** /game/relationship/ignore | Ignores a player
[**game_join_channel**](GameApi.md#game_join_channel) | **POST** /game/chat/joinChannel | Joins a chat channel
[**game_leave_channel**](GameApi.md#game_leave_channel) | **POST** /game/chat/leaveChannel | Leaves a chat channel
[**game_logout**](GameApi.md#game_logout) | **POST** /game/login/logout | Closes the session
[**game_move_charges**](GameApi.md#game_move_charges) | **POST** /game/item/moveCharges | Moves item charges
[**game_move_item**](GameApi.md#game_move_item) | **POST** /game/item/moveItem | Moves items
[**game_open_item_pack**](GameApi.md#game_open_item_pack) | **POST** /game/item/openItemPack | Opens an item pack
[**game_party_create_or_report_single_player**](GameApi.md#game_party_create_or_report_single_player) | **POST** /game/party/createOrReportSinglePlayer | Creates or reports a single-player match
[**game_party_finalize_replay_upload**](GameApi.md#game_party_finalize_replay_upload) | **POST** /game/party/finalizeReplayUpload | Confirms or discards a replay upload
[**game_party_peer_add**](GameApi.md#game_party_peer_add) | **POST** /game/party/peerAdd | Adds peers to the lobby
[**game_party_peer_update**](GameApi.md#game_party_peer_update) | **POST** /game/party/peerUpdate | Updates peers of the lobby
[**game_party_report_match**](GameApi.md#game_party_report_match) | **POST** /game/party/reportMatch | Reports the result of a match
[**game_party_send_match_chat**](GameApi.md#game_party_send_match_chat) | **POST** /game/party/sendMatchChat | Sends a chat message inside a match
[**game_party_update_host**](GameApi.md#game_party_update_host) | **POST** /game/party/updateHost | Transfers the host of the lobby
[**game_platform_login**](GameApi.md#game_platform_login) | **POST** /game/login/platformlogin | Logs in to the game service and creates the session 
[**game_read_session**](GameApi.md#game_read_session) | **POST** /game/login/readSession | Polls the queued notification frames
[**game_reply_to_invitation**](GameApi.md#game_reply_to_invitation) | **POST** /game/invitation/replyToInvitation | Answers an invitation
[**game_report_user**](GameApi.md#game_report_user) | **POST** /game/playerreport/reportUser | Reports a player
[**game_send_text**](GameApi.md#game_send_text) | **POST** /game/chat/sendText | Sends a message to a channel
[**game_send_whisper**](GameApi.md#game_send_whisper) | **POST** /game/chat/sendWhisper | Sends a whisper (single-recipient legacy form)
[**game_send_whispers**](GameApi.md#game_send_whispers) | **POST** /game/chat/sendWhispers | Sends a whisper to several recipients
[**game_set_avatar_metadata**](GameApi.md#game_set_avatar_metadata) | **POST** /game/account/setAvatarMetadata | Stores the avatar metadata
[**game_set_avatar_stat_values**](GameApi.md#game_set_avatar_stat_values) | **POST** /game/leaderboard/setAvatarStatValues | Stores avatar statistic values
[**game_set_crossplay_enabled**](GameApi.md#game_set_crossplay_enabled) | **POST** /game/account/setCrossplayEnabled | Enables crossplay
[**game_set_language**](GameApi.md#game_set_language) | **POST** /game/account/setLanguage | Sets the client language 
[**game_set_presence**](GameApi.md#game_set_presence) | **POST** /game/relationship/setPresence | Sets the presence
[**game_set_presence_property**](GameApi.md#game_set_presence_property) | **POST** /game/relationship/setPresenceProperty | Sets one presence property
[**game_sign_items**](GameApi.md#game_sign_items) | **POST** /game/item/signItems | Signs an item list
[**game_update_challenge_progress**](GameApi.md#game_update_challenge_progress) | **POST** /game/challenge/updateProgress | Adds single-player challenge progress (A3 legacy form)
[**game_update_challenge_progress_batched**](GameApi.md#game_update_challenge_progress_batched) | **POST** /game/challenge/updateProgressBatched | Adds batched challenge progress
[**game_update_clan**](GameApi.md#game_update_clan) | **POST** /game/clan/update | Updates a clan
[**game_update_item_attributes**](GameApi.md#game_update_item_attributes) | **POST** /game/item/updateItemAttributes | Updates item attributes
[**game_update_item_loadout**](GameApi.md#game_update_item_loadout) | **POST** /game/item/updateItemLoadout | Updates an item loadout
[**game_web_socket**](GameApi.md#game_web_socket) | **GET** /wss/ | Notification socket (WebSocket)


# **game_achievement_sync_stats**
> List[object] game_achievement_sync_stats()

Syncs achievement statistics

Syncs the achievement statistics of the profile and answers `[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Syncs achievement statistics
        api_response = api_instance.game_achievement_sync_stats()
        print("The response of GameApi->game_achievement_sync_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_achievement_sync_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_add_friend**
> List[object] game_add_friend(target_profile_id=target_profile_id)

Requests a friendship

Starts a friend request for the target profile and answers `[0]` with its
profile; the client then completes the handshake with
`/game/relationship/acceptFriend`. An unknown target answers `[2, []]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    target_profile_id = 56 # int |  (optional)

    try:
        # Requests a friendship
        api_response = api_instance.game_add_friend(target_profile_id=target_profile_id)
        print("The response of GameApi->game_add_friend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_add_friend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_profile_id** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_add_profile_property**
> List[object] game_add_profile_property(property_id, property_value)

Writes one profile property

Stores the key/value pair on the caller's profile and answers `[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    property_id = 'property_id_example' # str | 
    property_value = 'property_value_example' # str | 

    try:
        # Writes one profile property
        api_response = api_instance.game_add_profile_property(property_id, property_value)
        print("The response of GameApi->game_add_profile_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_add_profile_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**|  | 
 **property_value** | **str**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_by_platform_session**
> List[object] game_advertisement_by_platform_session(platform_session_id, online_platform=online_platform)

Looks a lobby up by platform session id

Returns the first lobby whose platform session id matches, or an empty row; officially only AoE4 is known to call it.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    platform_session_id = 56 # int | 
    online_platform = 'online_platform_example' # str | bound, never used.  (optional)

    try:
        # Looks a lobby up by platform session id
        api_response = api_instance.game_advertisement_by_platform_session(platform_session_id, online_platform=online_platform)
        print("The response of GameApi->game_advertisement_by_platform_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_by_platform_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_session_id** | **int**|  | 
 **online_platform** | **str**| bound, never used.  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_advertisements_get**
> List[object] game_advertisement_find_advertisements_get(count=count, start=start, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags, numeric_tag_names=numeric_tag_names, numeric_tag_values=numeric_tag_values, string_tag_names=string_tag_names, string_tag_values=string_tag_values)

Searches visible joinable lobbies (GET)

Joinable, visible (not started) lobbies of the title, excluding the caller's
own, filtered by the checksum/mod/version fields and the tag filter;
`count`/`start` page the rows.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    count = 56 # int | page size (0 = all). (optional)
    start = 56 # int | offset. (optional)
    app_binary_checksum = 56 # int |  (optional)
    data_checksum = 56 # int |  (optional)
    match_type_id = 56 # int |  (optional)
    mod_dll_file = 'mod_dll_file_example' # str |  (optional)
    mod_dll_checksum = 56 # int |  (optional)
    mod_name = 'mod_name_example' # str |  (optional)
    mod_version = 'mod_version_example' # str |  (optional)
    version_flags = 56 # int |  (optional)
    numeric_tag_names = 'numeric_tag_names_example' # str | JSON array — tag filter (A2/AoM/A4). (optional)
    numeric_tag_values = 'numeric_tag_values_example' # str |  (optional)
    string_tag_names = 'string_tag_names_example' # str |  (optional)
    string_tag_values = 'string_tag_values_example' # str |  (optional)

    try:
        # Searches visible joinable lobbies (GET)
        api_response = api_instance.game_advertisement_find_advertisements_get(count=count, start=start, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags, numeric_tag_names=numeric_tag_names, numeric_tag_values=numeric_tag_values, string_tag_names=string_tag_names, string_tag_values=string_tag_values)
        print("The response of GameApi->game_advertisement_find_advertisements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_find_advertisements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| page size (0 &#x3D; all). | [optional] 
 **start** | **int**| offset. | [optional] 
 **app_binary_checksum** | **int**|  | [optional] 
 **data_checksum** | **int**|  | [optional] 
 **match_type_id** | **int**|  | [optional] 
 **mod_dll_file** | **str**|  | [optional] 
 **mod_dll_checksum** | **int**|  | [optional] 
 **mod_name** | **str**|  | [optional] 
 **mod_version** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 
 **numeric_tag_names** | **str**| JSON array — tag filter (A2/AoM/A4). | [optional] 
 **numeric_tag_values** | **str**|  | [optional] 
 **string_tag_names** | **str**|  | [optional] 
 **string_tag_values** | **str**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_advertisements_post**
> List[object] game_advertisement_find_advertisements_post(count=count, start=start, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)

Searches visible joinable lobbies (POST)

Same handler and answer as the GET form (the AoE1/AoE3 quick-match clients
post). The A1/AoE3 clients also send `profile_ids`, `race_ids` and
`statGroup_ids`, and A2/A4/AoM send `desc`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    count = 56 # int |  (optional)
    start = 56 # int |  (optional)
    app_binary_checksum = 56 # int |  (optional)
    data_checksum = 56 # int |  (optional)
    match_type_id = 'match_type_id_example' # str | JSON value, may be null. (optional)
    mod_dll_file = 'mod_dll_file_example' # str |  (optional)
    mod_dll_checksum = 56 # int |  (optional)
    mod_name = 'mod_name_example' # str |  (optional)
    mod_version = 'mod_version_example' # str |  (optional)
    version_flags = 56 # int |  (optional)

    try:
        # Searches visible joinable lobbies (POST)
        api_response = api_instance.game_advertisement_find_advertisements_post(count=count, start=start, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)
        print("The response of GameApi->game_advertisement_find_advertisements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_find_advertisements_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | [optional] 
 **start** | **int**|  | [optional] 
 **app_binary_checksum** | **int**|  | [optional] 
 **data_checksum** | **int**|  | [optional] 
 **match_type_id** | **str**| JSON value, may be null. | [optional] 
 **mod_dll_file** | **str**|  | [optional] 
 **mod_dll_checksum** | **int**|  | [optional] 
 **mod_name** | **str**|  | [optional] 
 **mod_version** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_observable_get**
> List[object] game_advertisement_find_observable_get(count=count, start=start, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)

Searches observable running games (GET)

The observable lobbies of the title with `state` 1 (every observable lobby is
started), their rows carrying the stamped start time. The third slot carries a
profile row per member of every listed lobby.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    count = 56 # int |  (optional)
    start = 56 # int |  (optional)
    app_binary_checksum = 56 # int |  (optional)
    data_checksum = 56 # int |  (optional)
    match_type_id = 'match_type_id_example' # str |  (optional)
    mod_dll_file = 'mod_dll_file_example' # str |  (optional)
    mod_dll_checksum = 56 # int |  (optional)
    mod_name = 'mod_name_example' # str |  (optional)
    mod_version = 'mod_version_example' # str |  (optional)
    version_flags = 56 # int |  (optional)

    try:
        # Searches observable running games (GET)
        api_response = api_instance.game_advertisement_find_observable_get(count=count, start=start, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)
        print("The response of GameApi->game_advertisement_find_observable_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_find_observable_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | [optional] 
 **start** | **int**|  | [optional] 
 **app_binary_checksum** | **int**|  | [optional] 
 **data_checksum** | **int**|  | [optional] 
 **match_type_id** | **str**|  | [optional] 
 **mod_dll_file** | **str**|  | [optional] 
 **mod_dll_checksum** | **int**|  | [optional] 
 **mod_name** | **str**|  | [optional] 
 **mod_version** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_observable_post**
> List[object] game_advertisement_find_observable_post(observer_group_id=observer_group_id)

Searches observable running games (POST)

The AoE3-only legacy form. The query carries `observerGroupID`: anything other
than "0" answers `[0,[],[]]` at once.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    observer_group_id = 'observer_group_id_example' # str | anything ≠ \"0\" answers empty. (optional)

    try:
        # Searches observable running games (POST)
        api_response = api_instance.game_advertisement_find_observable_post(observer_group_id=observer_group_id)
        print("The response of GameApi->game_advertisement_find_observable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_find_observable_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observer_group_id** | **str**| anything ≠ \&quot;0\&quot; answers empty. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_get_advertisements**
> List[object] game_advertisement_get_advertisements(match_ids=match_ids)

Lists the title's lobbies

Without `match_ids`, every lobby of the title (any state, joined or running);
with the array, exactly those lobbies.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_ids = 'match_ids_example' # str | JSON array of advertisement ids — the answer is then exactly those lobbies. (optional)

    try:
        # Lists the title's lobbies
        api_response = api_instance.game_advertisement_get_advertisements(match_ids=match_ids)
        print("The response of GameApi->game_advertisement_get_advertisements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_get_advertisements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_ids** | **str**| JSON array of advertisement ids — the answer is then exactly those lobbies. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_get_lan_advertisements_get**
> List[object] game_advertisement_get_lan_advertisements_get(lan_server_guids, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)

Lists the LAN lobbies (GET)

Lists the lobbies whose internal LAN battle-server GUID is in `lanServerGuids`
and whose peer list includes the caller, gated by the checksum/mod filters.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    lan_server_guids = 'lan_server_guids_example' # str | JSON array of LAN GUIDs (`[]` answers empty immediately); A1 sends them unquoted.
    app_binary_checksum = 56 # int |  (optional)
    data_checksum = 56 # int |  (optional)
    match_type_id = 56 # int |  (optional)
    mod_dll_file = 'mod_dll_file_example' # str |  (optional)
    mod_dll_checksum = 56 # int |  (optional)
    mod_name = 'mod_name_example' # str |  (optional)
    mod_version = 'mod_version_example' # str |  (optional)
    version_flags = 56 # int |  (optional)

    try:
        # Lists the LAN lobbies (GET)
        api_response = api_instance.game_advertisement_get_lan_advertisements_get(lan_server_guids, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)
        print("The response of GameApi->game_advertisement_get_lan_advertisements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_get_lan_advertisements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lan_server_guids** | **str**| JSON array of LAN GUIDs (&#x60;[]&#x60; answers empty immediately); A1 sends them unquoted. | 
 **app_binary_checksum** | **int**|  | [optional] 
 **data_checksum** | **int**|  | [optional] 
 **match_type_id** | **int**|  | [optional] 
 **mod_dll_file** | **str**|  | [optional] 
 **mod_dll_checksum** | **int**|  | [optional] 
 **mod_name** | **str**|  | [optional] 
 **mod_version** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_get_lan_advertisements_post**
> List[object] game_advertisement_get_lan_advertisements_post(lan_server_guids, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)

Lists the LAN lobbies (POST)

Same handler and answer as the GET form; the AoE1 client posts its query (the standard AoE3 legacy form).

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    lan_server_guids = 'lan_server_guids_example' # str | JSON array of LAN GUIDs (`[]` answers empty).
    app_binary_checksum = 56 # int |  (optional)
    data_checksum = 56 # int |  (optional)
    match_type_id = 56 # int |  (optional)
    mod_dll_file = 'mod_dll_file_example' # str |  (optional)
    mod_dll_checksum = 56 # int |  (optional)
    mod_name = 'mod_name_example' # str |  (optional)
    mod_version = 'mod_version_example' # str |  (optional)
    version_flags = 56 # int |  (optional)

    try:
        # Lists the LAN lobbies (POST)
        api_response = api_instance.game_advertisement_get_lan_advertisements_post(lan_server_guids, app_binary_checksum=app_binary_checksum, data_checksum=data_checksum, match_type_id=match_type_id, mod_dll_file=mod_dll_file, mod_dll_checksum=mod_dll_checksum, mod_name=mod_name, mod_version=mod_version, version_flags=version_flags)
        print("The response of GameApi->game_advertisement_get_lan_advertisements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_get_lan_advertisements_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lan_server_guids** | **str**| JSON array of LAN GUIDs (&#x60;[]&#x60; answers empty). | 
 **app_binary_checksum** | **int**|  | [optional] 
 **data_checksum** | **int**|  | [optional] 
 **match_type_id** | **int**|  | [optional] 
 **mod_dll_file** | **str**|  | [optional] 
 **mod_dll_checksum** | **int**|  | [optional] 
 **mod_name** | **str**|  | [optional] 
 **mod_version** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_host**
> List[object] game_advertisement_host(advertisementid, description, appbinarychecksum=appbinarychecksum, datachecksum=datachecksum, moddllfile=moddllfile, moddllchecksum=moddllchecksum, modname=modname, modversion=modversion, version_flags=version_flags, automatch_poll_id=automatch_poll_id, relay_region=relay_region, mapname=mapname, hostid=hostid, is_observable=is_observable, observer_delay=observer_delay, observer_password=observer_password, password=password, passworded=passworded, visible=visible, joinable=joinable, statgroup=statgroup, matchtype=matchtype, maxplayers=maxplayers, options=options, slotinfo=slotinfo, psn_session_id=psn_session_id, state=state, service_type=service_type, race=race, team=team, party=party)

Creates and hosts a lobby advertisement

Creates the lobby (`advertisementid` must be -1 for a fresh lobby), assigns
its id and answers with the battle server of
the relay region, the region, the current peers and the metadata. When
`automatchPoll_id > 0` the lobby is the matchmaking host of a pending
reservation and the other players are notified (`Automatch2GameMessage`); AoE1
additionally attaches the queued peers server-side. `joinable` is true for A1
and AoE3 below the Baltic Powers, AoE1 lobbies use one port pair less (no
out-of-band slot) and no battle-server name in their advertisement rows. The
AoE1/AoE3 clients send every field in the query string and repeat it in the
body; only the body is bound.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int | -1 to create.
    description = 'description_example' # str | lobby title; \\\"AUTOMATCH\\\"/\\\"SESSION_MATCH_KEY\\\" mark matchmaking and session lobbies.
    appbinarychecksum = 56 # int | version checksum, matched at join. (optional)
    datachecksum = 56 # int |  (optional)
    moddllfile = 'moddllfile_example' # str | \\\"INVALID\\\" without mods. (optional)
    moddllchecksum = 56 # int |  (optional)
    modname = 'modname_example' # str |  (optional)
    modversion = 'modversion_example' # str |  (optional)
    version_flags = 56 # int |  (optional)
    automatch_poll_id = 56 # int | >0: this is the host lobby of a matchmaking reservation. (optional)
    relay_region = 'relay_region_example' # str | region name or the LAN battle-server GUID (read from the body). (optional)
    mapname = 'mapname_example' # str |  (optional)
    hostid = 56 # int | 0 = the session user. (optional)
    is_observable = True # bool |  (optional)
    observer_delay = 56 # int |  (optional)
    observer_password = 'observer_password_example' # str |  (optional)
    password = 'password_example' # str | matched verbatim at join; never echoed. (optional)
    passworded = True # bool |  (optional)
    visible = True # bool |  (optional)
    joinable = True # bool | forced true for A1 and old AoE3 libraries. (optional)
    statgroup = 56 # int | accepted but unused. (optional)
    matchtype = 56 # int |  (optional)
    maxplayers = 56 # int |  (optional)
    options = 'options_example' # str | opaque base64+zlib block, stored and echoed. (optional)
    slotinfo = 'slotinfo_example' # str | opaque base64+zlib block. (optional)
    psn_session_id = 56 # int | empty string tolerated. (optional)
    state = 56 # int | usually -1 at creation. (optional)
    service_type = 56 # int | 0 online; 1 marks a LAN lobby. (optional)
    race = 56 # int |  (optional)
    team = 56 # int |  (optional)
    party = 56 # int | -1 none, else the parent lobby id (it must exist and be a party root). (optional)

    try:
        # Creates and hosts a lobby advertisement
        api_response = api_instance.game_advertisement_host(advertisementid, description, appbinarychecksum=appbinarychecksum, datachecksum=datachecksum, moddllfile=moddllfile, moddllchecksum=moddllchecksum, modname=modname, modversion=modversion, version_flags=version_flags, automatch_poll_id=automatch_poll_id, relay_region=relay_region, mapname=mapname, hostid=hostid, is_observable=is_observable, observer_delay=observer_delay, observer_password=observer_password, password=password, passworded=passworded, visible=visible, joinable=joinable, statgroup=statgroup, matchtype=matchtype, maxplayers=maxplayers, options=options, slotinfo=slotinfo, psn_session_id=psn_session_id, state=state, service_type=service_type, race=race, team=team, party=party)
        print("The response of GameApi->game_advertisement_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**| -1 to create. | 
 **description** | **str**| lobby title; \\\&quot;AUTOMATCH\\\&quot;/\\\&quot;SESSION_MATCH_KEY\\\&quot; mark matchmaking and session lobbies. | 
 **appbinarychecksum** | **int**| version checksum, matched at join. | [optional] 
 **datachecksum** | **int**|  | [optional] 
 **moddllfile** | **str**| \\\&quot;INVALID\\\&quot; without mods. | [optional] 
 **moddllchecksum** | **int**|  | [optional] 
 **modname** | **str**|  | [optional] 
 **modversion** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 
 **automatch_poll_id** | **int**| &gt;0: this is the host lobby of a matchmaking reservation. | [optional] 
 **relay_region** | **str**| region name or the LAN battle-server GUID (read from the body). | [optional] 
 **mapname** | **str**|  | [optional] 
 **hostid** | **int**| 0 &#x3D; the session user. | [optional] 
 **is_observable** | **bool**|  | [optional] 
 **observer_delay** | **int**|  | [optional] 
 **observer_password** | **str**|  | [optional] 
 **password** | **str**| matched verbatim at join; never echoed. | [optional] 
 **passworded** | **bool**|  | [optional] 
 **visible** | **bool**|  | [optional] 
 **joinable** | **bool**| forced true for A1 and old AoE3 libraries. | [optional] 
 **statgroup** | **int**| accepted but unused. | [optional] 
 **matchtype** | **int**|  | [optional] 
 **maxplayers** | **int**|  | [optional] 
 **options** | **str**| opaque base64+zlib block, stored and echoed. | [optional] 
 **slotinfo** | **str**| opaque base64+zlib block. | [optional] 
 **psn_session_id** | **int**| empty string tolerated. | [optional] 
 **state** | **int**| usually -1 at creation. | [optional] 
 **service_type** | **int**| 0 online; 1 marks a LAN lobby. | [optional] 
 **race** | **int**|  | [optional] 
 **team** | **int**|  | [optional] 
 **party** | **int**| -1 none, else the parent lobby id (it must exist and be a party root). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_join**
> List[object] game_advertisement_join(advertisementid, appbinarychecksum=appbinarychecksum, datachecksum=datachecksum, moddllfile=moddllfile, moddllchecksum=moddllchecksum, modname=modname, modversion=modversion, version_flags=version_flags, password=password, party=party, race=race, team=team)

Joins a lobby

Validates the optional lobby password and
answers with the battle server and the joiner's own peer row. A mismatch of
version/modChecksums, `joinable` = false, `party` not matching the lobby, a
wrong password or an unknown advertisement refuses the join; a matchmaking
join skips those checks (the lobby is server-managed).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int | 
    appbinarychecksum = 56 # int | must match the lobby's. (optional)
    datachecksum = 56 # int |  (optional)
    moddllfile = 'moddllfile_example' # str |  (optional)
    moddllchecksum = 56 # int |  (optional)
    modname = 'modname_example' # str |  (optional)
    modversion = 'modversion_example' # str |  (optional)
    version_flags = 56 # int |  (optional)
    password = 'password_example' # str | required whenever the lobby has one and it is not a matchmaking join. (optional)
    party = 56 # int | -1 or the lobby party; forced -1 on a matchmaking join. (optional)
    race = 56 # int |  (optional)
    team = 56 # int | forced -1 on a matchmaking join. (optional)

    try:
        # Joins a lobby
        api_response = api_instance.game_advertisement_join(advertisementid, appbinarychecksum=appbinarychecksum, datachecksum=datachecksum, moddllfile=moddllfile, moddllchecksum=moddllchecksum, modname=modname, modversion=modversion, version_flags=version_flags, password=password, party=party, race=race, team=team)
        print("The response of GameApi->game_advertisement_join:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_join: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **appbinarychecksum** | **int**| must match the lobby&#39;s. | [optional] 
 **datachecksum** | **int**|  | [optional] 
 **moddllfile** | **str**|  | [optional] 
 **moddllchecksum** | **int**|  | [optional] 
 **modname** | **str**|  | [optional] 
 **modversion** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 
 **password** | **str**| required whenever the lobby has one and it is not a matchmaking join. | [optional] 
 **party** | **int**| -1 or the lobby party; forced -1 on a matchmaking join. | [optional] 
 **race** | **int**|  | [optional] 
 **team** | **int**| forced -1 on a matchmaking join. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_leave**
> List[object] game_advertisement_leave(advertisementid)

Leaves a lobby

Removes the session user from the lobby (and from any matchmaking queue); the last peer out deletes the lobby. `[0]` when the user was a peer, `[2]` otherwise.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int | 

    try:
        # Leaves a lobby
        api_response = api_instance.game_advertisement_leave(advertisementid)
        print("The response of GameApi->game_advertisement_leave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_leave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_start_observing**
> List[object] game_advertisement_start_observing(advertisementid=advertisementid)

Starts observing a running game

Registers the session user as observer of the lobby and answers with the
battle server of the lobby's region, the peer ids and the start time.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int |  (optional)

    try:
        # Starts observing a running game
        api_response = api_instance.game_advertisement_start_observing(advertisementid=advertisementid)
        print("The response of GameApi->game_advertisement_start_observing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_start_observing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_stop_observing**
> List[object] game_advertisement_stop_observing(advertisementid=advertisementid)

Stops observing a game

Removes the session user from the lobby's observers and answers `[0]` (also
for an unknown advertisement; `[2]` on a binding failure).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int |  (optional)

    try:
        # Stops observing a game
        api_response = api_instance.game_advertisement_stop_observing(advertisementid=advertisementid)
        print("The response of GameApi->game_advertisement_stop_observing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_stop_observing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update**
> List[object] game_advertisement_update(advertisementid, appbinarychecksum=appbinarychecksum, datachecksum=datachecksum, moddllfile=moddllfile, moddllchecksum=moddllchecksum, modname=modname, modversion=modversion, version_flags=version_flags, description=description, automatch_poll_id=automatch_poll_id, mapname=mapname, hostid=hostid, is_observable=is_observable, observer_delay=observer_delay, observer_password=observer_password, password=password, passworded=passworded, visible=visible, joinable=joinable, matchtype=matchtype, maxplayers=maxplayers, options=options, slotinfo=slotinfo, psn_session_id=psn_session_id, state=state)

Updates a lobby

Updates the lobby from the form. When the advertised id is this user's
matchmaking reservation and no lobby exists yet, the lobby is created here
(server-supplied description, map, maxplayers and relay region; `joinable`
true; the caller a peer) — the matchmaking host never calls `host`. While the
lobby is a matchmaking reservation the server-supplied fields stay; a `state`
of 1 stamps the start time and the state never moves back. A2/A4/AoM and AoE3
from library 194 answer with the encoded advertisement as a second slot; A1
and the old AoE3 library answer `[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int | 
    appbinarychecksum = 56 # int |  (optional)
    datachecksum = 56 # int |  (optional)
    moddllfile = 'moddllfile_example' # str |  (optional)
    moddllchecksum = 56 # int |  (optional)
    modname = 'modname_example' # str |  (optional)
    modversion = 'modversion_example' # str |  (optional)
    version_flags = 56 # int |  (optional)
    description = 'description_example' # str |  (optional)
    automatch_poll_id = 56 # int |  (optional)
    mapname = 'mapname_example' # str |  (optional)
    hostid = 56 # int | 0 = the session user. (optional)
    is_observable = True # bool |  (optional)
    observer_delay = 56 # int |  (optional)
    observer_password = 'observer_password_example' # str |  (optional)
    password = 'password_example' # str |  (optional)
    passworded = True # bool |  (optional)
    visible = True # bool |  (optional)
    joinable = True # bool | forced true for A1 and old AoE3 libraries. (optional)
    matchtype = 56 # int |  (optional)
    maxplayers = 56 # int |  (optional)
    options = 'options_example' # str |  (optional)
    slotinfo = 'slotinfo_example' # str |  (optional)
    psn_session_id = 56 # int | also stored as the platform session id on A1/old AoE3. (optional)
    state = 56 # int | once 1, never back (the official behaviour). (optional)

    try:
        # Updates a lobby
        api_response = api_instance.game_advertisement_update(advertisementid, appbinarychecksum=appbinarychecksum, datachecksum=datachecksum, moddllfile=moddllfile, moddllchecksum=moddllchecksum, modname=modname, modversion=modversion, version_flags=version_flags, description=description, automatch_poll_id=automatch_poll_id, mapname=mapname, hostid=hostid, is_observable=is_observable, observer_delay=observer_delay, observer_password=observer_password, password=password, passworded=passworded, visible=visible, joinable=joinable, matchtype=matchtype, maxplayers=maxplayers, options=options, slotinfo=slotinfo, psn_session_id=psn_session_id, state=state)
        print("The response of GameApi->game_advertisement_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **appbinarychecksum** | **int**|  | [optional] 
 **datachecksum** | **int**|  | [optional] 
 **moddllfile** | **str**|  | [optional] 
 **moddllchecksum** | **int**|  | [optional] 
 **modname** | **str**|  | [optional] 
 **modversion** | **str**|  | [optional] 
 **version_flags** | **int**|  | [optional] 
 **description** | **str**|  | [optional] 
 **automatch_poll_id** | **int**|  | [optional] 
 **mapname** | **str**|  | [optional] 
 **hostid** | **int**| 0 &#x3D; the session user. | [optional] 
 **is_observable** | **bool**|  | [optional] 
 **observer_delay** | **int**|  | [optional] 
 **observer_password** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **passworded** | **bool**|  | [optional] 
 **visible** | **bool**|  | [optional] 
 **joinable** | **bool**| forced true for A1 and old AoE3 libraries. | [optional] 
 **matchtype** | **int**|  | [optional] 
 **maxplayers** | **int**|  | [optional] 
 **options** | **str**|  | [optional] 
 **slotinfo** | **str**|  | [optional] 
 **psn_session_id** | **int**| also stored as the platform session id on A1/old AoE3. | [optional] 
 **state** | **int**| once 1, never back (the official behaviour). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_platform_lobby_id**
> List[object] game_advertisement_update_platform_lobby_id(match_id, platformlobby_id=platformlobby_id)

Stores the platform lobby id of the lobby

The A1/AoE3 flow: same storage and the three-slot `PlatformSessionUpdateMessage` frame as updatePlatformSessionID.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | 
    platformlobby_id = 56 # int |  (optional)

    try:
        # Stores the platform lobby id of the lobby
        api_response = api_instance.game_advertisement_update_platform_lobby_id(match_id, platformlobby_id=platformlobby_id)
        print("The response of GameApi->game_advertisement_update_platform_lobby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_update_platform_lobby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 
 **platformlobby_id** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_platform_session_id**
> List[object] game_advertisement_update_platform_session_id(match_id, platform_session_id=platform_session_id)

Stores the platform session id of the lobby

Stores the platform session id (visible as advertisement row slot 1) when the
caller is a peer of `matchID`, or keeps it for the pending matchmaking flow,
and sends the `PlatformSessionUpdateMessage` frame to every peer (`[matchID,
metadata, platformSessionID]`, plus the `0,"",""` tail for the modern
libraries).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | 
    platform_session_id = 56 # int | read from the body (Steam/Xbox session id). (optional)

    try:
        # Stores the platform session id of the lobby
        api_response = api_instance.game_advertisement_update_platform_session_id(match_id, platform_session_id=platform_session_id)
        print("The response of GameApi->game_advertisement_update_platform_session_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_update_platform_session_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 
 **platform_session_id** | **int**| read from the body (Steam/Xbox session id). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_state**
> List[object] game_advertisement_update_state(advertisementid=advertisementid, state=state)

Updates the lobby state

Stores `state`; state 1 (started) stamps the start time once and sends the `MatchStartMessage` frame
to every peer with a session.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int |  (optional)
    state = 56 # int | 1 = started. (optional)

    try:
        # Updates the lobby state
        api_response = api_instance.game_advertisement_update_state(advertisementid=advertisementid, state=state)
        print("The response of GameApi->game_advertisement_update_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_update_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | [optional] 
 **state** | **int**| 1 &#x3D; started. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_tags**
> List[object] game_advertisement_update_tags(advertisementid, numeric_tag_names=numeric_tag_names, numeric_tag_values=numeric_tag_values, string_tag_names=string_tag_names, string_tag_values=string_tag_values)

Replaces the lobby tags

Host-only. Replaces the whole tag set, which findAdvertisements filters on
(e.g. AoE IV input_kbm). The name and value arrays must have the same length.
A request without tag fields clears the tag set.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    advertisementid = 56 # int | 
    numeric_tag_names = 'numeric_tag_names_example' # str | JSON array of names. (optional)
    numeric_tag_values = 'numeric_tag_values_example' # str | JSON array of int32. (optional)
    string_tag_names = 'string_tag_names_example' # str | JSON array of names. (optional)
    string_tag_values = 'string_tag_values_example' # str | JSON array of strings. (optional)

    try:
        # Replaces the lobby tags
        api_response = api_instance.game_advertisement_update_tags(advertisementid, numeric_tag_names=numeric_tag_names, numeric_tag_values=numeric_tag_values, string_tag_names=string_tag_names, string_tag_values=string_tag_values)
        print("The response of GameApi->game_advertisement_update_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_advertisement_update_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **numeric_tag_names** | **str**| JSON array of names. | [optional] 
 **numeric_tag_values** | **str**| JSON array of int32. | [optional] 
 **string_tag_names** | **str**| JSON array of names. | [optional] 
 **string_tag_values** | **str**| JSON array of strings. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_apply_offline_achievement_updates**
> List[object] game_apply_offline_achievement_updates()

Applies offline achievement progress (no-op)

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Applies offline achievement progress (no-op)
        api_response = api_instance.game_apply_offline_achievement_updates()
        print("The response of GameApi->game_apply_offline_achievement_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_apply_offline_achievement_updates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_apply_offline_leaderboard_updates**
> List[object] game_apply_offline_leaderboard_updates()

Applies offline ladder progress

Applies the offline avatar-stat deltas sent as `avatarStat_ids`/`values`/`updateTypes` and answers `[0, [], []]`.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Applies offline ladder progress
        api_response = api_instance.game_apply_offline_leaderboard_updates()
        print("The response of GameApi->game_apply_offline_leaderboard_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_apply_offline_leaderboard_updates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_apply_to_clan**
> List[object] game_apply_to_clan(clan_list_name)

Applies to a clan

Applies to the clan named `clanList_name`. Result 0 means the invite was
sent, 6 that the clan is full.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    clan_list_name = 'clan_list_name_example' # str | the name of the clan.

    try:
        # Applies to a clan
        api_response = api_instance.game_apply_to_clan(clan_list_name)
        print("The response of GameApi->game_apply_to_clan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_apply_to_clan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_list_name** | **str**| the name of the clan. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_polling_get**
> List[object] game_automatch_polling_get(match_types=match_types)

Enters and polls the matchmaking queue (GET)

The AoE1/AoE2/AoE3/AoM clients poll with a GET; the fields travel in the query string (the same binder). A4 has no GET form.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_types = 'match_types_example' # str | JSON array of queue ids. (optional)

    try:
        # Enters and polls the matchmaking queue (GET)
        api_response = api_instance.game_automatch_polling_get(match_types=match_types)
        print("The response of GameApi->game_automatch_polling_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_automatch_polling_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_types** | **str**| JSON array of queue ids. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_polling_post**
> List[object] game_automatch_polling_post(match_types=match_types, race_info_race_id=race_info_race_id, race_info_key=race_info_key, faction_ids=faction_ids, veto_map_key=veto_map_key, veto_maps=veto_maps, options=options, party_session_id=party_session_id, relay_region=relay_region, previously_given_match_id=previously_given_match_id, notified_automatch_success=notified_automatch_success, race_info_profile_id=race_info_profile_id)

Enters and polls the matchmaking queue (POST)

Enters the caller (and the linked party, keyed by `partySessionID`) in the
queues of `matchTypes` and answers the poll state. An empty `matchTypes` array
removes the caller from the queue. When a pair appears, the reservation id is
minted (slot 13's `matchID`) and the `Automatch2GameMessage` joiner frame is
pushed to the peers by the lobby creation stage. A4 binds
`previouslyGivenMatchId` to re-attach to a live match; the race and veto
vectors are stored for the pairing.

The unmatched body is a fixed 22-slot row of constants (A1 omits the third
port slot — 20); the matched body (A2/A4/AoM; A1/A3 reuse the unmatched shape
with the reservation id filled in) carries the host profile, the map, the
queue and the battle server.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_types = 'match_types_example' # str | JSON array of queue ids ([]: leave the queue): A1 [8]; A2 [22,23,24]...; A3 [2]/[3]/[4]; A4 [20..23],[860]; AoM [28..39]. (optional)
    race_info_race_id = 'race_info_race_id_example' # str | JSON array; the race per queue, echoed in the status rows. (optional)
    race_info_key = 'race_info_key_example' # str | JSON array; the veto index per queue (A4 semantics). (optional)
    faction_ids = 'faction_ids_example' # str | JSON array stored with the queue entry. (optional)
    veto_map_key = 'veto_map_key_example' # str | JSON array (A4 map veto keys). (optional)
    veto_maps = 'veto_maps_example' # str | JSON array (A4 map vetoes). (optional)
    options = 'options_example' # str | JSON array, stored unused. (optional)
    party_session_id = 56 # int | links the party members through their advertisement rosters. (optional)
    relay_region = 'relay_region_example' # str | \\\"westeurope\\\" or the LAN GUID; selects the battle server. (optional)
    previously_given_match_id = 56 # int | A4 re-attach to an existing reservation. (optional)
    notified_automatch_success = True # bool | logged. (optional)
    race_info_profile_id = 'race_info_profile_id_example' # str | logged. (optional)

    try:
        # Enters and polls the matchmaking queue (POST)
        api_response = api_instance.game_automatch_polling_post(match_types=match_types, race_info_race_id=race_info_race_id, race_info_key=race_info_key, faction_ids=faction_ids, veto_map_key=veto_map_key, veto_maps=veto_maps, options=options, party_session_id=party_session_id, relay_region=relay_region, previously_given_match_id=previously_given_match_id, notified_automatch_success=notified_automatch_success, race_info_profile_id=race_info_profile_id)
        print("The response of GameApi->game_automatch_polling_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_automatch_polling_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_types** | **str**| JSON array of queue ids ([]: leave the queue): A1 [8]; A2 [22,23,24]...; A3 [2]/[3]/[4]; A4 [20..23],[860]; AoM [28..39]. | [optional] 
 **race_info_race_id** | **str**| JSON array; the race per queue, echoed in the status rows. | [optional] 
 **race_info_key** | **str**| JSON array; the veto index per queue (A4 semantics). | [optional] 
 **faction_ids** | **str**| JSON array stored with the queue entry. | [optional] 
 **veto_map_key** | **str**| JSON array (A4 map veto keys). | [optional] 
 **veto_maps** | **str**| JSON array (A4 map vetoes). | [optional] 
 **options** | **str**| JSON array, stored unused. | [optional] 
 **party_session_id** | **int**| links the party members through their advertisement rosters. | [optional] 
 **relay_region** | **str**| \\\&quot;westeurope\\\&quot; or the LAN GUID; selects the battle server. | [optional] 
 **previously_given_match_id** | **int**| A4 re-attach to an existing reservation. | [optional] 
 **notified_automatch_success** | **bool**| logged. | [optional] 
 **race_info_profile_id** | **str**| logged. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_stop_polling_get**
> List[object] game_automatch_stop_polling_get()

Leaves the matchmaking queue (GET)

The legacy form for the older clients; same handler and answer.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Leaves the matchmaking queue (GET)
        api_response = api_instance.game_automatch_stop_polling_get()
        print("The response of GameApi->game_automatch_stop_polling_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_automatch_stop_polling_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_stop_polling_post**
> List[object] game_automatch_stop_polling_post(commit=commit, owner_profile_id=owner_profile_id)

Leaves the matchmaking queue (POST)

Leaves the queue, keeping a match the caller is part of alive (the others are
not requeued) and stopping the party as a unit. `commit` marks the end of the
stop handshake. The answer is `[0]`, or `[2]` when commit=1.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    commit = 56 # int | read, ignored. (optional)
    owner_profile_id = 56 # int | logged. (optional)

    try:
        # Leaves the matchmaking queue (POST)
        api_response = api_instance.game_automatch_stop_polling_post(commit=commit, owner_profile_id=owner_profile_id)
        print("The response of GameApi->game_automatch_stop_polling_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_automatch_stop_polling_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commit** | **int**| read, ignored. | [optional] 
 **owner_profile_id** | **int**| logged. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_update_status_get**
> List[object] game_automatch_update_status_get()

Acknowledges the queue state (GET)

The legacy form; same `[0, ack]` answer.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Acknowledges the queue state (GET)
        api_response = api_instance.game_automatch_update_status_get()
        print("The response of GameApi->game_automatch_update_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_automatch_update_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_update_status_post**
> List[object] game_automatch_update_status_post(match_id=match_id, result=result, result_code=result_code)

Acknowledges the queue state (POST)

[0, ack] — the per-title acknowledgment value of the resolved queue (A2 0, A4 -30; the captures show [0,0] and [0,30]).

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | resolves the queue. (optional)
    result = 56 # int | logged. (optional)
    result_code = 56 # int | logged. (optional)

    try:
        # Acknowledges the queue state (POST)
        api_response = api_instance.game_automatch_update_status_post(match_id=match_id, result=result, result_code=result_code)
        print("The response of GameApi->game_automatch_update_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_automatch_update_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| resolves the queue. | [optional] 
 **result** | **int**| logged. | [optional] 
 **result_code** | **int**| logged. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cancel_invitation**
> List[object] game_cancel_invitation(gatheringid, inviteeid)

Cancels an invitation

Idempotent; the invitee receives a `CancelInvitationMessage` frame
(`[inviterProfile row, gatheringid]`).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    gatheringid = 56 # int | 
    inviteeid = 56 # int | 

    try:
        # Cancels an invitation
        api_response = api_instance.game_cancel_invitation(gatheringid, inviteeid)
        print("The response of GameApi->game_cancel_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_cancel_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gatheringid** | **int**|  | 
 **inviteeid** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clear_profile_property**
> List[object] game_clear_profile_property(property_id)

Deletes one profile property

Deletes the property from the caller's profile and answers `[0]` (also when
the property did not exist).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    property_id = 'property_id_example' # str | 

    try:
        # Deletes one profile property
        api_response = api_instance.game_clear_profile_property(property_id)
        print("The response of GameApi->game_clear_profile_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_clear_profile_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clear_relationship**
> List[object] game_clear_relationship()

Deletes a relationship

Removes the relationship with `targetProfileID` (`relationType` selects
friend, ignore or block) and answers `[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Deletes a relationship
        api_response = api_instance.game_clear_relationship()
        print("The response of GameApi->game_clear_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_clear_relationship: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cloud_get_file_url_get**
> List[object] game_cloud_get_file_url_get(names)

Returns the download URLs of builtin assets (GET)

Resolves each name of `names` against the builtin asset index of the title and
answers a `FileDescriptorRow` per name (null for an unknown name). A title
without an index answers every descriptor null with code 2, which is the
answer of the A4 captures.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    names = 'names_example' # str | JSON array of asset names.

    try:
        # Returns the download URLs of builtin assets (GET)
        api_response = api_instance.game_cloud_get_file_url_get(names)
        print("The response of GameApi->game_cloud_get_file_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_cloud_get_file_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **str**| JSON array of asset names. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cloud_get_file_url_post**
> List[object] game_cloud_get_file_url_post(names)

Returns the download URLs of builtin assets (POST)

The AoE3 body form (the client duplicates every field in the query string too; the body is bound).

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    names = 'names_example' # str | JSON array of asset names.

    try:
        # Returns the download URLs of builtin assets (POST)
        api_response = api_instance.game_cloud_get_file_url_post(names)
        print("The response of GameApi->game_cloud_get_file_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_cloud_get_file_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **str**| JSON array of asset names. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cloud_get_temp_credentials**
> List[object] game_cloud_get_temp_credentials(key)

Issues the SAS credential for a blob

Answers the time-limited credential the client appends as the `sig` query of
its `/cloudfiles/` request. `key` is the full client-side URL path; a leading
`/cloudfiles/` is trimmed for the lookup. The SAS query starts at `sig=`. An
unknown key answers the failure array, whose expiry slot carries now+5
minutes.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    key = 'key_example' # str | the blob lookup — the `/cloudfiles/...` path of the client's URL.

    try:
        # Issues the SAS credential for a blob
        api_response = api_instance.game_cloud_get_temp_credentials(key)
        print("The response of GameApi->game_cloud_get_temp_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_cloud_get_temp_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| the blob lookup — the &#x60;/cloudfiles/...&#x60; path of the client&#39;s URL. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_community_event_get_event_challenge_progress**
> List[object] game_community_event_get_event_challenge_progress(event_id)

Challenge progress of an event

The challenge progress of the session user in the event `event_id`: one
progress record per challenge of the event, `[]` when the user has none.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    event_id = 56 # int | the event.

    try:
        # Challenge progress of an event
        api_response = api_instance.game_community_event_get_event_challenge_progress(event_id)
        print("The response of GameApi->game_community_event_get_event_challenge_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_community_event_get_event_challenge_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the event. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_create_clan**
> List[object] game_create_clan(name, full_name, description=description, icon=icon, join_policy=join_policy, metadata=metadata, message_of_the_day=message_of_the_day, tags=tags, cost=cost, item_price_id=item_price_id, paymentitem=paymentitem, chat=chat, invite=invite, promote=promote, demote=demote, remove=remove, disband=disband, edit_info=edit_info, edit_permission=edit_permission, rank=rank, permission_name=permission_name, loc_string_id=loc_string_id)

Creates a clan

Creates the clan of the caller with the requested name, tag and metadata.
The documented trace answers `[3, null, null, []]`: the creation was refused
and no clan came back.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    name = 'name_example' # str | the clan tag.
    full_name = 'full_name_example' # str | the full name of the clan.
    description = 'description_example' # str | the public description. (optional)
    icon = 'icon_example' # str | the crest id (e.g. CR-001). (optional)
    join_policy = 56 # int | the join policy (0 open, 1 invite/request only). (optional)
    metadata = 'metadata_example' # str | the clan metadata. (optional)
    message_of_the_day = 'message_of_the_day_example' # str | the message shown to the members. (optional)
    tags = 'tags_example' # str | JSON array of the clan tags. (optional)
    cost = 56 # int | cost of the creation (0). (optional)
    item_price_id = 56 # int | the item paid for the creation (-1 none). (optional)
    paymentitem = 56 # int | the payment item (-1 none). (optional)
    chat = 'chat_example' # str | JSON array of role permissions; [] in the trace. (optional)
    invite = 'invite_example' # str | JSON array of role permissions; [] in the trace. (optional)
    promote = 'promote_example' # str | JSON array of role permissions; [] in the trace. (optional)
    demote = 'demote_example' # str | JSON array of role permissions; [] in the trace. (optional)
    remove = 'remove_example' # str | JSON array of role permissions; [] in the trace. (optional)
    disband = 'disband_example' # str | JSON array of role permissions; [] in the trace. (optional)
    edit_info = 'edit_info_example' # str | JSON array of role permissions; [] in the trace. (optional)
    edit_permission = 'edit_permission_example' # str | JSON array of role permissions; [] in the trace. (optional)
    rank = 'rank_example' # str | JSON array of the role ranks; [] in the trace. (optional)
    permission_name = 'permission_name_example' # str | JSON array of the role names; [] in the trace. (optional)
    loc_string_id = 'loc_string_id_example' # str | JSON array of the role locstring ids; [] in the trace. (optional)

    try:
        # Creates a clan
        api_response = api_instance.game_create_clan(name, full_name, description=description, icon=icon, join_policy=join_policy, metadata=metadata, message_of_the_day=message_of_the_day, tags=tags, cost=cost, item_price_id=item_price_id, paymentitem=paymentitem, chat=chat, invite=invite, promote=promote, demote=demote, remove=remove, disband=disband, edit_info=edit_info, edit_permission=edit_permission, rank=rank, permission_name=permission_name, loc_string_id=loc_string_id)
        print("The response of GameApi->game_create_clan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_create_clan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the clan tag. | 
 **full_name** | **str**| the full name of the clan. | 
 **description** | **str**| the public description. | [optional] 
 **icon** | **str**| the crest id (e.g. CR-001). | [optional] 
 **join_policy** | **int**| the join policy (0 open, 1 invite/request only). | [optional] 
 **metadata** | **str**| the clan metadata. | [optional] 
 **message_of_the_day** | **str**| the message shown to the members. | [optional] 
 **tags** | **str**| JSON array of the clan tags. | [optional] 
 **cost** | **int**| cost of the creation (0). | [optional] 
 **item_price_id** | **int**| the item paid for the creation (-1 none). | [optional] 
 **paymentitem** | **int**| the payment item (-1 none). | [optional] 
 **chat** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **invite** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **promote** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **demote** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **remove** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **disband** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **edit_info** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **edit_permission** | **str**| JSON array of role permissions; [] in the trace. | [optional] 
 **rank** | **str**| JSON array of the role ranks; [] in the trace. | [optional] 
 **permission_name** | **str**| JSON array of the role names; [] in the trace. | [optional] 
 **loc_string_id** | **str**| JSON array of the role locstring ids; [] in the trace. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_create_item_loadout**
> List[object] game_create_item_loadout(name, type, item_or_loc_ids=item_or_loc_ids)

Creates an item loadout

Creates the loadout and answers `[0, [loadoutRow]]`. The request carries
`name`, `type` and `itemOrLocIDs` as a JSON array string.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    name = 'name_example' # str | 
    type = 56 # int | 1001 gameplay items.
    item_or_loc_ids = 'item_or_loc_ids_example' # str | the official clients send a JSON array string — see the binding defect note. (optional)

    try:
        # Creates an item loadout
        api_response = api_instance.game_create_item_loadout(name, type, item_or_loc_ids=item_or_loc_ids)
        print("The response of GameApi->game_create_item_loadout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_create_item_loadout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | **int**| 1001 gameplay items. | 
 **item_or_loc_ids** | **str**| the official clients send a JSON array string — see the binding defect note. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_delete_offline_message**
> List[object] game_delete_offline_message()

Deletes a queued offline message

Deletes the message from the offline inbox and answers `[0]` (also for an
unknown id).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Deletes a queued offline message
        api_response = api_instance.game_delete_offline_message()
        print("The response of GameApi->game_delete_offline_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_delete_offline_message: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_detach_items**
> List[object] game_detach_items(item_ids, item_locations, item_charges)

Detaches items

Detaches every listed item from its container or equipment location (`-1`
leaves the parallel slot unchanged; a charge value resets the durability to
it). Per-item result rows: 0 for a detached item, 1 for a deduplicated no-op
and 2 for an unknown item.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    item_ids = 'item_ids_example' # str | JSON array of item ids.
    item_locations = 'item_locations_example' # str | JSON array; -1 keeps.
    item_charges = 'item_charges_example' # str | JSON array; -1 keeps, else the new durability.

    try:
        # Detaches items
        api_response = api_instance.game_detach_items(item_ids, item_locations, item_charges)
        print("The response of GameApi->game_detach_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_detach_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_ids** | **str**| JSON array of item ids. | 
 **item_locations** | **str**| JSON array; -1 keeps. | 
 **item_charges** | **str**| JSON array; -1 keeps, else the new durability. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_disband_clan**
> List[object] game_disband_clan()

Disbands a clan

Disbands the clan of the caller.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Disbands a clan
        api_response = api_instance.game_disband_clan()
        print("The response of GameApi->game_disband_clan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_disband_clan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_equip_item_loadout**
> List[object] game_equip_item_loadout(id)

Equips an item loadout

Echoes the loadout row and answers `[0, loadoutRow, []]`; the service also
applies the item locations of the loadout.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    id = 56 # int | 

    try:
        # Equips an item loadout
        api_response = api_instance.game_equip_item_loadout(id)
        print("The response of GameApi->game_equip_item_loadout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_equip_item_loadout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_extend_invitation**
> List[object] game_extend_invitation(gatheringid, inviteeid, gatheringpassword=gatheringpassword)

Invites a player to a lobby

Validates the lobby and its password, stores the invitation
and sends the `ExtendInvitationMessage`
frame — `[inviterProfile row, gatheringid, gatheringpassword]` — to
the invitee's session, or queues it through readSession when
offline. The payload is the byte shape of the official AoE4 frame.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    gatheringid = 56 # int | the lobby id.
    inviteeid = 56 # int | 
    gatheringpassword = 'gatheringpassword_example' # str | must equal the lobby password. (optional)

    try:
        # Invites a player to a lobby
        api_response = api_instance.game_extend_invitation(gatheringid, inviteeid, gatheringpassword=gatheringpassword)
        print("The response of GameApi->game_extend_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_extend_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gatheringid** | **int**| the lobby id. | 
 **inviteeid** | **int**|  | 
 **gatheringpassword** | **str**| must equal the lobby password. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_find_clans**
> List[object] game_find_clans(count=count, start=start, name=name, join_policies=join_policies, tags=tags)

Searches clans 

Pages the clans of the title as `ClanRow` rows, filtered by `name`,
`joinPolicies` and `tags`, with `count`/`start` paging. No match answers `[0,
[]]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    count = 56 # int | page size. (optional)
    start = 56 # int | index of the first row of the page. (optional)
    name = 'name_example' # str | substring of the clan name; empty lists every clan. (optional)
    join_policies = 'join_policies_example' # str | JSON array of the join policies to include ([0,1,2] includes them all).  (optional)
    tags = 'tags_example' # str | JSON array of the clan tags to filter by; [] includes them all. (optional)

    try:
        # Searches clans 
        api_response = api_instance.game_find_clans(count=count, start=start, name=name, join_policies=join_policies, tags=tags)
        print("The response of GameApi->game_find_clans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_find_clans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| page size. | [optional] 
 **start** | **int**| index of the first row of the page. | [optional] 
 **name** | **str**| substring of the clan name; empty lists every clan. | [optional] 
 **join_policies** | **str**| JSON array of the join policies to include ([0,1,2] includes them all).  | [optional] 
 **tags** | **str**| JSON array of the clan tags to filter by; [] includes them all. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_find_profiles**
> List[object] game_find_profiles(name)

Searches profiles by alias

Case-insensitive substring search on `name`; the matching rows carry the presence tail.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    name = 'name_example' # str | substring of the alias, case-insensitive.

    try:
        # Searches profiles by alias
        api_response = api_instance.game_find_profiles(name)
        print("The response of GameApi->game_find_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_find_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| substring of the alias, case-insensitive. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_find_profiles_by_platform_id**
> List[object] game_find_profiles_by_platform_id(platform_ids)

Searches profiles by platform id

Binds `platformIDs` (JSON array) and returns the matching profile rows with
their presence tail. The A2+ clients send a JSON *number* array; the A1 client
sends a JSON *string* array, which is answered with `[0,[]]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    platform_ids = 'platform_ids_example' # str | JSON array of platform user ids (numbers from A2+, quoted strings from A1).

    try:
        # Searches profiles by platform id
        api_response = api_instance.game_find_profiles_by_platform_id(platform_ids)
        print("The response of GameApi->game_find_profiles_by_platform_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_find_profiles_by_platform_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_ids** | **str**| JSON array of platform user ids (numbers from A2+, quoted strings from A1). | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_achievements**
> List[object] game_get_achievements(profile_ids=profile_ids)

Achievements of the caller 

The earned achievements of the session user: `[0, [[<sessionUserProfileId>,
<earned rows>]]]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_ids = 'profile_ids_example' # str | the profiles whose achievements are requested.  (optional)

    try:
        # Achievements of the caller 
        api_response = api_instance.game_get_achievements(profile_ids=profile_ids)
        print("The response of GameApi->game_get_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | **str**| the profiles whose achievements are requested.  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_automatch_map**
> List[object] game_get_automatch_map()

Returns the matchmaking map pool

The pool of maps the matchmaker offers; the pool rotates between sessions.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Returns the matchmaking map pool
        api_response = api_instance.game_get_automatch_map()
        print("The response of GameApi->game_get_automatch_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_automatch_map: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_automatch_map_legacy**
> List[object] game_get_automatch_map_legacy()

Returns the matchmaking map pool (legacy path)

The pre-automatch2 route of the A4 client; same body as the automatch2 form.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Returns the matchmaking map pool (legacy path)
        api_response = api_instance.game_get_automatch_map_legacy()
        print("The response of GameApi->game_get_automatch_map_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_automatch_map_legacy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_available_achievements**
> List[object] game_get_available_achievements(signature=signature)

Achievement catalogue

The signed catalogue `[0, achievementRows, signature]` of the title; a
`signature` query that matches gets the short `[0, [], signature]` form. A1
has no catalogue.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    signature = 'signature_example' # str | when it matches, the short \"unchanged\" form is served. (optional)

    try:
        # Achievement catalogue
        api_response = api_instance.game_get_available_achievements(signature=signature)
        print("The response of GameApi->game_get_available_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_available_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature** | **str**| when it matches, the short \&quot;unchanged\&quot; form is served. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_available_community_events**
> List[object] game_get_available_community_events()

Available community events

A4 publishes a rolling ranked season (90-day windows dating from 2022-04-13,
current and previous) plus the menu backgrounds as the first rows; AoM serves
its Athens events (three daily skirmish-plus, two monthly pantheon-pinup) with
their ladders and ladder maps; A2 answers the seven-block shape of its event
list; A1/A3 answer `[0, [], []]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Available community events
        api_response = api_instance.game_get_available_community_events()
        print("The response of GameApi->game_get_available_community_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_available_community_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_available_leaderboards**
> List[object] game_get_available_leaderboards()

Ladder catalogue

The ladder catalogue of the title: `[0, <ladder rows>, ...]`, closing with
`[]` (not a signature). A1 has no catalogue and answers the body `null`. The
matchType rows carry five fields from the 2025 catalogues on.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Ladder catalogue
        api_response = api_instance.game_get_available_leaderboards()
        print("The response of GameApi->game_get_available_leaderboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_available_leaderboards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_avatar_stat_leader_board**
> List[object] game_get_avatar_stat_leader_board()

Avatar statistics ladder 

The avatar-statistics ladder: the ranking rows of the requested statistic.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Avatar statistics ladder 
        api_response = api_instance.game_get_avatar_stat_leader_board()
        print("The response of GameApi->game_get_avatar_stat_leader_board:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_avatar_stat_leader_board: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_challenge_progress_by_profile_id**
> List[object] game_get_challenge_progress_by_profile_id(profile_id=profile_id)

Challenge progress of another profile

The progress rows of `profile_id` (the same completed-by-default encoding) or `[0, []]` for an unknown id.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_id = 56 # int |  (optional)

    try:
        # Challenge progress of another profile
        api_response = api_instance.game_get_challenge_progress_by_profile_id(profile_id=profile_id)
        print("The response of GameApi->game_get_challenge_progress_by_profile_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_challenge_progress_by_profile_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_challenge_progress_get**
> List[object] game_get_challenge_progress_get()

Challenge progress (GET)

The challenge progress rows of the session user.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Challenge progress (GET)
        api_response = api_instance.game_get_challenge_progress_get()
        print("The response of GameApi->game_get_challenge_progress_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_challenge_progress_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_challenge_progress_post**
> List[object] game_get_challenge_progress_post()

Challenge progress (POST, legacy form)

The AoE3 legacy form of the same handler (no parameters).

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Challenge progress (POST, legacy form)
        api_response = api_instance.game_get_challenge_progress_post()
        print("The response of GameApi->game_get_challenge_progress_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_challenge_progress_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_challenges**
> List[object] game_get_challenges(signature=signature)

Challenge catalogue

The signed catalogue `[0, groups, definitions, signature]` of the title; the
matching-`signature` short form is `[0, [], [], signature]`. Anonymous.


### Example


```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)


# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    signature = 'signature_example' # str | when it matches, the short form is served. (optional)

    try:
        # Challenge catalogue
        api_response = api_instance.game_get_challenges(signature=signature)
        print("The response of GameApi->game_get_challenges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_challenges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature** | **str**| when it matches, the short form is served. | [optional] 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_chat_channels_get**
> List[object] game_get_chat_channels_get()

Lists the chat channels (GET)

`[0, channels, 100]` — the channels of the title, with the live member count
of each. A title without a channel catalogue answers an empty list.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Lists the chat channels (GET)
        api_response = api_instance.game_get_chat_channels_get()
        print("The response of GameApi->game_get_chat_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_chat_channels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_chat_channels_post**
> List[object] game_get_chat_channels_post()

Lists the chat channels (POST)

The AoE1/AoE3 legacy form of the same handler.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Lists the chat channels (POST)
        api_response = api_instance.game_get_chat_channels_post()
        print("The response of GameApi->game_get_chat_channels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_chat_channels_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_clan**
> List[object] game_get_clan(names)

Clans by name

Answers the clans named in `names` (a JSON array) as `ClanRow` rows; an
unknown name is skipped.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    names = 'names_example' # str | JSON array of the clan names.

    try:
        # Clans by name
        api_response = api_instance.game_get_clan(names)
        print("The response of GameApi->game_get_clan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_clan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **str**| JSON array of the clan names. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_clan_info_full**
> List[object] game_get_clan_info_full(name)

Full clan record

The full record of the clan `name`: the `ClanRow` of the clan followed by
its role permission rows (`[[rank, 9 permissions, role name,
locstringID], ...]`) and its member rows (`[[profile row,
membershipStatus, playerlistPermissionRank], ...]`; the rank is `-1`
without one).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    name = 'name_example' # str | the clan name.

    try:
        # Full clan record
        api_response = api_instance.game_get_clan_info_full(name)
        print("The response of GameApi->game_get_clan_info_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_clan_info_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the clan name. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_event_leaderboard**
> List[object] game_get_event_leaderboard(leaderboard_id=leaderboard_id, start=start, count=count, sort_by=sort_by)

Event leaderboard 

The leaderboard page of the requested event.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    leaderboard_id = 56 # int | ignored. (optional)
    start = 56 # int | ignored. (optional)
    count = 56 # int | ignored. (optional)
    sort_by = 56 # int | ignored. (optional)

    try:
        # Event leaderboard 
        api_response = api_instance.game_get_event_leaderboard(leaderboard_id=leaderboard_id, start=start, count=count, sort_by=sort_by)
        print("The response of GameApi->game_get_event_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_event_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_id** | **int**| ignored. | [optional] 
 **start** | **int**| ignored. | [optional] 
 **count** | **int**| ignored. | [optional] 
 **sort_by** | **int**| ignored. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_event_stats**
> List[object] game_get_event_stats(event_id=event_id, group_type=group_type, member_id=member_id)

Event statistics 

The statistics of the requested event: the profile rows, the totals and the
score blocks the title reports.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    event_id = 56 # int | the event. (optional)
    group_type = 56 # int | 1 in the captures. (optional)
    member_id = 56 # int | the profile whose statistics are requested. (optional)

    try:
        # Event statistics 
        api_response = api_instance.game_get_event_stats(event_id=event_id, group_type=group_type, member_id=member_id)
        print("The response of GameApi->game_get_event_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_event_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the event. | [optional] 
 **group_type** | **int**| 1 in the captures. | [optional] 
 **member_id** | **int**| the profile whose statistics are requested. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_inventory_by_profile_ids**
> List[object] game_get_inventory_by_profile_ids(profile_ids=profile_ids)

Inventories and locations of profiles

One inventory row and one location row per requested profile.
Items are served only for the caller's own profile.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids. (optional)

    try:
        # Inventories and locations of profiles
        api_response = api_instance.game_get_inventory_by_profile_ids(profile_ids=profile_ids)
        print("The response of GameApi->game_get_inventory_by_profile_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_inventory_by_profile_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | **str**| JSON array of profile ids. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_item_bundle_items_json**
> GameGetItemBundleItemsJson200Response game_get_item_bundle_items_json(signature=signature)

Item bundle catalogue (signed, anonymous)

The same signed-catalogue protocol for the item bundle catalogue, the
anonymous sibling of getItemDefinitionsJson (the clients fetch it before the
login handshake binds a session).


### Example


```python
import rlink_client
from rlink_client.models.game_get_item_bundle_items_json200_response import GameGetItemBundleItemsJson200Response
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)


# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    signature = 'signature_example' # str |  (optional)

    try:
        # Item bundle catalogue (signed, anonymous)
        api_response = api_instance.game_get_item_bundle_items_json(signature=signature)
        print("The response of GameApi->game_get_item_bundle_items_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_item_bundle_items_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature** | **str**|  | [optional] 

### Return type

[**GameGetItemBundleItemsJson200Response**](GameGetItemBundleItemsJson200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The keyed bundle body — &#x60;itemBundles&#x60; rows &#x60;{\&quot;itemBundleID\&quot;: \&quot;&lt;n&gt;\&quot;, \&quot;items\&quot;: [{id, definitionID, durabilityType, durability, metadata, permissionFlags, permissionMask}]}&#x60;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_item_definitions_json**
> GameGetItemDefinitionsJson200Response game_get_item_definitions_json(signature=signature)

Item definition catalogue (signed)

The keyed catalogue of item definitions, served with the `dataSignature` the
client verifies. A `signature` query matching the carried dataSignature gets
the short `{"result":0,"dataSignature":...}` body; otherwise the full
`{"result":0,"itemCategories":[...],"itemDefinitions":[...],"dataSignature":...}`
body is served.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.models.game_get_item_definitions_json200_response import GameGetItemDefinitionsJson200Response
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    signature = 'signature_example' # str | the dataSignature the client already holds; a match serves the short form. (optional)

    try:
        # Item definition catalogue (signed)
        api_response = api_instance.game_get_item_definitions_json(signature=signature)
        print("The response of GameApi->game_get_item_definitions_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_item_definitions_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature** | **str**| the dataSignature the client already holds; a match serves the short form. | [optional] 

### Return type

[**GameGetItemDefinitionsJson200Response**](GameGetItemDefinitionsJson200Response.md)

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The keyed catalogue body (or the short form). The categories are &#x60;{categoryID, name, categoryGroup, metadata}&#x60; and each definition &#x60;{id, name, imageData, metaData, available, version, level, categoryIDs, localizedName?, localizedDescription?}&#x60;. This response is raw JSON, not a positional array.  |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_item_loadouts**
> List[object] game_get_item_loadouts()

The item loadouts of the caller

The loadout rows of the caller's profile; a profile with none answers `[0,
[]]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # The item loadouts of the caller
        api_response = api_instance.game_get_item_loadouts()
        print("The response of GameApi->game_get_item_loadouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_item_loadouts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_item_prices**
> List[object] game_get_item_prices()

Item prices (empty catalogue)

The prices of the requested items and the running sales: `[0, [], 0, []]`
while no sale is running.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Item prices (empty catalogue)
        api_response = api_instance.game_get_item_prices()
        print("The response of GameApi->game_get_item_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_item_prices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_leader_board**
> List[object] game_get_leader_board(leaderboard_id=leaderboard_id, start=start, count=count, sort_by=sort_by)

Page of a ladder

The ranked page `[result, statGroups, profileInfo, leaderboardStats]` — one
row per entry, index-aligned. `start` is 1-based, `count` is capped at 1000; a
rating without a stored identity is served as a placeholder profile. The rows
are sorted by rating DESC, then profile id ASC.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    leaderboard_id = 56 # int | the ladder; <= 0 falls back to the title default (A2 3 solo RM, others 1). (optional)
    start = 1 # int | 1-based offset. (optional) (default to 1)
    count = 100 # int | page size, capped at 1000. (optional) (default to 100)
    sort_by = 56 # int | the sort of the page (the clients send 1, rating).  (optional)

    try:
        # Page of a ladder
        api_response = api_instance.game_get_leader_board(leaderboard_id=leaderboard_id, start=start, count=count, sort_by=sort_by)
        print("The response of GameApi->game_get_leader_board:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_leader_board: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_id** | **int**| the ladder; &lt;&#x3D; 0 falls back to the title default (A2 3 solo RM, others 1). | [optional] 
 **start** | **int**| 1-based offset. | [optional] [default to 1]
 **count** | **int**| page size, capped at 1000. | [optional] [default to 100]
 **sort_by** | **int**| the sort of the page (the clients send 1, rating).  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_level_rewards_table_json**
> GameGetLevelRewardsTableJson200Response game_get_level_rewards_table_json(signature=signature)

Level rewards table (signed)

The same protocol for the level rewards table of A4.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.models.game_get_level_rewards_table_json200_response import GameGetLevelRewardsTableJson200Response
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    signature = 'signature_example' # str |  (optional)

    try:
        # Level rewards table (signed)
        api_response = api_instance.game_get_level_rewards_table_json(signature=signature)
        print("The response of GameApi->game_get_level_rewards_table_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_level_rewards_table_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature** | **str**|  | [optional] 

### Return type

[**GameGetLevelRewardsTableJson200Response**](GameGetLevelRewardsTableJson200Response.md)

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The keyed body — levelRewardsTable rows &#x60;{category, subcategory, level, xp, itemBundleID, metadata}&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_news**
> List[object] game_get_news()

News of the title

The news entries of the title; the third block carries the community-event
rows of its events. Anonymous (no sessionID).


### Example


```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)


# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # News of the title
        api_response = api_instance.game_get_news()
        print("The response of GameApi->game_get_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_news: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_offline_messages**
> List[object] game_get_offline_messages()

Polls the offline chat inbox

The offline inbox of the caller: the queued messages, the system messages of
the title (channel invitations and challenge notifications of the
SYSTEM_OFFLINEITEM_* family) and the deletion markers.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Polls the offline chat inbox
        api_response = api_instance.game_get_offline_messages()
        print("The response of GameApi->game_get_offline_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_offline_messages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_party_stat**
> List[object] game_get_party_stat(statsids=statsids, leaderboard_id=leaderboard_id)

Ladder statistics of a party

Resolves each `statsids` stat group to its user and answers the three blocks plus one rating row per profile (the official answer carries one row per ladder the profile is rated on).

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    statsids = 'statsids_example' # str | JSON array of stat group ids. (optional)
    leaderboard_id = 56 # int |  (optional)

    try:
        # Ladder statistics of a party
        api_response = api_instance.game_get_party_stat(statsids=statsids, leaderboard_id=leaderboard_id)
        print("The response of GameApi->game_get_party_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_party_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statsids** | **str**| JSON array of stat group ids. | [optional] 
 **leaderboard_id** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_personal_stat**
> List[object] game_get_personal_stat(profileids=profileids, leaderboard_id=leaderboard_id)

Personal ladder statistics

The stat groups, profile rows, ladder rows and avatar stats of the requested
profiles. A profile with a rating carries its row; a first-time A4 account
answers empty blocks. An unparsable `profileids` answers the literal `null`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profileids = 'profileids_example' # str | JSON array of profile ids. (optional)
    leaderboard_id = 56 # int | resolves the ladder of the rating rows when present. (optional)

    try:
        # Personal ladder statistics
        api_response = api_instance.game_get_personal_stat(profileids=profileids, leaderboard_id=leaderboard_id)
        print("The response of GameApi->game_get_personal_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_personal_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileids** | **str**| JSON array of profile ids. | [optional] 
 **leaderboard_id** | **int**| resolves the ladder of the rating rows when present. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_personalized_sale_items**
> List[object] game_get_personalized_sale_items()

Personalized sales

The personalised sale of the profile: `[0, [], []]` while no sale is running.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Personalized sales
        api_response = api_instance.game_get_personalized_sale_items()
        print("The response of GameApi->game_get_personalized_sale_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_personalized_sale_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_presence_data**
> List[object] game_get_presence_data(signature=signature)

Returns the presence definition catalogue

The signed presence catalogue of the title: the presence definitions with
their localised labels, plus the 344-char dataSignature. A `signature` that
matches gets the short `{"result":0,"dataSignature":...}` form.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    signature = 'signature_example' # str | when it matches the catalogue signature the short form is served. (optional)

    try:
        # Returns the presence definition catalogue
        api_response = api_instance.game_get_presence_data(signature=signature)
        print("The response of GameApi->game_get_presence_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_presence_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature** | **str**| when it matches the catalogue signature the short form is served. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_profile_name**
> List[object] game_get_profile_name(profile_ids)

Returns profile rows by ids

Binds `profile_ids` (JSON array) and returns plain profile rows (no presence
tail). The answer has one row per requested id, in request order, with `null`
placeholders for the ids that have no profile.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids.

    try:
        # Returns profile rows by ids
        api_response = api_instance.game_get_profile_name(profile_ids)
        print("The response of GameApi->game_get_profile_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_profile_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | **str**| JSON array of profile ids. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_profile_property**
> List[object] game_get_profile_property(property_id, profile_id)

Reads one profile property

Returns `[0, [value]]` for `property_id` of `profile_id` — stored by
`addProfileProperty`; `[0, []]` when the property or the profile is
unknown. An officially invalid profile id (the captures show -2) is
answered with the same 200 + `[0,[]]` body, while the official
service returns HTTP 400 with an HTML error page.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    property_id = 'property_id_example' # str | e.g. appearOffline, PlayFabID, HaveShownNativeCivDisclaimer.
    profile_id = 56 # int | 

    try:
        # Reads one profile property
        api_response = api_instance.game_get_profile_property(property_id, profile_id)
        print("The response of GameApi->game_get_profile_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_profile_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| e.g. appearOffline, PlayFabID, HaveShownNativeCivDisclaimer. | 
 **profile_id** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_recent_match_history_get**
> List[object] game_get_recent_match_history_get(profile_ids=profile_ids)

Recent match history (GET)

The 30 most recent matches that involved any of the `profile_ids`, as
MatchHistoryRow entries: the counters, the custom updates, the version info
and the member ratings.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids (invalid ids dropped). (optional)

    try:
        # Recent match history (GET)
        api_response = api_instance.game_get_recent_match_history_get(profile_ids=profile_ids)
        print("The response of GameApi->game_get_recent_match_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_recent_match_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | **str**| JSON array of profile ids (invalid ids dropped). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_recent_match_history_post**
> List[object] game_get_recent_match_history_post(profile_ids=profile_ids)

Recent match history (POST, legacy form)

The AoE3 legacy form — the same handler with `profile_ids` in the body.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids. (optional)

    try:
        # Recent match history (POST, legacy form)
        api_response = api_instance.game_get_recent_match_history_post(profile_ids=profile_ids)
        print("The response of GameApi->game_get_recent_match_history_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_recent_match_history_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | **str**| JSON array of profile ids. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_recent_match_single_player_history**
> List[object] game_get_recent_match_single_player_history(profile_ids=profile_ids)

Single-player match history (fixed empty answer)

`[13, []]` — single-player matches are not published to the ladder.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profile_ids = 'profile_ids_example' # str | ignored. (optional)

    try:
        # Single-player match history (fixed empty answer)
        api_response = api_instance.game_get_recent_match_single_player_history(profile_ids=profile_ids)
        print("The response of GameApi->game_get_recent_match_single_player_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_recent_match_single_player_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | **str**| ignored. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_relationships_get**
> List[object] game_get_relationships_get()

Lists friends and recent players (GET)

Answers the 8-slot relationship block for the session user: the friends of the
account (A3/A4/AoM) or its last connections (A1/A2), from the Steam/Xbox
friendship graph, with the presence of each.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Lists friends and recent players (GET)
        api_response = api_instance.game_get_relationships_get()
        print("The response of GameApi->game_get_relationships_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_relationships_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_relationships_post**
> List[object] game_get_relationships_post()

Lists friends and recent players (POST)

The A1/AoE3 legacy form of the same handler.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Lists friends and recent players (POST)
        api_response = api_instance.game_get_relationships_post()
        print("The response of GameApi->game_get_relationships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_relationships_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_scheduled_sale_and_items**
> List[object] game_get_scheduled_sale_and_items()

Scheduled sales

The scheduled sale and its items: `[0, [], [], 0]` while no sale is running.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Scheduled sales
        api_response = api_instance.game_get_scheduled_sale_and_items()
        print("The response of GameApi->game_get_scheduled_sale_and_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_scheduled_sale_and_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_stat_groups_by_profile_ids**
> List[object] game_get_stat_groups_by_profile_ids(profileids=profileids, leaderboard_id=leaderboard_id)

Stat groups of profiles

Resolves the stat groups, profiles and rating rows of the requested ids.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profileids = 'profileids_example' # str | JSON array of profile ids. (optional)
    leaderboard_id = 56 # int |  (optional)

    try:
        # Stat groups of profiles
        api_response = api_instance.game_get_stat_groups_by_profile_ids(profileids=profileids, leaderboard_id=leaderboard_id)
        print("The response of GameApi->game_get_stat_groups_by_profile_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_stat_groups_by_profile_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileids** | **str**| JSON array of profile ids. | [optional] 
 **leaderboard_id** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_stats_for_leaderboard_by_profile_name**
> List[object] game_get_stats_for_leaderboard_by_profile_name(profileids=profileids, leaderboard_id=leaderboard_id)

Ladder statistics by platform name

Resolves the profiles by id and answers the three blocks plus the rating rows
of the resolved ladder.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    profileids = 'profileids_example' # str | JSON array of profile ids (the official client sends ids, not names, despite the route name). (optional)
    leaderboard_id = 56 # int | the ladder of the rating rows. (optional)

    try:
        # Ladder statistics by platform name
        api_response = api_instance.game_get_stats_for_leaderboard_by_profile_name(profileids=profileids, leaderboard_id=leaderboard_id)
        print("The response of GameApi->game_get_stats_for_leaderboard_by_profile_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_stats_for_leaderboard_by_profile_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileids** | **str**| JSON array of profile ids (the official client sends ids, not names, despite the route name). | [optional] 
 **leaderboard_id** | **int**| the ladder of the rating rows. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_get_store_tokens**
> List[object] game_get_store_tokens()

Returns the Microsoft Store tokens 

Answers the Microsoft Store pair of the account: an XSTS JWT (aud
onestore.microsoft.com) and its base64 signature.


### Example


```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)


# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Returns the Microsoft Store tokens 
        api_response = api_instance.game_get_store_tokens()
        print("The response of GameApi->game_get_store_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_get_store_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_grant_achievement**
> List[object] game_grant_achievement()

Grants an achievement

Claims the achievement for the client.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Grants an achievement
        api_response = api_instance.game_grant_achievement()
        print("The response of GameApi->game_grant_achievement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_grant_achievement: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_ignore**
> List[object] game_ignore(target_profile_id=target_profile_id)

Ignores a player

Adds the target to the ignore list of the profile and answers `[0,
profileInfo, []]`; an unknown target answers `[2, []]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    target_profile_id = 56 # int |  (optional)

    try:
        # Ignores a player
        api_response = api_instance.game_ignore(target_profile_id=target_profile_id)
        print("The response of GameApi->game_ignore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_ignore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_profile_id** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_join_channel**
> List[object] game_join_channel(chatroom_id)

Joins a chat channel

Answers `[0, chatroomID string, 0, roster]` with the members already
inside; the notify goes to those members only (not the joiner) as a
`ChannelJoinMessage` frame — `[chatroomID string, [0, profileRow]]`,
the official AoE3 shape.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    chatroom_id = 56 # int | 

    try:
        # Joins a chat channel
        api_response = api_instance.game_join_channel(chatroom_id)
        print("The response of GameApi->game_join_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_join_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatroom_id** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leave_channel**
> List[object] game_leave_channel(chatroom_id)

Leaves a chat channel

Removes the caller (a `ChannelLeaveMessage` frame `[channelId string, profileRow]` notifies the remaining members); `[0]`, or `[2]` on a binding failure, an unknown channel, or when the caller was not a member.

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    chatroom_id = 56 # int | 

    try:
        # Leaves a chat channel
        api_response = api_instance.game_leave_channel(chatroom_id)
        print("The response of GameApi->game_leave_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_leave_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatroom_id** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_logout**
> List[object] game_logout()

Closes the session

Removes the session user from its lobby advertisement, cancels any matchmaking
search, leaves every chat channel, sets
presence 0, deletes the session and answers `[0]`. The friends receive
`PresenceMessage` (presence 0).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Closes the session
        api_response = api_instance.game_logout()
        print("The response of GameApi->game_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_move_charges**
> List[object] game_move_charges(charges, deletes, from_item_ids, to_item_ids)

Moves item charges

Moves charges between item instances: `charges`, `deletes`,
`fromItemIDs` and `toItemIDs` are parallel JSON arrays of the same length,
so entry *i* moves `charges[i]` charges from `fromItemIDs[i]` to
`toItemIDs[i]` and deletes the source instance when `deletes[i]` is not 0.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    charges = 'charges_example' # str | JSON array of the charges moved per entry.
    deletes = 'deletes_example' # str | JSON array; non-zero deletes the source instance.
    from_item_ids = 'from_item_ids_example' # str | JSON array of the source item instance ids.
    to_item_ids = 'to_item_ids_example' # str | JSON array of the target item instance ids.

    try:
        # Moves item charges
        api_response = api_instance.game_move_charges(charges, deletes, from_item_ids, to_item_ids)
        print("The response of GameApi->game_move_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_move_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charges** | **str**| JSON array of the charges moved per entry. | 
 **deletes** | **str**| JSON array; non-zero deletes the source instance. | 
 **from_item_ids** | **str**| JSON array of the source item instance ids. | 
 **to_item_ids** | **str**| JSON array of the target item instance ids. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_move_item**
> List[object] game_move_item(item_ids, item_location_ids, pos_ids, slot_ids)

Moves items

Moves each listed item to the parallel location (a container item id is
allowed); `slotIDs` writes the `eslot` metadata key. `posIDs` is accepted and
not applied (the clients send -1 there).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    item_ids = 'item_ids_example' # str | JSON array.
    item_location_ids = 'item_location_ids_example' # str | JSON array — new location or container id; -1 keeps.
    pos_ids = 'pos_ids_example' # str | JSON array (length-checked, unused; the clients send -1).
    slot_ids = 'slot_ids_example' # str | JSON array — -1 keeps; else the eslot metadata key.

    try:
        # Moves items
        api_response = api_instance.game_move_item(item_ids, item_location_ids, pos_ids, slot_ids)
        print("The response of GameApi->game_move_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_move_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_ids** | **str**| JSON array. | 
 **item_location_ids** | **str**| JSON array — new location or container id; -1 keeps. | 
 **pos_ids** | **str**| JSON array (length-checked, unused; the clients send -1). | 
 **slot_ids** | **str**| JSON array — -1 keeps; else the eslot metadata key. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_open_item_pack**
> List[object] game_open_item_pack(item_instance_id, item_location_id, choices=choices)

Opens an item pack

Opens the item pack instance `itemInstance_id` stored at
`itemLocation_id`; `choices` (a JSON array) selects among the items of a
pack whose contents are a choice.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    item_instance_id = 56 # int | the pack instance.
    item_location_id = 56 # int | the location the instance is stored in.
    choices = 'choices_example' # str | JSON array of the chosen items; [] when the pack offers no choice. (optional)

    try:
        # Opens an item pack
        api_response = api_instance.game_open_item_pack(item_instance_id, item_location_id, choices=choices)
        print("The response of GameApi->game_open_item_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_open_item_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_instance_id** | **int**| the pack instance. | 
 **item_location_id** | **int**| the location the instance is stored in. | 
 **choices** | **str**| JSON array of the chosen items; [] when the pack offers no choice. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_create_or_report_single_player**
> List[object] game_party_create_or_report_single_player(create_match_key=create_match_key, match_key=match_key, match_type_id=match_type_id, mapname=mapname, appbincrc=appbincrc, datacrc=datacrc, moddllcrc=moddllcrc, moddllfile=moddllfile, modname=modname, modversion=modversion, options=options, slot_info=slot_info, version_flags=version_flags, is_complete=is_complete, counters_zip=counters_zip, item_updates=item_updates, results=results, team_ids=team_ids, race_ids=race_ids, xp_gained=xp_gained)

Creates or reports a single-player match

With `createMatchKey=1` a pending match is created and a `matchKey` returned;
with 0 the stored pending match of `matchKey` is reported through the same
pipeline as reportMatch (single-player queues are unrated) and, with
`isComplete=1`, issued replay descriptors for both kinds (the single-player
path `S_<matchID>_<sha>.gz`, uploader slot 1).


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    create_match_key = 56 # int | 1 create / 0 report. (optional)
    match_key = 'match_key_example' # str | the 32-hex key to report. (optional)
    match_type_id = 56 # int | scenario id (A4 55/873; AoM 61-69). (optional)
    mapname = 'mapname_example' # str |  (optional)
    appbincrc = 56 # int | may be negative. (optional)
    datacrc = 56 # int |  (optional)
    moddllcrc = 56 # int |  (optional)
    moddllfile = 'moddllfile_example' # str |  (optional)
    modname = 'modname_example' # str |  (optional)
    modversion = 'modversion_example' # str |  (optional)
    options = 'options_example' # str | opaque base64+zlib block. (optional)
    slot_info = 'slot_info_example' # str | opaque base64+zlib block. (optional)
    version_flags = 56 # int |  (optional)
    is_complete = 56 # int | 1 = report with replay descriptors. (optional)
    counters_zip = 'counters_zip_example' # str | same form as reportMatch. (optional)
    item_updates = 'item_updates_example' # str |  (optional)
    results = 'results_example' # str | JSON array; only player 0 (the session user) is scored. (optional)
    team_ids = 'team_ids_example' # str |  (optional)
    race_ids = 'race_ids_example' # str |  (optional)
    xp_gained = 'xp_gained_example' # str |  (optional)

    try:
        # Creates or reports a single-player match
        api_response = api_instance.game_party_create_or_report_single_player(create_match_key=create_match_key, match_key=match_key, match_type_id=match_type_id, mapname=mapname, appbincrc=appbincrc, datacrc=datacrc, moddllcrc=moddllcrc, moddllfile=moddllfile, modname=modname, modversion=modversion, options=options, slot_info=slot_info, version_flags=version_flags, is_complete=is_complete, counters_zip=counters_zip, item_updates=item_updates, results=results, team_ids=team_ids, race_ids=race_ids, xp_gained=xp_gained)
        print("The response of GameApi->game_party_create_or_report_single_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_create_or_report_single_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_match_key** | **int**| 1 create / 0 report. | [optional] 
 **match_key** | **str**| the 32-hex key to report. | [optional] 
 **match_type_id** | **int**| scenario id (A4 55/873; AoM 61-69). | [optional] 
 **mapname** | **str**|  | [optional] 
 **appbincrc** | **int**| may be negative. | [optional] 
 **datacrc** | **int**|  | [optional] 
 **moddllcrc** | **int**|  | [optional] 
 **moddllfile** | **str**|  | [optional] 
 **modname** | **str**|  | [optional] 
 **modversion** | **str**|  | [optional] 
 **options** | **str**| opaque base64+zlib block. | [optional] 
 **slot_info** | **str**| opaque base64+zlib block. | [optional] 
 **version_flags** | **int**|  | [optional] 
 **is_complete** | **int**| 1 &#x3D; report with replay descriptors. | [optional] 
 **counters_zip** | **str**| same form as reportMatch. | [optional] 
 **item_updates** | **str**|  | [optional] 
 **results** | **str**| JSON array; only player 0 (the session user) is scored. | [optional] 
 **team_ids** | **str**|  | [optional] 
 **race_ids** | **str**|  | [optional] 
 **xp_gained** | **str**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_finalize_replay_upload**
> List[object] game_party_finalize_replay_upload(match_id=match_id, url=url, size=size, finalize_result=finalize_result, is_single_player=is_single_player, error_string=error_string)

Confirms or discards a replay upload

When `finalizeResult` is not 1 the replay blob behind `url` (the key below
`/cloudfiles/`) is deleted; the answer is `[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | logged only. (optional)
    url = 'url_example' # str | the descriptor URL whose blob is finalized or deleted. (optional)
    size = 56 # int | logged only. (optional)
    finalize_result = 56 # int | 1 = success; anything else deletes the blob. (optional)
    is_single_player = 56 # int | logged only. (optional)
    error_string = 'error_string_example' # str | logged only. (optional)

    try:
        # Confirms or discards a replay upload
        api_response = api_instance.game_party_finalize_replay_upload(match_id=match_id, url=url, size=size, finalize_result=finalize_result, is_single_player=is_single_player, error_string=error_string)
        print("The response of GameApi->game_party_finalize_replay_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_finalize_replay_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| logged only. | [optional] 
 **url** | **str**| the descriptor URL whose blob is finalized or deleted. | [optional] 
 **size** | **int**| logged only. | [optional] 
 **finalize_result** | **int**| 1 &#x3D; success; anything else deletes the blob. | [optional] 
 **is_single_player** | **int**| logged only. | [optional] 
 **error_string** | **str**| logged only. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_peer_add**
> List[object] game_party_peer_add(match_id, profile_ids, race_ids, team_ids)

Adds peers to the lobby

Host-only. Binds the parallel arrays `profile_ids`, `race_ids` and `teamIDs`
(equal lengths), adds every peer and rolls the whole batch back when one of
them fails. Every peer added by this call is removed again on failure; the
peers already in the lobby stay.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | advertisement id.
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids.
    race_ids = 'race_ids_example' # str | JSON array of civilization ids (AoE2 sends -1, AoE3 0).
    team_ids = 'team_ids_example' # str | JSON array of team ids (same length as profile_ids).

    try:
        # Adds peers to the lobby
        api_response = api_instance.game_party_peer_add(match_id, profile_ids, race_ids, team_ids)
        print("The response of GameApi->game_party_peer_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_peer_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| advertisement id. | 
 **profile_ids** | **str**| JSON array of profile ids. | 
 **race_ids** | **str**| JSON array of civilization ids (AoE2 sends -1, AoE3 0). | 
 **team_ids** | **str**| JSON array of team ids (same length as profile_ids). | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_peer_update**
> List[object] game_party_peer_update(match_id, profile_ids, race_ids, team_ids)

Updates peers of the lobby

Host-only. Updates the race and team of the peers that are already in the
lobby.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | 
    profile_ids = 'profile_ids_example' # str | JSON array of existing peers.
    race_ids = 'race_ids_example' # str | JSON array of new civilizations.
    team_ids = 'team_ids_example' # str | JSON array of new teams.

    try:
        # Updates peers of the lobby
        api_response = api_instance.game_party_peer_update(match_id, profile_ids, race_ids, team_ids)
        print("The response of GameApi->game_party_peer_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_peer_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 
 **profile_ids** | **str**| JSON array of existing peers. | 
 **race_ids** | **str**| JSON array of new civilizations. | 
 **team_ids** | **str**| JSON array of new teams. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_report_match**
> List[object] game_party_report_match(match_id, profile_ids, results, team_ids=team_ids, race_ids=race_ids, xp_gained=xp_gained, counters_zip=counters_zip, item_updates=item_updates, challenge_updates=challenge_updates, event_challenge_updates=event_challenge_updates, client_updates=client_updates, simplayer_ids=simplayer_ids, check_sums=check_sums, last_call_time=last_call_time)

Reports the result of a match

Persists the match and every player row, updates ratings (Elo for the ranked
ladders, the hidden MMR for the queues), the win/loss/streak counters and the
challenge progress from the client-update blobs, then answers 16 slots.

`countersZip` is a JSON string wrapping base64(gzip(JSON array of per-player
counter-object strings)), with one entry per profile: an unparsable value
empties the counters and the match is still stored; an empty value keeps
whatever the first reporter stored. `itemUpdates` is a JSON array of
per-player JSON strings whose keys (itemUpdates / challengeUpdates /
eventChallengeUpdates / clientUpdates) default to `[]`/`{}`. `simplayerIDs` is
int64 because AoE III sends 4294967295 for "no sim player".


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | 
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids.
    results = 'results_example' # str | JSON array of result codes: 1 win, 0 loss, 3 draw/incomplete.
    team_ids = 'team_ids_example' # str | JSON array, index-aligned; missing defaults 0. (optional)
    race_ids = 'race_ids_example' # str | JSON array, index-aligned. (optional)
    xp_gained = 'xp_gained_example' # str | JSON array, index-aligned. (optional)
    counters_zip = 'counters_zip_example' # str | base64(gzip(JSON array of per-player counter blobs)); \\\"\\\" keeps stored. (optional)
    item_updates = 'item_updates_example' # str | JSON array of per-player update JSON strings. (optional)
    challenge_updates = 'challenge_updates_example' # str | alternative carrier of the same block, accepted. (optional)
    event_challenge_updates = 'event_challenge_updates_example' # str | alternative carrier, accepted. (optional)
    client_updates = 'client_updates_example' # str | alternative carrier, accepted. (optional)
    simplayer_ids = 'simplayer_ids_example' # str | JSON array of int64 (AoE III sends 4294967295); logged only. (optional)
    check_sums = 'check_sums_example' # str | JSON array of int32; logged only. (optional)
    last_call_time = 56 # int | logged only. (optional)

    try:
        # Reports the result of a match
        api_response = api_instance.game_party_report_match(match_id, profile_ids, results, team_ids=team_ids, race_ids=race_ids, xp_gained=xp_gained, counters_zip=counters_zip, item_updates=item_updates, challenge_updates=challenge_updates, event_challenge_updates=event_challenge_updates, client_updates=client_updates, simplayer_ids=simplayer_ids, check_sums=check_sums, last_call_time=last_call_time)
        print("The response of GameApi->game_party_report_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_report_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 
 **profile_ids** | **str**| JSON array of profile ids. | 
 **results** | **str**| JSON array of result codes: 1 win, 0 loss, 3 draw/incomplete. | 
 **team_ids** | **str**| JSON array, index-aligned; missing defaults 0. | [optional] 
 **race_ids** | **str**| JSON array, index-aligned. | [optional] 
 **xp_gained** | **str**| JSON array, index-aligned. | [optional] 
 **counters_zip** | **str**| base64(gzip(JSON array of per-player counter blobs)); \\\&quot;\\\&quot; keeps stored. | [optional] 
 **item_updates** | **str**| JSON array of per-player update JSON strings. | [optional] 
 **challenge_updates** | **str**| alternative carrier of the same block, accepted. | [optional] 
 **event_challenge_updates** | **str**| alternative carrier, accepted. | [optional] 
 **client_updates** | **str**| alternative carrier, accepted. | [optional] 
 **simplayer_ids** | **str**| JSON array of int64 (AoE III sends 4294967295); logged only. | [optional] 
 **check_sums** | **str**| JSON array of int32; logged only. | [optional] 
 **last_call_time** | **int**| logged only. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_send_match_chat**
> List[object] game_party_send_match_chat(message_type_id=message_type_id, match_id=match_id, broadcast=broadcast, message=message, metadata=metadata, to_profile_ids=to_profile_ids, to_profile_id=to_profile_id)

Sends a chat message inside a match

The sender must be a peer of the advertisement. Every listed receiver with a
session gets a `MatchReceivedChatMessage` frame (`[senderId, message, message,
messageType, matchID, (metadata)]`, the 6-slot form from client library 194),
or the same frame queued through readSession when it is offline.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    message_type_id = 56 # int | message type (0 in the captures). (optional)
    match_id = 56 # int | advertisement id. (optional)
    broadcast = True # bool | stored, unused for the fan-out. (optional)
    message = 'message_example' # str |  (optional)
    metadata = 'metadata_example' # str | JSON blob, encoded only from client library 194. (optional)
    to_profile_ids = 'to_profile_ids_example' # str | JSON array of receivers (modern libraries). (optional)
    to_profile_id = 56 # int | single receiver (AoE3 below 194). (optional)

    try:
        # Sends a chat message inside a match
        api_response = api_instance.game_party_send_match_chat(message_type_id=message_type_id, match_id=match_id, broadcast=broadcast, message=message, metadata=metadata, to_profile_ids=to_profile_ids, to_profile_id=to_profile_id)
        print("The response of GameApi->game_party_send_match_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_send_match_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_type_id** | **int**| message type (0 in the captures). | [optional] 
 **match_id** | **int**| advertisement id. | [optional] 
 **broadcast** | **bool**| stored, unused for the fan-out. | [optional] 
 **message** | **str**|  | [optional] 
 **metadata** | **str**| JSON blob, encoded only from client library 194. | [optional] 
 **to_profile_ids** | **str**| JSON array of receivers (modern libraries). | [optional] 
 **to_profile_id** | **int**| single receiver (AoE3 below 194). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_update_host**
> List[object] game_party_update_host(match_id)

Transfers the host of the lobby

The first remaining peer becomes the host (the migration the client performs
when the host leaves). The answer is `[0]`, also when the caller already is
the host; some captures answer `1` for the same request.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    match_id = 56 # int | 

    try:
        # Transfers the host of the lobby
        api_response = api_instance.game_party_update_host(match_id)
        print("The response of GameApi->game_party_update_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_party_update_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_platform_login**
> List[object] game_platform_login(platform_user_id, alias, account_type=account_type, title=title, mac_address=mac_address, client_lib_version=client_lib_version)

Logs in to the game service and creates the session 

Authenticates the platform account from `accountType`, `platformUserID`,
`alias`, `title`, `macAddress`, `clientLibVersion` and the platform ticket in
`auth`, sets the `reliclink` cookie, publishes the join presence, notifies the
other connected clients and returns
the relay servers of the account's region. The session token travels as
`connectionToken` in the answer and is the `sessionID` every other route
sends.

It is an anonymous route (it is the one that mints the session). When the
platform ticket cannot be validated the answer is the 2-coded array, whose
`serverTime` slot — unlike the success path — carries an RFC3339 string.

AoE1 sends every parameter in the query string and repeats them in the body
(the binder reads the body); it also receives one extra top-level slot
(`extra`, always `[]`) after `banMessage`, and no `stats` row inside
`selectProfile` (null instead of `[]`).

`selectProfile.leaderboardStats` carries one row per ladder the profile is
placed on; `accountInfo` carries the country and currency of the account; the
`Request-Context` header identifies the application (AoE1-3 use their fixed
application id, newer deployments vary) and `Request-Path` carries the request
path.


### Example


```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)


# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    platform_user_id = 56 # int | Steam id64 / Xbox id.
    alias = 'alias_example' # str | display name.
    account_type = 'account_type_example' # str | XBOXLIVE selects the Xbox identity (account type 9, `/xboxlive/...` path). (optional)
    title = 'title_example' # str | e.g. age2/athens. (optional)
    mac_address = 'mac_address_example' # str | network MAC address. (optional)
    client_lib_version = 56 # int | drives the row shapes (190 sanitized alias, 193 trailing -1, 194 \\\"The Baltic Powers\\\" formats). (optional)

    try:
        # Logs in to the game service and creates the session 
        api_response = api_instance.game_platform_login(platform_user_id, alias, account_type=account_type, title=title, mac_address=mac_address, client_lib_version=client_lib_version)
        print("The response of GameApi->game_platform_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_platform_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_user_id** | **int**| Steam id64 / Xbox id. | 
 **alias** | **str**| display name. | 
 **account_type** | **str**| XBOXLIVE selects the Xbox identity (account type 9, &#x60;/xboxlive/...&#x60; path). | [optional] 
 **title** | **str**| e.g. age2/athens. | [optional] 
 **mac_address** | **str**| network MAC address. | [optional] 
 **client_lib_version** | **int**| drives the row shapes (190 sanitized alias, 193 trailing -1, 194 \\\&quot;The Baltic Powers\\\&quot; formats). | [optional] 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional login answer (or the 2-coded error array); sets the cookies &#x60;reliclink&#x60; (&#x60;Expires&#x60;/&#x60;Max-Age&#x60; 1h) and the headers &#x60;Request-Context&#x60;, &#x60;Cache-Control&#x60;, &#x60;Expires&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_read_session**
> List[object] game_read_session(ack=ack)

Polls the queued notification frames

The fall-back notification channel when the client has no live WebSocket:
answers with every frame queued on the session (the same frames `/wss/`
pushes, envelope `[0, <action>, <subjectUserId>, <payload>]`, message list as explained
in the websocket API spec, long-polling up to 19 s; `ack` is the last
message id the client processed and is echoed when nothing was queued. An
absent or unparsable `ack` binds as 0. The message counter advances by one per
frame of the answer, which is what the AoE I/AoE III (legacy) client expects.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    ack = 56 # int | last processed message id. (optional)

    try:
        # Polls the queued notification frames
        api_response = api_instance.game_read_session(ack=ack)
        print("The response of GameApi->game_read_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_read_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ack** | **int**| last processed message id. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_reply_to_invitation**
> List[object] game_reply_to_invitation(gatheringid, invitationreply, inviterid)

Answers an invitation

Accepts or declines: the inviter receives a `ReplyInvitationMessage` frame
(`[replierProfile row, gatheringid, "1"|"0"]`, the official AoE4 shape). A
reply from a player that was never invited still answers `[0]` and notifies.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    gatheringid = 56 # int | 
    invitationreply = 'invitationreply_example' # str | \\\"0\\\" decline / \\\"1\\\" accept.
    inviterid = 56 # int | must be a peer of the lobby.

    try:
        # Answers an invitation
        api_response = api_instance.game_reply_to_invitation(gatheringid, invitationreply, inviterid)
        print("The response of GameApi->game_reply_to_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_reply_to_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gatheringid** | **int**|  | 
 **invitationreply** | **str**| \\\&quot;0\\\&quot; decline / \\\&quot;1\\\&quot; accept. | 
 **inviterid** | **int**| must be a peer of the lobby. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_report_user**
> List[object] game_report_user()

Reports a player

Reports the target profile with the requested category and text and answers
`[0, 0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Reports a player
        api_response = api_instance.game_report_user()
        print("The response of GameApi->game_report_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_report_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_send_text**
> List[object] game_send_text(chatroom_id, message)

Sends a message to a channel

The sender must be a member; every member's session receives a
`ChannelChatMessage` frame. From client library 194 the frame tail carries the
message twice.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    chatroom_id = 56 # int | 
    message = 'message_example' # str | 

    try:
        # Sends a message to a channel
        api_response = api_instance.game_send_text(chatroom_id, message)
        print("The response of GameApi->game_send_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_send_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatroom_id** | **int**|  | 
 **message** | **str**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_send_whisper**
> List[object] game_send_whisper(message, recipient_id)

Sends a whisper (single-recipient legacy form)

Same handler as `sendWhispers` with a single recipient id. The
receiver's session gets a `PersonalChatMessage` frame
(`[senderProfile, "", message]` — the pre-194 tail). Not in the
captures, registered for symmetry with the observed plural form.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    message = 'message_example' # str | 
    recipient_id = 56 # int | 

    try:
        # Sends a whisper (single-recipient legacy form)
        api_response = api_instance.game_send_whisper(message, recipient_id)
        print("The response of GameApi->game_send_whisper:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_send_whisper: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**|  | 
 **recipient_id** | **int**|  | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_send_whispers**
> List[object] game_send_whispers(message, recipient_ids)

Sends a whisper to several recipients

Every online recipient's session receives a `PersonalChatMessage` frame
(`[senderProfile, "", "", message, message]`, the shape of the AoE4/AoM
frames); the acknowledgment carries one nested code per batch.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    message = 'message_example' # str | 
    recipient_ids = 'recipient_ids_example' # str | JSON array of profile ids.

    try:
        # Sends a whisper to several recipients
        api_response = api_instance.game_send_whispers(message, recipient_ids)
        print("The response of GameApi->game_send_whispers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_send_whispers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**|  | 
 **recipient_ids** | **str**| JSON array of profile ids. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_set_avatar_metadata**
> List[object] game_set_avatar_metadata(meta_data)

Stores the avatar metadata

Binds `metaData` (a JSON body `{"metaData": ...}` is accepted too) and
stores it per user; the value is echoed verbatim in the profile rows
from then on. A1 sends a full URL, A3/AoM JSON of the form
`{"v":1,...}`/`{"v":2,...}`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    meta_data = 'meta_data_example' # str | raw metadata string stored and echoed in profile rows.

    try:
        # Stores the avatar metadata
        api_response = api_instance.game_set_avatar_metadata(meta_data)
        print("The response of GameApi->game_set_avatar_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_set_avatar_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_data** | **str**| raw metadata string stored and echoed in profile rows. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_set_avatar_stat_values**
> List[object] game_set_avatar_stat_values(avatar_stat_ids, values, update_types)

Stores avatar statistic values

Binds the parallel `avatarStat_ids`, `values` and `updateTypes` arrays (equal
lengths) and stores the stats. Every
stored stat is announced with an `AvatarStatsUpdatedMessage` frame carrying
the updated rows.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    avatar_stat_ids = 'avatar_stat_ids_example' # str | JSON array of stat definition ids.
    values = 'values_example' # str | JSON array of int64 values.
    update_types = 'update_types_example' # str | JSON array of int32 update types.

    try:
        # Stores avatar statistic values
        api_response = api_instance.game_set_avatar_stat_values(avatar_stat_ids, values, update_types)
        print("The response of GameApi->game_set_avatar_stat_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_set_avatar_stat_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_stat_ids** | **str**| JSON array of stat definition ids. | 
 **values** | **str**| JSON array of int64 values. | 
 **update_types** | **str**| JSON array of int32 update types. | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_set_crossplay_enabled**
> List[object] game_set_crossplay_enabled(crossplay_enabled=crossplay_enabled)

Enables crossplay

Reads `crossplayEnabled` (the AoE1 client names it `enable`) from the body and
answers `[0]` when it is `"1"`, `[2]` otherwise. Only the enable path appears
in the captures.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    crossplay_enabled = 'crossplay_enabled_example' # str | 1 to enable; the body is read, not the query string (A1 fallback name: enable). (optional)

    try:
        # Enables crossplay
        api_response = api_instance.game_set_crossplay_enabled(crossplay_enabled=crossplay_enabled)
        print("The response of GameApi->game_set_crossplay_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_set_crossplay_enabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossplay_enabled** | **str**| 1 to enable; the body is read, not the query string (A1 fallback name: enable). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_set_language**
> List[object] game_set_language()

Sets the client language 

Stores the client language in the account and answers `[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Sets the client language 
        api_response = api_instance.game_set_language()
        print("The response of GameApi->game_set_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_set_language: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_set_presence**
> List[object] game_set_presence(presence_id=presence_id)

Sets the presence

Stores `presence_id` for the session user and broadcasts a `PresenceMessage`
frame (`[profile row + presence tail]`) to every session, including the
caller's own. The first presence 1 of a session answers `[2]`, the later ones
`[0]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    presence_id = 56 # int | the definition id (A2 1..40; e.g. AoM 2/7/36). (optional)

    try:
        # Sets the presence
        api_response = api_instance.game_set_presence(presence_id=presence_id)
        print("The response of GameApi->game_set_presence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_set_presence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presence_id** | **int**| the definition id (A2 1..40; e.g. AoM 2/7/36). | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_set_presence_property**
> List[object] game_set_presence_property(presence_property_def_id=presence_property_def_id, value=value)

Sets one presence property

Stores the `[propertyDefID, value]` pair on the caller's presence
(an empty value deletes the property) and broadcasts the same
`PresenceMessage` frame so the clients see the change.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    presence_property_def_id = 56 # int | property definition id (e.g. 1409823 with the platform session AoM 1). (optional)
    value = 'value_example' # str | free text (\\\"RP_In_The_Main_Menu\\\" or a session id); \\\"\\\" deletes. (optional)

    try:
        # Sets one presence property
        api_response = api_instance.game_set_presence_property(presence_property_def_id=presence_property_def_id, value=value)
        print("The response of GameApi->game_set_presence_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_set_presence_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presence_property_def_id** | **int**| property definition id (e.g. 1409823 with the platform session AoM 1). | [optional] 
 **value** | **str**| free text (\\\&quot;RP_In_The_Main_Menu\\\&quot; or a session id); \\\&quot;\\\&quot; deletes. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_sign_items**
> List[object] game_sign_items(item_ids)

Signs an item list

Signs the `crc` the client computed over the item list with the service's
signing key (crc32 → SHA-512 → the RelicLink PKCS#1 v1.5 variant, the same
344-char signature family) and answers `[0, "<signature>"]`; a refused request
answers `[2, ""]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    item_ids = 'item_ids_example' # str | the raw value is signed verbatim (crc32 of the string).

    try:
        # Signs an item list
        api_response = api_instance.game_sign_items(item_ids)
        print("The response of GameApi->game_sign_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_sign_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_ids** | **str**| the raw value is signed verbatim (crc32 of the string). | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_update_challenge_progress**
> List[object] game_update_challenge_progress(progress_id=progress_id, completion_count=completion_count)

Adds single-player challenge progress (A3 legacy form)

Walks the payload for challenge records keyed by `progressID` (A3 legacy) or
`definition.definitionID`, merges them into the progress of the profile
(existing fields are never erased) and answers `[0, <updated rows>, []]`; a
request that cannot be decoded answers `[2, [], []]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    progress_id = 56 # int |  (optional)
    completion_count = 56 # int |  (optional)

    try:
        # Adds single-player challenge progress (A3 legacy form)
        api_response = api_instance.game_update_challenge_progress(progress_id=progress_id, completion_count=completion_count)
        print("The response of GameApi->game_update_challenge_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_update_challenge_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **progress_id** | **int**|  | [optional] 
 **completion_count** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_update_challenge_progress_batched**
> List[object] game_update_challenge_progress_batched(progress_ids=progress_ids, update_amounts=update_amounts)

Adds batched challenge progress

Applies the update amounts against the challenge definition
targets. Because every record starts completed, a batch without
work answers `[0]` and writes nothing. A decode/store failure
answers the bare `[2]`. The A4 client posts its fields as form
data; other builds send the same names as a JSON body.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    progress_ids = 'progress_ids_example' # str | JSON array of progress ids. (optional)
    update_amounts = 'update_amounts_example' # str | JSON array of int64 amounts, index-aligned. (optional)

    try:
        # Adds batched challenge progress
        api_response = api_instance.game_update_challenge_progress_batched(progress_ids=progress_ids, update_amounts=update_amounts)
        print("The response of GameApi->game_update_challenge_progress_batched:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_update_challenge_progress_batched: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **progress_ids** | **str**| JSON array of progress ids. | [optional] 
 **update_amounts** | **str**| JSON array of int64 amounts, index-aligned. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_update_clan**
> List[object] game_update_clan(clan_list_id, description=description, icon=icon, join_policy=join_policy, message_of_the_day=message_of_the_day, metadata=metadata, tags=tags)

Updates a clan

Updates the clan `clanList_id` with the fields of the request.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    clan_list_id = 56 # int | the clan.
    description = 'description_example' # str | the public description. (optional)
    icon = 'icon_example' # str | the crest id (e.g. CR-001). (optional)
    join_policy = 56 # int | the join policy (0 open, 1 invite/request only). (optional)
    message_of_the_day = 'message_of_the_day_example' # str | the message shown to the members. (optional)
    metadata = 'metadata_example' # str | the clan metadata. (optional)
    tags = 'tags_example' # str | JSON array of the clan tags. (optional)

    try:
        # Updates a clan
        api_response = api_instance.game_update_clan(clan_list_id, description=description, icon=icon, join_policy=join_policy, message_of_the_day=message_of_the_day, metadata=metadata, tags=tags)
        print("The response of GameApi->game_update_clan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_update_clan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_list_id** | **int**| the clan. | 
 **description** | **str**| the public description. | [optional] 
 **icon** | **str**| the crest id (e.g. CR-001). | [optional] 
 **join_policy** | **int**| the join policy (0 open, 1 invite/request only). | [optional] 
 **message_of_the_day** | **str**| the message shown to the members. | [optional] 
 **metadata** | **str**| the clan metadata. | [optional] 
 **tags** | **str**| JSON array of the clan tags. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_update_item_attributes**
> List[object] game_update_item_attributes(attribute_keys, attribute_values, item_instance_ids, xp_gains)

Updates item attributes

Writes the per-item attribute keys. `is_new` stores the bare value;
every other key is written with the source/mtype pair — the official
rows show only the value slot (clients tolerate the extra keys). 

### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    attribute_keys = 'attribute_keys_example' # str | JSON array of per-item string arrays.
    attribute_values = 'attribute_values_example' # str | JSON array of per-item string arrays, parallel.
    item_instance_ids = 'item_instance_ids_example' # str | JSON array of item ids.
    xp_gains = 'xp_gains_example' # str | JSON array (length-checked, unused; the clients send -1).

    try:
        # Updates item attributes
        api_response = api_instance.game_update_item_attributes(attribute_keys, attribute_values, item_instance_ids, xp_gains)
        print("The response of GameApi->game_update_item_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_update_item_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_keys** | **str**| JSON array of per-item string arrays. | 
 **attribute_values** | **str**| JSON array of per-item string arrays, parallel. | 
 **item_instance_ids** | **str**| JSON array of item ids. | 
 **xp_gains** | **str**| JSON array (length-checked, unused; the clients send -1). | 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_update_item_loadout**
> List[object] game_update_item_loadout(id, name, type, item_or_loc_ids=item_or_loc_ids)

Updates an item loadout

Replaces the name, type and item ids of the loadout and answers `[0,
[loadoutRow]]`.


### Example

* Api Key Authentication (GameSession):

```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: GameSession
configuration.api_key['GameSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GameSession'] = 'Bearer'

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    type = 56 # int | 
    item_or_loc_ids = 'item_or_loc_ids_example' # str | officially a JSON array string — see the binding defect note. (optional)

    try:
        # Updates an item loadout
        api_response = api_instance.game_update_item_loadout(id, name, type, item_or_loc_ids=item_or_loc_ids)
        print("The response of GameApi->game_update_item_loadout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameApi->game_update_item_loadout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **type** | **int**|  | 
 **item_or_loc_ids** | **str**| officially a JSON array string — see the binding defect note. | [optional] 

### Return type

**List[object]**

### Authorization

[GameSession](../README.md#GameSession)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positional JSON array; the slot order is in the operation&#39;s &#x60;x-response-positions&#x60;. |  -  |
**401** | Missing or unknown session credential. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_web_socket**
> game_web_socket()

Notification socket (WebSocket)

Upgrades the connection. The first frame a client must send binds the session:
`{"operation": 0, "sessionToken": "<connectionToken>"}` (the platformlogin
token) within 60 seconds — a missing or invalid bind closes the socket with
code 1000 and a reason. The client's `{"operation": 1, "ackCount": N}`
keepalives are accepted as activity; an `operation:0` with a newer token
rebinds the socket to the new session. While open, the socket refreshes the
session every 30 seconds; one socket per session (the newest wins). From then
on the service pushes text frames `[0, <action>, <recipientProfileId>,
<payload>]`: friend events, presence, chat, invitations, platform session
updates, match start, match results, avatar stats and matchmaking joins — the
frames produced by the REST calls of other clients (per-action payload slots
in websockets API spec). A client without a live socket receives the
same frames queued through readSession. The frame families also include the
challenge, achievement, item, offline-message, friend-request and
session-status actions of the client library.


### Example


```python
import rlink_client
from rlink_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aoe-api.worldsedgelink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.worldsedgelink.com"
)


# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rlink_client.GameApi(api_client)

    try:
        # Notification socket (WebSocket)
        api_instance.game_web_socket()
    except Exception as e:
        print("Exception when calling GameApi->game_web_socket: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching to the WebSocket protocol; notification frames follow. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

