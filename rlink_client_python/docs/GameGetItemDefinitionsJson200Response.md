# GameGetItemDefinitionsJson200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **int** |  | 
**item_categories** | **List[object]** |  | [optional] 
**item_definitions** | **List[object]** |  | [optional] 
**data_signature** | **str** | the 344-char dataSignature. | 

## Example

```python
from rlink_client.models.game_get_item_definitions_json200_response import GameGetItemDefinitionsJson200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GameGetItemDefinitionsJson200Response from a JSON string
game_get_item_definitions_json200_response_instance = GameGetItemDefinitionsJson200Response.from_json(json)
# print the JSON string representation of the object
print(GameGetItemDefinitionsJson200Response.to_json())

# convert the object into a dict
game_get_item_definitions_json200_response_dict = game_get_item_definitions_json200_response_instance.to_dict()
# create an instance of GameGetItemDefinitionsJson200Response from a dict
game_get_item_definitions_json200_response_from_dict = GameGetItemDefinitionsJson200Response.from_dict(game_get_item_definitions_json200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


