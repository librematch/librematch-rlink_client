# CommunityGetAvatarStatForProfile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**avatar_stats_for_profile** | [**List[CommunityAvatarStat]**](CommunityAvatarStat.md) |  | 

## Example

```python
from rlink_client.models.community_get_avatar_stat_for_profile200_response import CommunityGetAvatarStatForProfile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetAvatarStatForProfile200Response from a JSON string
community_get_avatar_stat_for_profile200_response_instance = CommunityGetAvatarStatForProfile200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetAvatarStatForProfile200Response.to_json())

# convert the object into a dict
community_get_avatar_stat_for_profile200_response_dict = community_get_avatar_stat_for_profile200_response_instance.to_dict()
# create an instance of CommunityGetAvatarStatForProfile200Response from a dict
community_get_avatar_stat_for_profile200_response_from_dict = CommunityGetAvatarStatForProfile200Response.from_dict(community_get_avatar_stat_for_profile200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


