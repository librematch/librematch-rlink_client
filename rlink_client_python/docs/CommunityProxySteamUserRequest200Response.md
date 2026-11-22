# CommunityProxySteamUserRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**avatars** | [**List[CommunityProfile]**](CommunityProfile.md) |  | 
**steam_results** | [**SteamResponse**](SteamResponse.md) |  | 

## Example

```python
from rlink_client.models.community_proxy_steam_user_request200_response import CommunityProxySteamUserRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityProxySteamUserRequest200Response from a JSON string
community_proxy_steam_user_request200_response_instance = CommunityProxySteamUserRequest200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityProxySteamUserRequest200Response.to_json())

# convert the object into a dict
community_proxy_steam_user_request200_response_dict = community_proxy_steam_user_request200_response_instance.to_dict()
# create an instance of CommunityProxySteamUserRequest200Response from a dict
community_proxy_steam_user_request200_response_from_dict = CommunityProxySteamUserRequest200Response.from_dict(community_proxy_steam_user_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


