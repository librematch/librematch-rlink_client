# CommunityFindAdvertisements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CommunityResult**](CommunityResult.md) |  | 
**matches** | [**List[CommunityMatchSummary]**](CommunityMatchSummary.md) |  | 
**avatars** | [**List[CommunityProfile]**](CommunityProfile.md) |  | 

## Example

```python
from rlink_client.models.community_find_advertisements200_response import CommunityFindAdvertisements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityFindAdvertisements200Response from a JSON string
community_find_advertisements200_response_instance = CommunityFindAdvertisements200Response.from_json(json)
# print the JSON string representation of the object
print(CommunityFindAdvertisements200Response.to_json())

# convert the object into a dict
community_find_advertisements200_response_dict = community_find_advertisements200_response_instance.to_dict()
# create an instance of CommunityFindAdvertisements200Response from a dict
community_find_advertisements200_response_from_dict = CommunityFindAdvertisements200Response.from_dict(community_find_advertisements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


