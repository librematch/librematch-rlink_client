# CommunityGetPersonalStat200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**stat_groups** | [**List[CommunityStatGroup]**](CommunityStatGroup.md) |  | 
**leaderboard_stats** | [**List[CommunityLeaderboardStat]**](CommunityLeaderboardStat.md) |  | 

## Example

```python
from rlink_client.models.community_get_personal_stat200_response import CommunityGetPersonalStat200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetPersonalStat200Response from a JSON string
community_get_personal_stat200_response_instance = CommunityGetPersonalStat200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetPersonalStat200Response.to_json())

# convert the object into a dict
community_get_personal_stat200_response_dict = community_get_personal_stat200_response_instance.to_dict()
# create an instance of CommunityGetPersonalStat200Response from a dict
community_get_personal_stat200_response_from_dict = CommunityGetPersonalStat200Response.from_dict(community_get_personal_stat200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


