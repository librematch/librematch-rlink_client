# SteamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SteamResponseResponse**](SteamResponseResponse.md) |  | [optional] 

## Example

```python
from rlink_client.models.steam_response import SteamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SteamResponse from a JSON string
steam_response_instance = SteamResponse.from_json(json)
# print the JSON string representation of the object
print(SteamResponse.to_json())

# convert the object into a dict
steam_response_dict = steam_response_instance.to_dict()
# create an instance of SteamResponse from a dict
steam_response_from_dict = SteamResponse.from_dict(steam_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


