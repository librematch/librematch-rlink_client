# CommunityResult

Envelope of every /community response. A bad `title` query parameter is answered with the code-2 envelope over HTTP 200.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 0 success, 2 invalid request (including a title the service does not serve).  | 
**message** | **str** |  | 

## Example

```python
from rlink_client.models.community_result import CommunityResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityResult from a JSON string
community_result_instance = CommunityResult.from_json(json)
# print the JSON string representation of the object
print(CommunityResult.to_json())

# convert the object into a dict
community_result_dict = community_result_instance.to_dict()
# create an instance of CommunityResult from a dict
community_result_from_dict = CommunityResult.from_dict(community_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


