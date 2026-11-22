# CommunityGetAvailableCommunityEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**community_events** | [**List[CommunityEvent]**](CommunityEvent.md) |  | 
**leaderboards** | [**List[CommunityEventLeaderboard]**](CommunityEventLeaderboard.md) | event ladders (AoM only; omitted when empty). | [optional] 
**leaderboard_maps** | [**List[CommunityEventLeaderboardMap]**](CommunityEventLeaderboardMap.md) | event ladder maps (AoM only; omitted when empty). | [optional] 

## Example

```python
from rlink_client.models.community_get_available_community_events200_response import CommunityGetAvailableCommunityEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetAvailableCommunityEvents200Response from a JSON string
community_get_available_community_events200_response_instance = CommunityGetAvailableCommunityEvents200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetAvailableCommunityEvents200Response.to_json())

# convert the object into a dict
community_get_available_community_events200_response_dict = community_get_available_community_events200_response_instance.to_dict()
# create an instance of CommunityGetAvailableCommunityEvents200Response from a dict
community_get_available_community_events200_response_from_dict = CommunityGetAvailableCommunityEvents200Response.from_dict(community_get_available_community_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


