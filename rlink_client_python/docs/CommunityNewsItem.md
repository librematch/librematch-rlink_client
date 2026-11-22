# CommunityNewsItem

11 named fields. `newstitle_locstringid`, `newssubtitle_locstringid` and `newstext_locstringid` are the localisation ids of the translated strings (-1 when the entry carries no localised text). AoM maps the catalogue image slot to newsimage and the other titles to the headline slot. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Numeric or string, as declared in news.toml. | 
**hidden** | **int** |  | 
**newscategory** | **str** |  | 
**newstitle_locstringid** | **int** |  | 
**newssubtitle_locstringid** | **int** |  | 
**newstext_locstringid** | **int** |  | 
**newsimage** | **str** |  | 
**newsbody** | **str** |  | 
**metadata** | **str** |  | 
**datevisible** | **int** |  | 
**expirytime** | **int** |  | 

## Example

```python
from rlink_client.models.community_news_item import CommunityNewsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityNewsItem from a JSON string
community_news_item_instance = CommunityNewsItem.from_json(json)
# print the JSON string representation of the object
print(CommunityNewsItem.to_json())

# convert the object into a dict
community_news_item_dict = community_news_item_instance.to_dict()
# create an instance of CommunityNewsItem from a dict
community_news_item_from_dict = CommunityNewsItem.from_dict(community_news_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


