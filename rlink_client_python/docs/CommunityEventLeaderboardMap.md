# CommunityEventLeaderboardMap

One event ladder map of the AoM event block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communityevent_id** | **int** |  | 
**communityeventleaderboard_id** | **int** |  | 
**matchtype_id** | **int** |  | 
**statgroup_type** | **int** |  | 
**civilization_id** | **int** |  | 

## Example

```python
from rlink_client.models.community_event_leaderboard_map import CommunityEventLeaderboardMap

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityEventLeaderboardMap from a JSON string
community_event_leaderboard_map_instance = CommunityEventLeaderboardMap.from_json(json)
# print the JSON string representation of the object
print(CommunityEventLeaderboardMap.to_json())

# convert the object into a dict
community_event_leaderboard_map_dict = community_event_leaderboard_map_instance.to_dict()
# create an instance of CommunityEventLeaderboardMap from a dict
community_event_leaderboard_map_from_dict = CommunityEventLeaderboardMap.from_dict(community_event_leaderboard_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


