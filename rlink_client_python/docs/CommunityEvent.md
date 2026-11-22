# CommunityEvent

One event of /community/CommunityEvent/getAvailableCommunityEvents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A4 rolling seasons (RankedSeasonEventIDBase + offset) or the AoM catalogue id. | 
**name** | **str** |  | 
**start** | **int** | Unix seconds. | 
**end** | **int** | Unix seconds. | 
**expiry_time** | **int** | Unix seconds. | 
**scheduledstarttime** | **int** |  | [optional] 
**scheduledendtime** | **int** |  | [optional] 
**scheduledexpirytime** | **int** |  | [optional] 
**actualstarttime** | **int** |  | [optional] 
**actualendtime** | **int** |  | [optional] 
**customdata** | **str** | JSON string carried verbatim (season metadata, AoM daily challenge config). | 
**eventstate** | **int** | State of the event: 1 running, 2 finished.  | 
**eventtype** | **int** | Type of the event: A4 rolling seasons 6, AoM daily 2 / pantheon 3.  | 
**localized_name** | **str** | Same as name (omitted when empty). | [optional] 

## Example

```python
from rlink_client.models.community_event import CommunityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityEvent from a JSON string
community_event_instance = CommunityEvent.from_json(json)
# print the JSON string representation of the object
print(CommunityEvent.to_json())

# convert the object into a dict
community_event_dict = community_event_instance.to_dict()
# create an instance of CommunityEvent from a dict
community_event_from_dict = CommunityEvent.from_dict(community_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


