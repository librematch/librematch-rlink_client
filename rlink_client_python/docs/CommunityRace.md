# CommunityRace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**faction_id** | **int** |  | 
**locstringid** | **int** |  | 
**localized_name** | **str** |  | [optional] 

## Example

```python
from rlink_client.models.community_race import CommunityRace

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityRace from a JSON string
community_race_instance = CommunityRace.from_json(json)
# print the JSON string representation of the object
print(CommunityRace.to_json())

# convert the object into a dict
community_race_dict = community_race_instance.to_dict()
# create an instance of CommunityRace from a dict
community_race_from_dict = CommunityRace.from_dict(community_race_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


