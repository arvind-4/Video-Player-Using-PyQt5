"""Tests for the play_video() toggle logic."""

from unittest.mock import MagicMock
from PyQt5.QtMultimedia import QMediaPlayer


class TestPlayVideo:
    """play_video toggles between play and pause."""

    def test_calls_play_when_stopped(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.play_video()
        player.media_player.play.assert_called_once()

    def test_calls_pause_when_already_playing(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.PlayingState
        player.play_video()
        player.media_player.pause.assert_called_once()

    def test_does_not_call_pause_when_stopped(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.play_video()
        player.media_player.pause.assert_not_called()

    def test_does_not_call_play_when_already_playing(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.PlayingState
        player.play_video()
        player.media_player.play.assert_not_called()

    def test_calls_play_when_paused(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.PausedState
        player.play_video()
        player.media_player.play.assert_called_once()

    def test_toggle_sequence_stopped_then_playing(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.play_video()
        player.media_player.play.assert_called_once()

        player.media_player.state.return_value = QMediaPlayer.PlayingState
        player.play_video()
        player.media_player.pause.assert_called_once()
