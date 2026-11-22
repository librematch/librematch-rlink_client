# CommunityMatchSummary

One lobby of /community/advertisement/findAdvertisements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**steamlobbyid** | **int** | Steam lobby id, 0 when the lobby is not on Steam.  | 
**goodoldgameslobbyid** | **int** | 0 when the ladder does not publish the value.  | 
**xboxsessionid** | **str** |  | 
**host_profile_id** | **int** |  | 
**state** | **int** |  | 
**description** | **str** |  | 
**visible** | **int** |  | 
**mapname** | **str** |  | 
**options** | **str** |  | 
**passwordprotected** | **int** | 1/0; lobby passwords are never exposed. | 
**maxplayers** | **int** |  | 
**slotinfo** | **str** |  | 
**matchtype_id** | **int** |  | 
**matchmembers** | [**List[CommunityMatchSummaryMember]**](CommunityMatchSummaryMember.md) |  | 
**observernum** | **int** |  | 
**observermax** | **int** |  | 
**isobservable** | **int** |  | 
**observerdelay** | **int** |  | 
**hasobserverpassword** | **int** | 1/0; the observer password is never exposed. | 
**servicetype** | **int** | 0/1 (LAN lobbies are 1). | 
**relayserver_region** | **str** |  | 

## Example

```python
from rlink_client.models.community_match_summary import CommunityMatchSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMatchSummary from a JSON string
community_match_summary_instance = CommunityMatchSummary.from_json(json)
# print the JSON string representation of the object
print(CommunityMatchSummary.to_json())

# convert the object into a dict
community_match_summary_dict = community_match_summary_instance.to_dict()
# create an instance of CommunityMatchSummary from a dict
community_match_summary_from_dict = CommunityMatchSummary.from_dict(community_match_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


