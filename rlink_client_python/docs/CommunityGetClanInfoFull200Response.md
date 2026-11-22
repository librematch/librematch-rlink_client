# CommunityGetClanInfoFull200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**clan** | **object** |  | 

## Example

```python
from rlink_client.models.community_get_clan_info_full200_response import CommunityGetClanInfoFull200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetClanInfoFull200Response from a JSON string
community_get_clan_info_full200_response_instance = CommunityGetClanInfoFull200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetClanInfoFull200Response.to_json())

# convert the object into a dict
community_get_clan_info_full200_response_dict = community_get_clan_info_full200_response_instance.to_dict()
# create an instance of CommunityGetClanInfoFull200Response from a dict
community_get_clan_info_full200_response_from_dict = CommunityGetClanInfoFull200Response.from_dict(community_get_clan_info_full200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


