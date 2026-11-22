# SteamPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steamid** | **str** |  | [optional] 
**communityvisibilitystate** | **int** |  | [optional] 
**profilestate** | **int** |  | [optional] 
**personaname** | **str** |  | [optional] 
**profileurl** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**avatarmedium** | **str** |  | [optional] 
**avatarfull** | **str** |  | [optional] 
**avatarhash** | **str** |  | [optional] 
**personastate** | **int** |  | [optional] 
**realname** | **str** |  | [optional] 
**primaryclanid** | **str** |  | [optional] 
**timecreated** | **int** |  | [optional] 
**personastateflags** | **int** |  | [optional] 
**loccountrycode** | **str** |  | [optional] 

## Example

```python
from rlink_client.models.steam_player import SteamPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of SteamPlayer from a JSON string
steam_player_instance = SteamPlayer.from_json(json)
# print the JSON string representation of the object
print(SteamPlayer.to_json())

# convert the object into a dict
steam_player_dict = steam_player_instance.to_dict()
# create an instance of SteamPlayer from a dict
steam_player_from_dict = SteamPlayer.from_dict(steam_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


