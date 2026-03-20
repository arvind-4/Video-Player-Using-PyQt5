"""Tests for logo_changed() — play button icon switching."""

from unittest.mock import MagicMock
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QStyle


class TestLogoChanged:
    """Play button icon switches to Pause during playback and back otherwise."""

    def _icon_image(self, player, sp_icon):
        """Return QImage of a standard icon for pixel-data comparison."""
        return player.style().standardIcon(sp_icon).pixmap(32).toImage()

    def test_icon_is_pause_when_playing(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.PlayingState
        player.logo_changed()
        assert player.play_button.icon().pixmap(32).toImage() == self._icon_image(
            player, QStyle.SP_MediaPause
        )

    def test_icon_is_play_when_stopped(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.logo_changed()
        assert player.play_button.icon().pixmap(32).toImage() == self._icon_image(
            player, QStyle.SP_MediaPlay
        )

    def test_icon_is_play_when_paused(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.PausedState
        player.logo_changed()
        assert player.play_button.icon().pixmap(32).toImage() == self._icon_image(
            player, QStyle.SP_MediaPlay
        )

    def test_icon_toggles_correctly(self, player):
        player.media_player = MagicMock()

        player.media_player.state.return_value = QMediaPlayer.PlayingState
        player.logo_changed()
        assert player.play_button.icon().pixmap(32).toImage() == self._icon_image(
            player, QStyle.SP_MediaPause
        )

        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.logo_changed()
        assert player.play_button.icon().pixmap(32).toImage() == self._icon_image(
            player, QStyle.SP_MediaPlay
        )
