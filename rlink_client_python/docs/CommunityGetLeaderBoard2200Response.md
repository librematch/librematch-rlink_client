# CommunityGetLeaderBoard2200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**stat_groups** | [**List[CommunityStatGroup]**](CommunityStatGroup.md) |  | 
**leaderboard_stats** | [**List[CommunityLeaderboardStat]**](CommunityLeaderboardStat.md) |  | 
**rank_total** | **int** |  | 

## Example

```python
from rlink_client.models.community_get_leader_board2200_response import CommunityGetLeaderBoard2200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetLeaderBoard2200Response from a JSON string
community_get_leader_board2200_response_instance = CommunityGetLeaderBoard2200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetLeaderBoard2200Response.to_json())

# convert the object into a dict
community_get_leader_board2200_response_dict = community_get_leader_board2200_response_instance.to_dict()
# create an instance of CommunityGetLeaderBoard2200Response from a dict
community_get_leader_board2200_response_from_dict = CommunityGetLeaderBoard2200Response.from_dict(community_get_leader_board2200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


