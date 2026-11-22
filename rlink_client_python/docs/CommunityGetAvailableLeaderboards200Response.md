# CommunityGetAvailableLeaderboards200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**leaderboards** | [**List[CommunityLeaderboard]**](CommunityLeaderboard.md) |  | 
**match_types** | [**List[CommunityMatchType]**](CommunityMatchType.md) |  | 
**races** | [**List[CommunityRace]**](CommunityRace.md) |  | 
**factions** | [**List[CommunityFaction]**](CommunityFaction.md) | filled for AoM only. | 
**leaderboard_regions** | [**List[CommunityRegion]**](CommunityRegion.md) |  | 

## Example

```python
from rlink_client.models.community_get_available_leaderboards200_response import CommunityGetAvailableLeaderboards200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetAvailableLeaderboards200Response from a JSON string
community_get_available_leaderboards200_response_instance = CommunityGetAvailableLeaderboards200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetAvailableLeaderboards200Response.to_json())

# convert the object into a dict
community_get_available_leaderboards200_response_dict = community_get_available_leaderboards200_response_instance.to_dict()
# create an instance of CommunityGetAvailableLeaderboards200Response from a dict
community_get_available_leaderboards200_response_from_dict = CommunityGetAvailableLeaderboards200Response.from_dict(community_get_available_leaderboards200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


