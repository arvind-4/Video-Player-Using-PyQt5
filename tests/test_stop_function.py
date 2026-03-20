"""Tests for the stop_function() method."""

from unittest.mock import MagicMock


class TestStopFunction:
    """stop_function delegates directly to media_player.stop()."""

    def test_calls_media_player_stop(self, player):
        player.media_player = MagicMock()
        player.stop_function()
        player.media_player.stop.assert_called_once()

    def test_does_not_call_play(self, player):
        player.media_player = MagicMock()
        player.stop_function()
        player.media_player.play.assert_not_called()

    def test_does_not_call_pause(self, player):
        player.media_player = MagicMock()
        player.stop_function()
        player.media_player.pause.assert_not_called()

    def test_stop_called_exactly_once(self, player):
        player.media_player = MagicMock()
        player.stop_function()
        assert player.media_player.stop.call_count == 1
