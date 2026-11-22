# CommunityLeaderboardStat

18 fields, the shape the live service returns (the wiki documents 14). `regionrank`, `regionranktotal`, `highestrank` and `highestranklevel` are the regional standing and the peak of the player. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statgroup_id** | **int** |  | 
**leaderboard_id** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**streak** | **int** | Positive for a winning streak, negative for a losing one. | 
**disputes** | **int** | 0 when the ladder does not publish the value.  | 
**drops** | **int** | 0 when the ladder does not publish the value.  | 
**rank** | **int** | -1 when the profile holds no rank. | 
**ranktotal** | **int** | Number of players in the ladder; -1 unknown ladder, 0 empty.  | 
**ranklevel** | **int** |  | 
**rating** | **int** |  | 
**regionrank** | **int** | Rank of the player inside the region.  | 
**regionranktotal** | **int** | -1 when the ladder does not publish the value.  | 
**lastmatchdate** | **int** |  | 
**highestrank** | **int** | Peak rank of the player.  | 
**highestranklevel** | **int** | 0 when the ladder does not publish the value.  | 
**highestrating** | **int** |  | 
**metadata** | **str** |  | 

## Example

```python
from rlink_client.models.community_leaderboard_stat import CommunityLeaderboardStat

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityLeaderboardStat from a JSON string
community_leaderboard_stat_instance = CommunityLeaderboardStat.from_json(json)
# print the JSON string representation of the object
print(CommunityLeaderboardStat.to_json())

# convert the object into a dict
community_leaderboard_stat_dict = community_leaderboard_stat_instance.to_dict()
# create an instance of CommunityLeaderboardStat from a dict
community_leaderboard_stat_from_dict = CommunityLeaderboardStat.from_dict(community_leaderboard_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


