# CommunityLeaderboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**isranked** | **int** |  | 
**leaderboardmap** | [**List[CommunityLeaderboardMap]**](CommunityLeaderboardMap.md) |  | 

## Example

```python
from rlink_client.models.community_leaderboard import CommunityLeaderboard

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityLeaderboard from a JSON string
community_leaderboard_instance = CommunityLeaderboard.from_json(json)
# print the JSON string representation of the object
print(CommunityLeaderboard.to_json())

# convert the object into a dict
community_leaderboard_dict = community_leaderboard_instance.to_dict()
# create an instance of CommunityLeaderboard from a dict
community_leaderboard_from_dict = CommunityLeaderboard.from_dict(community_leaderboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


