# CommunityEventLeaderboard

One event ladder of the AoM event block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communityevent_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**isranked** | **int** |  | 
**scoringtype** | **int** |  | 

## Example

```python
from rlink_client.models.community_event_leaderboard import CommunityEventLeaderboard

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityEventLeaderboard from a JSON string
community_event_leaderboard_instance = CommunityEventLeaderboard.from_json(json)
# print the JSON string representation of the object
print(CommunityEventLeaderboard.to_json())

# convert the object into a dict
community_event_leaderboard_dict = community_event_leaderboard_instance.to_dict()
# create an instance of CommunityEventLeaderboard from a dict
community_event_leaderboard_from_dict = CommunityEventLeaderboard.from_dict(community_event_leaderboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


