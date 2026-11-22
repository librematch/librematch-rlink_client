# CommunityLeaderboardMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchtype_id** | **int** |  | 
**statgroup_type** | **int** |  | 
**civilization_id** | **int** | The official name of this field&#39;s family is race_id; the live service already answers civilization_id. | 

## Example

```python
from rlink_client.models.community_leaderboard_map import CommunityLeaderboardMap

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityLeaderboardMap from a JSON string
community_leaderboard_map_instance = CommunityLeaderboardMap.from_json(json)
# print the JSON string representation of the object
print(CommunityLeaderboardMap.to_json())

# convert the object into a dict
community_leaderboard_map_dict = community_leaderboard_map_instance.to_dict()
# create an instance of CommunityLeaderboardMap from a dict
community_leaderboard_map_from_dict = CommunityLeaderboardMap.from_dict(community_leaderboard_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


