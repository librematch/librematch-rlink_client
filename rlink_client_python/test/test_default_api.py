# coding: utf-8

"""
    Relic Link API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2022.11.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_community_clan_find(self):
        """Test case for community_clan_find"""
        pass

    def test_community_find_advertisements(self):
        """Test case for community_find_advertisements"""
        pass

    def test_community_get_achievements(self):
        """Test case for community_get_achievements"""
        pass

    def test_community_get_available_achievements(self):
        """Test case for community_get_available_achievements"""
        pass

    def test_community_get_available_community_events(self):
        """Test case for community_get_available_community_events"""
        pass

    def test_community_get_available_leaderboards(self):
        """Test case for community_get_available_leaderboards"""
        pass

    def test_community_get_avatar_stat_for_profile(self):
        """Test case for community_get_avatar_stat_for_profile"""
        pass

    def test_community_get_clan_info_full(self):
        """Test case for community_get_clan_info_full"""
        pass

    def test_community_get_inventory_by_profile_ids(self):
        """Test case for community_get_inventory_by_profile_ids"""
        pass

    def test_community_get_leaderboard2(self):
        """Test case for community_get_leaderboard2"""
        pass

    def test_community_get_personal_stat(self):
        """Test case for community_get_personal_stat"""
        pass

    def test_community_get_recent_match_history(self):
        """Test case for community_get_recent_match_history"""
        pass

    def test_community_news(self):
        """Test case for community_news"""
        pass

    def test_community_proxy_steam_user_request(self):
        """Test case for community_proxy_steam_user_request"""
        pass

    def test_game_account_find_profiles(self):
        """Test case for game_account_find_profiles"""
        pass

    def test_game_account_find_profiles_by_platform_id(self):
        """Test case for game_account_find_profiles_by_platform_id"""
        pass

    def test_game_account_get_profile_name(self):
        """Test case for game_account_get_profile_name"""
        pass

    def test_game_account_get_profile_property(self):
        """Test case for game_account_get_profile_property"""
        pass

    def test_game_account_set_avatar_metadata(self):
        """Test case for game_account_set_avatar_metadata"""
        pass

    def test_game_account_set_language(self):
        """Test case for game_account_set_language"""
        pass

    def test_game_achievement_get_achievements(self):
        """Test case for game_achievement_get_achievements"""
        pass

    def test_game_achievement_get_available_achievements(self):
        """Test case for game_achievement_get_available_achievements"""
        pass

    def test_game_achievement_sync_stats(self):
        """Test case for game_achievement_sync_stats"""
        pass

    def test_game_advertisement_find_advertisements(self):
        """Test case for game_advertisement_find_advertisements"""
        pass

    def test_game_advertisement_find_observable_advertisements_get(self):
        """Test case for game_advertisement_find_observable_advertisements_get"""
        pass

    def test_game_advertisement_find_observable_advertisements_post(self):
        """Test case for game_advertisement_find_observable_advertisements_post"""
        pass

    def test_game_advertisement_get_advertisements(self):
        """Test case for game_advertisement_get_advertisements"""
        pass

    def test_game_advertisement_get_lan_advertisements(self):
        """Test case for game_advertisement_get_lan_advertisements"""
        pass

    def test_game_advertisement_host(self):
        """Test case for game_advertisement_host"""
        pass

    def test_game_advertisement_join(self):
        """Test case for game_advertisement_join"""
        pass

    def test_game_advertisement_leave(self):
        """Test case for game_advertisement_leave"""
        pass

    def test_game_advertisement_start_observing(self):
        """Test case for game_advertisement_start_observing"""
        pass

    def test_game_advertisement_stop_observing(self):
        """Test case for game_advertisement_stop_observing"""
        pass

    def test_game_advertisement_update(self):
        """Test case for game_advertisement_update"""
        pass

    def test_game_advertisement_update_platform_lobby_id(self):
        """Test case for game_advertisement_update_platform_lobby_id"""
        pass

    def test_game_advertisement_update_state(self):
        """Test case for game_advertisement_update_state"""
        pass

    def test_game_advertisement_update_tags(self):
        """Test case for game_advertisement_update_tags"""
        pass

    def test_game_automatch2_get_automatch_map(self):
        """Test case for game_automatch2_get_automatch_map"""
        pass

    def test_game_automatch2_polling(self):
        """Test case for game_automatch2_polling"""
        pass

    def test_game_automatch2_stop_polling(self):
        """Test case for game_automatch2_stop_polling"""
        pass

    def test_game_automatch2_update_status(self):
        """Test case for game_automatch2_update_status"""
        pass

    def test_game_automatch_get_automatch_map(self):
        """Test case for game_automatch_get_automatch_map"""
        pass

    def test_game_challenge_get_challenge_progress(self):
        """Test case for game_challenge_get_challenge_progress"""
        pass

    def test_game_challenge_get_challenge_progress_by_profile_id(self):
        """Test case for game_challenge_get_challenge_progress_by_profile_id"""
        pass

    def test_game_challenge_get_challenges(self):
        """Test case for game_challenge_get_challenges"""
        pass

    def test_game_challenge_update_progress_batched(self):
        """Test case for game_challenge_update_progress_batched"""
        pass

    def test_game_chat_delete_offline_message(self):
        """Test case for game_chat_delete_offline_message"""
        pass

    def test_game_chat_get_chat_channels(self):
        """Test case for game_chat_get_chat_channels"""
        pass

    def test_game_chat_get_offline_messages(self):
        """Test case for game_chat_get_offline_messages"""
        pass

    def test_game_clan_apply(self):
        """Test case for game_clan_apply"""
        pass

    def test_game_clan_create(self):
        """Test case for game_clan_create"""
        pass

    def test_game_clan_disband(self):
        """Test case for game_clan_disband"""
        pass

    def test_game_clan_find(self):
        """Test case for game_clan_find"""
        pass

    def test_game_clan_get_clan(self):
        """Test case for game_clan_get_clan"""
        pass

    def test_game_clan_get_clan_info_full(self):
        """Test case for game_clan_get_clan_info_full"""
        pass

    def test_game_clan_update(self):
        """Test case for game_clan_update"""
        pass

    def test_game_cloud_get_file_url_get(self):
        """Test case for game_cloud_get_file_url_get"""
        pass

    def test_game_cloud_get_file_url_post(self):
        """Test case for game_cloud_get_file_url_post"""
        pass

    def test_game_cloud_get_temp_credentials(self):
        """Test case for game_cloud_get_temp_credentials"""
        pass

    def test_game_community_event_get_available_community_events(self):
        """Test case for game_community_event_get_available_community_events"""
        pass

    def test_game_community_event_get_event_challenge_progress(self):
        """Test case for game_community_event_get_event_challenge_progress"""
        pass

    def test_game_community_event_get_event_stats(self):
        """Test case for game_community_event_get_event_stats"""
        pass

    def test_game_invitation_cancel_invitation(self):
        """Test case for game_invitation_cancel_invitation"""
        pass

    def test_game_invitation_extend_invitation(self):
        """Test case for game_invitation_extend_invitation"""
        pass

    def test_game_item_detach_items(self):
        """Test case for game_item_detach_items"""
        pass

    def test_game_item_get_inventory_by_profile_ids(self):
        """Test case for game_item_get_inventory_by_profile_ids"""
        pass

    def test_game_item_get_item_bundle_items_json(self):
        """Test case for game_item_get_item_bundle_items_json"""
        pass

    def test_game_item_get_item_definitions_json(self):
        """Test case for game_item_get_item_definitions_json"""
        pass

    def test_game_item_get_item_loadouts(self):
        """Test case for game_item_get_item_loadouts"""
        pass

    def test_game_item_get_item_prices(self):
        """Test case for game_item_get_item_prices"""
        pass

    def test_game_item_get_level_rewards_table_json(self):
        """Test case for game_item_get_level_rewards_table_json"""
        pass

    def test_game_item_get_personalized_sale_items(self):
        """Test case for game_item_get_personalized_sale_items"""
        pass

    def test_game_item_get_scheduled_sale_and_items(self):
        """Test case for game_item_get_scheduled_sale_and_items"""
        pass

    def test_game_item_move_charges(self):
        """Test case for game_item_move_charges"""
        pass

    def test_game_item_move_item(self):
        """Test case for game_item_move_item"""
        pass

    def test_game_item_open_item_pack(self):
        """Test case for game_item_open_item_pack"""
        pass

    def test_game_item_sign_item(self):
        """Test case for game_item_sign_item"""
        pass

    def test_game_item_update_item_attributes(self):
        """Test case for game_item_update_item_attributes"""
        pass

    def test_game_leaderboard_get_available_leaderboards(self):
        """Test case for game_leaderboard_get_available_leaderboards"""
        pass

    def test_game_leaderboard_get_leaderboard(self):
        """Test case for game_leaderboard_get_leaderboard"""
        pass

    def test_game_leaderboard_get_party_stat(self):
        """Test case for game_leaderboard_get_party_stat"""
        pass

    def test_game_leaderboard_get_personal_stat(self):
        """Test case for game_leaderboard_get_personal_stat"""
        pass

    def test_game_leaderboard_get_recent_match_history_get(self):
        """Test case for game_leaderboard_get_recent_match_history_get"""
        pass

    def test_game_leaderboard_get_recent_match_history_post(self):
        """Test case for game_leaderboard_get_recent_match_history_post"""
        pass

    def test_game_leaderboard_get_recent_match_single_player_history(self):
        """Test case for game_leaderboard_get_recent_match_single_player_history"""
        pass

    def test_game_leaderboard_get_stat_groups_by_profile_ids(self):
        """Test case for game_leaderboard_get_stat_groups_by_profile_ids"""
        pass

    def test_game_leaderboard_get_stats_for_leaderboard_by_profile_name(self):
        """Test case for game_leaderboard_get_stats_for_leaderboard_by_profile_name"""
        pass

    def test_game_leaderboard_set_avatar_stat_values(self):
        """Test case for game_leaderboard_set_avatar_stat_values"""
        pass

    def test_game_login_logout(self):
        """Test case for game_login_logout"""
        pass

    def test_game_login_platform_login(self):
        """Test case for game_login_platform_login"""
        pass

    def test_game_login_read_session(self):
        """Test case for game_login_read_session"""
        pass

    def test_game_news_get_news(self):
        """Test case for game_news_get_news"""
        pass

    def test_game_party_create_or_report_single_player(self):
        """Test case for game_party_create_or_report_single_player"""
        pass

    def test_game_party_finalize_replay_upload(self):
        """Test case for game_party_finalize_replay_upload"""
        pass

    def test_game_party_peer_add(self):
        """Test case for game_party_peer_add"""
        pass

    def test_game_party_peer_update(self):
        """Test case for game_party_peer_update"""
        pass

    def test_game_party_report_match(self):
        """Test case for game_party_report_match"""
        pass

    def test_game_party_send_match_chat(self):
        """Test case for game_party_send_match_chat"""
        pass

    def test_game_playerreport_report_user(self):
        """Test case for game_playerreport_report_user"""
        pass

    def test_game_relationship_clear_relationship(self):
        """Test case for game_relationship_clear_relationship"""
        pass

    def test_game_relationship_get_presence_data(self):
        """Test case for game_relationship_get_presence_data"""
        pass

    def test_game_relationship_get_relationships(self):
        """Test case for game_relationship_get_relationships"""
        pass

    def test_game_relationship_ignore(self):
        """Test case for game_relationship_ignore"""
        pass

    def test_game_relationship_set_presence(self):
        """Test case for game_relationship_set_presence"""
        pass

    def test_game_relationship_set_presence_property(self):
        """Test case for game_relationship_set_presence_property"""
        pass


if __name__ == "__main__":
    unittest.main()
