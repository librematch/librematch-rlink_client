# rlink-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 24.11.01
- Package version: 1.0.0
- Generator version: 7.11.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import rlink_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rlink_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = rlink_client.DefaultApi(api_client)
    join_policies = [0,1,2] # int | 
    name = 'name_example' # str | 
    tags = '[]' # str | 
    start = 0 # int | 
    count = 200 # int | 
    title = '[\"age2\",\"age1\"]' # str |  (optional)

    try:
        api_response = api_instance.community_clan_find(join_policies, name, tags, start, count, title=title)
        print("The response of DefaultApi->community_clan_find:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->community_clan_find: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://aoe-api.worldsedgelink.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**community_clan_find**](docs/DefaultApi.md#community_clan_find) | **GET** /community/clan/find | 
*DefaultApi* | [**community_find_advertisements**](docs/DefaultApi.md#community_find_advertisements) | **GET** /community/advertisement/findAdvertisements | 
*DefaultApi* | [**community_get_achievements**](docs/DefaultApi.md#community_get_achievements) | **GET** /community/achievement/getAchievements | 
*DefaultApi* | [**community_get_available_achievements**](docs/DefaultApi.md#community_get_available_achievements) | **GET** /community/achievement/getAvailableAchievements | 
*DefaultApi* | [**community_get_available_community_events**](docs/DefaultApi.md#community_get_available_community_events) | **GET** /community/CommunityEvent/getAvailableCommunityEvents | 
*DefaultApi* | [**community_get_available_leaderboards**](docs/DefaultApi.md#community_get_available_leaderboards) | **GET** /community/leaderboard/getAvailableLeaderboards | 
*DefaultApi* | [**community_get_avatar_stat_for_profile**](docs/DefaultApi.md#community_get_avatar_stat_for_profile) | **GET** /community/leaderboard/GetAvatarStatForProfile | 
*DefaultApi* | [**community_get_clan_info_full**](docs/DefaultApi.md#community_get_clan_info_full) | **GET** /community/clan/getClanInfoFull | 
*DefaultApi* | [**community_get_inventory_by_profile_ids**](docs/DefaultApi.md#community_get_inventory_by_profile_ids) | **GET** /community/item/getInventoryByProfileIDs | 
*DefaultApi* | [**community_get_leaderboard2**](docs/DefaultApi.md#community_get_leaderboard2) | **GET** /community/leaderboard/getLeaderboard2 | 
*DefaultApi* | [**community_get_personal_stat**](docs/DefaultApi.md#community_get_personal_stat) | **GET** /community/leaderboard/GetPersonalStat | 
*DefaultApi* | [**community_get_recent_match_history**](docs/DefaultApi.md#community_get_recent_match_history) | **GET** /community/leaderboard/getRecentMatchHistory | 
*DefaultApi* | [**community_news_get_news**](docs/DefaultApi.md#community_news_get_news) | **GET** /community/news/getNews | 
*DefaultApi* | [**community_proxy_steam_user_request**](docs/DefaultApi.md#community_proxy_steam_user_request) | **GET** /community/external/proxysteamuserrequest | 
*DefaultApi* | [**game_account_find_profiles**](docs/DefaultApi.md#game_account_find_profiles) | **GET** /game/account/FindProfiles | 
*DefaultApi* | [**game_account_find_profiles_by_platform_id**](docs/DefaultApi.md#game_account_find_profiles_by_platform_id) | **GET** /game/account/FindProfilesByPlatformID | 
*DefaultApi* | [**game_account_get_profile_name**](docs/DefaultApi.md#game_account_get_profile_name) | **GET** /game/account/getProfileName | 
*DefaultApi* | [**game_account_get_profile_property**](docs/DefaultApi.md#game_account_get_profile_property) | **GET** /game/account/getProfileProperty | 
*DefaultApi* | [**game_account_set_avatar_metadata**](docs/DefaultApi.md#game_account_set_avatar_metadata) | **POST** /game/account/setAvatarMetadata | 
*DefaultApi* | [**game_account_set_language**](docs/DefaultApi.md#game_account_set_language) | **POST** /game/account/setLanguage | 
*DefaultApi* | [**game_achievement_get_achievements**](docs/DefaultApi.md#game_achievement_get_achievements) | **GET** /game/Achievement/getAchievements | 
*DefaultApi* | [**game_achievement_get_available_achievements**](docs/DefaultApi.md#game_achievement_get_available_achievements) | **GET** /game/Achievement/getAvailableAchievements | 
*DefaultApi* | [**game_achievement_sync_stats**](docs/DefaultApi.md#game_achievement_sync_stats) | **POST** /game/achievement/syncStats | 
*DefaultApi* | [**game_advertisement_find_advertisements**](docs/DefaultApi.md#game_advertisement_find_advertisements) | **GET** /game/advertisement/findAdvertisements | 
*DefaultApi* | [**game_advertisement_find_observable_advertisements_get**](docs/DefaultApi.md#game_advertisement_find_observable_advertisements_get) | **GET** /game/advertisement/findObservableAdvertisements | 
*DefaultApi* | [**game_advertisement_find_observable_advertisements_post**](docs/DefaultApi.md#game_advertisement_find_observable_advertisements_post) | **POST** /game/advertisement/findObservableAdvertisements | 
*DefaultApi* | [**game_advertisement_get_advertisements**](docs/DefaultApi.md#game_advertisement_get_advertisements) | **GET** /game/advertisement/getAdvertisements | 
*DefaultApi* | [**game_advertisement_get_lan_advertisements**](docs/DefaultApi.md#game_advertisement_get_lan_advertisements) | **GET** /game/advertisement/getLanAdvertisements | 
*DefaultApi* | [**game_advertisement_host**](docs/DefaultApi.md#game_advertisement_host) | **POST** /game/advertisement/host | 
*DefaultApi* | [**game_advertisement_join**](docs/DefaultApi.md#game_advertisement_join) | **POST** /game/advertisement/join | 
*DefaultApi* | [**game_advertisement_leave**](docs/DefaultApi.md#game_advertisement_leave) | **POST** /game/advertisement/leave | 
*DefaultApi* | [**game_advertisement_start_observing**](docs/DefaultApi.md#game_advertisement_start_observing) | **POST** /game/advertisement/startObserving | 
*DefaultApi* | [**game_advertisement_stop_observing**](docs/DefaultApi.md#game_advertisement_stop_observing) | **POST** /game/advertisement/stopObserving | 
*DefaultApi* | [**game_advertisement_update**](docs/DefaultApi.md#game_advertisement_update) | **POST** /game/advertisement/update | 
*DefaultApi* | [**game_advertisement_update_platform_lobby_id**](docs/DefaultApi.md#game_advertisement_update_platform_lobby_id) | **POST** /game/advertisement/updatePlatformLobbyID | 
*DefaultApi* | [**game_advertisement_update_state**](docs/DefaultApi.md#game_advertisement_update_state) | **POST** /game/advertisement/updateState | 
*DefaultApi* | [**game_advertisement_update_tags**](docs/DefaultApi.md#game_advertisement_update_tags) | **POST** /game/advertisement/updateTags | 
*DefaultApi* | [**game_automatch2_get_automatch_map**](docs/DefaultApi.md#game_automatch2_get_automatch_map) | **GET** /game/automatch2/getAutomatchMap | 
*DefaultApi* | [**game_automatch2_polling**](docs/DefaultApi.md#game_automatch2_polling) | **POST** /game/automatch2/polling | 
*DefaultApi* | [**game_automatch2_stop_polling**](docs/DefaultApi.md#game_automatch2_stop_polling) | **POST** /game/automatch2/stoppolling | 
*DefaultApi* | [**game_automatch2_update_status**](docs/DefaultApi.md#game_automatch2_update_status) | **POST** /game/automatch2/updateStatus | 
*DefaultApi* | [**game_automatch_get_automatch_map**](docs/DefaultApi.md#game_automatch_get_automatch_map) | **GET** /game/automatch/getAutomatchMap | 
*DefaultApi* | [**game_challenge_get_challenge_progress**](docs/DefaultApi.md#game_challenge_get_challenge_progress) | **GET** /game/Challenge/getChallengeProgress | 
*DefaultApi* | [**game_challenge_get_challenge_progress_by_profile_id**](docs/DefaultApi.md#game_challenge_get_challenge_progress_by_profile_id) | **GET** /game/Challenge/getChallengeProgressByProfileID | 
*DefaultApi* | [**game_challenge_get_challenges**](docs/DefaultApi.md#game_challenge_get_challenges) | **GET** /game/Challenge/getChallenges | 
*DefaultApi* | [**game_challenge_update_progress_batched**](docs/DefaultApi.md#game_challenge_update_progress_batched) | **POST** /game/challenge/updateProgressBatched | 
*DefaultApi* | [**game_chat_delete_offline_message**](docs/DefaultApi.md#game_chat_delete_offline_message) | **POST** /game/chat/deleteOfflineMessage | 
*DefaultApi* | [**game_chat_get_chat_channels**](docs/DefaultApi.md#game_chat_get_chat_channels) | **GET** /game/chat/getChatChannels | 
*DefaultApi* | [**game_chat_get_offline_messages**](docs/DefaultApi.md#game_chat_get_offline_messages) | **GET** /game/chat/getOfflineMessages | 
*DefaultApi* | [**game_clan_apply**](docs/DefaultApi.md#game_clan_apply) | **POST** /game/clan/apply | 
*DefaultApi* | [**game_clan_create**](docs/DefaultApi.md#game_clan_create) | **POST** /game/clan/create | 
*DefaultApi* | [**game_clan_disband**](docs/DefaultApi.md#game_clan_disband) | **POST** /game/clan/disband | 
*DefaultApi* | [**game_clan_find**](docs/DefaultApi.md#game_clan_find) | **GET** /game/clan/find | 
*DefaultApi* | [**game_clan_get_clan**](docs/DefaultApi.md#game_clan_get_clan) | **GET** /game/clan/getClan | 
*DefaultApi* | [**game_clan_get_clan_info_full**](docs/DefaultApi.md#game_clan_get_clan_info_full) | **GET** /game/clan/getClanInfoFull | 
*DefaultApi* | [**game_clan_update**](docs/DefaultApi.md#game_clan_update) | **POST** /game/clan/update | 
*DefaultApi* | [**game_cloud_get_file_url_get**](docs/DefaultApi.md#game_cloud_get_file_url_get) | **GET** /game/cloud/getFileURL | 
*DefaultApi* | [**game_cloud_get_file_url_post**](docs/DefaultApi.md#game_cloud_get_file_url_post) | **POST** /game/cloud/getFileURL | 
*DefaultApi* | [**game_cloud_get_temp_credentials**](docs/DefaultApi.md#game_cloud_get_temp_credentials) | **GET** /game/cloud/getTempCredentials | 
*DefaultApi* | [**game_community_event_get_available_community_events**](docs/DefaultApi.md#game_community_event_get_available_community_events) | **GET** /game/CommunityEvent/getAvailableCommunityEvents | 
*DefaultApi* | [**game_community_event_get_event_challenge_progress**](docs/DefaultApi.md#game_community_event_get_event_challenge_progress) | **GET** /game/CommunityEvent/getEventChallengeProgress | 
*DefaultApi* | [**game_community_event_get_event_stats**](docs/DefaultApi.md#game_community_event_get_event_stats) | **GET** /game/CommunityEvent/getEventStats | 
*DefaultApi* | [**game_invitation_cancel_invitation**](docs/DefaultApi.md#game_invitation_cancel_invitation) | **POST** /game/invitation/cancelInvitation | 
*DefaultApi* | [**game_invitation_extend_invitation**](docs/DefaultApi.md#game_invitation_extend_invitation) | **POST** /game/invitation/extendInvitation | 
*DefaultApi* | [**game_item_detach_items**](docs/DefaultApi.md#game_item_detach_items) | **POST** /game/item/detachItems | 
*DefaultApi* | [**game_item_get_inventory_by_profile_ids**](docs/DefaultApi.md#game_item_get_inventory_by_profile_ids) | **GET** /game/item/getInventoryByProfileIDs | 
*DefaultApi* | [**game_item_get_item_bundle_items_json**](docs/DefaultApi.md#game_item_get_item_bundle_items_json) | **GET** /game/item/getItemBundleItemsJson | 
*DefaultApi* | [**game_item_get_item_definitions_json**](docs/DefaultApi.md#game_item_get_item_definitions_json) | **GET** /game/item/getItemDefinitionsJson | 
*DefaultApi* | [**game_item_get_item_loadouts**](docs/DefaultApi.md#game_item_get_item_loadouts) | **GET** /game/item/getItemLoadouts | 
*DefaultApi* | [**game_item_get_item_prices**](docs/DefaultApi.md#game_item_get_item_prices) | **GET** /game/item/getItemPrices | 
*DefaultApi* | [**game_item_get_level_rewards_table_json**](docs/DefaultApi.md#game_item_get_level_rewards_table_json) | **GET** /game/item/getLevelRewardsTableJson | 
*DefaultApi* | [**game_item_get_personalized_sale_items**](docs/DefaultApi.md#game_item_get_personalized_sale_items) | **GET** /game/item/getPersonalizedSaleItems | 
*DefaultApi* | [**game_item_get_scheduled_sale_and_items**](docs/DefaultApi.md#game_item_get_scheduled_sale_and_items) | **GET** /game/item/getScheduledSaleAndItems | 
*DefaultApi* | [**game_item_move_charges**](docs/DefaultApi.md#game_item_move_charges) | **POST** /game/item/moveCharges | 
*DefaultApi* | [**game_item_move_item**](docs/DefaultApi.md#game_item_move_item) | **POST** /game/item/moveItem | 
*DefaultApi* | [**game_item_open_item_pack**](docs/DefaultApi.md#game_item_open_item_pack) | **POST** /game/item/openItemPack | 
*DefaultApi* | [**game_item_sign_item**](docs/DefaultApi.md#game_item_sign_item) | **POST** /game/item/signItems | 
*DefaultApi* | [**game_item_update_item_attributes**](docs/DefaultApi.md#game_item_update_item_attributes) | **POST** /game/item/updateItemAttributes | 
*DefaultApi* | [**game_leaderboard_get_available_leaderboards**](docs/DefaultApi.md#game_leaderboard_get_available_leaderboards) | **GET** /game/Leaderboard/getAvailableLeaderboards | 
*DefaultApi* | [**game_leaderboard_get_leaderboard**](docs/DefaultApi.md#game_leaderboard_get_leaderboard) | **GET** /game/Leaderboard/getLeaderBoard | 
*DefaultApi* | [**game_leaderboard_get_party_stat**](docs/DefaultApi.md#game_leaderboard_get_party_stat) | **GET** /game/Leaderboard/getPartyStat | 
*DefaultApi* | [**game_leaderboard_get_personal_stat**](docs/DefaultApi.md#game_leaderboard_get_personal_stat) | **GET** /game/Leaderboard/getPersonalStat | 
*DefaultApi* | [**game_leaderboard_get_recent_match_history_get**](docs/DefaultApi.md#game_leaderboard_get_recent_match_history_get) | **GET** /game/Leaderboard/getRecentMatchHistory | 
*DefaultApi* | [**game_leaderboard_get_recent_match_history_post**](docs/DefaultApi.md#game_leaderboard_get_recent_match_history_post) | **POST** /game/Leaderboard/getRecentMatchHistory | 
*DefaultApi* | [**game_leaderboard_get_recent_match_single_player_history**](docs/DefaultApi.md#game_leaderboard_get_recent_match_single_player_history) | **GET** /game/Leaderboard/getRecentMatchSinglePlayerHistory | 
*DefaultApi* | [**game_leaderboard_get_stat_groups_by_profile_ids**](docs/DefaultApi.md#game_leaderboard_get_stat_groups_by_profile_ids) | **GET** /game/Leaderboard/getStatGroupsByProfileIDs | 
*DefaultApi* | [**game_leaderboard_get_stats_for_leaderboard_by_profile_name**](docs/DefaultApi.md#game_leaderboard_get_stats_for_leaderboard_by_profile_name) | **GET** /game/Leaderboard/getStatsForLeaderboardByProfileName | 
*DefaultApi* | [**game_leaderboard_set_avatar_stat_values**](docs/DefaultApi.md#game_leaderboard_set_avatar_stat_values) | **POST** /game/leaderboard/setAvatarStatValues | 
*DefaultApi* | [**game_login_logout**](docs/DefaultApi.md#game_login_logout) | **POST** /game/login/logout | 
*DefaultApi* | [**game_login_platform_login**](docs/DefaultApi.md#game_login_platform_login) | **POST** /game/login/platformlogin | 
*DefaultApi* | [**game_login_read_session**](docs/DefaultApi.md#game_login_read_session) | **POST** /game/login/readSession | 
*DefaultApi* | [**game_news_get_news**](docs/DefaultApi.md#game_news_get_news) | **GET** /game/news/getNews | 
*DefaultApi* | [**game_party_create_or_report_single_player**](docs/DefaultApi.md#game_party_create_or_report_single_player) | **POST** /game/party/createOrReportSinglePlayer | 
*DefaultApi* | [**game_party_finalize_replay_upload**](docs/DefaultApi.md#game_party_finalize_replay_upload) | **POST** /game/party/finalizeReplayUpload | 
*DefaultApi* | [**game_party_peer_add**](docs/DefaultApi.md#game_party_peer_add) | **POST** /game/party/peerAdd | 
*DefaultApi* | [**game_party_peer_update**](docs/DefaultApi.md#game_party_peer_update) | **POST** /game/party/peerUpdate | 
*DefaultApi* | [**game_party_report_match**](docs/DefaultApi.md#game_party_report_match) | **POST** /game/party/reportMatch | 
*DefaultApi* | [**game_party_send_match_chat**](docs/DefaultApi.md#game_party_send_match_chat) | **POST** /game/party/sendMatchChat | 
*DefaultApi* | [**game_playerreport_report_user**](docs/DefaultApi.md#game_playerreport_report_user) | **POST** /game/playerreport/reportuser | 
*DefaultApi* | [**game_relationship_clear_relationship**](docs/DefaultApi.md#game_relationship_clear_relationship) | **POST** /game/relationship/clearRelationship | 
*DefaultApi* | [**game_relationship_get_presence_data**](docs/DefaultApi.md#game_relationship_get_presence_data) | **GET** /game/relationship/getPresenceData | 
*DefaultApi* | [**game_relationship_get_relationships**](docs/DefaultApi.md#game_relationship_get_relationships) | **GET** /game/relationship/getRelationships | 
*DefaultApi* | [**game_relationship_ignore**](docs/DefaultApi.md#game_relationship_ignore) | **POST** /game/relationship/ignore | 
*DefaultApi* | [**game_relationship_set_presence**](docs/DefaultApi.md#game_relationship_set_presence) | **POST** /game/relationship/setPresence | 
*DefaultApi* | [**game_relationship_set_presence_property**](docs/DefaultApi.md#game_relationship_set_presence_property) | **POST** /game/relationship/setPresenceProperty | 


## Documentation For Models



<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="connectID"></a>
### connectID

- **Type**: API key
- **API key parameter name**: connect_id
- **Location**: URL query string

<a id="sessionID"></a>
### sessionID

- **Type**: API key
- **API key parameter name**: sessionID
- **Location**: URL query string

<a id="authLogin"></a>
### authLogin

- **Type**: API key
- **API key parameter name**: auth
- **Location**: URL query string


## Author




