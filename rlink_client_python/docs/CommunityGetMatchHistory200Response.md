# CommunityGetMatchHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**match_history** | [**List[CommunityMatch]**](CommunityMatch.md) |  | 
**profiles** | [**List[CommunityProfile]**](CommunityProfile.md) |  | 

## Example

```python
from rlink_client.models.community_get_match_history200_response import CommunityGetMatchHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityGetMatchHistory200Response from a JSON string
community_get_match_history200_response_instance = CommunityGetMatchHistory200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityGetMatchHistory200Response.to_json())

# convert the object into a dict
community_get_match_history200_response_dict = community_get_match_history200_response_instance.to_dict()
# create an instance of CommunityGetMatchHistory200Response from a dict
community_get_match_history200_response_from_dict = CommunityGetMatchHistory200Response.from_dict(community_get_match_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


