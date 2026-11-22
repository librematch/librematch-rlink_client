# CommunityMatchSummaryMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** |  | 
**profile_id** | **int** |  | 
**ranking** | **int** | -1 when the ladder does not publish the value.  | 
**statgroup_id** | **int** |  | 
**civilization_id** | **int** |  | 
**teamid** | **int** |  | 

## Example

```python
from rlink_client.models.community_match_summary_member import CommunityMatchSummaryMember

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMatchSummaryMember from a JSON string
community_match_summary_member_instance = CommunityMatchSummaryMember.from_json(json)
# print the JSON string representation of the object
print(CommunityMatchSummaryMember.to_json())

# convert the object into a dict
community_match_summary_member_dict = community_match_summary_member_instance.to_dict()
# create an instance of CommunityMatchSummaryMember from a dict
community_match_summary_member_from_dict = CommunityMatchSummaryMember.from_dict(community_match_summary_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


