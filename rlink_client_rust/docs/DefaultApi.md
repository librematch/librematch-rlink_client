# \DefaultApi

All URIs are relative to *<https://aoe-api.reliclink.com>*

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

## community_clan_find

> community_clan_find(join_policies, name, tags, start, count, title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**join_policies** | **i32** |  | [required] |
**name** | **String** |  | [required] |
**tags** | **String** |  | [required] |
**start** | **i32** |  | [required] |
**count** | **i32** |  | [required] |
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_find_advertisements

> community_find_advertisements(title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_achievements

> community_get_achievements(title, profileids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |
**profileids** | Option<**i32**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_available_achievements

> community_get_available_achievements(title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_available_community_events

> community_get_available_community_events(title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_available_leaderboards

> community_get_available_leaderboards(title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_avatar_stat_for_profile

> community_get_avatar_stat_for_profile(title, profile_names)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |
**profile_names** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_clan_info_full

> community_get_clan_info_full(name, title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** |  | [required] |
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_inventory_by_profile_ids

> community_get_inventory_by_profile_ids(title, profileids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |
**profileids** | Option<**i32**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_leaderboard2

> community_get_leaderboard2(start, count, title, leaderboard_id, sort_by, platform)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**start** | **i32** |  | [required] |
**count** | **i32** |  | [required] |
**title** | Option<**String**> |  |  |
**leaderboard_id** | Option<**i32**> |  |  |
**sort_by** | Option<**i32**> |  |  |
**platform** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_personal_stat

> community_get_personal_stat(title, profile_ids, profile_names, aliases)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |
**profile_ids** | Option<**String**> |  |  |
**profile_names** | Option<**String**> |  |  |
**aliases** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_get_recent_match_history

> community_get_recent_match_history(title, profile_ids, profile_names)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |
**profile_ids** | Option<**String**> |  |  |
**profile_names** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_news

> community_news(title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## community_proxy_steam_user_request

> community_proxy_steam_user_request(request, title, profile_ids, profile_names)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**request** | Option<**String**> |  |  |
**title** | Option<**String**> |  |  |
**profile_ids** | Option<**String**> |  |  |
**profile_names** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_account_find_profiles

> game_account_find_profiles(call_num, connect_id, last_call_time, name, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**name** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_account_find_profiles_by_platform_id

> game_account_find_profiles_by_platform_id(call_num, connect_id, last_call_time, session_id, platform_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**platform_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_account_get_profile_name

> game_account_get_profile_name(call_num, connect_id, last_call_time, profile_ids, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_account_get_profile_property

> game_account_get_profile_property(call_num, connect_id, last_call_time, session_id, profile_id, property_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profile_id** | **i32** |  | [required] |
**property_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_account_set_avatar_metadata

> game_account_set_avatar_metadata(call_num, connect_id, last_call_time, session_id, meta_data)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**meta_data** | [**serde_json::Value**](.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_account_set_language

> game_account_set_language(call_num, connect_id, last_call_time, session_id, title, language)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**title** | Option<**String**> |  |  |
**language** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_achievement_get_achievements

> game_achievement_get_achievements(call_num, connect_id, last_call_time, session_id, profile_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_achievement_get_available_achievements

> game_achievement_get_available_achievements(call_num, connect_id, last_call_time, session_id, signature)

No authentication needed

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**signature** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_achievement_sync_stats

> game_achievement_sync_stats(call_num, connect_id, last_call_time, session_id, account_type, auth)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**account_type** | **String** |  | [required] |
**auth** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_find_advertisements

> game_advertisement_find_advertisements(app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, profile_ids, race_ids, session_id, stat_group_ids, version_flags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**app_binary_checksum** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_type_id** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |
**race_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**stat_group_ids** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_find_observable_advertisements_get

> game_advertisement_find_observable_advertisements_get(call_num, connect_id, last_call_time, session_id, app_binary_checksum, count, data_checksum, desc, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_group_id, sort_order, start, version_flags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**app_binary_checksum** | **i32** |  | [required] |
**count** | **i32** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**desc** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**observer_group_id** | **i32** |  | [required] |
**sort_order** | **i32** |  | [required] |
**start** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_find_observable_advertisements_post

> game_advertisement_find_observable_advertisements_post(call_num, connect_id, last_call_time, session_id, app_binary_checksum, count, data_checksum, desc, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_group_id, sort_order, start, version_flags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**app_binary_checksum** | **i32** |  | [required] |
**count** | **i32** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**desc** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**observer_group_id** | **i32** |  | [required] |
**sort_order** | **i32** |  | [required] |
**start** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_get_advertisements

> game_advertisement_get_advertisements(call_num, connect_id, last_call_time, match_ids, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_get_lan_advertisements

> game_advertisement_get_lan_advertisements(app_binary_checksum, call_num, connect_id, data_checksum, lan_server_guids, last_call_time, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, session_id, version_flags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**app_binary_checksum** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**lan_server_guids** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_type_id** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**version_flags** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_host

> game_advertisement_host(advertisementid, app_binary_checksum, automatch_poll_id, call_num, connect_id, data_checksum, description, hostid, is_observable, last_call_time, mapname, matchtype, maxplayers, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_delay, observer_password, options, party, password, passworded, race, relay_region, service_type, session_id, slotinfo, state, statgroup, team, version_flags, visible)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**app_binary_checksum** | **i32** |  | [required] |
**automatch_poll_id** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**description** | **String** | Lobby title | [required] |
**hostid** | **i32** |  | [required] |
**is_observable** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**mapname** | **String** |  | [required] |
**matchtype** | **i32** |  | [required] |
**maxplayers** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**observer_delay** | **i32** |  | [required] |
**observer_password** | **String** |  | [required] |
**options** | **String** |  | [required] |
**party** | **i32** |  | [required] |
**password** | **String** |  | [required] |
**passworded** | **i32** |  | [required] |
**race** | **i32** |  | [required] |
**relay_region** | **String** |  | [required] |
**service_type** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**slotinfo** | **String** | zlib compressed | [required] |
**state** | **i32** |  | [required] |
**statgroup** | **i32** |  | [required] |
**team** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |
**visible** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_join

> game_advertisement_join(advertisementid, app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, mod_dll_checksum, mod_dll_file, mod_name, mod_version, party, password, race, session_id, statgroup, team, version_flags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**app_binary_checksum** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**party** | **i32** |  | [required] |
**password** | **String** |  | [required] |
**race** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**statgroup** | **i32** |  | [required] |
**team** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_leave

> game_advertisement_leave(advertisementid, call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_start_observing

> game_advertisement_start_observing(advertisementid, app_binary_checksum, call_num, connect_id, data_checksum, last_call_time, mod_dll_checksum, mod_dll_file, mod_name, mod_version, password, session_id, version_flags, with_party_session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**app_binary_checksum** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**password** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**version_flags** | **i32** |  | [required] |
**with_party_session_id** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_stop_observing

> game_advertisement_stop_observing(advertisementid, call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_update

> game_advertisement_update(advertisementid, app_binary_checksum, automatch_poll_id, call_num, connect_id, data_checksum, description, hostid, is_observable, last_call_time, mapname, matchtype, maxplayers, mod_dll_checksum, mod_dll_file, mod_name, mod_version, observer_delay, observer_password, options, password, passworded, race, session_id, slotinfo, state, team, version_flags, visible)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**app_binary_checksum** | **i32** |  | [required] |
**automatch_poll_id** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_checksum** | **i32** |  | [required] |
**description** | **String** | Lobby title | [required] |
**hostid** | **i32** |  | [required] |
**is_observable** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**mapname** | **String** |  | [required] |
**matchtype** | **i32** |  | [required] |
**maxplayers** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**observer_delay** | **i32** |  | [required] |
**observer_password** | **String** |  | [required] |
**options** | **String** |  | [required] |
**password** | **String** |  | [required] |
**passworded** | **i32** |  | [required] |
**race** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**slotinfo** | **String** | zlib compressed | [required] |
**state** | **i32** |  | [required] |
**team** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |
**visible** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_update_platform_lobby_id

> game_advertisement_update_platform_lobby_id(call_num, connect_id, last_call_time, match_id, platformlobby_id, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**platformlobby_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_update_state

> game_advertisement_update_state(advertisementid, call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_advertisement_update_tags

> game_advertisement_update_tags(advertisementid, call_num, connect_id, last_call_time, numeric_tag_names, numeric_tag_values, session_id, string_tag_names, string_tag_values)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**advertisementid** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**numeric_tag_names** | **String** |  | [required] |
**numeric_tag_values** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**string_tag_names** | **String** |  | [required] |
**string_tag_values** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_automatch2_get_automatch_map

> game_automatch2_get_automatch_map(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_automatch2_polling

> game_automatch2_polling(app_bin_crc, call_num, connect_id, data_crc, faction_ids, last_call_time, match_types, mod_dll_checksum, mod_dll_file, mod_name, mod_version, options, party_session_id, race_info_key, race_info_profile_id, race_info_race_id, relay_ping_times, relay_region, relay_regions, session_id, version_flags, veto_map_key, veto_maps)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**app_bin_crc** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**data_crc** | **i32** | backwards appBinCRC? | [required] |
**faction_ids** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_types** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**options** | **String** |  | [required] |
**party_session_id** | **i32** |  | [required] |
**race_info_key** | **i32** |  | [required] |
**race_info_profile_id** | **i32** |  | [required] |
**race_info_race_id** | **i32** |  | [required] |
**relay_ping_times** | **i32** |  | [required] |
**relay_region** | **String** |  | [required] |
**relay_regions** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**version_flags** | **i32** |  | [required] |
**veto_map_key** | **i32** |  | [required] |
**veto_maps** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_automatch2_stop_polling

> game_automatch2_stop_polling(call_num, commit, connect_id, last_call_time, owner_profile_id, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**commit** | **i32** |  | [required] |
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**owner_profile_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_automatch2_update_status

> game_automatch2_update_status(call_num, connect_id, last_call_time, match_id, result, result_code, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**result** | **i32** |  | [required] |
**result_code** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_automatch_get_automatch_map

> game_automatch_get_automatch_map(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_challenge_get_challenge_progress

> game_challenge_get_challenge_progress(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_challenge_get_challenge_progress_by_profile_id

> game_challenge_get_challenge_progress_by_profile_id(call_num, connect_id, last_call_time, profile_id, session_id)

TODO: Request not available in Wiki, this is guessed

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**profile_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_challenge_get_challenges

> game_challenge_get_challenges(call_num, connect_id, last_call_time, session_id, signature)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**signature** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_challenge_update_progress_batched

> game_challenge_update_progress_batched(call_num, connect_id, last_call_time, progress_ids, session_id, update_amounts)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**progress_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**update_amounts** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_chat_delete_offline_message

> game_chat_delete_offline_message(call_num, connect_id, last_call_time, message_id, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**message_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_chat_get_chat_channels

> game_chat_get_chat_channels(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_chat_get_offline_messages

> game_chat_get_offline_messages(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_apply

> game_clan_apply(call_num, clan_list_name, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**clan_list_name** | **String** |  | [required] |
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_create

> game_clan_create(call_num, chat, connect_id, cost, demote, description, disband, edit_info, edit_permission, full_name, icon, invite, item_price_id, join_policy, last_call_time, loc_string_id, message_of_the_day, metadata, name, paymentitem, permission_name, promote, rank, remove, session_id, tags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**chat** | **String** |  | [required] |
**connect_id** | **String** |  | [required] |
**cost** | **i32** |  | [required] |
**demote** | **String** |  | [required] |
**description** | **String** | Lobby title | [required] |
**disband** | **String** |  | [required] |
**edit_info** | **String** |  | [required] |
**edit_permission** | **String** |  | [required] |
**full_name** | **String** |  | [required] |
**icon** | **String** |  | [required] |
**invite** | **String** |  | [required] |
**item_price_id** | **i32** |  | [required] |
**join_policy** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**loc_string_id** | **i32** |  | [required] |
**message_of_the_day** | **String** |  | [required] |
**metadata** | [**serde_json::Value**](.md) |  | [required] |
**name** | **String** |  | [required] |
**paymentitem** | **i32** |  | [required] |
**permission_name** | **String** |  | [required] |
**promote** | **String** |  | [required] |
**rank** | **String** |  | [required] |
**remove** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**tags** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_disband

> game_clan_disband(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_find

> game_clan_find(call_num, connect_id, count, join_policies, last_call_time, name, session_id, start, tags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**count** | **i32** |  | [required] |
**join_policies** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**name** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**start** | **i32** |  | [required] |
**tags** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_get_clan

> game_clan_get_clan(call_num, connect_id, last_call_time, names, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**names** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_get_clan_info_full

> game_clan_get_clan_info_full(call_num, connect_id, last_call_time, name, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**name** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_clan_update

> game_clan_update(call_num, clan_list_id, connect_id, description, icon, join_policy, last_call_time, message_of_the_day, metadata, session_id, tags)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**clan_list_id** | **i32** |  | [required] |
**connect_id** | **String** |  | [required] |
**description** | **String** | Lobby title | [required] |
**icon** | **String** |  | [required] |
**join_policy** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**message_of_the_day** | **String** |  | [required] |
**metadata** | [**serde_json::Value**](.md) |  | [required] |
**session_id** | **String** |  | [required] |
**tags** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_cloud_get_file_url_get

> game_cloud_get_file_url_get(call_num, connect_id, last_call_time, names, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**names** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_cloud_get_file_url_post

> game_cloud_get_file_url_post(call_num, connect_id, last_call_time, names, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**names** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_cloud_get_temp_credentials

> game_cloud_get_temp_credentials(call_num, connect_id, last_call_time, session_id, key)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**key** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_community_event_get_available_community_events

> game_community_event_get_available_community_events(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_community_event_get_event_challenge_progress

> game_community_event_get_event_challenge_progress(call_num, connect_id, event_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**event_id** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_community_event_get_event_stats

> game_community_event_get_event_stats(call_num, connect_id, event_id, group_type, last_call_time, member_id, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**event_id** | **i32** |  | [required] |
**group_type** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**member_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_invitation_cancel_invitation

> game_invitation_cancel_invitation(call_num, connect_id, gatheringid, inviteeid, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**gatheringid** | **i32** |  | [required] |
**inviteeid** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_invitation_extend_invitation

> game_invitation_extend_invitation(call_num, connect_id, gatheringid, gatheringpassword, inviteeid, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**gatheringid** | **i32** |  | [required] |
**gatheringpassword** | **String** |  | [required] |
**inviteeid** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_detach_items

> game_item_detach_items(call_num, connect_id, item_charges, item_ids, item_locations, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**item_charges** | **i32** |  | [required] |
**item_ids** | **i32** |  | [required] |
**item_locations** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_inventory_by_profile_ids

> game_item_get_inventory_by_profile_ids(call_num, connect_id, last_call_time, session_id, profile_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_item_bundle_items_json

> game_item_get_item_bundle_items_json(call_num, connect_id, last_call_time, session_id, signature)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**signature** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_item_definitions_json

> game_item_get_item_definitions_json(call_num, connect_id, last_call_time, session_id, signature)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**signature** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_item_loadouts

> game_item_get_item_loadouts(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_item_prices

> game_item_get_item_prices(account_type, call_num, connect_id, last_call_time, session_id, country, currency, sale_version)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_type** | **String** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**country** | **String** |  | [required] |
**currency** | **String** |  | [required] |
**sale_version** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_level_rewards_table_json

> game_item_get_level_rewards_table_json(call_num, connect_id, last_call_time, session_id, signature)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**signature** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_personalized_sale_items

> game_item_get_personalized_sale_items(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_get_scheduled_sale_and_items

> game_item_get_scheduled_sale_and_items(call_num, connect_id, last_call_time, session_id, sale_type)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**sale_type** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_move_charges

> game_item_move_charges(call_num, charges, connect_id, deletes, from_item_ids, last_call_time, session_id, to_item_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**charges** | **i32** |  | [required] |
**connect_id** | **String** |  | [required] |
**deletes** | **i32** |  | [required] |
**from_item_ids** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**to_item_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_move_item

> game_item_move_item(call_num, connect_id, item_ids, item_location_ids, last_call_time, pos_ids, session_id, slot_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**item_ids** | **i32** |  | [required] |
**item_location_ids** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**pos_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**slot_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_open_item_pack

> game_item_open_item_pack(call_num, choices, connect_id, item_instance_id, item_location_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**choices** | **i32** |  | [required] |
**connect_id** | **String** |  | [required] |
**item_instance_id** | **i32** |  | [required] |
**item_location_id** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_sign_item

> game_item_sign_item(call_num, connect_id, crc, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**crc** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_item_update_item_attributes

> game_item_update_item_attributes(attribute_keys, attribute_values, call_num, connect_id, item_instance_ids, last_call_time, session_id, xp_gains)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**attribute_keys** | **String** |  | [required] |
**attribute_values** | **String** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**item_instance_ids** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**xp_gains** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_available_leaderboards

> game_leaderboard_get_available_leaderboards(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_leaderboard

> game_leaderboard_get_leaderboard(call_num, connect_id, last_call_time, session_id, start, count, leaderboard_id, sort_by)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**start** | **i32** |  | [required] |
**count** | **i32** |  | [required] |
**leaderboard_id** | Option<**i32**> |  |  |
**sort_by** | Option<**i32**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_party_stat

> game_leaderboard_get_party_stat(call_num, connect_id, last_call_time, session_id, statsids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**statsids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_personal_stat

> game_leaderboard_get_personal_stat(call_num, connect_id, last_call_time, session_id)

TODO: No request documented in Wiki, guessed parameters

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_recent_match_history_get

> game_leaderboard_get_recent_match_history_get(call_num, connect_id, last_call_time, session_id, profile_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_recent_match_history_post

> game_leaderboard_get_recent_match_history_post(call_num, connect_id, last_call_time, session_id, profile_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_recent_match_single_player_history

> game_leaderboard_get_recent_match_single_player_history(call_num, connect_id, last_call_time, session_id, profile_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profile_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_stat_groups_by_profile_ids

> game_leaderboard_get_stat_groups_by_profile_ids(call_num, connect_id, last_call_time, session_id, profileids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profileids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_get_stats_for_leaderboard_by_profile_name

> game_leaderboard_get_stats_for_leaderboard_by_profile_name(call_num, connect_id, last_call_time, session_id, profileids, leaderboard_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**profileids** | **i32** |  | [required] |
**leaderboard_id** | Option<**i32**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_leaderboard_set_avatar_stat_values

> game_leaderboard_set_avatar_stat_values(avatar_stat_ids, call_num, connect_id, last_call_time, session_id, update_types, values)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**avatar_stat_ids** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |
**update_types** | **i32** |  | [required] |
**values** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_login_logout

> game_login_logout(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_login_platform_login

> game_login_platform_login(account_type, active_match_id, alias, app_id, auth, call_num, client_lib_version, connect_id, country, installation_type, last_call_time, mac_address, major_version, minor_version, platform_user_id, start_game_token, sync_hash, timeout_override, language, store_license_token, title)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_type** | **String** |  | [required] |
**active_match_id** | **i32** |  | [required] |[default to -1]
**alias** | **String** |  | [required] |
**app_id** | **i32** |  | [required] |
**auth** | **String** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**client_lib_version** | **i32** |  | [required] |
**connect_id** | **String** |  | [required] |
**country** | **String** |  | [required] |
**installation_type** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**mac_address** | **String** |  | [required] |
**major_version** | **String** |  | [required] |
**minor_version** | **i32** |  | [required] |
**platform_user_id** | **i32** |  | [required] |
**start_game_token** | **String** |  | [required] |
**sync_hash** | **i32** |  | [required] |
**timeout_override** | **i32** |  | [required] |[default to 0]
**language** | Option<**String**> |  |  |
**store_license_token** | Option<**String**> |  |  |
**title** | Option<**String**> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_login_read_session

> game_login_read_session(ack, poll_num, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**ack** | **i32** |  | [required] |
**poll_num** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_news_get_news

> game_news_get_news(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_party_create_or_report_single_player

> game_party_create_or_report_single_player(appbincrc, call_num, connect_id, counters_zip, create_match_key, datacrc, is_complete, item_updates, last_call_time, mapname, match_key, match_type_id, mod_dll_checksum, mod_dll_file, mod_name, mod_version, options, race_ids, results, session_id, slot_info, team_ids, version_flags, xp_gained)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**appbincrc** | **i32** |  | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**counters_zip** | **String** | zlib-compressed | [required] |
**create_match_key** | **i32** |  | [required] |[default to 1]
**datacrc** | **i32** |  | [required] |
**is_complete** | **i32** |  | [required] |[default to 0]
**item_updates** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**mapname** | **String** |  | [required] |
**match_key** | **String** |  | [required] |
**match_type_id** | **i32** |  | [required] |
**mod_dll_checksum** | **i32** |  | [required] |
**mod_dll_file** | **String** |  | [required] |
**mod_name** | **String** |  | [required] |
**mod_version** | **String** |  | [required] |
**options** | **String** |  | [required] |
**race_ids** | **i32** |  | [required] |
**results** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**slot_info** | **String** | zlib-compressed | [required] |
**team_ids** | **i32** |  | [required] |
**version_flags** | **i32** |  | [required] |
**xp_gained** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_party_finalize_replay_upload

> game_party_finalize_replay_upload(call_num, connect_id, error_string, finalize_result, is_single_player, last_call_time, match_id, session_id, size, url)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**error_string** | **String** |  | [required] |
**finalize_result** | **i32** |  | [required] |[default to 1]
**is_single_player** | **i32** |  | [required] |[default to 0]
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**size** | **i32** |  | [required] |
**url** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_party_peer_add

> game_party_peer_add(call_num, connect_id, last_call_time, match_id, profile_ids, race_ids, session_id, stat_group_ids, team_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**profile_ids** | **i32** |  | [required] |
**race_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**stat_group_ids** | **i32** |  | [required] |
**team_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_party_peer_update

> game_party_peer_update(call_num, connect_id, is_non_participants, last_call_time, match_id, profile_ids, race_ids, session_id, team_ids)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**is_non_participants** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**profile_ids** | **i32** |  | [required] |
**race_ids** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**team_ids** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_party_report_match

> game_party_report_match(call_num, check_sums, connect_id, counters_zip, item_updates, last_call_time, match_id, profile_ids, race_ids, results, session_id, simplayer_ids, team_ids, xp_gained)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**check_sums** | **i32** |  | [required] |
**connect_id** | **String** |  | [required] |
**counters_zip** | **String** | zlib-compressed | [required] |
**item_updates** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**profile_ids** | **i32** |  | [required] |
**race_ids** | **i32** |  | [required] |
**results** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**simplayer_ids** | **i32** |  | [required] |
**team_ids** | **i32** |  | [required] |
**xp_gained** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_party_send_match_chat

> game_party_send_match_chat(broadcast, call_num, connect_id, from_profile_id, last_call_time, match_id, message, message_type_id, session_id, to_profile_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**broadcast** | **i32** | aoe4: 1, aoe2de: 0 | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**from_profile_id** | **i32** |  | [required] |
**last_call_time** | **String** |  | [required] |
**match_id** | **i32** |  | [required] |
**message** | **String** |  | [required] |
**message_type_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**to_profile_id** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_playerreport_report_user

> game_playerreport_report_user(call_num, comment, connect_id, last_call_time, metadata, report_reason, report_type, reportee_profile_id, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**comment** | **String** |  | [required] |
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**metadata** | [**serde_json::Value**](.md) |  | [required] |
**report_reason** | **i32** | 7=all reasons | [required] |
**report_type** | **i32** |  | [required] |
**reportee_profile_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_relationship_clear_relationship

> game_relationship_clear_relationship(call_num, connect_id, last_call_time, relation_type, session_id, target_profile_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**relation_type** | **i32** | 1=Unban, 2=Unmute | [required] |
**session_id** | **String** |  | [required] |
**target_profile_id** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_relationship_get_presence_data

> game_relationship_get_presence_data(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_relationship_get_relationships

> game_relationship_get_relationships(call_num, connect_id, last_call_time, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_relationship_ignore

> game_relationship_ignore(blocklevel, call_num, connect_id, last_call_time, relation_type, session_id, target_profile_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**blocklevel** | **i32** | 1=lobby ban, 2=mute | [required] |
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**relation_type** | **i32** | 1=Unban, 2=Unmute | [required] |
**session_id** | **String** |  | [required] |
**target_profile_id** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_relationship_set_presence

> game_relationship_set_presence(call_num, connect_id, last_call_time, presence_id, session_id)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**presence_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## game_relationship_set_presence_property

> game_relationship_set_presence_property(call_num, connect_id, last_call_time, presence_property_def_id, session_id, value)

### Parameters

Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**call_num** | **i32** |  | [required] |[default to 0]
**connect_id** | **String** |  | [required] |
**last_call_time** | **String** |  | [required] |
**presence_property_def_id** | **i32** |  | [required] |
**session_id** | **String** |  | [required] |
**value** | **i32** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
