# CommunityGetInventoryByProfileIDs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**item_instances_by_profile_id** | **List[Dict[str, List[object]]]** |  | 

## Example

```python
from rlink_client.models.community_get_inventory_by_profile_ids200_response import CommunityGetInventoryByProfileIDs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetInventoryByProfileIDs200Response from a JSON string
community_get_inventory_by_profile_ids200_response_instance = CommunityGetInventoryByProfileIDs200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetInventoryByProfileIDs200Response.to_json())

# convert the object into a dict
community_get_inventory_by_profile_ids200_response_dict = community_get_inventory_by_profile_ids200_response_instance.to_dict()
# create an instance of CommunityGetInventoryByProfileIDs200Response from a dict
community_get_inventory_by_profile_ids200_response_from_dict = CommunityGetInventoryByProfileIDs200Response.from_dict(community_get_inventory_by_profile_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


