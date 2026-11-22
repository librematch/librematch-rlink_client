# CommunityGetAchievements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**user_achievements_map** | **List[Dict[str, List[CommunityEarnedAchievement]]]** | One single-key object per profile; the key is the unquoted profile id. | 

## Example

```python
from rlink_client.models.community_get_achievements200_response import CommunityGetAchievements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetAchievements200Response from a JSON string
community_get_achievements200_response_instance = CommunityGetAchievements200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetAchievements200Response.to_json())

# convert the object into a dict
community_get_achievements200_response_dict = community_get_achievements200_response_instance.to_dict()
# create an instance of CommunityGetAchievements200Response from a dict
community_get_achievements200_response_from_dict = CommunityGetAchievements200Response.from_dict(community_get_achievements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


