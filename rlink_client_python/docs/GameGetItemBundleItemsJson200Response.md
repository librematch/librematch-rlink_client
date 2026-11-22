# GameGetItemBundleItemsJson200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **int** |  | 
**item_bundles** | **List[object]** |  | [optional] 
**data_signature** | **str** |  | 

## Example

```python
from rlink_client.models.game_get_item_bundle_items_json200_response import GameGetItemBundleItemsJson200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GameGetItemBundleItemsJson200Response from a JSON string
game_get_item_bundle_items_json200_response_instance = GameGetItemBundleItemsJson200Response.from_json(json)
# print the JSON string representation of the object
print(GameGetItemBundleItemsJson200Response.to_json())

# convert the object into a dict
game_get_item_bundle_items_json200_response_dict = game_get_item_bundle_items_json200_response_instance.to_dict()
# create an instance of GameGetItemBundleItemsJson200Response from a dict
game_get_item_bundle_items_json200_response_from_dict = GameGetItemBundleItemsJson200Response.from_dict(game_get_item_bundle_items_json200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


