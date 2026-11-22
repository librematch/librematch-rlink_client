# CommunityFindClans200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**clans** | **List[object]** |  | 

## Example

```python
from rlink_client.models.community_find_clans200_response import CommunityFindClans200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityFindClans200Response from a JSON string
community_find_clans200_response_instance = CommunityFindClans200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityFindClans200Response.to_json())

# convert the object into a dict
community_find_clans200_response_dict = community_find_clans200_response_instance.to_dict()
# create an instance of CommunityFindClans200Response from a dict
community_find_clans200_response_from_dict = CommunityFindClans200Response.from_dict(community_find_clans200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


