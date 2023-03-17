# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.community_news_get_news import Api

from rlink_client.paths import PathValues

path = PathValues.COMMUNITY_NEWS_GET_NEWS
