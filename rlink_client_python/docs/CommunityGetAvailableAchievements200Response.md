# CommunityGetAvailableAchievements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**achievement_defs** | [**List[CommunityAchievementDefinition]**](CommunityAchievementDefinition.md) |  | 

## Example

```python
from rlink_client.models.community_get_available_achievements200_response import CommunityGetAvailableAchievements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetAvailableAchievements200Response from a JSON string
community_get_available_achievements200_response_instance = CommunityGetAvailableAchievements200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetAvailableAchievements200Response.to_json())

# convert the object into a dict
community_get_available_achievements200_response_dict = community_get_available_achievements200_response_instance.to_dict()
# create an instance of CommunityGetAvailableAchievements200Response from a dict
community_get_available_achievements200_response_from_dict = CommunityGetAvailableAchievements200Response.from_dict(community_get_available_achievements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


