<a name="__pageTop"></a>
# rlink_client.apis.tags.default_api.DefaultApi

All URIs are relative to *https://aoe-api.reliclink.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**community_clan_find**](#community_clan_find) | **get** /community/clan/find | 
[**community_find_advertisements**](#community_find_advertisements) | **get** /community/advertisement/findAdvertisements | 
[**community_get_achievements**](#community_get_achievements) | **get** /community/achievement/getAchievements | 
[**community_get_available_achievements**](#community_get_available_achievements) | **get** /community/achievement/getAvailableAchievements | 
[**community_get_available_community_events**](#community_get_available_community_events) | **get** /community/CommunityEvent/getAvailableCommunityEvents | 
[**community_get_available_leaderboards**](#community_get_available_leaderboards) | **get** /community/leaderboard/getAvailableLeaderboards | 
[**community_get_avatar_stat_for_profile**](#community_get_avatar_stat_for_profile) | **get** /community/leaderboard/GetAvatarStatForProfile | 
[**community_get_clan_info_full**](#community_get_clan_info_full) | **get** /community/clan/getClanInfoFull | 
[**community_get_inventory_by_profile_ids**](#community_get_inventory_by_profile_ids) | **get** /community/item/getInventoryByProfileIDs | 
[**community_get_leaderboard2**](#community_get_leaderboard2) | **get** /community/leaderboard/getLeaderboard2 | 
[**community_get_personal_stat**](#community_get_personal_stat) | **get** /community/leaderboard/GetPersonalStat | 
[**community_get_recent_match_history**](#community_get_recent_match_history) | **get** /community/leaderboard/getRecentMatchHistory | 
[**community_news_get_news**](#community_news_get_news) | **get** /community/news/getNews | 
[**community_proxy_steam_user_request**](#community_proxy_steam_user_request) | **get** /community/external/proxysteamuserrequest | 
[**game_account_find_profiles**](#game_account_find_profiles) | **get** /game/account/FindProfiles | 
[**game_account_find_profiles_by_platform_id**](#game_account_find_profiles_by_platform_id) | **get** /game/account/FindProfilesByPlatformID | 
[**game_account_get_profile_name**](#game_account_get_profile_name) | **get** /game/account/getProfileName | 
[**game_account_get_profile_property**](#game_account_get_profile_property) | **get** /game/account/getProfileProperty | 
[**game_account_set_avatar_metadata**](#game_account_set_avatar_metadata) | **post** /game/account/setAvatarMetadata | 
[**game_account_set_language**](#game_account_set_language) | **post** /game/account/setLanguage | 
[**game_achievement_get_achievements**](#game_achievement_get_achievements) | **get** /game/Achievement/getAchievements | 
[**game_achievement_get_available_achievements**](#game_achievement_get_available_achievements) | **get** /game/Achievement/getAvailableAchievements | 
[**game_achievement_sync_stats**](#game_achievement_sync_stats) | **post** /game/achievement/syncStats | 
[**game_advertisement_find_advertisements**](#game_advertisement_find_advertisements) | **get** /game/advertisement/findAdvertisements | 
[**game_advertisement_find_observable_advertisements_get**](#game_advertisement_find_observable_advertisements_get) | **get** /game/advertisement/findObservableAdvertisements | 
[**game_advertisement_find_observable_advertisements_post**](#game_advertisement_find_observable_advertisements_post) | **post** /game/advertisement/findObservableAdvertisements | 
[**game_advertisement_get_advertisements**](#game_advertisement_get_advertisements) | **get** /game/advertisement/getAdvertisements | 
[**game_advertisement_get_lan_advertisements**](#game_advertisement_get_lan_advertisements) | **get** /game/advertisement/getLanAdvertisements | 
[**game_advertisement_host**](#game_advertisement_host) | **post** /game/advertisement/host | 
[**game_advertisement_join**](#game_advertisement_join) | **post** /game/advertisement/join | 
[**game_advertisement_leave**](#game_advertisement_leave) | **post** /game/advertisement/leave | 
[**game_advertisement_start_observing**](#game_advertisement_start_observing) | **post** /game/advertisement/startObserving | 
[**game_advertisement_stop_observing**](#game_advertisement_stop_observing) | **post** /game/advertisement/stopObserving | 
[**game_advertisement_update**](#game_advertisement_update) | **post** /game/advertisement/update | 
[**game_advertisement_update_platform_lobby_id**](#game_advertisement_update_platform_lobby_id) | **post** /game/advertisement/updatePlatformLobbyID | 
[**game_advertisement_update_state**](#game_advertisement_update_state) | **post** /game/advertisement/updateState | 
[**game_advertisement_update_tags**](#game_advertisement_update_tags) | **post** /game/advertisement/updateTags | 
[**game_automatch2_get_automatch_map**](#game_automatch2_get_automatch_map) | **get** /game/automatch2/getAutomatchMap | 
[**game_automatch2_polling**](#game_automatch2_polling) | **post** /game/automatch2/polling | 
[**game_automatch2_stop_polling**](#game_automatch2_stop_polling) | **post** /game/automatch2/stoppolling | 
[**game_automatch2_update_status**](#game_automatch2_update_status) | **post** /game/automatch2/updateStatus | 
[**game_automatch_get_automatch_map**](#game_automatch_get_automatch_map) | **get** /game/automatch/getAutomatchMap | 
[**game_challenge_get_challenge_progress**](#game_challenge_get_challenge_progress) | **get** /game/Challenge/getChallengeProgress | 
[**game_challenge_get_challenge_progress_by_profile_id**](#game_challenge_get_challenge_progress_by_profile_id) | **get** /game/Challenge/getChallengeProgressByProfileID | 
[**game_challenge_get_challenges**](#game_challenge_get_challenges) | **get** /game/Challenge/getChallenges | 
[**game_challenge_update_progress_batched**](#game_challenge_update_progress_batched) | **post** /game/challenge/updateProgressBatched | 
[**game_chat_delete_offline_message**](#game_chat_delete_offline_message) | **post** /game/chat/deleteOfflineMessage | 
[**game_chat_get_chat_channels**](#game_chat_get_chat_channels) | **get** /game/chat/getChatChannels | 
[**game_chat_get_offline_messages**](#game_chat_get_offline_messages) | **get** /game/chat/getOfflineMessages | 
[**game_clan_apply**](#game_clan_apply) | **post** /game/clan/apply | 
[**game_clan_create**](#game_clan_create) | **post** /game/clan/create | 
[**game_clan_disband**](#game_clan_disband) | **post** /game/clan/disband | 
[**game_clan_find**](#game_clan_find) | **get** /game/clan/find | 
[**game_clan_get_clan**](#game_clan_get_clan) | **get** /game/clan/getClan | 
[**game_clan_get_clan_info_full**](#game_clan_get_clan_info_full) | **get** /game/clan/getClanInfoFull | 
[**game_clan_update**](#game_clan_update) | **post** /game/clan/update | 
[**game_cloud_get_file_url_get**](#game_cloud_get_file_url_get) | **get** /game/cloud/getFileURL | 
[**game_cloud_get_file_url_post**](#game_cloud_get_file_url_post) | **post** /game/cloud/getFileURL | 
[**game_cloud_get_temp_credentials**](#game_cloud_get_temp_credentials) | **get** /game/cloud/getTempCredentials | 
[**game_community_event_get_available_community_events**](#game_community_event_get_available_community_events) | **get** /game/CommunityEvent/getAvailableCommunityEvents | 
[**game_community_event_get_event_challenge_progress**](#game_community_event_get_event_challenge_progress) | **get** /game/CommunityEvent/getEventChallengeProgress | 
[**game_community_event_get_event_stats**](#game_community_event_get_event_stats) | **get** /game/CommunityEvent/getEventStats | 
[**game_invitation_cancel_invitation**](#game_invitation_cancel_invitation) | **post** /game/invitation/cancelInvitation | 
[**game_invitation_extend_invitation**](#game_invitation_extend_invitation) | **post** /game/invitation/extendInvitation | 
[**game_item_detach_items**](#game_item_detach_items) | **post** /game/item/detachItems | 
[**game_item_get_inventory_by_profile_ids**](#game_item_get_inventory_by_profile_ids) | **get** /game/item/getInventoryByProfileIDs | 
[**game_item_get_item_bundle_items_json**](#game_item_get_item_bundle_items_json) | **get** /game/item/getItemBundleItemsJson | 
[**game_item_get_item_definitions_json**](#game_item_get_item_definitions_json) | **get** /game/item/getItemDefinitionsJson | 
[**game_item_get_item_loadouts**](#game_item_get_item_loadouts) | **get** /game/item/getItemLoadouts | 
[**game_item_get_item_prices**](#game_item_get_item_prices) | **get** /game/item/getItemPrices | 
[**game_item_get_level_rewards_table_json**](#game_item_get_level_rewards_table_json) | **get** /game/item/getLevelRewardsTableJson | 
[**game_item_get_personalized_sale_items**](#game_item_get_personalized_sale_items) | **get** /game/item/getPersonalizedSaleItems | 
[**game_item_get_scheduled_sale_and_items**](#game_item_get_scheduled_sale_and_items) | **get** /game/item/getScheduledSaleAndItems | 
[**game_item_move_charges**](#game_item_move_charges) | **post** /game/item/moveCharges | 
[**game_item_move_item**](#game_item_move_item) | **post** /game/item/moveItem | 
[**game_item_open_item_pack**](#game_item_open_item_pack) | **post** /game/item/openItemPack | 
[**game_item_sign_item**](#game_item_sign_item) | **post** /game/item/signItems | 
[**game_item_update_item_attributes**](#game_item_update_item_attributes) | **post** /game/item/updateItemAttributes | 
[**game_leaderboard_get_available_leaderboards**](#game_leaderboard_get_available_leaderboards) | **get** /game/Leaderboard/getAvailableLeaderboards | 
[**game_leaderboard_get_leaderboard**](#game_leaderboard_get_leaderboard) | **get** /game/Leaderboard/getLeaderBoard | 
[**game_leaderboard_get_party_stat**](#game_leaderboard_get_party_stat) | **get** /game/Leaderboard/getPartyStat | 
[**game_leaderboard_get_personal_stat**](#game_leaderboard_get_personal_stat) | **get** /game/Leaderboard/getPersonalStat | 
[**game_leaderboard_get_recent_match_history_get**](#game_leaderboard_get_recent_match_history_get) | **get** /game/Leaderboard/getRecentMatchHistory | 
[**game_leaderboard_get_recent_match_history_post**](#game_leaderboard_get_recent_match_history_post) | **post** /game/Leaderboard/getRecentMatchHistory | 
[**game_leaderboard_get_recent_match_single_player_history**](#game_leaderboard_get_recent_match_single_player_history) | **get** /game/Leaderboard/getRecentMatchSinglePlayerHistory | 
[**game_leaderboard_get_stat_groups_by_profile_ids**](#game_leaderboard_get_stat_groups_by_profile_ids) | **get** /game/Leaderboard/getStatGroupsByProfileIDs | 
[**game_leaderboard_get_stats_for_leaderboard_by_profile_name**](#game_leaderboard_get_stats_for_leaderboard_by_profile_name) | **get** /game/Leaderboard/getStatsForLeaderboardByProfileName | 
[**game_leaderboard_set_avatar_stat_values**](#game_leaderboard_set_avatar_stat_values) | **post** /game/leaderboard/setAvatarStatValues | 
[**game_login_logout**](#game_login_logout) | **post** /game/login/logout | 
[**game_login_platform_login**](#game_login_platform_login) | **post** /game/login/platformlogin | 
[**game_login_read_session**](#game_login_read_session) | **post** /game/login/readSession | 
[**game_news_get_news**](#game_news_get_news) | **get** /game/news/getNews | 
[**game_party_create_or_report_single_player**](#game_party_create_or_report_single_player) | **post** /game/party/createOrReportSinglePlayer | 
[**game_party_finalize_replay_upload**](#game_party_finalize_replay_upload) | **post** /game/party/finalizeReplayUpload | 
[**game_party_peer_add**](#game_party_peer_add) | **post** /game/party/peerAdd | 
[**game_party_peer_update**](#game_party_peer_update) | **post** /game/party/peerUpdate | 
[**game_party_report_match**](#game_party_report_match) | **post** /game/party/reportMatch | 
[**game_party_send_match_chat**](#game_party_send_match_chat) | **post** /game/party/sendMatchChat | 
[**game_playerreport_report_user**](#game_playerreport_report_user) | **post** /game/playerreport/reportuser | 
[**game_relationship_clear_relationship**](#game_relationship_clear_relationship) | **post** /game/relationship/clearRelationship | 
[**game_relationship_get_presence_data**](#game_relationship_get_presence_data) | **get** /game/relationship/getPresenceData | 
[**game_relationship_get_relationships**](#game_relationship_get_relationships) | **get** /game/relationship/getRelationships | 
[**game_relationship_ignore**](#game_relationship_ignore) | **post** /game/relationship/ignore | 
[**game_relationship_set_presence**](#game_relationship_set_presence) | **post** /game/relationship/setPresence | 
[**game_relationship_set_presence_property**](#game_relationship_set_presence_property) | **post** /game/relationship/setPresenceProperty | 

# **community_clan_find**
<a name="community_clan_find"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_clan_find(join_policiesnametagsstartcount)



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'joinPolicies': [0,1,2],
        'name': "name_example",
        'tags': "[]",
        'start': 0,
        'count': 200,
    }
    try:
        api_response = api_instance.community_clan_find(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_clan_find: %s\n" % e)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'joinPolicies': [0,1,2],
        'name': "name_example",
        'tags': "[]",
        'start': 0,
        'count': 200,
    }
    try:
        api_response = api_instance.community_clan_find(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_clan_find: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
joinPolicies | JoinPoliciesSchema | | 
name | NameSchema | | 
tags | TagsSchema | | 
start | StartSchema | | 
count | CountSchema | | 


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JoinPoliciesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_clan_find.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_clan_find.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_find_advertisements**
<a name="community_find_advertisements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_find_advertisements()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
    }
    try:
        api_response = api_instance.community_find_advertisements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_find_advertisements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_find_advertisements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_find_advertisements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_achievements**
<a name="community_get_achievements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_achievements()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'profileids': [196240],
    }
    try:
        api_response = api_instance.community_get_achievements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_achievements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
profileids | ProfileidsSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_achievements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_achievements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_available_achievements**
<a name="community_get_available_achievements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_available_achievements()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
    }
    try:
        api_response = api_instance.community_get_available_achievements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_available_achievements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_available_achievements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_available_achievements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_available_community_events**
<a name="community_get_available_community_events"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_available_community_events()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
    }
    try:
        api_response = api_instance.community_get_available_community_events(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_available_community_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_available_community_events.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_available_community_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_available_leaderboards**
<a name="community_get_available_leaderboards"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_available_leaderboards()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
    }
    try:
        api_response = api_instance.community_get_available_leaderboards(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_available_leaderboards: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_available_leaderboards.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_available_leaderboards.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_avatar_stat_for_profile**
<a name="community_get_avatar_stat_for_profile"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_avatar_stat_for_profile()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'profile_names': "[%22/steam/76561197984749679%22]",
    }
    try:
        api_response = api_instance.community_get_avatar_stat_for_profile(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_avatar_stat_for_profile: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
profile_names | ProfileNamesSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileNamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_avatar_stat_for_profile.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_avatar_stat_for_profile.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_clan_info_full**
<a name="community_get_clan_info_full"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_clan_info_full(name)



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'name': "name_example",
    }
    try:
        api_response = api_instance.community_get_clan_info_full(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_clan_info_full: %s\n" % e)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'name': "name_example",
    }
    try:
        api_response = api_instance.community_get_clan_info_full(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_clan_info_full: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
name | NameSchema | | 


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_clan_info_full.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_clan_info_full.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_inventory_by_profile_ids**
<a name="community_get_inventory_by_profile_ids"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_inventory_by_profile_ids()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'profileids': [196240],
    }
    try:
        api_response = api_instance.community_get_inventory_by_profile_ids(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_inventory_by_profile_ids: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
profileids | ProfileidsSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_inventory_by_profile_ids.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_inventory_by_profile_ids.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_leaderboard2**
<a name="community_get_leaderboard2"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_leaderboard2(startcount)



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'start': 0,
        'count': 200,
    }
    try:
        api_response = api_instance.community_get_leaderboard2(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_leaderboard2: %s\n" % e)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'leaderboard_id': 3,
        'start': 0,
        'count': 200,
        'sortBy': 1,
        'platform': "PC_STEAM",
    }
    try:
        api_response = api_instance.community_get_leaderboard2(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_leaderboard2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
leaderboard_id | LeaderboardIdSchema | | optional
start | StartSchema | | 
count | CountSchema | | 
sortBy | SortBySchema | | optional
platform | PlatformSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeaderboardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PlatformSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_leaderboard2.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_leaderboard2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_personal_stat**
<a name="community_get_personal_stat"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_personal_stat()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'profile_ids': "[\"192640\"]",
        'profile_names': "[%22/steam/76561197984749679%22]",
        'aliases': "[BlackRock]",
    }
    try:
        api_response = api_instance.community_get_personal_stat(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_personal_stat: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
profile_ids | ProfileIdsSchema | | optional
profile_names | ProfileNamesSchema | | optional
aliases | AliasesSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileNamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AliasesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_personal_stat.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_personal_stat.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_get_recent_match_history**
<a name="community_get_recent_match_history"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_get_recent_match_history()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
        'profile_ids': "[\"192640\"]",
        'profile_names': "[%22/steam/76561197984749679%22]",
    }
    try:
        api_response = api_instance.community_get_recent_match_history(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_get_recent_match_history: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional
profile_ids | ProfileIdsSchema | | optional
profile_names | ProfileNamesSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileNamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_get_recent_match_history.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_get_recent_match_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_news_get_news**
<a name="community_news_get_news"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_news_get_news()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'title': "[\"age2\",\"age1\"]",
    }
    try:
        api_response = api_instance.community_news_get_news(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_news_get_news: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
title | TitleSchema | | optional


# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_news_get_news.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_news_get_news.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **community_proxy_steam_user_request**
<a name="community_proxy_steam_user_request"></a>
> bool, date, datetime, dict, float, int, list, str, none_type community_proxy_steam_user_request()



### Example

```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'request': "/ISteamUser/GetPlayerSummaries/v0002/",
        'title': "[\"age2\",\"age1\"]",
        'profile_ids': "[\"192640\"]",
        'profileNames': "[\"/steam/76561197984749679\"]",
    }
    try:
        api_response = api_instance.community_proxy_steam_user_request(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->community_proxy_steam_user_request: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json;charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
request | RequestSchema | | optional
title | TitleSchema | | optional
profile_ids | ProfileIdsSchema | | optional
profileNames | ProfileNamesSchema | | optional


# RequestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileNamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#community_proxy_steam_user_request.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### community_proxy_steam_user_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsoncharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsoncharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_account_find_profiles**
<a name="game_account_find_profiles"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_account_find_profiles(last_call_timename)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'name': "name_example",
    }
    try:
        api_response = api_instance.game_account_find_profiles(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_find_profiles: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
name | NameSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_account_find_profiles.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_account_find_profiles.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_account_find_profiles_by_platform_id**
<a name="game_account_find_profiles_by_platform_id"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_account_find_profiles_by_platform_id(last_call_timeplatform_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'platformIDs': [[76561197960287614,76561197978627567,76561197978943286,76561198000229224,76561197972009043,76561197964180873,76561197966000898,76561197976722725]],
    }
    try:
        api_response = api_instance.game_account_find_profiles_by_platform_id(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_find_profiles_by_platform_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
platformIDs | PlatformIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlatformIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_account_find_profiles_by_platform_id.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_account_find_profiles_by_platform_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_account_get_profile_name**
<a name="game_account_get_profile_name"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_account_get_profile_name(last_call_timeprofile_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profile_ids': [196240],
    }
    try:
        api_response = api_instance.game_account_get_profile_name(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_get_profile_name: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profile_ids | ProfileIdsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_account_get_profile_name.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_account_get_profile_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_account_get_profile_property**
<a name="game_account_get_profile_property"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_account_get_profile_property(last_call_timeprofile_idproperty_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profile_id': 196240,
        'property_id': "[\"appearOffline\"]",
    }
    try:
        api_response = api_instance.game_account_get_profile_property(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_get_profile_property: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profile_id | ProfileIdSchema | | 
property_id | PropertyIdSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PropertyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_account_get_profile_property.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_account_get_profile_property.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_account_set_avatar_metadata**
<a name="game_account_set_avatar_metadata"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_account_set_avatar_metadata(last_call_timemeta_data)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'metaData': dict(),
    }
    try:
        api_response = api_instance.game_account_set_avatar_metadata(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_set_avatar_metadata: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
metaData | MetaDataSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetaDataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_account_set_avatar_metadata.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_account_set_avatar_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_account_set_language**
<a name="game_account_set_language"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_account_set_language(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_account_set_language(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_set_language: %s\n" % e)

    # example passing only optional values
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'title': "[\"age1\",\"age2\",\"age3\",\"age4\"]",
        'language': "[\"en\",\"de\",\"es\",\"fr\"]",
    }
    try:
        api_response = api_instance.game_account_set_language(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_account_set_language: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
title | TitleSchema | | optional
language | LanguageSchema | | optional


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_account_set_language.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_account_set_language.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_achievement_get_achievements**
<a name="game_achievement_get_achievements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_achievement_get_achievements(last_call_timeprofile_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profileIDs': [196240,196241],
    }
    try:
        api_response = api_instance.game_achievement_get_achievements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_achievement_get_achievements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profileIDs | ProfileIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_achievement_get_achievements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_achievement_get_achievements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_achievement_get_available_achievements**
<a name="game_achievement_get_available_achievements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_achievement_get_available_achievements(last_call_timesignature)



No authentication needed

### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'signature': "wqFWpWL7ZV67HZ7b1kXEAtWofi34DFHX/HoiyJm46ooePlthNsS5F2TQiLHzUOSYuV/VGDmpk1Dr7r6E/OukY/lDE4MgrRQBkOTvV8HAnqJIAcqDTiZN9l1bimxn14vrnnNaBcOZyOvnkZD5oVahECESHlxgEewOhTdkOxLAuXLA+QxXYBlswaperH95/wGhUg11NN0AG2L/6ej929D5NIqDGlVrmp1oBRNYTqRhbvOgjyII0XElAvKwaR+bYKGqchd8RU4WGwPsrhN/5IKl4E7SpJH9UAWV4bH9v6lVwJqz8NGCawmq1p+V22G239k/c7x6chtyOJBPG9N220ot5A==",
    }
    try:
        api_response = api_instance.game_achievement_get_available_achievements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_achievement_get_available_achievements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
signature | SignatureSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SignatureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_achievement_get_available_achievements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_achievement_get_available_achievements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_achievement_sync_stats**
<a name="game_achievement_sync_stats"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_achievement_sync_stats(last_call_timeaccount_typeauth)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'accountType': "STEAM",
        'auth': "STEAM",
    }
    try:
        api_response = api_instance.game_achievement_sync_stats(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_achievement_sync_stats: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
accountType | AccountTypeSchema | | 
auth | AuthSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_achievement_sync_stats.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_achievement_sync_stats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_find_advertisements**
<a name="game_advertisement_find_advertisements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_find_advertisements(app_binary_checksumdata_checksumlast_call_timematch_type_idmod_dll_checksummod_dll_filemod_namemod_versionprofile_idsrace_idsstat_group_idsversion_flags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'appBinaryChecksum': 24916,
        'callNum': 148,
        'dataChecksum': -638535971,
        'lastCallTime': "918824",
        'matchType_id': 0,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'profile_ids': [196240],
        'race_ids': [1,2],
        'statGroup_ids': [12,34],
        'versionFlags': 0,
    }
    try:
        api_response = api_instance.game_advertisement_find_advertisements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_find_advertisements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appBinaryChecksum | AppBinaryChecksumSchema | | 
callNum | CallNumSchema | | 
dataChecksum | DataChecksumSchema | | 
lastCallTime | LastCallTimeSchema | | 
matchType_id | MatchTypeIdSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
profile_ids | ProfileIdsSchema | | 
race_ids | RaceIdsSchema | | 
statGroup_ids | StatGroupIdsSchema | | 
versionFlags | VersionFlagsSchema | | 


# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatGroupIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_find_advertisements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_find_advertisements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_find_observable_advertisements_get**
<a name="game_advertisement_find_observable_advertisements_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_find_observable_advertisements_get(last_call_timeapp_binary_checksumcountdata_checksumdescmod_dll_checksummod_dll_filemod_namemod_versionobserver_group_idsort_orderstartversion_flags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'appBinaryChecksum': 24916,
        'count': 200,
        'dataChecksum': -638535971,
        'desc': 0,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'observerGroupID': 0,
        'sortOrder': 0,
        'start': 0,
        'versionFlags': 0,
    }
    try:
        api_response = api_instance.game_advertisement_find_observable_advertisements_get(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_find_observable_advertisements_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
appBinaryChecksum | AppBinaryChecksumSchema | | 
count | CountSchema | | 
dataChecksum | DataChecksumSchema | | 
desc | DescSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
observerGroupID | ObserverGroupIDSchema | | 
sortOrder | SortOrderSchema | | 
start | StartSchema | | 
versionFlags | VersionFlagsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DescSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ObserverGroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortOrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_find_observable_advertisements_get.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_find_observable_advertisements_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_find_observable_advertisements_post**
<a name="game_advertisement_find_observable_advertisements_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_find_observable_advertisements_post(last_call_timeapp_binary_checksumcountdata_checksumdescmod_dll_checksummod_dll_filemod_namemod_versionobserver_group_idsort_orderstartversion_flags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'appBinaryChecksum': 24916,
        'count': 200,
        'dataChecksum': -638535971,
        'desc': 0,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'observerGroupID': 0,
        'sortOrder': 0,
        'start': 0,
        'versionFlags': 0,
    }
    try:
        api_response = api_instance.game_advertisement_find_observable_advertisements_post(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_find_observable_advertisements_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
appBinaryChecksum | AppBinaryChecksumSchema | | 
count | CountSchema | | 
dataChecksum | DataChecksumSchema | | 
desc | DescSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
observerGroupID | ObserverGroupIDSchema | | 
sortOrder | SortOrderSchema | | 
start | StartSchema | | 
versionFlags | VersionFlagsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DescSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ObserverGroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortOrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_find_observable_advertisements_post.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_find_observable_advertisements_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_get_advertisements**
<a name="game_advertisement_get_advertisements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_get_advertisements(last_call_timematch_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'match_ids': [132,123],
    }
    try:
        api_response = api_instance.game_advertisement_get_advertisements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_get_advertisements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
match_ids | MatchIdsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_get_advertisements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_get_advertisements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_get_lan_advertisements**
<a name="game_advertisement_get_lan_advertisements"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_get_lan_advertisements(app_binary_checksumdata_checksumlan_server_guidslast_call_timematch_type_idmod_dll_checksummod_dll_filemod_namemod_versionversion_flags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'appBinaryChecksum': 24916,
        'callNum': 148,
        'dataChecksum': -638535971,
        'lanServerGuids': "[\"123e88e6-88e1-4aa7-ab3c-a2975fc0b04d\"]",
        'lastCallTime': "918824",
        'matchType_id': 0,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'versionFlags': 0,
    }
    try:
        api_response = api_instance.game_advertisement_get_lan_advertisements(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_get_lan_advertisements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appBinaryChecksum | AppBinaryChecksumSchema | | 
callNum | CallNumSchema | | 
dataChecksum | DataChecksumSchema | | 
lanServerGuids | LanServerGuidsSchema | | 
lastCallTime | LastCallTimeSchema | | 
matchType_id | MatchTypeIdSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
versionFlags | VersionFlagsSchema | | 


# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LanServerGuidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_get_lan_advertisements.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_get_lan_advertisements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_host**
<a name="game_advertisement_host"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_host(advertisementidapp_binary_checksumautomatch_poll_iddata_checksumdescriptionhostidis_observablelast_call_timemapnamematchtypemaxplayersmod_dll_checksummod_dll_filemod_namemod_versionobserver_delayobserver_passwordoptionspartypasswordpasswordedracerelay_regionservice_typeslotinfostatestatgroupteamversion_flagsvisible)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'appBinaryChecksum': 24916,
        'automatchPoll_id': -1,
        'callNum': 148,
        'dataChecksum': -638535971,
        'description': "[\"SESSION_MATCH_KEY\",\"Test\"]",
        'hostid': 1,
        'isObservable': 1,
        'lastCallTime': "918824",
        'mapname': "[\"no_map\",\"ang_chp1_hastings\"]",
        'matchtype': 19,
        'maxplayers': 8,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'observerDelay': 180,
        'observerPassword': "unknown password",
        'options': "opts",
        'party': -1,
        'password': "test",
        'passworded': [0,1],
        'race': 2039321,
        'relayRegion': "[\"australiasoutheast\",\"brazilsouth\",\"koreacentral\",\"ukwest\",\"southeastasia\",\"westus2\",\"westindia\",\"westeurope\",\"eastus\"]",
        'serviceType': 0,
        'slotinfo': "eNrtjkEKwjAQRT3LrKNYl10XoWBBqjtxMaQTHGySkoxCEe8uiaDewE127zMP5lUbdXrAFLzhkVpn/IoHqJeVgigo7F3bvKcQ2sRrBQb17yWgpi+7647uNGYxrQ5FX47z9FGELe0pbANa6g7Z49gTDnPm9PYWM1oSbFAQaoCnKpWlslSWyr9XnhcvuymdYw==",
        'state': -1,
        'statgroup': -1,
        'team': -1,
        'versionFlags': 0,
        'visible': 0,
    }
    try:
        api_response = api_instance.game_advertisement_host(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_host: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
appBinaryChecksum | AppBinaryChecksumSchema | | 
automatchPoll_id | AutomatchPollIdSchema | | 
callNum | CallNumSchema | | 
dataChecksum | DataChecksumSchema | | 
description | DescriptionSchema | | 
hostid | HostidSchema | | 
isObservable | IsObservableSchema | | 
lastCallTime | LastCallTimeSchema | | 
mapname | MapnameSchema | | 
matchtype | MatchtypeSchema | | 
maxplayers | MaxplayersSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
observerDelay | ObserverDelaySchema | | 
observerPassword | ObserverPasswordSchema | | 
options | OptionsSchema | | 
party | PartySchema | | 
password | PasswordSchema | | 
passworded | PasswordedSchema | | 
race | RaceSchema | | 
relayRegion | RelayRegionSchema | | 
serviceType | ServiceTypeSchema | | 
slotinfo | SlotinfoSchema | | 
state | StateSchema | | 
statgroup | StatgroupSchema | | 
team | TeamSchema | | 
versionFlags | VersionFlagsSchema | | 
visible | VisibleSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AutomatchPollIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HostidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsObservableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MapnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchtypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MaxplayersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ObserverDelaySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ObserverPasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PasswordedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RelayRegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SlotinfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatgroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VisibleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_host.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_host.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_join**
<a name="game_advertisement_join"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_join(advertisementidapp_binary_checksumdata_checksumlast_call_timemod_dll_checksummod_dll_filemod_namemod_versionpartypasswordracestatgroupteamversion_flags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'appBinaryChecksum': 24916,
        'callNum': 148,
        'dataChecksum': -638535971,
        'lastCallTime': "918824",
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'party': -1,
        'password': "test",
        'race': 2039321,
        'statgroup': -1,
        'team': -1,
        'versionFlags': 0,
    }
    try:
        api_response = api_instance.game_advertisement_join(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_join: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
appBinaryChecksum | AppBinaryChecksumSchema | | 
callNum | CallNumSchema | | 
dataChecksum | DataChecksumSchema | | 
lastCallTime | LastCallTimeSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
party | PartySchema | | 
password | PasswordSchema | | 
race | RaceSchema | | 
statgroup | StatgroupSchema | | 
team | TeamSchema | | 
versionFlags | VersionFlagsSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatgroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_join.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_join.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_leave**
<a name="game_advertisement_leave"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_leave(advertisementidlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_advertisement_leave(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_leave: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_leave.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_leave.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_start_observing**
<a name="game_advertisement_start_observing"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_start_observing(advertisementidapp_binary_checksumdata_checksumlast_call_timemod_dll_checksummod_dll_filemod_namemod_versionpasswordversion_flagswith_party_session_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'appBinaryChecksum': 24916,
        'callNum': 148,
        'dataChecksum': -638535971,
        'lastCallTime': "918824",
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'password': "test",
        'versionFlags': 0,
        'withPartySessionID': 50865084,
    }
    try:
        api_response = api_instance.game_advertisement_start_observing(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_start_observing: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
appBinaryChecksum | AppBinaryChecksumSchema | | 
callNum | CallNumSchema | | 
dataChecksum | DataChecksumSchema | | 
lastCallTime | LastCallTimeSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
password | PasswordSchema | | 
versionFlags | VersionFlagsSchema | | 
withPartySessionID | WithPartySessionIDSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithPartySessionIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_start_observing.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_start_observing.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_stop_observing**
<a name="game_advertisement_stop_observing"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_stop_observing(advertisementidlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_advertisement_stop_observing(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_stop_observing: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_stop_observing.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_stop_observing.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_update**
<a name="game_advertisement_update"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_update(advertisementidapp_binary_checksumautomatch_poll_iddata_checksumdescriptionhostidis_observablelast_call_timemapnamematchtypemaxplayersmod_dll_checksummod_dll_filemod_namemod_versionobserver_delayobserver_passwordoptionspasswordpasswordedraceslotinfostateteamversion_flagsvisible)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'appBinaryChecksum': 24916,
        'automatchPoll_id': -1,
        'callNum': 148,
        'dataChecksum': -638535971,
        'description': "[\"SESSION_MATCH_KEY\",\"Test\"]",
        'hostid': 1,
        'isObservable': 1,
        'lastCallTime': "918824",
        'mapname': "[\"no_map\",\"ang_chp1_hastings\"]",
        'matchtype': 19,
        'maxplayers': 8,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'observerDelay': 180,
        'observerPassword': "unknown password",
        'options': "opts",
        'password': "test",
        'passworded': [0,1],
        'race': 2039321,
        'slotinfo': "eNrtjkEKwjAQRT3LrKNYl10XoWBBqjtxMaQTHGySkoxCEe8uiaDewE127zMP5lUbdXrAFLzhkVpn/IoHqJeVgigo7F3bvKcQ2sRrBQb17yWgpi+7647uNGYxrQ5FX47z9FGELe0pbANa6g7Z49gTDnPm9PYWM1oSbFAQaoCnKpWlslSWyr9XnhcvuymdYw==",
        'state': -1,
        'team': -1,
        'versionFlags': 0,
        'visible': 0,
    }
    try:
        api_response = api_instance.game_advertisement_update(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
appBinaryChecksum | AppBinaryChecksumSchema | | 
automatchPoll_id | AutomatchPollIdSchema | | 
callNum | CallNumSchema | | 
dataChecksum | DataChecksumSchema | | 
description | DescriptionSchema | | 
hostid | HostidSchema | | 
isObservable | IsObservableSchema | | 
lastCallTime | LastCallTimeSchema | | 
mapname | MapnameSchema | | 
matchtype | MatchtypeSchema | | 
maxplayers | MaxplayersSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
observerDelay | ObserverDelaySchema | | 
observerPassword | ObserverPasswordSchema | | 
options | OptionsSchema | | 
password | PasswordSchema | | 
passworded | PasswordedSchema | | 
race | RaceSchema | | 
slotinfo | SlotinfoSchema | | 
state | StateSchema | | 
team | TeamSchema | | 
versionFlags | VersionFlagsSchema | | 
visible | VisibleSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AppBinaryChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AutomatchPollIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HostidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsObservableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MapnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchtypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MaxplayersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ObserverDelaySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ObserverPasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PasswordedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SlotinfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VisibleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_update.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_update_platform_lobby_id**
<a name="game_advertisement_update_platform_lobby_id"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_update_platform_lobby_id(last_call_timematch_idplatformlobby_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'matchID': 50865084,
        'platformlobbyID': 109775243868575631,
    }
    try:
        api_response = api_instance.game_advertisement_update_platform_lobby_id(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_update_platform_lobby_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
matchID | MatchIDSchema | | 
platformlobbyID | PlatformlobbyIDSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PlatformlobbyIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_update_platform_lobby_id.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_update_platform_lobby_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_update_state**
<a name="game_advertisement_update_state"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_update_state(advertisementidlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_advertisement_update_state(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_update_state: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_update_state.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_update_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_advertisement_update_tags**
<a name="game_advertisement_update_tags"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_advertisement_update_tags(advertisementidlast_call_timenumeric_tag_namesnumeric_tag_valuesstring_tag_namesstring_tag_values)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'advertisementid': -1,
        'callNum': 148,
        'lastCallTime': "918824",
        'numericTagNames': "[\"CheatsEnabled\",\"Dataset\",\"TreatyLength\",\"Ranked\",\"Password\"]",
        'numericTagValues': [0,1,0,0,0],
        'stringTagNames': "[\"GameType\",\"MapStyleType\",\"Speed\",\"VictoryType\",\"Server\"]",
        'stringTagValues': "[\"0\",\"0\",\"2\",\"9\",\"westeurope\"]",
    }
    try:
        api_response = api_instance.game_advertisement_update_tags(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_advertisement_update_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
advertisementid | AdvertisementidSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
numericTagNames | NumericTagNamesSchema | | 
numericTagValues | NumericTagValuesSchema | | 
stringTagNames | StringTagNamesSchema | | 
stringTagValues | StringTagValuesSchema | | 


# AdvertisementidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NumericTagNamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NumericTagValuesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StringTagNamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StringTagValuesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_advertisement_update_tags.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_advertisement_update_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_automatch2_get_automatch_map**
<a name="game_automatch2_get_automatch_map"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_automatch2_get_automatch_map(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_automatch2_get_automatch_map(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_automatch2_get_automatch_map: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_automatch2_get_automatch_map.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_automatch2_get_automatch_map.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_automatch2_polling**
<a name="game_automatch2_polling"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_automatch2_polling(app_bin_crcdata_crcfaction_idslast_call_timematch_typesmod_dll_checksummod_dll_filemod_namemod_versionoptionsparty_session_idrace_info_keyrace_info_profile_idrace_info_race_idrelay_ping_timesrelay_regionrelay_regionsversion_flagsveto_map_keyveto_maps)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'appBinCRC': 9876,
        'callNum': 148,
        'dataCRC': 6789,
        'factionIDs': [0,0,0,0],
        'lastCallTime': "918824",
        'matchTypes': [20,21,22,23],
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'options': "opts",
        'partySessionID': 50865084,
        'raceInfoKey': [0,1,2,3],
        'raceInfoProfileID': [233334,233334,233334,233334],
        'raceInfoRaceID': [2039321,2039321,2039321,2039321],
        'relayPingTimes': [264,220,253,45,187,191,153,45,119],
        'relayRegion': "[\"australiasoutheast\",\"brazilsouth\",\"koreacentral\",\"ukwest\",\"southeastasia\",\"westus2\",\"westindia\",\"westeurope\",\"eastus\"]",
        'relayRegions': "[\"australiasoutheast\",\"brazilsouth\",\"koreacentral\",\"ukwest\",\"southeastasia\",\"westus2\",\"westindia\",\"westeurope\",\"eastus\"]",
        'versionFlags': 0,
        'vetoMapKey': [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3],
        'vetoMaps': "[\"hideout_tiny\",\"hideout_small\",\"hideout_medium\",\"hideout_large\",\"archipelago_medium\",\"high_view_small\",\"archipelago_large\",\"high_view_medium\",\"archipelago_gigantic\",\"high_view_large\",\"archipelago_small\",\"high_view_tiny\",\"hideout_tiny\",\"hideout_small\",\"hideout_medium\",\"hideout_large\",\"archipelago_medium\",\"high_view_small\",\"archipelago_large\",\"high_view_medium\",\"archipelago_gigantic\",\"high_view_large\",\"archipelago_small\",\"high_view_tiny\",\"hideout_tiny\",\"hideout_small\",\"hideout_medium\",\"hideout_large\",\"archipelago_medium\",\"high_view_small\",\"archipelago_large\",\"high_view_medium\",\"archipelago_gigantic\",\"high_view_large\",\"archipelago_small\",\"high_view_tiny\",\"hideout_tiny\",\"hideout_small\",\"hideout_medium\",\"hideout_large\",\"archipelago_medium\",\"high_view_small\",\"archipelago_large\",\"high_view_medium\",\"archipelago_gigantic\",\"high_view_large\",\"archipelago_small\",\"high_view_tiny\"]",
    }
    try:
        api_response = api_instance.game_automatch2_polling(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_automatch2_polling: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appBinCRC | AppBinCRCSchema | | 
callNum | CallNumSchema | | 
dataCRC | DataCRCSchema | | 
factionIDs | FactionIDsSchema | | 
lastCallTime | LastCallTimeSchema | | 
matchTypes | MatchTypesSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
options | OptionsSchema | | 
partySessionID | PartySessionIDSchema | | 
raceInfoKey | RaceInfoKeySchema | | 
raceInfoProfileID | RaceInfoProfileIDSchema | | 
raceInfoRaceID | RaceInfoRaceIDSchema | | 
relayPingTimes | RelayPingTimesSchema | | 
relayRegion | RelayRegionSchema | | 
relayRegions | RelayRegionsSchema | | 
versionFlags | VersionFlagsSchema | | 
vetoMapKey | VetoMapKeySchema | | 
vetoMaps | VetoMapsSchema | | 


# AppBinCRCSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# DataCRCSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FactionIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchTypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartySessionIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceInfoKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceInfoProfileIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceInfoRaceIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RelayPingTimesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RelayRegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RelayRegionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VetoMapKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VetoMapsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_automatch2_polling.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_automatch2_polling.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_automatch2_stop_polling**
<a name="game_automatch2_stop_polling"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_automatch2_stop_polling(commitlast_call_timeowner_profile_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'commit': 0,
        'lastCallTime': "918824",
        'ownerProfileID': 233334,
    }
    try:
        api_response = api_instance.game_automatch2_stop_polling(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_automatch2_stop_polling: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
commit | CommitSchema | | 
lastCallTime | LastCallTimeSchema | | 
ownerProfileID | OwnerProfileIDSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# CommitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OwnerProfileIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_automatch2_stop_polling.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_automatch2_stop_polling.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_automatch2_update_status**
<a name="game_automatch2_update_status"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_automatch2_update_status(last_call_timematch_idresultresult_code)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'matchID': 50865084,
        'result': 1,
        'resultCode': 0,
    }
    try:
        api_response = api_instance.game_automatch2_update_status(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_automatch2_update_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
matchID | MatchIDSchema | | 
result | ResultSchema | | 
resultCode | ResultCodeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResultSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResultCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_automatch2_update_status.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_automatch2_update_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_automatch_get_automatch_map**
<a name="game_automatch_get_automatch_map"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_automatch_get_automatch_map(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_automatch_get_automatch_map(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_automatch_get_automatch_map: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_automatch_get_automatch_map.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_automatch_get_automatch_map.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_challenge_get_challenge_progress**
<a name="game_challenge_get_challenge_progress"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_challenge_get_challenge_progress(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_challenge_get_challenge_progress(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_challenge_get_challenge_progress: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_challenge_get_challenge_progress.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_challenge_get_challenge_progress.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_challenge_get_challenge_progress_by_profile_id**
<a name="game_challenge_get_challenge_progress_by_profile_id"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_challenge_get_challenge_progress_by_profile_id(last_call_timeprofile_id)



TODO: Request not available in Wiki, this is guessed

### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profile_id': 196240,
    }
    try:
        api_response = api_instance.game_challenge_get_challenge_progress_by_profile_id(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_challenge_get_challenge_progress_by_profile_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profile_id | ProfileIdSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_challenge_get_challenge_progress_by_profile_id.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_challenge_get_challenge_progress_by_profile_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_challenge_get_challenges**
<a name="game_challenge_get_challenges"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_challenge_get_challenges(last_call_timesignature)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'signature': "wqFWpWL7ZV67HZ7b1kXEAtWofi34DFHX/HoiyJm46ooePlthNsS5F2TQiLHzUOSYuV/VGDmpk1Dr7r6E/OukY/lDE4MgrRQBkOTvV8HAnqJIAcqDTiZN9l1bimxn14vrnnNaBcOZyOvnkZD5oVahECESHlxgEewOhTdkOxLAuXLA+QxXYBlswaperH95/wGhUg11NN0AG2L/6ej929D5NIqDGlVrmp1oBRNYTqRhbvOgjyII0XElAvKwaR+bYKGqchd8RU4WGwPsrhN/5IKl4E7SpJH9UAWV4bH9v6lVwJqz8NGCawmq1p+V22G239k/c7x6chtyOJBPG9N220ot5A==",
    }
    try:
        api_response = api_instance.game_challenge_get_challenges(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_challenge_get_challenges: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
signature | SignatureSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SignatureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_challenge_get_challenges.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_challenge_get_challenges.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_challenge_update_progress_batched**
<a name="game_challenge_update_progress_batched"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_challenge_update_progress_batched(last_call_timeprogress_idsupdate_amounts)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'progressIDs': [646542981],
        'updateAmounts': [1],
    }
    try:
        api_response = api_instance.game_challenge_update_progress_batched(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_challenge_update_progress_batched: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
progressIDs | ProgressIDsSchema | | 
updateAmounts | UpdateAmountsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProgressIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# UpdateAmountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_challenge_update_progress_batched.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_challenge_update_progress_batched.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_chat_delete_offline_message**
<a name="game_chat_delete_offline_message"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_chat_delete_offline_message(last_call_timemessage_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'messageID': 70218256,
    }
    try:
        api_response = api_instance.game_chat_delete_offline_message(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_chat_delete_offline_message: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
messageID | MessageIDSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MessageIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_chat_delete_offline_message.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_chat_delete_offline_message.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_chat_get_chat_channels**
<a name="game_chat_get_chat_channels"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_chat_get_chat_channels(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_chat_get_chat_channels(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_chat_get_chat_channels: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_chat_get_chat_channels.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_chat_get_chat_channels.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_chat_get_offline_messages**
<a name="game_chat_get_offline_messages"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_chat_get_offline_messages(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_chat_get_offline_messages(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_chat_get_offline_messages: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_chat_get_offline_messages.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_chat_get_offline_messages.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_apply**
<a name="game_clan_apply"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_apply(clan_list_namelast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'clanList_name': "TURK",
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_clan_apply(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_apply: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
clanList_name | ClanListNameSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ClanListNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_apply.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_apply.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_create**
<a name="game_clan_create"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_create(chatcostdemotedescriptiondisbandedit_infoedit_permissionfull_nameiconinviteitem_price_idjoin_policylast_call_timeloc_string_idmessage_of_the_daymetadatanamepaymentitempermission_namepromoterankremovetags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'chat': "[\"\"]",
        'cost': 0,
        'demote': "[\"\"]",
        'description': "[\"SESSION_MATCH_KEY\",\"Test\"]",
        'disband': "[\"\"]",
        'editInfo': "[\"\"]",
        'editPermission': "[\"\"]",
        'fullName': "Rusty",
        'icon': "CR-001",
        'invite': "[\"\"]",
        'itemPrice_id': -1,
        'joinPolicy': 1,
        'lastCallTime': "918824",
        'locStringID': [],
        'messageOfTheDay': "messageOfTheDay_example",
        'metadata': dict(),
        'name': "name_example",
        'paymentitem': -1,
        'permissionName': "[]",
        'promote': "[]",
        'rank': "[]",
        'remove': "[]",
        'tags': "[]",
    }
    try:
        api_response = api_instance.game_clan_create(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
chat | ChatSchema | | 
cost | CostSchema | | 
demote | DemoteSchema | | 
description | DescriptionSchema | | 
disband | DisbandSchema | | 
editInfo | EditInfoSchema | | 
editPermission | EditPermissionSchema | | 
fullName | FullNameSchema | | 
icon | IconSchema | | 
invite | InviteSchema | | 
itemPrice_id | ItemPriceIdSchema | | 
joinPolicy | JoinPolicySchema | | 
lastCallTime | LastCallTimeSchema | | 
locStringID | LocStringIDSchema | | 
messageOfTheDay | MessageOfTheDaySchema | | 
metadata | MetadataSchema | | 
name | NameSchema | | 
paymentitem | PaymentitemSchema | | 
permissionName | PermissionNameSchema | | 
promote | PromoteSchema | | 
rank | RankSchema | | 
remove | RemoveSchema | | 
tags | TagsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ChatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CostSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DemoteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DisbandSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EditInfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EditPermissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FullNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IconSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# InviteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ItemPriceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# JoinPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LocStringIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MessageOfTheDaySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaymentitemSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PermissionNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PromoteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RankSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RemoveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_create.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_disband**
<a name="game_clan_disband"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_disband(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_clan_disband(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_disband: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_disband.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_disband.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_find**
<a name="game_clan_find"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_find(countjoin_policieslast_call_timenamestarttags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'count': 200,
        'joinPolicies': [0,1,2],
        'lastCallTime': "918824",
        'name': "name_example",
        'start': 0,
        'tags': "[]",
    }
    try:
        api_response = api_instance.game_clan_find(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_find: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
count | CountSchema | | 
joinPolicies | JoinPoliciesSchema | | 
lastCallTime | LastCallTimeSchema | | 
name | NameSchema | | 
start | StartSchema | | 
tags | TagsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# JoinPoliciesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_find.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_find.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_get_clan**
<a name="game_clan_get_clan"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_get_clan(last_call_timenames)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'names': "[\"Liiit\"]",
    }
    try:
        api_response = api_instance.game_clan_get_clan(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_get_clan: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
names | NamesSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_get_clan.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_get_clan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_get_clan_info_full**
<a name="game_clan_get_clan_info_full"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_get_clan_info_full(last_call_timename)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'name': "name_example",
    }
    try:
        api_response = api_instance.game_clan_get_clan_info_full(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_get_clan_info_full: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
name | NameSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_get_clan_info_full.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_get_clan_info_full.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_clan_update**
<a name="game_clan_update"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_clan_update(clan_list_iddescriptioniconjoin_policylast_call_timemessage_of_the_daymetadatatags)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'clanList_id': 110061,
        'description': "[\"SESSION_MATCH_KEY\",\"Test\"]",
        'icon': "CR-001",
        'joinPolicy': 1,
        'lastCallTime': "918824",
        'messageOfTheDay': "messageOfTheDay_example",
        'metadata': dict(),
        'tags': "[]",
    }
    try:
        api_response = api_instance.game_clan_update(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_clan_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
clanList_id | ClanListIdSchema | | 
description | DescriptionSchema | | 
icon | IconSchema | | 
joinPolicy | JoinPolicySchema | | 
lastCallTime | LastCallTimeSchema | | 
messageOfTheDay | MessageOfTheDaySchema | | 
metadata | MetadataSchema | | 
tags | TagsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ClanListIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IconSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JoinPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MessageOfTheDaySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_clan_update.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_clan_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_cloud_get_file_url_get**
<a name="game_cloud_get_file_url_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_cloud_get_file_url_get(last_call_timenames)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'names': "[\"Liiit\"]",
    }
    try:
        api_response = api_instance.game_cloud_get_file_url_get(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_cloud_get_file_url_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
names | NamesSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_cloud_get_file_url_get.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_cloud_get_file_url_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_cloud_get_file_url_post**
<a name="game_cloud_get_file_url_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_cloud_get_file_url_post(last_call_timenames)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'names': "[\"Liiit\"]",
    }
    try:
        api_response = api_instance.game_cloud_get_file_url_post(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_cloud_get_file_url_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
names | NamesSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_cloud_get_file_url_post.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_cloud_get_file_url_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_cloud_get_temp_credentials**
<a name="game_cloud_get_temp_credentials"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_cloud_get_temp_credentials(last_call_timekey)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'key': "/cloudfiles/game/6b861a867ce5f4e66131c929fe13db8baa40b5bb412255adcc225e6604ff703f",
    }
    try:
        api_response = api_instance.game_cloud_get_temp_credentials(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_cloud_get_temp_credentials: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
key | KeySchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_cloud_get_temp_credentials.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_cloud_get_temp_credentials.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_community_event_get_available_community_events**
<a name="game_community_event_get_available_community_events"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_community_event_get_available_community_events(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_community_event_get_available_community_events(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_community_event_get_available_community_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_community_event_get_available_community_events.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_community_event_get_available_community_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_community_event_get_event_challenge_progress**
<a name="game_community_event_get_event_challenge_progress"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_community_event_get_event_challenge_progress(event_idlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'event_id': 22,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_community_event_get_event_challenge_progress(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_community_event_get_event_challenge_progress: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
event_id | EventIdSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# EventIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_community_event_get_event_challenge_progress.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_community_event_get_event_challenge_progress.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_community_event_get_event_stats**
<a name="game_community_event_get_event_stats"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_community_event_get_event_stats(event_idgroup_typelast_call_timemember_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'event_id': 22,
        'group_type': 1,
        'lastCallTime': "918824",
        'member_id': 11190194,
    }
    try:
        api_response = api_instance.game_community_event_get_event_stats(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_community_event_get_event_stats: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
event_id | EventIdSchema | | 
group_type | GroupTypeSchema | | 
lastCallTime | LastCallTimeSchema | | 
member_id | MemberIdSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# EventIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GroupTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MemberIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_community_event_get_event_stats.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_community_event_get_event_stats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_invitation_cancel_invitation**
<a name="game_invitation_cancel_invitation"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_invitation_cancel_invitation(gatheringidinviteeidlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'gatheringid': 186430525,
        'inviteeid': 421346,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_invitation_cancel_invitation(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_invitation_cancel_invitation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
gatheringid | GatheringidSchema | | 
inviteeid | InviteeidSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# GatheringidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# InviteeidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_invitation_cancel_invitation.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_invitation_cancel_invitation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_invitation_extend_invitation**
<a name="game_invitation_extend_invitation"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_invitation_extend_invitation(gatheringidgatheringpasswordinviteeidlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'gatheringid': 186430525,
        'gatheringpassword': "password!",
        'inviteeid': 421346,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_invitation_extend_invitation(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_invitation_extend_invitation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
gatheringid | GatheringidSchema | | 
gatheringpassword | GatheringpasswordSchema | | 
inviteeid | InviteeidSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# GatheringidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GatheringpasswordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# InviteeidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_invitation_extend_invitation.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_invitation_extend_invitation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_detach_items**
<a name="game_item_detach_items"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_detach_items(item_chargesitem_idsitem_locationslast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'itemCharges': [1,1,1,1,1,1],
        'itemIDs': [449911890,449911890,449911888,449911890,449911888,449911889],
        'itemLocations': [0,0,0,0,0,0],
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_item_detach_items(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_detach_items: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
itemCharges | ItemChargesSchema | | 
itemIDs | ItemIDsSchema | | 
itemLocations | ItemLocationsSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ItemChargesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ItemIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ItemLocationsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_detach_items.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_detach_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_inventory_by_profile_ids**
<a name="game_item_get_inventory_by_profile_ids"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_inventory_by_profile_ids(last_call_timeprofile_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profileIDs': [196240,196241],
    }
    try:
        api_response = api_instance.game_item_get_inventory_by_profile_ids(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_inventory_by_profile_ids: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profileIDs | ProfileIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_inventory_by_profile_ids.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_inventory_by_profile_ids.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_item_bundle_items_json**
<a name="game_item_get_item_bundle_items_json"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_item_bundle_items_json(last_call_timesignature)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'signature': "wqFWpWL7ZV67HZ7b1kXEAtWofi34DFHX/HoiyJm46ooePlthNsS5F2TQiLHzUOSYuV/VGDmpk1Dr7r6E/OukY/lDE4MgrRQBkOTvV8HAnqJIAcqDTiZN9l1bimxn14vrnnNaBcOZyOvnkZD5oVahECESHlxgEewOhTdkOxLAuXLA+QxXYBlswaperH95/wGhUg11NN0AG2L/6ej929D5NIqDGlVrmp1oBRNYTqRhbvOgjyII0XElAvKwaR+bYKGqchd8RU4WGwPsrhN/5IKl4E7SpJH9UAWV4bH9v6lVwJqz8NGCawmq1p+V22G239k/c7x6chtyOJBPG9N220ot5A==",
    }
    try:
        api_response = api_instance.game_item_get_item_bundle_items_json(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_item_bundle_items_json: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
signature | SignatureSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SignatureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_item_bundle_items_json.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_item_bundle_items_json.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_item_definitions_json**
<a name="game_item_get_item_definitions_json"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_item_definitions_json(last_call_timesignature)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'signature': "wqFWpWL7ZV67HZ7b1kXEAtWofi34DFHX/HoiyJm46ooePlthNsS5F2TQiLHzUOSYuV/VGDmpk1Dr7r6E/OukY/lDE4MgrRQBkOTvV8HAnqJIAcqDTiZN9l1bimxn14vrnnNaBcOZyOvnkZD5oVahECESHlxgEewOhTdkOxLAuXLA+QxXYBlswaperH95/wGhUg11NN0AG2L/6ej929D5NIqDGlVrmp1oBRNYTqRhbvOgjyII0XElAvKwaR+bYKGqchd8RU4WGwPsrhN/5IKl4E7SpJH9UAWV4bH9v6lVwJqz8NGCawmq1p+V22G239k/c7x6chtyOJBPG9N220ot5A==",
    }
    try:
        api_response = api_instance.game_item_get_item_definitions_json(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_item_definitions_json: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
signature | SignatureSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SignatureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_item_definitions_json.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_item_definitions_json.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_item_loadouts**
<a name="game_item_get_item_loadouts"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_item_loadouts(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_item_get_item_loadouts(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_item_loadouts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_item_loadouts.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_item_loadouts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_item_prices**
<a name="game_item_get_item_prices"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_item_prices(account_typelast_call_timecountrycurrencysale_version)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'accountType': "STEAM",
        'callNum': 148,
        'lastCallTime': "918824",
        'country': "[\"US\",\"DE\"]",
        'currency': "[\"usd\"]",
        'saleVersion': -1,
    }
    try:
        api_response = api_instance.game_item_get_item_prices(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_item_prices: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountType | AccountTypeSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
country | CountrySchema | | 
currency | CurrencySchema | | 
saleVersion | SaleVersionSchema | | 


# AccountTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CurrencySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SaleVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_item_prices.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_item_prices.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_level_rewards_table_json**
<a name="game_item_get_level_rewards_table_json"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_level_rewards_table_json(last_call_timesignature)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'signature': "wqFWpWL7ZV67HZ7b1kXEAtWofi34DFHX/HoiyJm46ooePlthNsS5F2TQiLHzUOSYuV/VGDmpk1Dr7r6E/OukY/lDE4MgrRQBkOTvV8HAnqJIAcqDTiZN9l1bimxn14vrnnNaBcOZyOvnkZD5oVahECESHlxgEewOhTdkOxLAuXLA+QxXYBlswaperH95/wGhUg11NN0AG2L/6ej929D5NIqDGlVrmp1oBRNYTqRhbvOgjyII0XElAvKwaR+bYKGqchd8RU4WGwPsrhN/5IKl4E7SpJH9UAWV4bH9v6lVwJqz8NGCawmq1p+V22G239k/c7x6chtyOJBPG9N220ot5A==",
    }
    try:
        api_response = api_instance.game_item_get_level_rewards_table_json(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_level_rewards_table_json: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
signature | SignatureSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SignatureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_level_rewards_table_json.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_level_rewards_table_json.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_personalized_sale_items**
<a name="game_item_get_personalized_sale_items"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_personalized_sale_items(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_item_get_personalized_sale_items(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_personalized_sale_items: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_personalized_sale_items.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_personalized_sale_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_get_scheduled_sale_and_items**
<a name="game_item_get_scheduled_sale_and_items"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_get_scheduled_sale_and_items(last_call_timesale_type)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'saleType': 1,
    }
    try:
        api_response = api_instance.game_item_get_scheduled_sale_and_items(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_get_scheduled_sale_and_items: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
saleType | SaleTypeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SaleTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_get_scheduled_sale_and_items.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_get_scheduled_sale_and_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_move_charges**
<a name="game_item_move_charges"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_move_charges(chargesdeletesfrom_item_idslast_call_timeto_item_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'charges': [1],
        'deletes': [1],
        'fromItemIDs': [449911778],
        'lastCallTime': "918824",
        'toItemIDs': [449911716],
    }
    try:
        api_response = api_instance.game_item_move_charges(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_move_charges: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
charges | ChargesSchema | | 
deletes | DeletesSchema | | 
fromItemIDs | FromItemIDsSchema | | 
lastCallTime | LastCallTimeSchema | | 
toItemIDs | ToItemIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ChargesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DeletesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FromItemIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToItemIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_move_charges.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_move_charges.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_move_item**
<a name="game_item_move_item"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_move_item(item_idsitem_location_idslast_call_timepos_idsslot_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'itemIDs': [449911890,449911890,449911888,449911890,449911888,449911889],
        'itemLocationIDs': [0,2],
        'lastCallTime': "918824",
        'posIDs': [-1,-1],
        'slotIDs': [-1,-1],
    }
    try:
        api_response = api_instance.game_item_move_item(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_move_item: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
itemIDs | ItemIDsSchema | | 
itemLocationIDs | ItemLocationIDsSchema | | 
lastCallTime | LastCallTimeSchema | | 
posIDs | PosIDsSchema | | 
slotIDs | SlotIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ItemIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ItemLocationIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PosIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SlotIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_move_item.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_move_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_open_item_pack**
<a name="game_item_open_item_pack"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_open_item_pack(choicesitem_instance_iditem_location_idlast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'choices': [],
        'itemInstance_id': 449956852,
        'itemLocation_id': 0,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_item_open_item_pack(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_open_item_pack: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
choices | ChoicesSchema | | 
itemInstance_id | ItemInstanceIdSchema | | 
itemLocation_id | ItemLocationIdSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ChoicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ItemInstanceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ItemLocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_open_item_pack.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_open_item_pack.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_sign_item**
<a name="game_item_sign_item"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_sign_item(crclast_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'crc': 3611078805,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_item_sign_item(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_sign_item: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
crc | CrcSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# CrcSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_sign_item.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_sign_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_item_update_item_attributes**
<a name="game_item_update_item_attributes"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_item_update_item_attributes(attribute_keysattribute_valuesitem_instance_idslast_call_timexp_gains)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'attributeKeys': "[[\"is_new\"]]",
        'attributeValues': "[[\"0\"]]",
        'callNum': 148,
        'itemInstance_ids': [449911889],
        'lastCallTime': "918824",
        'xpGains': [0],
    }
    try:
        api_response = api_instance.game_item_update_item_attributes(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_item_update_item_attributes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
attributeKeys | AttributeKeysSchema | | 
attributeValues | AttributeValuesSchema | | 
callNum | CallNumSchema | | 
itemInstance_ids | ItemInstanceIdsSchema | | 
lastCallTime | LastCallTimeSchema | | 
xpGains | XpGainsSchema | | 


# AttributeKeysSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AttributeValuesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ItemInstanceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XpGainsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_item_update_item_attributes.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_item_update_item_attributes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_available_leaderboards**
<a name="game_leaderboard_get_available_leaderboards"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_available_leaderboards(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_leaderboard_get_available_leaderboards(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_available_leaderboards: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_available_leaderboards.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_available_leaderboards.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_leaderboard**
<a name="game_leaderboard_get_leaderboard"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_leaderboard(last_call_timestartcount)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'start': 0,
        'count': 200,
    }
    try:
        api_response = api_instance.game_leaderboard_get_leaderboard(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_leaderboard: %s\n" % e)

    # example passing only optional values
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'leaderboard_id': 3,
        'start': 0,
        'sortBy': 1,
        'count': 200,
    }
    try:
        api_response = api_instance.game_leaderboard_get_leaderboard(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_leaderboard: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
leaderboard_id | LeaderboardIdSchema | | optional
start | StartSchema | | 
sortBy | SortBySchema | | optional
count | CountSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeaderboardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_leaderboard.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_leaderboard.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_party_stat**
<a name="game_leaderboard_get_party_stat"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_party_stat(last_call_timestatsids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'statsids': [1,2],
    }
    try:
        api_response = api_instance.game_leaderboard_get_party_stat(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_party_stat: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
statsids | StatsidsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatsidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_party_stat.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_party_stat.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_personal_stat**
<a name="game_leaderboard_get_personal_stat"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_personal_stat(last_call_time)



TODO: No request documented in Wiki, guessed parameters

### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_leaderboard_get_personal_stat(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_personal_stat: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_personal_stat.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_personal_stat.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_recent_match_history_get**
<a name="game_leaderboard_get_recent_match_history_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_recent_match_history_get(last_call_timeprofile_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profile_ids': [196240],
    }
    try:
        api_response = api_instance.game_leaderboard_get_recent_match_history_get(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_recent_match_history_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profile_ids | ProfileIdsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_recent_match_history_get.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_recent_match_history_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_recent_match_history_post**
<a name="game_leaderboard_get_recent_match_history_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_recent_match_history_post(last_call_timeprofile_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profile_ids': [196240],
    }
    try:
        api_response = api_instance.game_leaderboard_get_recent_match_history_post(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_recent_match_history_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profile_ids | ProfileIdsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_recent_match_history_post.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_recent_match_history_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_recent_match_single_player_history**
<a name="game_leaderboard_get_recent_match_single_player_history"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_recent_match_single_player_history(last_call_timeprofile_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profile_ids': [196240],
    }
    try:
        api_response = api_instance.game_leaderboard_get_recent_match_single_player_history(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_recent_match_single_player_history: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profile_ids | ProfileIdsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_recent_match_single_player_history.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_recent_match_single_player_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_stat_groups_by_profile_ids**
<a name="game_leaderboard_get_stat_groups_by_profile_ids"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_stat_groups_by_profile_ids(last_call_timeprofileids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profileids': [2132331,31323213],
    }
    try:
        api_response = api_instance.game_leaderboard_get_stat_groups_by_profile_ids(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_stat_groups_by_profile_ids: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
profileids | ProfileidsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_stat_groups_by_profile_ids.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_stat_groups_by_profile_ids.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_get_stats_for_leaderboard_by_profile_name**
<a name="game_leaderboard_get_stats_for_leaderboard_by_profile_name"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_get_stats_for_leaderboard_by_profile_name(last_call_timeprofileids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'profileids': [2132331,31323213],
    }
    try:
        api_response = api_instance.game_leaderboard_get_stats_for_leaderboard_by_profile_name(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_stats_for_leaderboard_by_profile_name: %s\n" % e)

    # example passing only optional values
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'leaderboard_id': 3,
        'profileids': [2132331,31323213],
    }
    try:
        api_response = api_instance.game_leaderboard_get_stats_for_leaderboard_by_profile_name(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_get_stats_for_leaderboard_by_profile_name: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
leaderboard_id | LeaderboardIdSchema | | optional
profileids | ProfileidsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeaderboardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ProfileidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_get_stats_for_leaderboard_by_profile_name.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_get_stats_for_leaderboard_by_profile_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_leaderboard_set_avatar_stat_values**
<a name="game_leaderboard_set_avatar_stat_values"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_leaderboard_set_avatar_stat_values(avatar_stat_idslast_call_timeupdate_typesvalues)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'avatarStat_ids': [156],
        'callNum': 148,
        'lastCallTime': "918824",
        'updateTypes': [2],
        'values': [687],
    }
    try:
        api_response = api_instance.game_leaderboard_set_avatar_stat_values(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_leaderboard_set_avatar_stat_values: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
avatarStat_ids | AvatarStatIdsSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
updateTypes | UpdateTypesSchema | | 
values | ValuesSchema | | 


# AvatarStatIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UpdateTypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ValuesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_leaderboard_set_avatar_stat_values.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_leaderboard_set_avatar_stat_values.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_login_logout**
<a name="game_login_logout"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_login_logout(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_login_logout(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_login_logout: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_login_logout.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_login_logout.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_login_platform_login**
<a name="game_login_platform_login"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_login_platform_login(account_typealiasapp_idclient_lib_versionconnect_idcountryinstallation_typelast_call_timemac_addressmajor_versionminor_versionplatform_user_idstart_game_tokensync_hash)



### Example

* Api Key Authentication (authLogin):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authLogin
configuration.api_key['authLogin'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authLogin'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'accountType': "STEAM",
        'activeMatchId': -1,
        'alias': "Name",
        'appID': 1466860,
        'callNum': 148,
        'clientLibVersion': 176,
        'connect_id': "bgoo2n1murnn43kzdnnfc9fhp2no19",
        'country': "[\"US\",\"DE\"]",
        'installationType': "windows",
        'lastCallTime': "918824",
        'macAddress': "D4-BA-A1-43-29-19",
        'majorVersion': "4.0.0",
        'minorVersion': 24916,
        'platformUserID': 765613333337299,
        'startGameToken': "startGameToken_example",
        'syncHash': [0,0],
        'timeoutOverride': 0,
    }
    try:
        api_response = api_instance.game_login_platform_login(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_login_platform_login: %s\n" % e)

    # example passing only optional values
    query_params = {
        'accountType': "STEAM",
        'activeMatchId': -1,
        'alias': "Name",
        'appID': 1466860,
        'callNum': 148,
        'clientLibVersion': 176,
        'connect_id': "bgoo2n1murnn43kzdnnfc9fhp2no19",
        'country': "[\"US\",\"DE\"]",
        'installationType': "windows",
        'language': "[\"en\",\"de\",\"es\",\"fr\"]",
        'lastCallTime': "918824",
        'macAddress': "D4-BA-A1-43-29-19",
        'majorVersion': "4.0.0",
        'minorVersion': 24916,
        'platformUserID': 765613333337299,
        'startGameToken': "startGameToken_example",
        'storeLicenseToken': "storeLicenseToken_example",
        'syncHash': [0,0],
        'timeoutOverride': 0,
        'title': "[\"age1\",\"age2\",\"age3\",\"age4\"]",
    }
    try:
        api_response = api_instance.game_login_platform_login(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_login_platform_login: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountType | AccountTypeSchema | | 
activeMatchId | ActiveMatchIdSchema | | 
alias | AliasSchema | | 
appID | AppIDSchema | | 
callNum | CallNumSchema | | 
clientLibVersion | ClientLibVersionSchema | | 
connect_id | ConnectIdSchema | | 
country | CountrySchema | | 
installationType | InstallationTypeSchema | | 
language | LanguageSchema | | optional
lastCallTime | LastCallTimeSchema | | 
macAddress | MacAddressSchema | | 
majorVersion | MajorVersionSchema | | 
minorVersion | MinorVersionSchema | | 
platformUserID | PlatformUserIDSchema | | 
startGameToken | StartGameTokenSchema | | 
storeLicenseToken | StoreLicenseTokenSchema | | optional
syncHash | SyncHashSchema | | 
timeoutOverride | TimeoutOverrideSchema | | 
title | TitleSchema | | optional


# AccountTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ActiveMatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of -1

# AliasSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AppIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ClientLibVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ConnectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# InstallationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MacAddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MajorVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MinorVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PlatformUserIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartGameTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StoreLicenseTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SyncHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TimeoutOverrideSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_login_platform_login.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_login_platform_login.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[authLogin](../../../README.md#authLogin)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_login_read_session**
<a name="game_login_read_session"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_login_read_session(ackpoll_num)



### Example

* Api Key Authentication (sessionID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'ack': 0,
        'pollNum': 0,
    }
    try:
        api_response = api_instance.game_login_read_session(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_login_read_session: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ack | AckSchema | | 
pollNum | PollNumSchema | | 


# AckSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PollNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_login_read_session.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_login_read_session.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_news_get_news**
<a name="game_news_get_news"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_news_get_news(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_news_get_news(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_news_get_news: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_news_get_news.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_news_get_news.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_party_create_or_report_single_player**
<a name="game_party_create_or_report_single_player"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_party_create_or_report_single_player(appbincrccounters_zipdatacrcitem_updateslast_call_timemapnamematch_keymatch_type_idmod_dll_checksummod_dll_filemod_namemod_versionoptionsrace_idsresultsslot_infoteam_idsversion_flagsxp_gained)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'appbincrc': 24916,
        'callNum': 148,
        'countersZip': "H4sIAAAAAAAACouOBQApu0wNAgAAAA==",
        'createMatchKey': 1,
        'datacrc': -638535971,
        'isComplete': 0,
        'itemUpdates': [],
        'lastCallTime': "918824",
        'mapname': "[\"no_map\",\"ang_chp1_hastings\"]",
        'matchKey': "matchKey_example",
        'matchTypeID': 17,
        'modDLLChecksum': 0,
        'modDLLFile': "INVALID",
        'modName': "INVALID",
        'modVersion': "INVALID",
        'options': "opts",
        'race_ids': [1,2],
        'results': [],
        'slotInfo': "eNrtVltvo0YU7m/xc7aCwSRLpH0wdgZj2Thg7lUfGMDiMmAaMDau+t97BpzEmzRdrdqXSH5AzJwznDmX7/tsHt389ueoetptUxqr5Xb3axqN7pEwvhXGN6O6CZp0V6qz0T1/M2rioGBL7ma0DcJnB+yegjBmS4T4u/GY7ct8GbcxPXvLfBU0YWJ2VX/sC4uVFvFj/ISfgiJebfpzaW3EQdT1a3bxvu6XRdwEs6AJRvejuFs0LqJ7A+HG36i3q+khJbZUkdKnpDTasKQb38F5/Oo7EAWLvrt4tW96e+c5Yk4Qb0YK7iIstyGiXOBIezXbHZdTuEfQOM9dgE0sLUU6Ba5RETRO1yk3+BHf+lhOPNQ8hnPmE09qVt2pxYud7YnrcjXYtsSRckvBWcD5tedE4Nsd3sQ5WYKRRHO7/w5qTcJCWxhT9VbNjZXmSMslJ/3hc7aroWS/xrTSkH6w+QfpcaPWasnyNfiwG2oP0bGN4Nul+QD3G3syZfbxYTWbwCNL7tCHJLBlGpZaSwpcQ40i5JWq6dlnHVvPMdrI1dN1pndrUxe1LIS31dfkIelEHBt6pL3twTZUMMzFMD2UUDjT13GeXw53cKss59amJ8CbH/ptiKFiwT2yNOzlBHrPWfNFRRzcsdmp6dd22X1toxMnnXM8eA7dR1ijkMveV350zugCh4MZqr1/KYRD717ztfx+5h/GSaEfpW/LEIdPwjJ/E2txzt2gnsPLRDlWgLOMYVXNsaxb8JgvsWC+vKg7UJ/CsDfM/XkuzGe7chkWOPfdVbqmTTTgBXfEpTYpKMdm7fADvnxFWhPB2JxxXcUF6+VD7wtcDewatQoMPZIaMqem7xypB3n60xeu7DxXmxJFygJk57YVzV4wKsi151Ia5oATReLDlOFqIU0m376N/rp5rx+M4Rfa8eVCPPgPxYMTb+++Fw/038QD/f/iMf0c4vFv5PYVu/Bcu46wlAFIGTFKkg4kgPWKIJwTweb+kaRIg1p5Gik0MwW5r5mBsO/tM2GRtvMdnm4sEI2y7nvMQKbNVFGb5Ug7wXvIj4tdmbJatptLkn5Eru+ICgBmdRk/OmeFBW1Y3b2/k4RHk0svBcZW7A7q+TCOxwiIbJ3FgZmKb2Odc+cAI43uHGsQj72HgHzpQrYY4a2H11juooktnAbOsYI76SWBe59tH3xhkcCM3ouBI1bR/FIIjNYsJO6Z1IFb0Rf8IXoCe+bbiwR61BLnKFrIrqFnkCcT8",
        'teamIDs': [],
        'versionFlags': 0,
        'xpGained': [0],
    }
    try:
        api_response = api_instance.game_party_create_or_report_single_player(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_party_create_or_report_single_player: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appbincrc | AppbincrcSchema | | 
callNum | CallNumSchema | | 
countersZip | CountersZipSchema | | 
createMatchKey | CreateMatchKeySchema | | 
datacrc | DatacrcSchema | | 
isComplete | IsCompleteSchema | | 
itemUpdates | ItemUpdatesSchema | | 
lastCallTime | LastCallTimeSchema | | 
mapname | MapnameSchema | | 
matchKey | MatchKeySchema | | 
matchTypeID | MatchTypeIDSchema | | 
modDLLChecksum | ModDLLChecksumSchema | | 
modDLLFile | ModDLLFileSchema | | 
modName | ModNameSchema | | 
modVersion | ModVersionSchema | | 
options | OptionsSchema | | 
race_ids | RaceIdsSchema | | 
results | ResultsSchema | | 
slotInfo | SlotInfoSchema | | 
teamIDs | TeamIDsSchema | | 
versionFlags | VersionFlagsSchema | | 
xpGained | XpGainedSchema | | 


# AppbincrcSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# CountersZipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreateMatchKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1

# DatacrcSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsCompleteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ItemUpdatesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MapnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchTypeIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLChecksumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ModDLLFileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RaceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResultsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SlotInfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VersionFlagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XpGainedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_party_create_or_report_single_player.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_party_create_or_report_single_player.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_party_finalize_replay_upload**
<a name="game_party_finalize_replay_upload"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_party_finalize_replay_upload(error_stringlast_call_timematch_idsizeurl)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'errorString': "[]",
        'finalizeResult': 1,
        'isSinglePlayer': [0,1],
        'lastCallTime': "918824",
        'match_id': 186444398,
        'size': 340242,
        'url': "https://rl0aoelivemk2blob.blob.core.windows.net/cloudfiles/436432/aoelive_/age2/replay/windows/4.0.0/0/M_186444398_8b31ed6602350cce7ee1736393cab532712c579e545fdd41995117491b1ae319.gz",
    }
    try:
        api_response = api_instance.game_party_finalize_replay_upload(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_party_finalize_replay_upload: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
errorString | ErrorStringSchema | | 
finalizeResult | FinalizeResultSchema | | 
isSinglePlayer | IsSinglePlayerSchema | | 
lastCallTime | LastCallTimeSchema | | 
match_id | MatchIdSchema | | 
size | SizeSchema | | 
url | UrlSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# ErrorStringSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinalizeResultSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1

# IsSinglePlayerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_party_finalize_replay_upload.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_party_finalize_replay_upload.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_party_peer_add**
<a name="game_party_peer_add"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_party_peer_add(last_call_timematch_idprofile_idsrace_idsstat_group_idsteam_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'match_id': 186444398,
        'profile_ids': [196240],
        'race_ids': [1,2],
        'statGroup_ids': [12,34],
        'teamIDs': [],
    }
    try:
        api_response = api_instance.game_party_peer_add(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_party_peer_add: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
match_id | MatchIdSchema | | 
profile_ids | ProfileIdsSchema | | 
race_ids | RaceIdsSchema | | 
statGroup_ids | StatGroupIdsSchema | | 
teamIDs | TeamIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatGroupIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_party_peer_add.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_party_peer_add.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_party_peer_update**
<a name="game_party_peer_update"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_party_peer_update(is_non_participantslast_call_timematch_idprofile_idsrace_idsteam_ids)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'isNonParticipants': [0,0],
        'lastCallTime': "918824",
        'match_id': 186444398,
        'profile_ids': [196240],
        'race_ids': [1,2],
        'teamIDs': [],
    }
    try:
        api_response = api_instance.game_party_peer_update(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_party_peer_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
isNonParticipants | IsNonParticipantsSchema | | 
lastCallTime | LastCallTimeSchema | | 
match_id | MatchIdSchema | | 
profile_ids | ProfileIdsSchema | | 
race_ids | RaceIdsSchema | | 
teamIDs | TeamIDsSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# IsNonParticipantsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_party_peer_update.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_party_peer_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_party_report_match**
<a name="game_party_report_match"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_party_report_match(check_sumscounters_zipitem_updateslast_call_timematch_idprofile_idsrace_idsresultssimplayer_idsteam_idsxp_gained)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'checkSums': [0,0],
        'countersZip': "H4sIAAAAAAAACouOBQApu0wNAgAAAA==",
        'itemUpdates': [],
        'lastCallTime': "918824",
        'match_id': 186444398,
        'profile_ids': [196240],
        'race_ids': [1,2],
        'results': [],
        'simplayerIDs': [1,7],
        'teamIDs': [],
        'xpGained': [0],
    }
    try:
        api_response = api_instance.game_party_report_match(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_party_report_match: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
checkSums | CheckSumsSchema | | 
countersZip | CountersZipSchema | | 
itemUpdates | ItemUpdatesSchema | | 
lastCallTime | LastCallTimeSchema | | 
match_id | MatchIdSchema | | 
profile_ids | ProfileIdsSchema | | 
race_ids | RaceIdsSchema | | 
results | ResultsSchema | | 
simplayerIDs | SimplayerIDsSchema | | 
teamIDs | TeamIDsSchema | | 
xpGained | XpGainedSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# CheckSumsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CountersZipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ItemUpdatesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ProfileIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RaceIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResultsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SimplayerIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamIDsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XpGainedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_party_report_match.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_party_report_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_party_send_match_chat**
<a name="game_party_send_match_chat"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_party_send_match_chat(broadcastfrom_profile_idlast_call_timematch_idmessagemessage_type_idto_profile_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'broadcast': [0,1],
        'callNum': 148,
        'from_profile_id': 0,
        'lastCallTime': "918824",
        'match_id': 186444398,
        'message': "0*gg",
        'messageTypeID': 0,
        'to_profile_id': 0,
    }
    try:
        api_response = api_instance.game_party_send_match_chat(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_party_send_match_chat: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
broadcast | BroadcastSchema | | 
callNum | CallNumSchema | | 
from_profile_id | FromProfileIdSchema | | 
lastCallTime | LastCallTimeSchema | | 
match_id | MatchIdSchema | | 
message | MessageSchema | | 
messageTypeID | MessageTypeIDSchema | | 
to_profile_id | ToProfileIdSchema | | 


# BroadcastSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# FromProfileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MessageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MessageTypeIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ToProfileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_party_send_match_chat.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_party_send_match_chat.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_playerreport_report_user**
<a name="game_playerreport_report_user"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_playerreport_report_user(commentlast_call_timemetadatareport_reasonreport_typereportee_profile_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'comment': "misclick",
        'lastCallTime': "918824",
        'metadata': dict(),
        'reportReason': 7,
        'reportType': 1,
        'reportee_profile_id': 209072,
    }
    try:
        api_response = api_instance.game_playerreport_report_user(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_playerreport_report_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
comment | CommentSchema | | 
lastCallTime | LastCallTimeSchema | | 
metadata | MetadataSchema | | 
reportReason | ReportReasonSchema | | 
reportType | ReportTypeSchema | | 
reportee_profile_id | ReporteeProfileIdSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# ReportReasonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ReportTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ReporteeProfileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_playerreport_report_user.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_playerreport_report_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_relationship_clear_relationship**
<a name="game_relationship_clear_relationship"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_relationship_clear_relationship(last_call_timerelation_typetarget_profile_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'relationType': [1,2],
        'targetProfileID': 4994658,
    }
    try:
        api_response = api_instance.game_relationship_clear_relationship(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_relationship_clear_relationship: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
relationType | RelationTypeSchema | | 
targetProfileID | TargetProfileIDSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RelationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TargetProfileIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_relationship_clear_relationship.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_relationship_clear_relationship.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_relationship_get_presence_data**
<a name="game_relationship_get_presence_data"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_relationship_get_presence_data(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_relationship_get_presence_data(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_relationship_get_presence_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_relationship_get_presence_data.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_relationship_get_presence_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_relationship_get_relationships**
<a name="game_relationship_get_relationships"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_relationship_get_relationships(last_call_time)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
    }
    try:
        api_response = api_instance.game_relationship_get_relationships(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_relationship_get_relationships: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_relationship_get_relationships.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_relationship_get_relationships.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_relationship_ignore**
<a name="game_relationship_ignore"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_relationship_ignore(blocklevellast_call_timerelation_typetarget_profile_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'blocklevel': [1,2],
        'callNum': 148,
        'lastCallTime': "918824",
        'relationType': [1,2],
        'targetProfileID': 4994658,
    }
    try:
        api_response = api_instance.game_relationship_ignore(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_relationship_ignore: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
blocklevel | BlocklevelSchema | | 
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
relationType | RelationTypeSchema | | 
targetProfileID | TargetProfileIDSchema | | 


# BlocklevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RelationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TargetProfileIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_relationship_ignore.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_relationship_ignore.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_relationship_set_presence**
<a name="game_relationship_set_presence"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_relationship_set_presence(last_call_timepresence_id)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'presence_id': 3,
    }
    try:
        api_response = api_instance.game_relationship_set_presence(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_relationship_set_presence: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
presence_id | PresenceIdSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PresenceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_relationship_set_presence.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_relationship_set_presence.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_relationship_set_presence_property**
<a name="game_relationship_set_presence_property"></a>
> bool, date, datetime, dict, float, int, list, str, none_type game_relationship_set_presence_property(last_call_timepresence_property_def_idvalue)



### Example

* Api Key Authentication (sessionID):
* Api Key Authentication (connectID):
```python
import rlink_client
from rlink_client.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://aoe-api.reliclink.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rlink_client.Configuration(
    host = "https://aoe-api.reliclink.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionID
configuration.api_key['sessionID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionID'] = 'Bearer'

# Configure API key authorization: connectID
configuration.api_key['connectID'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['connectID'] = 'Bearer'
# Enter a context with an instance of the API client
with rlink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'callNum': 148,
        'lastCallTime': "918824",
        'presencePropertyDef_id': 1409823,
        'value': -2,
    }
    try:
        api_response = api_instance.game_relationship_set_presence_property(
            query_params=query_params,
        )
        pprint(api_response)
    except rlink_client.ApiException as e:
        print("Exception when calling DefaultApi->game_relationship_set_presence_property: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
callNum | CallNumSchema | | 
lastCallTime | LastCallTimeSchema | | 
presencePropertyDef_id | PresencePropertyDefIdSchema | | 
value | ValueSchema | | 


# CallNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LastCallTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PresencePropertyDefIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ValueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#game_relationship_set_presence_property.ApiResponseFor200) | Can be anything: string, number, array, object, etc., including &#x60;null&#x60;

#### game_relationship_set_presence_property.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[sessionID](../../../README.md#sessionID), [connectID](../../../README.md#connectID)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

