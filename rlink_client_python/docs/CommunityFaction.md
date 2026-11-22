# CommunityFaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**locstringid** | **int** |  | 
**faction_id** | **int** |  | 

## Example

```python
from rlink_client.models.community_faction import CommunityFaction

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityFaction from a JSON string
community_faction_instance = CommunityFaction.from_json(json)
# print the JSON string representation of the object
print(CommunityFaction.to_json())

# convert the object into a dict
community_faction_dict = community_faction_instance.to_dict()
# create an instance of CommunityFaction from a dict
community_faction_from_dict = CommunityFaction.from_dict(community_faction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


