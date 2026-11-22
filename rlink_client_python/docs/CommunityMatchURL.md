# CommunityMatchURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | 
**url** | **str** |  | 
**size** | **int** |  | 
**datatype** | **int** | 0 or 1 (replay kind). | 

## Example

```python
from rlink_client.models.community_match_url import CommunityMatchURL

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMatchURL from a JSON string
community_match_url_instance = CommunityMatchURL.from_json(json)
# print the JSON string representation of the object
print(CommunityMatchURL.to_json())

# convert the object into a dict
community_match_url_dict = community_match_url_instance.to_dict()
# create an instance of CommunityMatchURL from a dict
community_match_url_from_dict = CommunityMatchURL.from_dict(community_match_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


