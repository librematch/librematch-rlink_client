# rlink_client.CommunityApi

All URIs are relative to *https://aoe-api.worldsedgelink.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**community_find_advertisements**](CommunityApi.md#community_find_advertisements) | **GET** /community/advertisement/findAdvertisements | Open lobbies (object form)
[**community_find_clans**](CommunityApi.md#community_find_clans) | **GET** /community/clan/find | Searches clans 
[**community_get_achievements**](CommunityApi.md#community_get_achievements) | **GET** /community/achievement/getAchievements | Earned achievements 
[**community_get_available_achievements**](CommunityApi.md#community_get_available_achievements) | **GET** /community/achievement/getAvailableAchievements | Achievement catalogue (object form)
[**community_get_available_community_events**](CommunityApi.md#community_get_available_community_events) | **GET** /community/CommunityEvent/getAvailableCommunityEvents | Community events (object form)
[**community_get_available_leaderboards**](CommunityApi.md#community_get_available_leaderboards) | **GET** /community/leaderboard/getAvailableLeaderboards | Ladder catalogue (object form)
[**community_get_available_leaderboards_alias**](CommunityApi.md#community_get_available_leaderboards_alias) | **GET** /community/leaderboard/GetAvailableLeaderboards | Ladder catalogue (capitalised alias)
[**community_get_avatar_stat_for_profile**](CommunityApi.md#community_get_avatar_stat_for_profile) | **GET** /community/leaderboard/GetAvatarStatForProfile | Avatar statistics (flat object form)
[**community_get_clan_info_full**](CommunityApi.md#community_get_clan_info_full) | **GET** /community/clan/getClanInfoFull | Clan information 
[**community_get_inventory_by_profile_ids**](CommunityApi.md#community_get_inventory_by_profile_ids) | **GET** /community/item/getInventoryByProfileIDs | Inventories by profile 
[**community_get_leader_board2**](CommunityApi.md#community_get_leader_board2) | **GET** /community/leaderboard/getLeaderBoard2 | Ladder page (object form)
[**community_get_match_history**](CommunityApi.md#community_get_match_history) | **GET** /community/leaderboard/getMatchHistory | Matches by id (object form)
[**community_get_news**](CommunityApi.md#community_get_news) | **GET** /community/news/getNews | News (object form)
[**community_get_personal_stat**](CommunityApi.md#community_get_personal_stat) | **GET** /community/leaderboard/GetPersonalStat | Personal ladder statistics (object form)
[**community_get_personal_stat_alias**](CommunityApi.md#community_get_personal_stat_alias) | **GET** /community/leaderboard/getPersonalStat | Personal ladder statistics (lowercase alias)
[**community_get_recent_match_history**](CommunityApi.md#community_get_recent_match_history) | **GET** /community/leaderboard/getRecentMatchHistory | Recent match history (object form)
[**community_get_replay_files**](CommunityApi.md#community_get_replay_files) | **GET** /community/leaderboard/getReplayFiles | Stored replays of matches
[**community_proxy_steam_user_request**](CommunityApi.md#community_proxy_steam_user_request) | **GET** /community/external/proxysteamuserrequest | Profiles and the Steam summary


# **community_find_advertisements**
> CommunityFindAdvertisements200Response community_find_advertisements(title=title)

Open lobbies (object form)

Every waiting (state 0), visible lobby with its members, in the object form of
the live 22-field shape. Lobby passwords, observer passwords and the internal
advertisement address are never echoed.


### Example


```python
import rlink_client
from rlink_client.models.community_find_advertisements200_response import CommunityFindAdvertisements200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Open lobbies (object form)
        api_response = api_instance.community_find_advertisements(title=title)
        print("The response of CommunityApi->community_find_advertisements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_find_advertisements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityFindAdvertisements200Response**](CommunityFindAdvertisements200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lobbies and the profiles of their members. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_find_clans**
> CommunityFindClans200Response community_find_clans(title=title)

Searches clans 

The clans of the title matching the search parameters, paged by
`count`/`start`; `clans: []` when none matches.


### Example


```python
import rlink_client
from rlink_client.models.community_find_clans200_response import CommunityFindClans200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Searches clans 
        api_response = api_instance.community_find_clans(title=title)
        print("The response of CommunityApi->community_find_clans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_find_clans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityFindClans200Response**](CommunityFindClans200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty clan list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_achievements**
> CommunityGetAchievements200Response community_get_achievements(title=title, profileids=profileids, profile_ids=profile_ids)

Earned achievements 

One map per requested profile id with the earned achievement list of the
profile; the keys are the bare profile ids without quotes, the live-service
quirk.


### Example


```python
import rlink_client
from rlink_client.models.community_get_achievements200_response import CommunityGetAchievements200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    profileids = 'profileids_example' # str | JSON array of profile ids (also profile_ids). (optional)
    profile_ids = 'profile_ids_example' # str |  (optional)

    try:
        # Earned achievements 
        api_response = api_instance.community_get_achievements(title=title, profileids=profileids, profile_ids=profile_ids)
        print("The response of CommunityApi->community_get_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **profileids** | **str**| JSON array of profile ids (also profile_ids). | [optional] 
 **profile_ids** | **str**|  | [optional] 

### Return type

[**CommunityGetAchievements200Response**](CommunityGetAchievements200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty earned achievements per profile. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_achievements**
> CommunityGetAvailableAchievements200Response community_get_available_achievements(title=title)

Achievement catalogue (object form)

The achievementDef rows of the per-title catalogue (rows marked deleted are
skipped).


### Example


```python
import rlink_client
from rlink_client.models.community_get_available_achievements200_response import CommunityGetAvailableAchievements200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Achievement catalogue (object form)
        api_response = api_instance.community_get_available_achievements(title=title)
        print("The response of CommunityApi->community_get_available_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_available_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityGetAvailableAchievements200Response**](CommunityGetAvailableAchievements200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Achievement catalogue. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_community_events**
> CommunityGetAvailableCommunityEvents200Response community_get_available_community_events(title=title)

Community events (object form)

A4 reshapes its rolling seasons (menu backgrounds folded in); AoM serves its
events with their leaderboards and ladder maps; the other titles answer an
empty list.


### Example


```python
import rlink_client
from rlink_client.models.community_get_available_community_events200_response import CommunityGetAvailableCommunityEvents200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Community events (object form)
        api_response = api_instance.community_get_available_community_events(title=title)
        print("The response of CommunityApi->community_get_available_community_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_available_community_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityGetAvailableCommunityEvents200Response**](CommunityGetAvailableCommunityEvents200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events, plus the AoM ladders. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_leaderboards**
> CommunityGetAvailableLeaderboards200Response community_get_available_leaderboards(title=title)

Ladder catalogue (object form)

The object form of the ladder catalogue of the title; A1 has no catalogue and
answers result 0 with every array empty.


### Example


```python
import rlink_client
from rlink_client.models.community_get_available_leaderboards200_response import CommunityGetAvailableLeaderboards200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Ladder catalogue (object form)
        api_response = api_instance.community_get_available_leaderboards(title=title)
        print("The response of CommunityApi->community_get_available_leaderboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_available_leaderboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityGetAvailableLeaderboards200Response**](CommunityGetAvailableLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Catalogue. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_available_leaderboards_alias**
> community_get_available_leaderboards_alias(title=title)

Ladder catalogue (capitalised alias)

Same handler — the capitalised spelling the live service and the spec disagree on.

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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Ladder catalogue (capitalised alias)
        api_instance.community_get_available_leaderboards_alias(title=title)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_available_leaderboards_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

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
**200** | Same body as getAvailableLeaderboards. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_avatar_stat_for_profile**
> CommunityGetAvatarStatForProfile200Response community_get_avatar_stat_for_profile(title=title, profile_ids=profile_ids, profileids=profileids, profile_names=profile_names, aliases=aliases)

Avatar statistics (flat object form)

The flat avatarStat rows of the requested profiles: no per-profile grouping
and no metadata field, the live shape.


### Example


```python
import rlink_client
from rlink_client.models.community_get_avatar_stat_for_profile200_response import CommunityGetAvatarStatForProfile200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids (also profileids). (optional)
    profileids = 'profileids_example' # str |  (optional)
    profile_names = 'profile_names_example' # str |  (optional)
    aliases = 'aliases_example' # str |  (optional)

    try:
        # Avatar statistics (flat object form)
        api_response = api_instance.community_get_avatar_stat_for_profile(title=title, profile_ids=profile_ids, profileids=profileids, profile_names=profile_names, aliases=aliases)
        print("The response of CommunityApi->community_get_avatar_stat_for_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_avatar_stat_for_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **profile_ids** | **str**| JSON array of profile ids (also profileids). | [optional] 
 **profileids** | **str**|  | [optional] 
 **profile_names** | **str**|  | [optional] 
 **aliases** | **str**|  | [optional] 

### Return type

[**CommunityGetAvatarStatForProfile200Response**](CommunityGetAvatarStatForProfile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flat avatar-stat list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_clan_info_full**
> CommunityGetClanInfoFull200Response community_get_clan_info_full(title=title)

Clan information 

The full record of the requested clan (`clan`), null when the clan does not
exist.


### Example


```python
import rlink_client
from rlink_client.models.community_get_clan_info_full200_response import CommunityGetClanInfoFull200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Clan information 
        api_response = api_instance.community_get_clan_info_full(title=title)
        print("The response of CommunityApi->community_get_clan_info_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_clan_info_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityGetClanInfoFull200Response**](CommunityGetClanInfoFull200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Null clan. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_inventory_by_profile_ids**
> CommunityGetInventoryByProfileIDs200Response community_get_inventory_by_profile_ids(title=title, profileids=profileids, profile_ids=profile_ids)

Inventories by profile 

One map per requested profile id, its key wrapped in literal double quotes
(the live-service quirk), listing the items the profile owns.


### Example


```python
import rlink_client
from rlink_client.models.community_get_inventory_by_profile_ids200_response import CommunityGetInventoryByProfileIDs200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    profileids = 'profileids_example' # str | JSON array of profile ids (the name/alias forms are bound but dropped). (optional)
    profile_ids = 'profile_ids_example' # str |  (optional)

    try:
        # Inventories by profile 
        api_response = api_instance.community_get_inventory_by_profile_ids(title=title, profileids=profileids, profile_ids=profile_ids)
        print("The response of CommunityApi->community_get_inventory_by_profile_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_inventory_by_profile_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **profileids** | **str**| JSON array of profile ids (the name/alias forms are bound but dropped). | [optional] 
 **profile_ids** | **str**|  | [optional] 

### Return type

[**CommunityGetInventoryByProfileIDs200Response**](CommunityGetInventoryByProfileIDs200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty inventories. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_leader_board2**
> CommunityGetLeaderBoard2200Response community_get_leader_board2(title=title, leaderboard_id=leaderboard_id, start=start, count=count, sort_by=sort_by, platform=platform)

Ladder page (object form)

The page of a ladder with the total population of the season. `statGroups` and
`leaderboardStats` are not index-aligned; clients join them by `statgroup_id`.


### Example


```python
import rlink_client
from rlink_client.models.community_get_leader_board2200_response import CommunityGetLeaderBoard2200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    leaderboard_id = 56 # int | default per title (A2 3 solo RM, others 1); <= 0 falls back to it. (optional)
    start = 1 # int | 1-based page index. (optional) (default to 1)
    count = 100 # int | page size, capped at 1000. (optional) (default to 100)
    sort_by = 56 # int | 0 wins descending; anything else (the default) rating descending. (optional)
    platform = 'platform_example' # str | the platform of the ladder (Steam or Xbox).  (optional)

    try:
        # Ladder page (object form)
        api_response = api_instance.community_get_leader_board2(title=title, leaderboard_id=leaderboard_id, start=start, count=count, sort_by=sort_by, platform=platform)
        print("The response of CommunityApi->community_get_leader_board2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_leader_board2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **leaderboard_id** | **int**| default per title (A2 3 solo RM, others 1); &lt;&#x3D; 0 falls back to it. | [optional] 
 **start** | **int**| 1-based page index. | [optional] [default to 1]
 **count** | **int**| page size, capped at 1000. | [optional] [default to 100]
 **sort_by** | **int**| 0 wins descending; anything else (the default) rating descending. | [optional] 
 **platform** | **str**| the platform of the ladder (Steam or Xbox).  | [optional] 

### Return type

[**CommunityGetLeaderBoard2200Response**](CommunityGetLeaderBoard2200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ladder page. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_match_history**
> CommunityGetMatchHistory200Response community_get_match_history(title=title, match_ids=match_ids)

Matches by id (object form)

The matches of `matchIDs` — the response key is `matchHistory` (not
matchHistoryStats) — with gamemod_id 1800 in every row. Unknown ids are
skipped.


### Example


```python
import rlink_client
from rlink_client.models.community_get_match_history200_response import CommunityGetMatchHistory200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    match_ids = 'match_ids_example' # str | JSON array of match ids (positive, at most 100). (optional)

    try:
        # Matches by id (object form)
        api_response = api_instance.community_get_match_history(title=title, match_ids=match_ids)
        print("The response of CommunityApi->community_get_match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **match_ids** | **str**| JSON array of match ids (positive, at most 100). | [optional] 

### Return type

[**CommunityGetMatchHistory200Response**](CommunityGetMatchHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested matches. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_news**
> CommunityGetNews200Response community_get_news(title=title)

News (object form)

The news entries of the title as named fields, sorted by `datevisible`
descending (id as the tie-break). `newstitle_locstringid`,
`newssubtitle_locstringid` and `newstext_locstringid` are the localisation ids
of the strings (-1 when the entry carries no localised text); the raw text
travels in the other fields.


### Example


```python
import rlink_client
from rlink_client.models.community_get_news200_response import CommunityGetNews200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # News (object form)
        api_response = api_instance.community_get_news(title=title)
        print("The response of CommunityApi->community_get_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_news: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

### Return type

[**CommunityGetNews200Response**](CommunityGetNews200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | News envelope (unknown/foreign title gets the code-2 envelope). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_personal_stat**
> CommunityGetPersonalStat200Response community_get_personal_stat(title=title, profileids=profileids, profile_ids=profile_ids, profile_names=profile_names, profile_names2=profile_names2, aliases=aliases)

Personal ladder statistics (object form)

One statGroup per resolved profile and one leaderboardStats row per
ladder the profile is rated on (no rankTotal: the live quirk).
Unrated profiles get a default-ladder row (1000 rating, rank -1);
unknown ids resolve to placeholder profiles (alias
"Player <id>"). `aliases` matches connected users only.


### Example


```python
import rlink_client
from rlink_client.models.community_get_personal_stat200_response import CommunityGetPersonalStat200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    profileids = 'profileids_example' # str | JSON array of profile ids (also accepted as profile_ids). (optional)
    profile_ids = 'profile_ids_example' # str |  (optional)
    profile_names = 'profile_names_example' # str | JSON array of `/steam/<id>` or `/xboxlive/<id>` (also profileNames). (optional)
    profile_names2 = 'profile_names_example' # str |  (optional)
    aliases = 'aliases_example' # str | JSON array of aliases; connected users only. (optional)

    try:
        # Personal ladder statistics (object form)
        api_response = api_instance.community_get_personal_stat(title=title, profileids=profileids, profile_ids=profile_ids, profile_names=profile_names, profile_names2=profile_names2, aliases=aliases)
        print("The response of CommunityApi->community_get_personal_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_personal_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **profileids** | **str**| JSON array of profile ids (also accepted as profile_ids). | [optional] 
 **profile_ids** | **str**|  | [optional] 
 **profile_names** | **str**| JSON array of &#x60;/steam/&lt;id&gt;&#x60; or &#x60;/xboxlive/&lt;id&gt;&#x60; (also profileNames). | [optional] 
 **profile_names2** | **str**|  | [optional] 
 **aliases** | **str**| JSON array of aliases; connected users only. | [optional] 

### Return type

[**CommunityGetPersonalStat200Response**](CommunityGetPersonalStat200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Personal ladder rows. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_personal_stat_alias**
> community_get_personal_stat_alias(title=title)

Personal ladder statistics (lowercase alias)

Same handler as GetPersonalStat.

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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)

    try:
        # Personal ladder statistics (lowercase alias)
        api_instance.community_get_personal_stat_alias(title=title)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_personal_stat_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 

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
**200** | Same body as GetPersonalStat. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_recent_match_history**
> CommunityGetRecentMatchHistory200Response community_get_recent_match_history(title=title, profile_ids=profile_ids, profileids=profileids, profile_names=profile_names, aliases=aliases)

Recent match history (object form)

The 30 most recent matches involving any requested profile plus the
union of the profiles of those matches. At least one usable
identification parameter is required: without it the answer is the
empty shape (same HTTP 200).


### Example


```python
import rlink_client
from rlink_client.models.community_get_recent_match_history200_response import CommunityGetRecentMatchHistory200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    profile_ids = 'profile_ids_example' # str | JSON array of profile ids (also profileids). (optional)
    profileids = 'profileids_example' # str |  (optional)
    profile_names = 'profile_names_example' # str |  (optional)
    aliases = 'aliases_example' # str |  (optional)

    try:
        # Recent match history (object form)
        api_response = api_instance.community_get_recent_match_history(title=title, profile_ids=profile_ids, profileids=profileids, profile_names=profile_names, aliases=aliases)
        print("The response of CommunityApi->community_get_recent_match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_recent_match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **profile_ids** | **str**| JSON array of profile ids (also profileids). | [optional] 
 **profileids** | **str**|  | [optional] 
 **profile_names** | **str**|  | [optional] 
 **aliases** | **str**|  | [optional] 

### Return type

[**CommunityGetRecentMatchHistory200Response**](CommunityGetRecentMatchHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recent matches and the union of their profiles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_get_replay_files**
> CommunityGetReplayFiles200Response community_get_replay_files(title=title, match_ids=match_ids)

Stored replays of matches

The descriptors of the replays of the requested matches: the signed blob URLs
and the `expiryUnix` at which they stop being served.


### Example


```python
import rlink_client
from rlink_client.models.community_get_replay_files200_response import CommunityGetReplayFiles200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    match_ids = 'match_ids_example' # str | JSON array of match ids. (optional)

    try:
        # Stored replays of matches
        api_response = api_instance.community_get_replay_files(title=title, match_ids=match_ids)
        print("The response of CommunityApi->community_get_replay_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_get_replay_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **match_ids** | **str**| JSON array of match ids. | [optional] 

### Return type

[**CommunityGetReplayFiles200Response**](CommunityGetReplayFiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Replay descriptors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_proxy_steam_user_request**
> CommunityProxySteamUserRequest200Response community_proxy_steam_user_request(title=title, profile_names=profile_names, profile_names2=profile_names2, aliases=aliases, request=request)

Profiles and the Steam summary

`avatars` carries the resolved profiles and `steamResults` the player
summaries of the Steam Web API. `request` is the Steam API path the request is
proxied to (evidently `ISteamUser/GetPlayerSummaries`).


### Example


```python
import rlink_client
from rlink_client.models.community_proxy_steam_user_request200_response import CommunityProxySteamUserRequest200Response
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
    api_instance = rlink_client.CommunityApi(api_client)
    title = 'title_example' # str | The title whose data is answered (`age1`-`age4`, `athens`). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  (optional)
    profile_names = 'profile_names_example' # str | JSON array of `/steam/<id>` (also profileNames). (optional)
    profile_names2 = 'profile_names_example' # str |  (optional)
    aliases = 'aliases_example' # str |  (optional)
    request = 'request_example' # str | the Steam Web API path the request is proxied to.  (optional)

    try:
        # Profiles and the Steam summary
        api_response = api_instance.community_proxy_steam_user_request(title=title, profile_names=profile_names, profile_names2=profile_names2, aliases=aliases, request=request)
        print("The response of CommunityApi->community_proxy_steam_user_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->community_proxy_steam_user_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title whose data is answered (&#x60;age1&#x60;-&#x60;age4&#x60;, &#x60;athens&#x60;). Absent: the title of the host the request reached. A foreign or unknown title answers 404 with no body, and a missing title on the andromeda host answers 400 with an HTML error page.  | [optional] 
 **profile_names** | **str**| JSON array of &#x60;/steam/&lt;id&gt;&#x60; (also profileNames). | [optional] 
 **profile_names2** | **str**|  | [optional] 
 **aliases** | **str**|  | [optional] 
 **request** | **str**| the Steam Web API path the request is proxied to.  | [optional] 

### Return type

[**CommunityProxySteamUserRequest200Response**](CommunityProxySteamUserRequest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profiles plus an empty Steam summary. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

