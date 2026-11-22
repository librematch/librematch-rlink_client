# CommunityAchievementDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Numeric or string catalogue id. | 
**name** | **str** |  | 
**name_locstringid** | **int** | Localisation id of the name, -1 when the text travels verbatim.  | 
**description_locstringid** | **int** | -1 when the ladder does not publish the value.  | 
**icon** | **str** |  | 
**timemodified** | **int** |  | 
**deleted** | **int** | Rows with deleted !&#x3D; 0 are not served. | 
**itembundle_id** | **int** | -1 when the catalogue row carries no bundle. | 

## Example

```python
from rlink_client.models.community_achievement_definition import CommunityAchievementDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityAchievementDefinition from a JSON string
community_achievement_definition_instance = CommunityAchievementDefinition.from_json(json)
# print the JSON string representation of the object
print(CommunityAchievementDefinition.to_json())

# convert the object into a dict
community_achievement_definition_dict = community_achievement_definition_instance.to_dict()
# create an instance of CommunityAchievementDefinition from a dict
community_achievement_definition_from_dict = CommunityAchievementDefinition.from_dict(community_achievement_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


