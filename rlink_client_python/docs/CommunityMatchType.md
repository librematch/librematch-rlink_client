# CommunityMatchType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**locstringid** | **int** | Localisation id of the name, -1 when the catalogue carries the text verbatim.  | 
**localized_name** | **str** |  | [optional] 

## Example

```python
from rlink_client.models.community_match_type import CommunityMatchType

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMatchType from a JSON string
community_match_type_instance = CommunityMatchType.from_json(json)
# print the JSON string representation of the object
print(CommunityMatchType.to_json())

# convert the object into a dict
community_match_type_dict = community_match_type_instance.to_dict()
# create an instance of CommunityMatchType from a dict
community_match_type_from_dict = CommunityMatchType.from_dict(community_match_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


