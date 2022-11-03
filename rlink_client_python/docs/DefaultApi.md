# swagger_client.DefaultApi

All URIs are relative to *https://aoe-api.reliclink.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**community_clan_find**](DefaultApi.md#community_clan_find) | **GET** /community/clan/find | 
[**community_find_advertisements**](DefaultApi.md#community_find_advertisements) | **GET** /community/advertisement/findAdvertisements | 
[**community_get_achievements**](DefaultApi.md#community_get_achievements) | **GET** /community/achievement/getAchievements | 
[**community_get_available_achievements**](DefaultApi.md#community_get_available_achievements) | **GET** /community/achievement/getAvailableAchievements | 
[**community_get_available_community_events**](DefaultApi.md#community_get_available_community_events) | **GET** /community/CommunityEvent/getAvailableCommunityEvents | 
[**community_get_available_leaderboards**](DefaultApi.md#community_get_available_leaderboards) | **GET** /community/leaderboard/getAvailableLeaderboards | 
[**community_get_avatar_stat_for_profile**](DefaultApi.md#community_get_avatar_stat_for_profile) | **GET** /community/leaderboard/GetAvatarStatForProfile | 
[**community_get_clan_info_full**](DefaultApi.md#community_get_clan_info_full) | **GET** /community/clan/getClanInfoFull | 
[**community_get_inventory_by_profile_ids**](DefaultApi.md#community_get_inventory_by_profile_ids) | **GET** /community/item/getInventoryByProfileIDs | 
[**community_get_leaderboard2**](DefaultApi.md#community_get_leaderboard2) | **GET** /community/leaderboard/getLeaderboard2 | 
[**community_get_personal_stat**](DefaultApi.md#community_get_personal_stat) | **GET** /community/leaderboard/GetPersonalStat | 
[**community_get_recent_match_history**](DefaultApi.md#community_get_recent_match_history) | **GET** /community/leaderboard/getRecentMatchHistory | 
[**community_news**](DefaultApi.md#community_news) | **GET** /community/news | 
[**community_proxy_steam_user_request**](DefaultApi.md#community_proxy_steam_user_request) | **GET** /community/external/proxysteamuserrequest | 
[**game_account_find_profiles**](DefaultApi.md#game_account_find_profiles) | **GET** /game/account/FindProfiles | 
[**game_account_find_profiles_by_platform_id**](DefaultApi.md#game_account_find_profiles_by_platform_id) | **GET** /game/account/FindProfilesByPlatformID | 
[**game_account_get_profile_name**](DefaultApi.md#game_account_get_profile_name) | **GET** /game/account/getProfileName | 
[**game_account_get_profile_property**](DefaultApi.md#game_account_get_profile_property) | **GET** /game/account/getProfileProperty | 
[**game_account_set_avatar_metadata**](DefaultApi.md#game_account_set_avatar_metadata) | **POST** /game/account/setAvatarMetadata | 
[**game_account_set_language**](DefaultApi.md#game_account_set_language) | **POST** /game/account/setLanguage | 
[**game_achievement_get_achievements**](DefaultApi.md#game_achievement_get_achievements) | **GET** /game/Achievement/getAchievements | 
[**game_achievement_get_available_achievements**](DefaultApi.md#game_achievement_get_available_achievements) | **GET** /game/Achievement/getAvailableAchievements | 
[**game_achievement_sync_stats**](DefaultApi.md#game_achievement_sync_stats) | **POST** /game/achievement/syncStats | 
[**game_advertisement_find_advertisements**](DefaultApi.md#game_advertisement_find_advertisements) | **GET** /game/advertisement/findAdvertisements | 
[**game_advertisement_find_observable_advertisements_get**](DefaultApi.md#game_advertisement_find_observable_advertisements_get) | **GET** /game/advertisement/findObservableAdvertisements | 
[**game_advertisement_find_observable_advertisements_post**](DefaultApi.md#game_advertisement_find_observable_advertisements_post) | **POST** /game/advertisement/findObservableAdvertisements | 
[**game_advertisement_get_advertisements**](DefaultApi.md#game_advertisement_get_advertisements) | **GET** /game/advertisement/getAdvertisements | 
[**game_advertisement_get_lan_advertisements**](DefaultApi.md#game_advertisement_get_lan_advertisements) | **GET** /game/advertisement/getLanAdvertisements | 
[**game_advertisement_host**](DefaultApi.md#game_advertisement_host) | **POST** /game/advertisement/host | 
[**game_advertisement_join**](DefaultApi.md#game_advertisement_join) | **POST** /game/advertisement/join | 
[**game_advertisement_leave**](DefaultApi.md#game_advertisement_leave) | **POST** /game/advertisement/leave | 
[**game_advertisement_start_observing**](DefaultApi.md#game_advertisement_start_observing) | **POST** /game/advertisement/startObserving | 
[**game_advertisement_stop_observing**](DefaultApi.md#game_advertisement_stop_observing) | **POST** /game/advertisement/stopObserving | 
[**game_advertisement_update**](DefaultApi.md#game_advertisement_update) | **POST** /game/advertisement/update | 
[**game_advertisement_update_platform_lobby_id**](DefaultApi.md#game_advertisement_update_platform_lobby_id) | **POST** /game/advertisement/updatePlatformLobbyID | 
[**game_advertisement_update_state**](DefaultApi.md#game_advertisement_update_state) | **POST** /game/advertisement/updateState | 
[**game_advertisement_update_tags**](DefaultApi.md#game_advertisement_update_tags) | **POST** /game/advertisement/updateTags | 
[**game_automatch2_get_automatch_map**](DefaultApi.md#game_automatch2_get_automatch_map) | **GET** /game/automatch2/getAutomatchMap | 
[**game_automatch2_polling**](DefaultApi.md#game_automatch2_polling) | **POST** /game/automatch2/polling | 
[**game_automatch2_stop_polling**](DefaultApi.md#game_automatch2_stop_polling) | **POST** /game/automatch2/stoppolling | 
[**game_automatch2_update_status**](DefaultApi.md#game_automatch2_update_status) | **POST** /game/automatch2/updateStatus | 
[**game_automatch_get_automatch_map**](DefaultApi.md#game_automatch_get_automatch_map) | **GET** /game/automatch/getAutomatchMap | 
[**game_challenge_get_challenge_progress**](DefaultApi.md#game_challenge_get_challenge_progress) | **GET** /game/Challenge/getChallengeProgress | 
[**game_challenge_get_challenge_progress_by_profile_id**](DefaultApi.md#game_challenge_get_challenge_progress_by_profile_id) | **GET** /game/Challenge/getChallengeProgressByProfileID | 
[**game_challenge_get_challenges**](DefaultApi.md#game_challenge_get_challenges) | **GET** /game/Challenge/getChallenges | 
[**game_challenge_update_progress_batched**](DefaultApi.md#game_challenge_update_progress_batched) | **POST** /game/challenge/updateProgressBatched | 
[**game_chat_delete_offline_message**](DefaultApi.md#game_chat_delete_offline_message) | **POST** /game/chat/deleteOfflineMessage | 
[**game_chat_get_chat_channels**](DefaultApi.md#game_chat_get_chat_channels) | **GET** /game/chat/getChatChannels | 
[**game_chat_get_offline_messages**](DefaultApi.md#game_chat_get_offline_messages) | **GET** /game/chat/getOfflineMessages | 
[**game_clan_apply**](DefaultApi.md#game_clan_apply) | **POST** /game/clan/apply | 
[**game_clan_create**](DefaultApi.md#game_clan_create) | **POST** /game/clan/create | 
[**game_clan_disband**](DefaultApi.md#game_clan_disband) | **POST** /game/clan/disband | 
[**game_clan_find**](DefaultApi.md#game_clan_find) | **GET** /game/clan/find | 
[**game_clan_get_clan**](DefaultApi.md#game_clan_get_clan) | **GET** /game/clan/getClan | 
[**game_clan_get_clan_info_full**](DefaultApi.md#game_clan_get_clan_info_full) | **GET** /game/clan/getClanInfoFull | 
[**game_clan_update**](DefaultApi.md#game_clan_update) | **POST** /game/clan/update | 
[**game_cloud_get_file_url_get**](DefaultApi.md#game_cloud_get_file_url_get) | **GET** /game/cloud/getFileURL | 
[**game_cloud_get_file_url_post**](DefaultApi.md#game_cloud_get_file_url_post) | **POST** /game/cloud/getFileURL | 
[**game_cloud_get_temp_credentials**](DefaultApi.md#game_cloud_get_temp_credentials) | **GET** /game/cloud/getTempCredentials | 
[**game_community_event_get_available_community_events**](DefaultApi.md#game_community_event_get_available_community_events) | **GET** /game/CommunityEvent/getAvailableCommunityEvents | 
[**game_community_event_get_event_challenge_progress**](DefaultApi.md#game_community_event_get_event_challenge_progress) | **GET** /game/CommunityEvent/getEventChallengeProgress | 
[**game_community_event_get_event_stats**](DefaultApi.md#game_community_event_get_event_stats) | **GET** /game/CommunityEvent/getEventStats | 
[**game_invitation_cancel_invitation**](DefaultApi.md#game_invitation_cancel_invitation) | **POST** /game/invitation/cancelInvitation | 
[**game_invitation_extend_invitation**](DefaultApi.md#game_invitation_extend_invitation) | **POST** /game/invitation/extendInvitation | 
[**game_item_detach_items**](DefaultApi.md#game_item_detach_items) | **POST** /game/item/detachItems | 
[**game_item_get_inventory_by_profile_ids**](DefaultApi.md#game_item_get_inventory_by_profile_ids) | **GET** /game/item/getInventoryByProfileIDs | 
[**game_item_get_item_bundle_items_json**](DefaultApi.md#game_item_get_item_bundle_items_json) | **GET** /game/item/getItemBundleItemsJson | 
[**game_item_get_item_definitions_json**](DefaultApi.md#game_item_get_item_definitions_json) | **GET** /game/item/getItemDefinitionsJson | 
[**game_item_get_item_loadouts**](DefaultApi.md#game_item_get_item_loadouts) | **GET** /game/item/getItemLoadouts | 
[**game_item_get_item_prices**](DefaultApi.md#game_item_get_item_prices) | **GET** /game/item/getItemPrices | 
[**game_item_get_level_rewards_table_json**](DefaultApi.md#game_item_get_level_rewards_table_json) | **GET** /game/item/getLevelRewardsTableJson | 
[**game_item_get_personalized_sale_items**](DefaultApi.md#game_item_get_personalized_sale_items) | **GET** /game/item/getPersonalizedSaleItems | 
[**game_item_get_scheduled_sale_and_items**](DefaultApi.md#game_item_get_scheduled_sale_and_items) | **GET** /game/item/getScheduledSaleAndItems | 
[**game_item_move_charges**](DefaultApi.md#game_item_move_charges) | **POST** /game/item/moveCharges | 
[**game_item_move_item**](DefaultApi.md#game_item_move_item) | **POST** /game/item/moveItem | 
[**game_item_open_item_pack**](DefaultApi.md#game_item_open_item_pack) | **POST** /game/item/openItemPack | 
[**game_item_sign_item**](DefaultApi.md#game_item_sign_item) | **POST** /game/item/signItems | 
[**game_item_update_item_attributes**](DefaultApi.md#game_item_update_item_attributes) | **POST** /game/item/updateItemAttributes | 
[**game_leaderboard_get_available_leaderboards**](DefaultApi.md#game_leaderboard_get_available_leaderboards) | **GET** /game/Leaderboard/getAvailableLeaderboards | 
[**game_leaderboard_get_leaderboard**](DefaultApi.md#game_leaderboard_get_leaderboard) | **GET** /game/Leaderboard/getLeaderBoard | 
[**game_leaderboard_get_party_stat**](DefaultApi.md#game_leaderboard_get_party_stat) | **GET** /game/Leaderboard/getPartyStat | 
[**game_leaderboard_get_personal_stat**](DefaultApi.md#game_leaderboard_get_personal_stat) | **GET** /game/Leaderboard/getPersonalStat | 
[**game_leaderboard_get_recent_match_history_get**](DefaultApi.md#game_leaderboard_get_recent_match_history_get) | **GET** /game/Leaderboard/getRecentMatchHistory | 
[**game_leaderboard_get_recent_match_history_post**](DefaultApi.md#game_leaderboard_get_recent_match_history_post) | **POST** /game/Leaderboard/getRecentMatchHistory | 
[**game_leaderboard_get_recent_match_single_player_history**](DefaultApi.md#game_leaderboard_get_recent_match_single_player_history) | **GET** /game/Leaderboard/getRecentMatchSinglePlayerHistory | 
[**game_leaderboard_get_stat_groups_by_profile_ids**](DefaultApi.md#game_leaderboard_get_stat_groups_by_profile_ids) | **GET** /game/Leaderboard/getStatGroupsByProfileIDs | 
[**game_leaderboard_get_stats_for_leaderboard_by_profile_name**](DefaultApi.md#game_leaderboard_get_stats_for_leaderboard_by_profile_name) | **GET** /game/Leaderboard/getStatsForLeaderboardByProfileName | 
[**game_leaderboard_set_avatar_stat_values**](DefaultApi.md#game_leaderboard_set_avatar_stat_values) | **POST** /game/leaderboard/setAvatarStatValues | 
[**game_login_logout**](DefaultApi.md#game_login_logout) | **POST** /game/login/logout | 
[**game_login_platform_login**](DefaultApi.md#game_login_platform_login) | **POST** /game/login/platformlogin | 
[**game_login_read_session**](DefaultApi.md#game_login_read_session) | **POST** /game/login/readSession | 
[**game_news_get_news**](DefaultApi.md#game_news_get_news) | **GET** /game/news/getNews | 
[**game_party_create_or_report_single_player**](DefaultApi.md#game_party_create_or_report_single_player) | **POST** /game/party/createOrReportSinglePlayer | 
[**game_party_finalize_replay_upload**](DefaultApi.md#game_party_finalize_replay_upload) | **POST** /game/party/finalizeReplayUpload | 
[**game_party_peer_add**](DefaultApi.md#game_party_peer_add) | **POST** /game/party/peerAdd | 
[**game_party_peer_update**](DefaultApi.md#game_party_peer_update) | **POST** /game/party/peerUpdate | 
[**game_party_report_match**](DefaultApi.md#game_party_report_match) | **POST** /game/party/reportMatch | 
[**game_party_send_match_chat**](DefaultApi.md#game_party_send_match_chat) | **POST** /game/party/sendMatchChat | 
[**game_playerreport_report_user**](DefaultApi.md#game_playerreport_report_user) | **POST** /game/playerreport/reportuser | 
[**game_relationship_clear_relationship**](DefaultApi.md#game_relationship_clear_relationship) | **POST** /game/relationship/clearRelationship | 
[**game_relationship_get_presence_data**](DefaultApi.md#game_relationship_get_presence_data) | **GET** /game/relationship/getPresenceData | 
[**game_relationship_get_relationships**](DefaultApi.md#game_relationship_get_relationships) | **GET** /game/relationship/getRelationships | 
[**game_relationship_ignore**](DefaultApi.md#game_relationship_ignore) | **POST** /game/relationship/ignore | 
[**game_relationship_set_presence**](DefaultApi.md#game_relationship_set_presence) | **POST** /game/relationship/setPresence | 
[**game_relationship_set_presence_property**](DefaultApi.md#game_relationship_set_presence_property) | **POST** /game/relationship/setPresenceProperty | 

# **community_clan_find**
> community_clan_find(join_policies, name, tags, start, count, title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
join_policies = 56 # int | 
name = 'name_example' # str | 
tags = 'tags_example' # str | 
start = 56 # int | 
count = 56 # int | 
title = 'title_example' # str |  (optional)

try:
    api_instance.community_clan_find(join_policies, name, tags, start, count, title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_clan_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **join_policies** | **int**|  | 
 **name** | **str**|  | 
 **tags** | **str**|  | 
 **start** | **int**|  | 
 **count** | **int**|  | 
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_find_advertisements**
> community_find_advertisements(title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)

try:
    api_instance.community_find_advertisements(title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_find_advertisements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_achievements**
> community_get_achievements(title=title, profileids=profileids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)
profileids = 56 # int |  (optional)

try:
    api_instance.community_get_achievements(title=title, profileids=profileids)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 
 **profileids** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_achievements**
> community_get_available_achievements(title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)

try:
    api_instance.community_get_available_achievements(title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_available_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_community_events**
> community_get_available_community_events(title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)

try:
    api_instance.community_get_available_community_events(title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_available_community_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_leaderboards**
> community_get_available_leaderboards(title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)

try:
    api_instance.community_get_available_leaderboards(title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_available_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_avatar_stat_for_profile**
> community_get_avatar_stat_for_profile(title=title, profile_names=profile_names)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)
profile_names = 'profile_names_example' # str |  (optional)

try:
    api_instance.community_get_avatar_stat_for_profile(title=title, profile_names=profile_names)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_avatar_stat_for_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 
 **profile_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_clan_info_full**
> community_get_clan_info_full(name, title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | 
title = 'title_example' # str |  (optional)

try:
    api_instance.community_get_clan_info_full(name, title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_clan_info_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_inventory_by_profile_ids**
> community_get_inventory_by_profile_ids(title=title, profileids=profileids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)
profileids = 56 # int |  (optional)

try:
    api_instance.community_get_inventory_by_profile_ids(title=title, profileids=profileids)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_inventory_by_profile_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 
 **profileids** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_leaderboard2**
> community_get_leaderboard2(start, count, title=title, leaderboard_id=leaderboard_id, sort_by=sort_by, platform=platform)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
start = 56 # int | 
count = 56 # int | 
title = 'title_example' # str |  (optional)
leaderboard_id = 56 # int |  (optional)
sort_by = 56 # int |  (optional)
platform = 'platform_example' # str |  (optional)

try:
    api_instance.community_get_leaderboard2(start, count, title=title, leaderboard_id=leaderboard_id, sort_by=sort_by, platform=platform)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_leaderboard2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | 
 **count** | **int**|  | 
 **title** | **str**|  | [optional] 
 **leaderboard_id** | **int**|  | [optional] 
 **sort_by** | **int**|  | [optional] 
 **platform** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_personal_stat**
> community_get_personal_stat(title=title, profile_ids=profile_ids, profile_names=profile_names, aliases=aliases)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)
profile_ids = 'profile_ids_example' # str |  (optional)
profile_names = 'profile_names_example' # str |  (optional)
aliases = 'aliases_example' # str |  (optional)

try:
    api_instance.community_get_personal_stat(title=title, profile_ids=profile_ids, profile_names=profile_names, aliases=aliases)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_personal_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 
 **profile_ids** | **str**|  | [optional] 
 **profile_names** | **str**|  | [optional] 
 **aliases** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_recent_match_history**
> community_get_recent_match_history(title=title, profile_ids=profile_ids, profile_names=profile_names)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)
profile_ids = 'profile_ids_example' # str |  (optional)
profile_names = 'profile_names_example' # str |  (optional)

try:
    api_instance.community_get_recent_match_history(title=title, profile_ids=profile_ids, profile_names=profile_names)
except ApiException as e:
    print("Exception when calling DefaultApi->community_get_recent_match_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 
 **profile_ids** | **str**|  | [optional] 
 **profile_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_news**
> community_news(title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
title = 'title_example' # str |  (optional)

try:
    api_instance.community_news(title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->community_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_proxy_steam_user_request**
> community_proxy_steam_user_request(request=request, title=title, profile_ids=profile_ids, profile_names=profile_names)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
request = 'request_example' # str |  (optional)
title = 'title_example' # str |  (optional)
profile_ids = 'profile_ids_example' # str |  (optional)
profile_names = 'profile_names_example' # str |  (optional)

try:
    api_instance.community_proxy_steam_user_request(request=request, title=title, profile_ids=profile_ids, profile_names=profile_names)
except ApiException as e:
    print("Exception when calling DefaultApi->community_proxy_steam_user_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **profile_ids** | **str**|  | [optional] 
 **profile_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_account_find_profiles**
> game_account_find_profiles(call_num, connect_id, last_call_time, name, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
name = 'name_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_account_find_profiles(call_num, connect_id, last_call_time, name, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_account_find_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **name** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_account_find_profiles_by_platform_id**
> game_account_find_profiles_by_platform_id(call_num, connect_id, last_call_time, session_id, platform_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
platform_i_ds = 56 # int | 

try:
    api_instance.game_account_find_profiles_by_platform_id(call_num, connect_id, last_call_time, session_id, platform_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_account_find_profiles_by_platform_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **platform_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_account_get_profile_name**
> game_account_get_profile_name(call_num, connect_id, last_call_time, profile_ids, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
profile_ids = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_account_get_profile_name(call_num, connect_id, last_call_time, profile_ids, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_account_get_profile_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **profile_ids** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_account_get_profile_property**
> game_account_get_profile_property(call_num, connect_id, last_call_time, session_id, profile_id, property_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profile_id = 56 # int | 
property_id = 'property_id_example' # str | 

try:
    api_instance.game_account_get_profile_property(call_num, connect_id, last_call_time, session_id, profile_id, property_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_account_get_profile_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profile_id** | **int**|  | 
 **property_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_account_set_avatar_metadata**
> game_account_set_avatar_metadata(call_num, connect_id, last_call_time, session_id, meta_data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
meta_data = NULL # object | 

try:
    api_instance.game_account_set_avatar_metadata(call_num, connect_id, last_call_time, session_id, meta_data)
except ApiException as e:
    print("Exception when calling DefaultApi->game_account_set_avatar_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **meta_data** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_account_set_language**
> game_account_set_language(call_num, connect_id, last_call_time, session_id, title=title, language=language)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
title = 'title_example' # str |  (optional)
language = 'language_example' # str |  (optional)

try:
    api_instance.game_account_set_language(call_num, connect_id, last_call_time, session_id, title=title, language=language)
except ApiException as e:
    print("Exception when calling DefaultApi->game_account_set_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **title** | **str**|  | [optional] 
 **language** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_achievement_get_achievements**
> game_achievement_get_achievements(call_num, connect_id, last_call_time, session_id, profile_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profile_i_ds = 56 # int | 

try:
    api_instance.game_achievement_get_achievements(call_num, connect_id, last_call_time, session_id, profile_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_achievement_get_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profile_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_achievement_get_available_achievements**
> game_achievement_get_available_achievements(call_num, connect_id, last_call_time, session_id, signature)



No authentication needed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
signature = 'signature_example' # str | 

try:
    api_instance.game_achievement_get_available_achievements(call_num, connect_id, last_call_time, session_id, signature)
except ApiException as e:
    print("Exception when calling DefaultApi->game_achievement_get_available_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **signature** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_achievement_sync_stats**
> game_achievement_sync_stats(call_num, connect_id, last_call_time, session_id, account_type, auth)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
account_type = 'account_type_example' # str | 
auth = 'auth_example' # str | 

try:
    api_instance.game_achievement_sync_stats(call_num, connect_id, last_call_time, session_id, account_type, auth)
except ApiException as e:
    print("Exception when calling DefaultApi->game_achievement_sync_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **account_type** | **str**|  | 
 **auth** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_advertisements**
> game_advertisement_find_advertisements(app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, profile_ids, race_ids, session_id, stat_group_ids, version_flags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
app_binary_checksum = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_checksum = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
match_type_id = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
profile_ids = 56 # int | 
race_ids = 56 # int | 
session_id = 'session_id_example' # str | 
stat_group_ids = 56 # int | 
version_flags = 56 # int | 

try:
    api_instance.game_advertisement_find_advertisements(app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, profile_ids, race_ids, session_id, stat_group_ids, version_flags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_find_advertisements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_binary_checksum** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_checksum** | **int**|  | 
 **last_call_time** | **str**|  | 
 **match_type_id** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **profile_ids** | **int**|  | 
 **race_ids** | **int**|  | 
 **session_id** | **str**|  | 
 **stat_group_ids** | **int**|  | 
 **version_flags** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_observable_advertisements_get**
> game_advertisement_find_observable_advertisements_get(call_num, connect_id, last_call_time, session_id, app_binary_checksum, count, data_checksum, desc, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_group_id, sort_order, start, version_flags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
app_binary_checksum = 56 # int | 
count = 56 # int | 
data_checksum = 56 # int | 
desc = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
observer_group_id = 56 # int | 
sort_order = 56 # int | 
start = 56 # int | 
version_flags = 56 # int | 

try:
    api_instance.game_advertisement_find_observable_advertisements_get(call_num, connect_id, last_call_time, session_id, app_binary_checksum, count, data_checksum, desc, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_group_id, sort_order, start, version_flags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_find_observable_advertisements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **app_binary_checksum** | **int**|  | 
 **count** | **int**|  | 
 **data_checksum** | **int**|  | 
 **desc** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **observer_group_id** | **int**|  | 
 **sort_order** | **int**|  | 
 **start** | **int**|  | 
 **version_flags** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_find_observable_advertisements_post**
> game_advertisement_find_observable_advertisements_post(call_num, connect_id, last_call_time, session_id, app_binary_checksum, count, data_checksum, desc, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_group_id, sort_order, start, version_flags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
app_binary_checksum = 56 # int | 
count = 56 # int | 
data_checksum = 56 # int | 
desc = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
observer_group_id = 56 # int | 
sort_order = 56 # int | 
start = 56 # int | 
version_flags = 56 # int | 

try:
    api_instance.game_advertisement_find_observable_advertisements_post(call_num, connect_id, last_call_time, session_id, app_binary_checksum, count, data_checksum, desc, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_group_id, sort_order, start, version_flags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_find_observable_advertisements_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **app_binary_checksum** | **int**|  | 
 **count** | **int**|  | 
 **data_checksum** | **int**|  | 
 **desc** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **observer_group_id** | **int**|  | 
 **sort_order** | **int**|  | 
 **start** | **int**|  | 
 **version_flags** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_get_advertisements**
> game_advertisement_get_advertisements(call_num, connect_id, last_call_time, match_ids, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
match_ids = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_advertisement_get_advertisements(call_num, connect_id, last_call_time, match_ids, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_get_advertisements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **match_ids** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_get_lan_advertisements**
> game_advertisement_get_lan_advertisements(app_binary_checksum, call_num, connect_id, data_checksum, lan_server_guids, last_call_time, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, session_id, version_flags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
app_binary_checksum = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_checksum = 56 # int | 
lan_server_guids = 'lan_server_guids_example' # str | 
last_call_time = 'last_call_time_example' # str | 
match_type_id = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
session_id = 'session_id_example' # str | 
version_flags = 56 # int | 

try:
    api_instance.game_advertisement_get_lan_advertisements(app_binary_checksum, call_num, connect_id, data_checksum, lan_server_guids, last_call_time, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, session_id, version_flags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_get_lan_advertisements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_binary_checksum** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_checksum** | **int**|  | 
 **lan_server_guids** | **str**|  | 
 **last_call_time** | **str**|  | 
 **match_type_id** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **session_id** | **str**|  | 
 **version_flags** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_host**
> game_advertisement_host(advertisementid, app_binary_checksum, automatch_poll_id, call_num, connect_id, data_checksum, description, hostid, is_observable, last_call_time, mapname, matchtype, maxplayers, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_delay, observer_password, options, party, password, passworded, race, relay_region, service_type, session_id, slotinfo, state, statgroup, team, version_flags, visible)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
app_binary_checksum = 56 # int | 
automatch_poll_id = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_checksum = 56 # int | 
description = 'description_example' # str | Lobby title
hostid = 56 # int | 
is_observable = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
mapname = 'mapname_example' # str | 
matchtype = 56 # int | 
maxplayers = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
observer_delay = 56 # int | 
observer_password = 'observer_password_example' # str | 
options = 'options_example' # str | 
party = 56 # int | 
password = 'password_example' # str | 
passworded = 56 # int | 
race = 56 # int | 
relay_region = 'relay_region_example' # str | 
service_type = 56 # int | 
session_id = 'session_id_example' # str | 
slotinfo = 'slotinfo_example' # str | zlib compressed
state = 56 # int | 
statgroup = 56 # int | 
team = 56 # int | 
version_flags = 56 # int | 
visible = 56 # int | 

try:
    api_instance.game_advertisement_host(advertisementid, app_binary_checksum, automatch_poll_id, call_num, connect_id, data_checksum, description, hostid, is_observable, last_call_time, mapname, matchtype, maxplayers, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_delay, observer_password, options, party, password, passworded, race, relay_region, service_type, session_id, slotinfo, state, statgroup, team, version_flags, visible)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **app_binary_checksum** | **int**|  | 
 **automatch_poll_id** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_checksum** | **int**|  | 
 **description** | **str**| Lobby title | 
 **hostid** | **int**|  | 
 **is_observable** | **int**|  | 
 **last_call_time** | **str**|  | 
 **mapname** | **str**|  | 
 **matchtype** | **int**|  | 
 **maxplayers** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **observer_delay** | **int**|  | 
 **observer_password** | **str**|  | 
 **options** | **str**|  | 
 **party** | **int**|  | 
 **password** | **str**|  | 
 **passworded** | **int**|  | 
 **race** | **int**|  | 
 **relay_region** | **str**|  | 
 **service_type** | **int**|  | 
 **session_id** | **str**|  | 
 **slotinfo** | **str**| zlib compressed | 
 **state** | **int**|  | 
 **statgroup** | **int**|  | 
 **team** | **int**|  | 
 **version_flags** | **int**|  | 
 **visible** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_join**
> game_advertisement_join(advertisementid, app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, mod_dll_checksum, mod_dll_file, mod_name, mod_version, party, password, race, session_id, statgroup, team, version_flags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
app_binary_checksum = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_checksum = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
party = 56 # int | 
password = 'password_example' # str | 
race = 56 # int | 
session_id = 'session_id_example' # str | 
statgroup = 56 # int | 
team = 56 # int | 
version_flags = 56 # int | 

try:
    api_instance.game_advertisement_join(advertisementid, app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, mod_dll_checksum, mod_dll_file, mod_name, mod_version, party, password, race, session_id, statgroup, team, version_flags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_join: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **app_binary_checksum** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_checksum** | **int**|  | 
 **last_call_time** | **str**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **party** | **int**|  | 
 **password** | **str**|  | 
 **race** | **int**|  | 
 **session_id** | **str**|  | 
 **statgroup** | **int**|  | 
 **team** | **int**|  | 
 **version_flags** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_leave**
> game_advertisement_leave(advertisementid, call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_advertisement_leave(advertisementid, call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_start_observing**
> game_advertisement_start_observing(advertisementid, app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, mod_dll_checksum, mod_dll_file, mod_name, mod_version, password, session_id, version_flags, with_party_session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
app_binary_checksum = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_checksum = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
password = 'password_example' # str | 
session_id = 'session_id_example' # str | 
version_flags = 56 # int | 
with_party_session_id = 56 # int | 

try:
    api_instance.game_advertisement_start_observing(advertisementid, app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, mod_dll_checksum, mod_dll_file, mod_name, mod_version, password, session_id, version_flags, with_party_session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_start_observing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **app_binary_checksum** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_checksum** | **int**|  | 
 **last_call_time** | **str**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **password** | **str**|  | 
 **session_id** | **str**|  | 
 **version_flags** | **int**|  | 
 **with_party_session_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_stop_observing**
> game_advertisement_stop_observing(advertisementid, call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_advertisement_stop_observing(advertisementid, call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_stop_observing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update**
> game_advertisement_update(advertisementid, app_binary_checksum, automatch_poll_id, call_num, connect_id, data_checksum, description, hostid, is_observable, last_call_time, mapname, matchtype, maxplayers, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_delay, observer_password, options, password, passworded, race, session_id, slotinfo, state, team, version_flags, visible)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
app_binary_checksum = 56 # int | 
automatch_poll_id = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_checksum = 56 # int | 
description = 'description_example' # str | Lobby title
hostid = 56 # int | 
is_observable = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
mapname = 'mapname_example' # str | 
matchtype = 56 # int | 
maxplayers = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
observer_delay = 56 # int | 
observer_password = 'observer_password_example' # str | 
options = 'options_example' # str | 
password = 'password_example' # str | 
passworded = 56 # int | 
race = 56 # int | 
session_id = 'session_id_example' # str | 
slotinfo = 'slotinfo_example' # str | zlib compressed
state = 56 # int | 
team = 56 # int | 
version_flags = 56 # int | 
visible = 56 # int | 

try:
    api_instance.game_advertisement_update(advertisementid, app_binary_checksum, automatch_poll_id, call_num, connect_id, data_checksum, description, hostid, is_observable, last_call_time, mapname, matchtype, maxplayers, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_delay, observer_password, options, password, passworded, race, session_id, slotinfo, state, team, version_flags, visible)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **app_binary_checksum** | **int**|  | 
 **automatch_poll_id** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_checksum** | **int**|  | 
 **description** | **str**| Lobby title | 
 **hostid** | **int**|  | 
 **is_observable** | **int**|  | 
 **last_call_time** | **str**|  | 
 **mapname** | **str**|  | 
 **matchtype** | **int**|  | 
 **maxplayers** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **observer_delay** | **int**|  | 
 **observer_password** | **str**|  | 
 **options** | **str**|  | 
 **password** | **str**|  | 
 **passworded** | **int**|  | 
 **race** | **int**|  | 
 **session_id** | **str**|  | 
 **slotinfo** | **str**| zlib compressed | 
 **state** | **int**|  | 
 **team** | **int**|  | 
 **version_flags** | **int**|  | 
 **visible** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_platform_lobby_id**
> game_advertisement_update_platform_lobby_id(call_num, connect_id, last_call_time, match_id, platformlobby_id, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
platformlobby_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_advertisement_update_platform_lobby_id(call_num, connect_id, last_call_time, match_id, platformlobby_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_update_platform_lobby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **platformlobby_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_state**
> game_advertisement_update_state(advertisementid, call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_advertisement_update_state(advertisementid, call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_update_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_advertisement_update_tags**
> game_advertisement_update_tags(advertisementid, call_num, connect_id, last_call_time, numeric_tag_names, numeric_tag_values, session_id, string_tag_names, string_tag_values)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
advertisementid = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
numeric_tag_names = 'numeric_tag_names_example' # str | 
numeric_tag_values = 56 # int | 
session_id = 'session_id_example' # str | 
string_tag_names = 'string_tag_names_example' # str | 
string_tag_values = 'string_tag_values_example' # str | 

try:
    api_instance.game_advertisement_update_tags(advertisementid, call_num, connect_id, last_call_time, numeric_tag_names, numeric_tag_values, session_id, string_tag_names, string_tag_values)
except ApiException as e:
    print("Exception when calling DefaultApi->game_advertisement_update_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisementid** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **numeric_tag_names** | **str**|  | 
 **numeric_tag_values** | **int**|  | 
 **session_id** | **str**|  | 
 **string_tag_names** | **str**|  | 
 **string_tag_values** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch2_get_automatch_map**
> game_automatch2_get_automatch_map(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_automatch2_get_automatch_map(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_automatch2_get_automatch_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch2_polling**
> game_automatch2_polling(app_bin_crc, call_num, connect_id, data_crc, faction_i_ds, last_call_time, match_types, mod_dll_checksum, mod_dll_file, mod_name, mod_version, options, party_session_id, race_info_key, race_info_profile_id, race_info_race_id, relay_ping_times, relay_region, relay_regions, session_id, version_flags, veto_map_key, veto_maps)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
app_bin_crc = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
data_crc = 56 # int | backwards appBinCRC?
faction_i_ds = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
match_types = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
options = 'options_example' # str | 
party_session_id = 56 # int | 
race_info_key = 56 # int | 
race_info_profile_id = 56 # int | 
race_info_race_id = 56 # int | 
relay_ping_times = 56 # int | 
relay_region = 'relay_region_example' # str | 
relay_regions = 'relay_regions_example' # str | 
session_id = 'session_id_example' # str | 
version_flags = 56 # int | 
veto_map_key = 56 # int | 
veto_maps = 'veto_maps_example' # str | 

try:
    api_instance.game_automatch2_polling(app_bin_crc, call_num, connect_id, data_crc, faction_i_ds, last_call_time, match_types, mod_dll_checksum, mod_dll_file, mod_name, mod_version, options, party_session_id, race_info_key, race_info_profile_id, race_info_race_id, relay_ping_times, relay_region, relay_regions, session_id, version_flags, veto_map_key, veto_maps)
except ApiException as e:
    print("Exception when calling DefaultApi->game_automatch2_polling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_bin_crc** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **data_crc** | **int**| backwards appBinCRC? | 
 **faction_i_ds** | **int**|  | 
 **last_call_time** | **str**|  | 
 **match_types** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **options** | **str**|  | 
 **party_session_id** | **int**|  | 
 **race_info_key** | **int**|  | 
 **race_info_profile_id** | **int**|  | 
 **race_info_race_id** | **int**|  | 
 **relay_ping_times** | **int**|  | 
 **relay_region** | **str**|  | 
 **relay_regions** | **str**|  | 
 **session_id** | **str**|  | 
 **version_flags** | **int**|  | 
 **veto_map_key** | **int**|  | 
 **veto_maps** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch2_stop_polling**
> game_automatch2_stop_polling(call_num, commit, connect_id, last_call_time, owner_profile_id, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
commit = 56 # int | 
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
owner_profile_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_automatch2_stop_polling(call_num, commit, connect_id, last_call_time, owner_profile_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_automatch2_stop_polling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **commit** | **int**|  | 
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **owner_profile_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch2_update_status**
> game_automatch2_update_status(call_num, connect_id, last_call_time, match_id, result, result_code, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
result = 56 # int | 
result_code = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_automatch2_update_status(call_num, connect_id, last_call_time, match_id, result, result_code, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_automatch2_update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **result** | **int**|  | 
 **result_code** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_automatch_get_automatch_map**
> game_automatch_get_automatch_map(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_automatch_get_automatch_map(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_automatch_get_automatch_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_challenge_get_challenge_progress**
> game_challenge_get_challenge_progress(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_challenge_get_challenge_progress(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_challenge_get_challenge_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_challenge_get_challenge_progress_by_profile_id**
> game_challenge_get_challenge_progress_by_profile_id(call_num, connect_id, last_call_time, profile_id, session_id)



TODO: Request not available in Wiki, this is guessed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
profile_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_challenge_get_challenge_progress_by_profile_id(call_num, connect_id, last_call_time, profile_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_challenge_get_challenge_progress_by_profile_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **profile_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_challenge_get_challenges**
> game_challenge_get_challenges(call_num, connect_id, last_call_time, session_id, signature)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
signature = 'signature_example' # str | 

try:
    api_instance.game_challenge_get_challenges(call_num, connect_id, last_call_time, session_id, signature)
except ApiException as e:
    print("Exception when calling DefaultApi->game_challenge_get_challenges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **signature** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_challenge_update_progress_batched**
> game_challenge_update_progress_batched(call_num, connect_id, last_call_time, progress_i_ds, session_id, update_amounts)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
progress_i_ds = 56 # int | 
session_id = 'session_id_example' # str | 
update_amounts = 56 # int | 

try:
    api_instance.game_challenge_update_progress_batched(call_num, connect_id, last_call_time, progress_i_ds, session_id, update_amounts)
except ApiException as e:
    print("Exception when calling DefaultApi->game_challenge_update_progress_batched: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **progress_i_ds** | **int**|  | 
 **session_id** | **str**|  | 
 **update_amounts** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_chat_delete_offline_message**
> game_chat_delete_offline_message(call_num, connect_id, last_call_time, message_id, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
message_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_chat_delete_offline_message(call_num, connect_id, last_call_time, message_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_chat_delete_offline_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **message_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_chat_get_chat_channels**
> game_chat_get_chat_channels(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_chat_get_chat_channels(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_chat_get_chat_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_chat_get_offline_messages**
> game_chat_get_offline_messages(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_chat_get_offline_messages(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_chat_get_offline_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_apply**
> game_clan_apply(call_num, clan_list_name, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
clan_list_name = 'clan_list_name_example' # str | 
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_clan_apply(call_num, clan_list_name, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_apply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **clan_list_name** | **str**|  | 
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_create**
> game_clan_create(call_num, chat, connect_id, cost, demote, description, disband, edit_info, edit_permission, full_name, icon, invite, item_price_id, join_policy, last_call_time, loc_string_id, message_of_the_day, metadata, name, paymentitem, permission_name, promote, rank, remove, session_id, tags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
chat = 'chat_example' # str | 
connect_id = 'connect_id_example' # str | 
cost = 56 # int | 
demote = 'demote_example' # str | 
description = 'description_example' # str | Lobby title
disband = 'disband_example' # str | 
edit_info = 'edit_info_example' # str | 
edit_permission = 'edit_permission_example' # str | 
full_name = 'full_name_example' # str | 
icon = 'icon_example' # str | 
invite = 'invite_example' # str | 
item_price_id = 56 # int | 
join_policy = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
loc_string_id = 56 # int | 
message_of_the_day = 'message_of_the_day_example' # str | 
metadata = NULL # object | 
name = 'name_example' # str | 
paymentitem = 56 # int | 
permission_name = 'permission_name_example' # str | 
promote = 'promote_example' # str | 
rank = 'rank_example' # str | 
remove = 'remove_example' # str | 
session_id = 'session_id_example' # str | 
tags = 'tags_example' # str | 

try:
    api_instance.game_clan_create(call_num, chat, connect_id, cost, demote, description, disband, edit_info, edit_permission, full_name, icon, invite, item_price_id, join_policy, last_call_time, loc_string_id, message_of_the_day, metadata, name, paymentitem, permission_name, promote, rank, remove, session_id, tags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **chat** | **str**|  | 
 **connect_id** | **str**|  | 
 **cost** | **int**|  | 
 **demote** | **str**|  | 
 **description** | **str**| Lobby title | 
 **disband** | **str**|  | 
 **edit_info** | **str**|  | 
 **edit_permission** | **str**|  | 
 **full_name** | **str**|  | 
 **icon** | **str**|  | 
 **invite** | **str**|  | 
 **item_price_id** | **int**|  | 
 **join_policy** | **int**|  | 
 **last_call_time** | **str**|  | 
 **loc_string_id** | **int**|  | 
 **message_of_the_day** | **str**|  | 
 **metadata** | [**object**](.md)|  | 
 **name** | **str**|  | 
 **paymentitem** | **int**|  | 
 **permission_name** | **str**|  | 
 **promote** | **str**|  | 
 **rank** | **str**|  | 
 **remove** | **str**|  | 
 **session_id** | **str**|  | 
 **tags** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_disband**
> game_clan_disband(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_clan_disband(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_disband: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_find**
> game_clan_find(call_num, connect_id, count, join_policies, last_call_time, name, session_id, start, tags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
count = 56 # int | 
join_policies = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
name = 'name_example' # str | 
session_id = 'session_id_example' # str | 
start = 56 # int | 
tags = 'tags_example' # str | 

try:
    api_instance.game_clan_find(call_num, connect_id, count, join_policies, last_call_time, name, session_id, start, tags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **count** | **int**|  | 
 **join_policies** | **int**|  | 
 **last_call_time** | **str**|  | 
 **name** | **str**|  | 
 **session_id** | **str**|  | 
 **start** | **int**|  | 
 **tags** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_get_clan**
> game_clan_get_clan(call_num, connect_id, last_call_time, names, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
names = 'names_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_clan_get_clan(call_num, connect_id, last_call_time, names, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_get_clan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **names** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_get_clan_info_full**
> game_clan_get_clan_info_full(call_num, connect_id, last_call_time, name, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
name = 'name_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_clan_get_clan_info_full(call_num, connect_id, last_call_time, name, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_get_clan_info_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **name** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_clan_update**
> game_clan_update(call_num, clan_list_id, connect_id, description, icon, join_policy, last_call_time, message_of_the_day, metadata, session_id, tags)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
clan_list_id = 56 # int | 
connect_id = 'connect_id_example' # str | 
description = 'description_example' # str | Lobby title
icon = 'icon_example' # str | 
join_policy = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
message_of_the_day = 'message_of_the_day_example' # str | 
metadata = NULL # object | 
session_id = 'session_id_example' # str | 
tags = 'tags_example' # str | 

try:
    api_instance.game_clan_update(call_num, clan_list_id, connect_id, description, icon, join_policy, last_call_time, message_of_the_day, metadata, session_id, tags)
except ApiException as e:
    print("Exception when calling DefaultApi->game_clan_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **clan_list_id** | **int**|  | 
 **connect_id** | **str**|  | 
 **description** | **str**| Lobby title | 
 **icon** | **str**|  | 
 **join_policy** | **int**|  | 
 **last_call_time** | **str**|  | 
 **message_of_the_day** | **str**|  | 
 **metadata** | [**object**](.md)|  | 
 **session_id** | **str**|  | 
 **tags** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cloud_get_file_url_get**
> game_cloud_get_file_url_get(call_num, connect_id, last_call_time, names, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
names = 'names_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_cloud_get_file_url_get(call_num, connect_id, last_call_time, names, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_cloud_get_file_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **names** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cloud_get_file_url_post**
> game_cloud_get_file_url_post(call_num, connect_id, last_call_time, names, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
names = 'names_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_cloud_get_file_url_post(call_num, connect_id, last_call_time, names, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_cloud_get_file_url_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **names** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_cloud_get_temp_credentials**
> game_cloud_get_temp_credentials(call_num, connect_id, last_call_time, session_id, key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
key = 'key_example' # str | 

try:
    api_instance.game_cloud_get_temp_credentials(call_num, connect_id, last_call_time, session_id, key)
except ApiException as e:
    print("Exception when calling DefaultApi->game_cloud_get_temp_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_community_event_get_available_community_events**
> game_community_event_get_available_community_events(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_community_event_get_available_community_events(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_community_event_get_available_community_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_community_event_get_event_challenge_progress**
> game_community_event_get_event_challenge_progress(call_num, connect_id, event_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
event_id = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_community_event_get_event_challenge_progress(call_num, connect_id, event_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_community_event_get_event_challenge_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **event_id** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_community_event_get_event_stats**
> game_community_event_get_event_stats(call_num, connect_id, event_id, group_type, last_call_time, member_id, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
event_id = 56 # int | 
group_type = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
member_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_community_event_get_event_stats(call_num, connect_id, event_id, group_type, last_call_time, member_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_community_event_get_event_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **event_id** | **int**|  | 
 **group_type** | **int**|  | 
 **last_call_time** | **str**|  | 
 **member_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_invitation_cancel_invitation**
> game_invitation_cancel_invitation(call_num, connect_id, gatheringid, inviteeid, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
gatheringid = 56 # int | 
inviteeid = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_invitation_cancel_invitation(call_num, connect_id, gatheringid, inviteeid, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_invitation_cancel_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **gatheringid** | **int**|  | 
 **inviteeid** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_invitation_extend_invitation**
> game_invitation_extend_invitation(call_num, connect_id, gatheringid, gatheringpassword, inviteeid, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
gatheringid = 56 # int | 
gatheringpassword = 'gatheringpassword_example' # str | 
inviteeid = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_invitation_extend_invitation(call_num, connect_id, gatheringid, gatheringpassword, inviteeid, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_invitation_extend_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **gatheringid** | **int**|  | 
 **gatheringpassword** | **str**|  | 
 **inviteeid** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_detach_items**
> game_item_detach_items(call_num, connect_id, item_charges, item_i_ds, item_locations, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
item_charges = 56 # int | 
item_i_ds = 56 # int | 
item_locations = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_item_detach_items(call_num, connect_id, item_charges, item_i_ds, item_locations, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_detach_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **item_charges** | **int**|  | 
 **item_i_ds** | **int**|  | 
 **item_locations** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_inventory_by_profile_ids**
> game_item_get_inventory_by_profile_ids(call_num, connect_id, last_call_time, session_id, profile_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profile_i_ds = 56 # int | 

try:
    api_instance.game_item_get_inventory_by_profile_ids(call_num, connect_id, last_call_time, session_id, profile_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_inventory_by_profile_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profile_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_item_bundle_items_json**
> game_item_get_item_bundle_items_json(call_num, connect_id, last_call_time, session_id, signature)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
signature = 'signature_example' # str | 

try:
    api_instance.game_item_get_item_bundle_items_json(call_num, connect_id, last_call_time, session_id, signature)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_item_bundle_items_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **signature** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_item_definitions_json**
> game_item_get_item_definitions_json(call_num, connect_id, last_call_time, session_id, signature)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
signature = 'signature_example' # str | 

try:
    api_instance.game_item_get_item_definitions_json(call_num, connect_id, last_call_time, session_id, signature)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_item_definitions_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **signature** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_item_loadouts**
> game_item_get_item_loadouts(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_item_get_item_loadouts(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_item_loadouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_item_prices**
> game_item_get_item_prices(account_type, call_num, connect_id, last_call_time, session_id, country, currency, sale_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
account_type = 'account_type_example' # str | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
country = 'country_example' # str | 
currency = 'currency_example' # str | 
sale_version = 56 # int | 

try:
    api_instance.game_item_get_item_prices(account_type, call_num, connect_id, last_call_time, session_id, country, currency, sale_version)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_item_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **country** | **str**|  | 
 **currency** | **str**|  | 
 **sale_version** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_level_rewards_table_json**
> game_item_get_level_rewards_table_json(call_num, connect_id, last_call_time, session_id, signature)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
signature = 'signature_example' # str | 

try:
    api_instance.game_item_get_level_rewards_table_json(call_num, connect_id, last_call_time, session_id, signature)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_level_rewards_table_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **signature** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_personalized_sale_items**
> game_item_get_personalized_sale_items(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_item_get_personalized_sale_items(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_personalized_sale_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_get_scheduled_sale_and_items**
> game_item_get_scheduled_sale_and_items(call_num, connect_id, last_call_time, session_id, sale_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
sale_type = 56 # int | 

try:
    api_instance.game_item_get_scheduled_sale_and_items(call_num, connect_id, last_call_time, session_id, sale_type)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_get_scheduled_sale_and_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **sale_type** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_move_charges**
> game_item_move_charges(call_num, charges, connect_id, deletes, from_item_i_ds, last_call_time, session_id, to_item_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
charges = 56 # int | 
connect_id = 'connect_id_example' # str | 
deletes = 56 # int | 
from_item_i_ds = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
to_item_i_ds = 56 # int | 

try:
    api_instance.game_item_move_charges(call_num, charges, connect_id, deletes, from_item_i_ds, last_call_time, session_id, to_item_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_move_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **charges** | **int**|  | 
 **connect_id** | **str**|  | 
 **deletes** | **int**|  | 
 **from_item_i_ds** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **to_item_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_move_item**
> game_item_move_item(call_num, connect_id, item_i_ds, item_location_i_ds, last_call_time, pos_i_ds, session_id, slot_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
item_i_ds = 56 # int | 
item_location_i_ds = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
pos_i_ds = 56 # int | 
session_id = 'session_id_example' # str | 
slot_i_ds = 56 # int | 

try:
    api_instance.game_item_move_item(call_num, connect_id, item_i_ds, item_location_i_ds, last_call_time, pos_i_ds, session_id, slot_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_move_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **item_i_ds** | **int**|  | 
 **item_location_i_ds** | **int**|  | 
 **last_call_time** | **str**|  | 
 **pos_i_ds** | **int**|  | 
 **session_id** | **str**|  | 
 **slot_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_open_item_pack**
> game_item_open_item_pack(call_num, choices, connect_id, item_instance_id, item_location_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
choices = 56 # int | 
connect_id = 'connect_id_example' # str | 
item_instance_id = 56 # int | 
item_location_id = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_item_open_item_pack(call_num, choices, connect_id, item_instance_id, item_location_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_open_item_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **choices** | **int**|  | 
 **connect_id** | **str**|  | 
 **item_instance_id** | **int**|  | 
 **item_location_id** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_sign_item**
> game_item_sign_item(call_num, connect_id, crc, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
crc = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_item_sign_item(call_num, connect_id, crc, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_sign_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **crc** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_item_update_item_attributes**
> game_item_update_item_attributes(attribute_keys, attribute_values, call_num, connect_id, item_instance_ids, last_call_time, session_id, xp_gains)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
attribute_keys = 'attribute_keys_example' # str | 
attribute_values = 'attribute_values_example' # str | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
item_instance_ids = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
xp_gains = 56 # int | 

try:
    api_instance.game_item_update_item_attributes(attribute_keys, attribute_values, call_num, connect_id, item_instance_ids, last_call_time, session_id, xp_gains)
except ApiException as e:
    print("Exception when calling DefaultApi->game_item_update_item_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_keys** | **str**|  | 
 **attribute_values** | **str**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **item_instance_ids** | **int**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **xp_gains** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_available_leaderboards**
> game_leaderboard_get_available_leaderboards(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_leaderboard_get_available_leaderboards(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_available_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_leaderboard**
> game_leaderboard_get_leaderboard(call_num, connect_id, last_call_time, session_id, start, count, leaderboard_id=leaderboard_id, sort_by=sort_by)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
start = 56 # int | 
count = 56 # int | 
leaderboard_id = 56 # int |  (optional)
sort_by = 56 # int |  (optional)

try:
    api_instance.game_leaderboard_get_leaderboard(call_num, connect_id, last_call_time, session_id, start, count, leaderboard_id=leaderboard_id, sort_by=sort_by)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **start** | **int**|  | 
 **count** | **int**|  | 
 **leaderboard_id** | **int**|  | [optional] 
 **sort_by** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_party_stat**
> game_leaderboard_get_party_stat(call_num, connect_id, last_call_time, session_id, statsids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
statsids = 56 # int | 

try:
    api_instance.game_leaderboard_get_party_stat(call_num, connect_id, last_call_time, session_id, statsids)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_party_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **statsids** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_personal_stat**
> game_leaderboard_get_personal_stat(call_num, connect_id, last_call_time, session_id)



TODO: No request documented in Wiki, guessed parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_leaderboard_get_personal_stat(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_personal_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_recent_match_history_get**
> game_leaderboard_get_recent_match_history_get(call_num, connect_id, last_call_time, session_id, profile_ids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profile_ids = 56 # int | 

try:
    api_instance.game_leaderboard_get_recent_match_history_get(call_num, connect_id, last_call_time, session_id, profile_ids)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_recent_match_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profile_ids** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_recent_match_history_post**
> game_leaderboard_get_recent_match_history_post(call_num, connect_id, last_call_time, session_id, profile_ids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profile_ids = 56 # int | 

try:
    api_instance.game_leaderboard_get_recent_match_history_post(call_num, connect_id, last_call_time, session_id, profile_ids)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_recent_match_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profile_ids** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_recent_match_single_player_history**
> game_leaderboard_get_recent_match_single_player_history(call_num, connect_id, last_call_time, session_id, profile_ids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profile_ids = 56 # int | 

try:
    api_instance.game_leaderboard_get_recent_match_single_player_history(call_num, connect_id, last_call_time, session_id, profile_ids)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_recent_match_single_player_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profile_ids** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_stat_groups_by_profile_ids**
> game_leaderboard_get_stat_groups_by_profile_ids(call_num, connect_id, last_call_time, session_id, profileids)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profileids = 56 # int | 

try:
    api_instance.game_leaderboard_get_stat_groups_by_profile_ids(call_num, connect_id, last_call_time, session_id, profileids)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_stat_groups_by_profile_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profileids** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_get_stats_for_leaderboard_by_profile_name**
> game_leaderboard_get_stats_for_leaderboard_by_profile_name(call_num, connect_id, last_call_time, session_id, profileids, leaderboard_id=leaderboard_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
profileids = 56 # int | 
leaderboard_id = 56 # int |  (optional)

try:
    api_instance.game_leaderboard_get_stats_for_leaderboard_by_profile_name(call_num, connect_id, last_call_time, session_id, profileids, leaderboard_id=leaderboard_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_get_stats_for_leaderboard_by_profile_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **profileids** | **int**|  | 
 **leaderboard_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_leaderboard_set_avatar_stat_values**
> game_leaderboard_set_avatar_stat_values(avatar_stat_ids, call_num, connect_id, last_call_time, session_id, update_types, values)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
avatar_stat_ids = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 
update_types = 56 # int | 
values = 56 # int | 

try:
    api_instance.game_leaderboard_set_avatar_stat_values(avatar_stat_ids, call_num, connect_id, last_call_time, session_id, update_types, values)
except ApiException as e:
    print("Exception when calling DefaultApi->game_leaderboard_set_avatar_stat_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_stat_ids** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 
 **update_types** | **int**|  | 
 **values** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_login_logout**
> game_login_logout(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_login_logout(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_login_logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_login_platform_login**
> game_login_platform_login(account_type, active_match_id, alias, app_id, auth, call_num, client_lib_version, connect_id, country, installation_type, last_call_time, mac_address, major_version, minor_version, platform_user_id, start_game_token, sync_hash, timeout_override, language=language, store_license_token=store_license_token, title=title)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
account_type = 'account_type_example' # str | 
active_match_id = -1 # int |  (default to -1)
alias = 'alias_example' # str | 
app_id = 56 # int | 
auth = 'auth_example' # str | 
call_num = 0 # int |  (default to 0)
client_lib_version = 56 # int | 
connect_id = 'connect_id_example' # str | 
country = 'country_example' # str | 
installation_type = 'installation_type_example' # str | 
last_call_time = 'last_call_time_example' # str | 
mac_address = 'mac_address_example' # str | 
major_version = 'major_version_example' # str | 
minor_version = 56 # int | 
platform_user_id = 56 # int | 
start_game_token = 'start_game_token_example' # str | 
sync_hash = 56 # int | 
timeout_override = 0 # int |  (default to 0)
language = 'language_example' # str |  (optional)
store_license_token = 'store_license_token_example' # str |  (optional)
title = 'title_example' # str |  (optional)

try:
    api_instance.game_login_platform_login(account_type, active_match_id, alias, app_id, auth, call_num, client_lib_version, connect_id, country, installation_type, last_call_time, mac_address, major_version, minor_version, platform_user_id, start_game_token, sync_hash, timeout_override, language=language, store_license_token=store_license_token, title=title)
except ApiException as e:
    print("Exception when calling DefaultApi->game_login_platform_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**|  | 
 **active_match_id** | **int**|  | [default to -1]
 **alias** | **str**|  | 
 **app_id** | **int**|  | 
 **auth** | **str**|  | 
 **call_num** | **int**|  | [default to 0]
 **client_lib_version** | **int**|  | 
 **connect_id** | **str**|  | 
 **country** | **str**|  | 
 **installation_type** | **str**|  | 
 **last_call_time** | **str**|  | 
 **mac_address** | **str**|  | 
 **major_version** | **str**|  | 
 **minor_version** | **int**|  | 
 **platform_user_id** | **int**|  | 
 **start_game_token** | **str**|  | 
 **sync_hash** | **int**|  | 
 **timeout_override** | **int**|  | [default to 0]
 **language** | **str**|  | [optional] 
 **store_license_token** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_login_read_session**
> game_login_read_session(ack, poll_num, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ack = 56 # int | 
poll_num = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_login_read_session(ack, poll_num, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_login_read_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ack** | **int**|  | 
 **poll_num** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_news_get_news**
> game_news_get_news(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_news_get_news(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_news_get_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_create_or_report_single_player**
> game_party_create_or_report_single_player(appbincrc, call_num, connect_id, counters_zip, create_match_key, datacrc, is_complete, item_updates, last_call_time, mapname, match_key, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, options, race_ids, results, session_id, slot_info, team_i_ds, version_flags, xp_gained)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
appbincrc = 56 # int | 
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
counters_zip = 'counters_zip_example' # str | zlib-compressed
create_match_key = 1 # int |  (default to 1)
datacrc = 56 # int | 
is_complete = 0 # int |  (default to 0)
item_updates = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
mapname = 'mapname_example' # str | 
match_key = 'match_key_example' # str | 
match_type_id = 56 # int | 
mod_dll_checksum = 56 # int | 
mod_dll_file = 'mod_dll_file_example' # str | 
mod_name = 'mod_name_example' # str | 
mod_version = 'mod_version_example' # str | 
options = 'options_example' # str | 
race_ids = 56 # int | 
results = 56 # int | 
session_id = 'session_id_example' # str | 
slot_info = 'slot_info_example' # str | zlib-compressed
team_i_ds = 56 # int | 
version_flags = 56 # int | 
xp_gained = 56 # int | 

try:
    api_instance.game_party_create_or_report_single_player(appbincrc, call_num, connect_id, counters_zip, create_match_key, datacrc, is_complete, item_updates, last_call_time, mapname, match_key, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, options, race_ids, results, session_id, slot_info, team_i_ds, version_flags, xp_gained)
except ApiException as e:
    print("Exception when calling DefaultApi->game_party_create_or_report_single_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appbincrc** | **int**|  | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **counters_zip** | **str**| zlib-compressed | 
 **create_match_key** | **int**|  | [default to 1]
 **datacrc** | **int**|  | 
 **is_complete** | **int**|  | [default to 0]
 **item_updates** | **int**|  | 
 **last_call_time** | **str**|  | 
 **mapname** | **str**|  | 
 **match_key** | **str**|  | 
 **match_type_id** | **int**|  | 
 **mod_dll_checksum** | **int**|  | 
 **mod_dll_file** | **str**|  | 
 **mod_name** | **str**|  | 
 **mod_version** | **str**|  | 
 **options** | **str**|  | 
 **race_ids** | **int**|  | 
 **results** | **int**|  | 
 **session_id** | **str**|  | 
 **slot_info** | **str**| zlib-compressed | 
 **team_i_ds** | **int**|  | 
 **version_flags** | **int**|  | 
 **xp_gained** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_finalize_replay_upload**
> game_party_finalize_replay_upload(call_num, connect_id, error_string, finalize_result, is_single_player, last_call_time, match_id, session_id, size, url)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
error_string = 'error_string_example' # str | 
finalize_result = 1 # int |  (default to 1)
is_single_player = 0 # int |  (default to 0)
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
session_id = 'session_id_example' # str | 
size = 56 # int | 
url = 'url_example' # str | 

try:
    api_instance.game_party_finalize_replay_upload(call_num, connect_id, error_string, finalize_result, is_single_player, last_call_time, match_id, session_id, size, url)
except ApiException as e:
    print("Exception when calling DefaultApi->game_party_finalize_replay_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **error_string** | **str**|  | 
 **finalize_result** | **int**|  | [default to 1]
 **is_single_player** | **int**|  | [default to 0]
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **session_id** | **str**|  | 
 **size** | **int**|  | 
 **url** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_peer_add**
> game_party_peer_add(call_num, connect_id, last_call_time, match_id, profile_ids, race_ids, session_id, stat_group_ids, team_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
profile_ids = 56 # int | 
race_ids = 56 # int | 
session_id = 'session_id_example' # str | 
stat_group_ids = 56 # int | 
team_i_ds = 56 # int | 

try:
    api_instance.game_party_peer_add(call_num, connect_id, last_call_time, match_id, profile_ids, race_ids, session_id, stat_group_ids, team_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_party_peer_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **profile_ids** | **int**|  | 
 **race_ids** | **int**|  | 
 **session_id** | **str**|  | 
 **stat_group_ids** | **int**|  | 
 **team_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_peer_update**
> game_party_peer_update(call_num, connect_id, is_non_participants, last_call_time, match_id, profile_ids, race_ids, session_id, team_i_ds)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
is_non_participants = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
profile_ids = 56 # int | 
race_ids = 56 # int | 
session_id = 'session_id_example' # str | 
team_i_ds = 56 # int | 

try:
    api_instance.game_party_peer_update(call_num, connect_id, is_non_participants, last_call_time, match_id, profile_ids, race_ids, session_id, team_i_ds)
except ApiException as e:
    print("Exception when calling DefaultApi->game_party_peer_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **is_non_participants** | **int**|  | 
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **profile_ids** | **int**|  | 
 **race_ids** | **int**|  | 
 **session_id** | **str**|  | 
 **team_i_ds** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_report_match**
> game_party_report_match(call_num, check_sums, connect_id, counters_zip, item_updates, last_call_time, match_id, profile_ids, race_ids, results, session_id, simplayer_i_ds, team_i_ds, xp_gained)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
check_sums = 56 # int | 
connect_id = 'connect_id_example' # str | 
counters_zip = 'counters_zip_example' # str | zlib-compressed
item_updates = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
profile_ids = 56 # int | 
race_ids = 56 # int | 
results = 56 # int | 
session_id = 'session_id_example' # str | 
simplayer_i_ds = 56 # int | 
team_i_ds = 56 # int | 
xp_gained = 56 # int | 

try:
    api_instance.game_party_report_match(call_num, check_sums, connect_id, counters_zip, item_updates, last_call_time, match_id, profile_ids, race_ids, results, session_id, simplayer_i_ds, team_i_ds, xp_gained)
except ApiException as e:
    print("Exception when calling DefaultApi->game_party_report_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **check_sums** | **int**|  | 
 **connect_id** | **str**|  | 
 **counters_zip** | **str**| zlib-compressed | 
 **item_updates** | **int**|  | 
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **profile_ids** | **int**|  | 
 **race_ids** | **int**|  | 
 **results** | **int**|  | 
 **session_id** | **str**|  | 
 **simplayer_i_ds** | **int**|  | 
 **team_i_ds** | **int**|  | 
 **xp_gained** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_party_send_match_chat**
> game_party_send_match_chat(broadcast, call_num, connect_id, from_profile_id, last_call_time, match_id, message, message_type_id, session_id, to_profile_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
broadcast = 56 # int | aoe4: 1, aoe2de: 0
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
from_profile_id = 56 # int | 
last_call_time = 'last_call_time_example' # str | 
match_id = 56 # int | 
message = 'message_example' # str | 
message_type_id = 56 # int | 
session_id = 'session_id_example' # str | 
to_profile_id = 56 # int | 

try:
    api_instance.game_party_send_match_chat(broadcast, call_num, connect_id, from_profile_id, last_call_time, match_id, message, message_type_id, session_id, to_profile_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_party_send_match_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast** | **int**| aoe4: 1, aoe2de: 0 | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **from_profile_id** | **int**|  | 
 **last_call_time** | **str**|  | 
 **match_id** | **int**|  | 
 **message** | **str**|  | 
 **message_type_id** | **int**|  | 
 **session_id** | **str**|  | 
 **to_profile_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_playerreport_report_user**
> game_playerreport_report_user(call_num, comment, connect_id, last_call_time, metadata, report_reason, report_type, reportee_profile_id, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
comment = 'comment_example' # str | 
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
metadata = NULL # object | 
report_reason = 56 # int | 7=all reasons
report_type = 56 # int | 
reportee_profile_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_playerreport_report_user(call_num, comment, connect_id, last_call_time, metadata, report_reason, report_type, reportee_profile_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_playerreport_report_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **comment** | **str**|  | 
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **metadata** | [**object**](.md)|  | 
 **report_reason** | **int**| 7&#x3D;all reasons | 
 **report_type** | **int**|  | 
 **reportee_profile_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_relationship_clear_relationship**
> game_relationship_clear_relationship(call_num, connect_id, last_call_time, relation_type, session_id, target_profile_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
relation_type = 56 # int | 1=Unban, 2=Unmute
session_id = 'session_id_example' # str | 
target_profile_id = 56 # int | 

try:
    api_instance.game_relationship_clear_relationship(call_num, connect_id, last_call_time, relation_type, session_id, target_profile_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_relationship_clear_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **relation_type** | **int**| 1&#x3D;Unban, 2&#x3D;Unmute | 
 **session_id** | **str**|  | 
 **target_profile_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_relationship_get_presence_data**
> game_relationship_get_presence_data(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_relationship_get_presence_data(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_relationship_get_presence_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_relationship_get_relationships**
> game_relationship_get_relationships(call_num, connect_id, last_call_time, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_relationship_get_relationships(call_num, connect_id, last_call_time, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_relationship_get_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_relationship_ignore**
> game_relationship_ignore(blocklevel, call_num, connect_id, last_call_time, relation_type, session_id, target_profile_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
blocklevel = 56 # int | 1=lobby ban, 2=mute
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
relation_type = 56 # int | 1=Unban, 2=Unmute
session_id = 'session_id_example' # str | 
target_profile_id = 56 # int | 

try:
    api_instance.game_relationship_ignore(blocklevel, call_num, connect_id, last_call_time, relation_type, session_id, target_profile_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_relationship_ignore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocklevel** | **int**| 1&#x3D;lobby ban, 2&#x3D;mute | 
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **relation_type** | **int**| 1&#x3D;Unban, 2&#x3D;Unmute | 
 **session_id** | **str**|  | 
 **target_profile_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_relationship_set_presence**
> game_relationship_set_presence(call_num, connect_id, last_call_time, presence_id, session_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
presence_id = 56 # int | 
session_id = 'session_id_example' # str | 

try:
    api_instance.game_relationship_set_presence(call_num, connect_id, last_call_time, presence_id, session_id)
except ApiException as e:
    print("Exception when calling DefaultApi->game_relationship_set_presence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **presence_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_relationship_set_presence_property**
> game_relationship_set_presence_property(call_num, connect_id, last_call_time, presence_property_def_id, session_id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
call_num = 0 # int |  (default to 0)
connect_id = 'connect_id_example' # str | 
last_call_time = 'last_call_time_example' # str | 
presence_property_def_id = 56 # int | 
session_id = 'session_id_example' # str | 
value = 56 # int | 

try:
    api_instance.game_relationship_set_presence_property(call_num, connect_id, last_call_time, presence_property_def_id, session_id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->game_relationship_set_presence_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_num** | **int**|  | [default to 0]
 **connect_id** | **str**|  | 
 **last_call_time** | **str**|  | 
 **presence_property_def_id** | **int**|  | 
 **session_id** | **str**|  | 
 **value** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

