# CommunityMatch

One match row of the /community match-history endpoints (`gamemod_id` is 1800 on getMatchHistory and 0 on getRecentMatchHistory).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**creator_profile_id** | **int** |  | 
**mapname** | **str** |  | 
**maxplayers** | **int** |  | 
**matchtype_id** | **int** |  | 
**options** | **str** | Base64+zlib block echoed verbatim. | 
**slotinfo** | **str** | Base64+zlib block echoed verbatim. | 
**description** | **str** | \&quot;AUTOMATCH\&quot; for a rated or queued match. | 
**startgametime** | **int** |  | 
**completiontime** | **int** |  | 
**observertotal** | **int** | Observers the match had.  | 
**matchhistoryreportresults** | [**List[CommunityReportResult]**](CommunityReportResult.md) |  | 
**matchhistoryitems** | **List[object]** | Per-player rows of the match.  | 
**matchurls** | [**List[CommunityMatchURL]**](CommunityMatchURL.md) |  | 
**matchhistorymember** | [**List[CommunityMatchMember]**](CommunityMatchMember.md) |  | 
**gamemod_id** | **int** | 1800 on getMatchHistory, 0 on getRecentMatchHistory (live-service behaviour). | 

## Example

```python
from rlink_client.models.community_match import CommunityMatch

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMatch from a JSON string
community_match_instance = CommunityMatch.from_json(json)
# print the JSON string representation of the object
print(CommunityMatch.to_json())

# convert the object into a dict
community_match_dict = community_match_instance.to_dict()
# create an instance of CommunityMatch from a dict
community_match_from_dict = CommunityMatch.from_dict(community_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


