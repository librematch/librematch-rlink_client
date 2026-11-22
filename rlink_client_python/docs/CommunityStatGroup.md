# CommunityStatGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **int** | 1 for a player stat group, 2 for a clan one.  | 
**members** | [**List[CommunityProfile]**](CommunityProfile.md) |  | 

## Example

```python
from rlink_client.models.community_stat_group import CommunityStatGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityStatGroup from a JSON string
community_stat_group_instance = CommunityStatGroup.from_json(json)
# print the JSON string representation of the object
print(CommunityStatGroup.to_json())

# convert the object into a dict
community_stat_group_dict = community_stat_group_instance.to_dict()
# create an instance of CommunityStatGroup from a dict
community_stat_group_from_dict = CommunityStatGroup.from_dict(community_stat_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


