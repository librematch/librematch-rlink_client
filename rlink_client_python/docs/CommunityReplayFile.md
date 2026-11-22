# CommunityReplayFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** | Profile that uploaded the replay.  | 
**matchhistory_id** | **int** |  | 
**url** | **str** | Plain LAN URL without a SAS signature. | 
**size** | **int** |  | 
**datatype** | **int** | 0 or 1 (replay kind). | 

## Example

```python
from rlink_client.models.community_replay_file import CommunityReplayFile

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityReplayFile from a JSON string
community_replay_file_instance = CommunityReplayFile.from_json(json)
# print the JSON string representation of the object
print(CommunityReplayFile.to_json())

# convert the object into a dict
community_replay_file_dict = community_replay_file_instance.to_dict()
# create an instance of CommunityReplayFile from a dict
community_replay_file_from_dict = CommunityReplayFile.from_dict(community_replay_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


