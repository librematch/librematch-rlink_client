# CommunityMatchMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchhistory_id** | **int** |  | 
**profile_id** | **int** |  | 
**civilization_id** | **int** |  | 
**statgroup_id** | **int** |  | 
**teamid** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**streak** | **int** |  | 
**arbitration** | **int** |  | 
**outcome** | **int** |  | 
**oldrating** | **int** |  | 
**newrating** | **int** |  | 
**reporttype** | **int** |  | 

## Example

```python
from rlink_client.models.community_match_member import CommunityMatchMember

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMatchMember from a JSON string
community_match_member_instance = CommunityMatchMember.from_json(json)
# print the JSON string representation of the object
print(CommunityMatchMember.to_json())

# convert the object into a dict
community_match_member_dict = community_match_member_instance.to_dict()
# create an instance of CommunityMatchMember from a dict
community_match_member_from_dict = CommunityMatchMember.from_dict(community_match_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


