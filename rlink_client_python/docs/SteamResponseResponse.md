# SteamResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[SteamPlayer]**](SteamPlayer.md) | Steam profiles the request resolved.  | [optional] 

## Example

```python
from rlink_client.models.steam_response_response import SteamResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SteamResponseResponse from a JSON string
steam_response_response_instance = SteamResponseResponse.from_json(json)
# print the JSON string representation of the object
print(SteamResponseResponse.to_json())

# convert the object into a dict
steam_response_response_dict = steam_response_response_instance.to_dict()
# create an instance of SteamResponseResponse from a dict
steam_response_response_from_dict = SteamResponseResponse.from_dict(steam_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


