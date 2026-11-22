# CommunityReportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchhistory_id** | **int** |  | 
**profile_id** | **int** |  | 
**resulttype** | **int** |  | 
**teamid** | **int** |  | 
**civilization_id** | **int** |  | 
**xpgained** | **int** |  | 
**counters** | **str** | JSON object string, \&quot;{}\&quot; when empty. | 
**customupdates** | **str** | JSON object string with itemUpdates/challengeUpdates/eventChallengeUpdates/clientUpdates. | 
**matchstartdate** | **int** |  | 

## Example

```python
from rlink_client.models.community_report_result import CommunityReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityReportResult from a JSON string
community_report_result_instance = CommunityReportResult.from_json(json)
# print the JSON string representation of the object
print(CommunityReportResult.to_json())

# convert the object into a dict
community_report_result_dict = community_report_result_instance.to_dict()
# create an instance of CommunityReportResult from a dict
community_report_result_from_dict = CommunityReportResult.from_dict(community_report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


