# CommunityRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**locstringid** | **int** |  | 
**localized_name** | **str** |  | [optional] 

## Example

```python
from rlink_client.models.community_region import CommunityRegion

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityRegion from a JSON string
community_region_instance = CommunityRegion.from_json(json)
# print the JSON string representation of the object
print(CommunityRegion.to_json())

# convert the object into a dict
community_region_dict = community_region_instance.to_dict()
# create an instance of CommunityRegion from a dict
community_region_from_dict = CommunityRegion.from_dict(community_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


