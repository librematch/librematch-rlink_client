# CommunityEarnedAchievement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievement_id** | **int** |  | [optional] 
**achieveddate** | **int** |  | [optional] 

## Example

```python
from rlink_client.models.community_earned_achievement import CommunityEarnedAchievement

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityEarnedAchievement from a JSON string
community_earned_achievement_instance = CommunityEarnedAchievement.from_json(json)
# print the JSON string representation of the object
print(CommunityEarnedAchievement.to_json())

# convert the object into a dict
community_earned_achievement_dict = community_earned_achievement_instance.to_dict()
# create an instance of CommunityEarnedAchievement from a dict
community_earned_achievement_from_dict = CommunityEarnedAchievement.from_dict(community_earned_achievement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


