# CommunityProfile

The /community object form of a profile: `xp` and `level` are the progression of the account, `country` its country and `clanlist_name` its clan (empty when the player has none). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | 
**name** | **str** | Platform identity, &#x60;/steam/&lt;id&gt;&#x60; or &#x60;/xboxlive/&lt;id&gt;&#x60;. | 
**alias** | **str** |  | 
**personal_statgroup_id** | **int** |  | 
**xp** | **int** |  | 
**level** | **int** |  | 
**leaderboardregion_id** | **int** |  | 
**country** | **str** | Country of the account, empty when it is unknown.  | 
**clanlist_name** | **str** | Clan of the player, empty when the player has none.  | 

## Example

```python
from rlink_client.models.community_profile import CommunityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityProfile from a JSON string
community_profile_instance = CommunityProfile.from_json(json)
# print the JSON string representation of the object
print(CommunityProfile.to_json())

# convert the object into a dict
community_profile_dict = community_profile_instance.to_dict()
# create an instance of CommunityProfile from a dict
community_profile_from_dict = CommunityProfile.from_dict(community_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


