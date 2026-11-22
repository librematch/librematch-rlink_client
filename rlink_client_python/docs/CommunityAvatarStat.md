# CommunityAvatarStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | 
**avatarstat_id** | **int** |  | 
**value** | **int** |  | 
**lastupdated** | **int** |  | 

## Example

```python
from rlink_client.models.community_avatar_stat import CommunityAvatarStat

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityAvatarStat from a JSON string
community_avatar_stat_instance = CommunityAvatarStat.from_json(json)
# print the JSON string representation of the object
print(CommunityAvatarStat.to_json())

# convert the object into a dict
community_avatar_stat_dict = community_avatar_stat_instance.to_dict()
# create an instance of CommunityAvatarStat from a dict
community_avatar_stat_from_dict = CommunityAvatarStat.from_dict(community_avatar_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


