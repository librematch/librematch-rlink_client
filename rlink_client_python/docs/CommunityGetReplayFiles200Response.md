# CommunityGetReplayFiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**expiry_unix** | **int** |  | 
**replay_files** | [**List[CommunityReplayFile]**](CommunityReplayFile.md) |  | 

## Example

```python
from rlink_client.models.community_get_replay_files200_response import CommunityGetReplayFiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetReplayFiles200Response from a JSON string
community_get_replay_files200_response_instance = CommunityGetReplayFiles200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetReplayFiles200Response.to_json())

# convert the object into a dict
community_get_replay_files200_response_dict = community_get_replay_files200_response_instance.to_dict()
# create an instance of CommunityGetReplayFiles200Response from a dict
community_get_replay_files200_response_from_dict = CommunityGetReplayFiles200Response.from_dict(community_get_replay_files200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


