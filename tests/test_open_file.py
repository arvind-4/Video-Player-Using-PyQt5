"""Tests for open_file() — file dialog, controls, and playback start."""

import pytest
from unittest.mock import MagicMock, patch
from PyQt5.QtMultimedia import QMediaPlayer


class TestOpenFile:
    """open_file() enables controls and starts playback when a path is chosen."""

    def _patch_dialog(self, path: str):
        return patch("src.main.QFileDialog.getOpenFileName", return_value=(path, ""))

    def test_controls_enabled_after_open(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        with self._patch_dialog("/fake/video.mp4"):
            player.open_file()
        assert player.play_button.isEnabled() is True
        assert player.stop_button.isEnabled() is True
        assert player.muted_checkbox.isEnabled() is True
        assert player.volume_slider.isEnabled() is True

    def test_set_media_called(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        with self._patch_dialog("/fake/video.mp4"):
            player.open_file()
        player.media_player.setMedia.assert_called_once()

    def test_play_called_after_open(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        with self._patch_dialog("/fake/video.mp4"):
            player.open_file()
        player.media_player.play.assert_called_once()

    def test_empty_path_does_not_enable_controls(self, player):
        player.media_player = MagicMock()
        with self._patch_dialog(""):
            player.open_file()
        assert player.play_button.isEnabled() is False
        assert player.stop_button.isEnabled() is False

    def test_empty_path_does_not_call_set_media(self, player):
        player.media_player = MagicMock()
        with self._patch_dialog(""):
            player.open_file()
        player.media_player.setMedia.assert_not_called()

    def test_empty_path_does_not_call_play(self, player):
        player.media_player = MagicMock()
        with self._patch_dialog(""):
            player.open_file()
        player.media_player.play.assert_not_called()

    def test_filename_stored(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        with self._patch_dialog("/fake/clip.mkv"):
            player.open_file()
        assert player.fileName == "/fake/clip.mkv"

    @pytest.mark.parametrize(
        "fmt", ["video.mp4", "audio.mp3", "movie.mkv", "clip.avi", "song.wav"]
    )
    def test_supported_formats_store_filename(self, player, fmt):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        with self._patch_dialog(f"/fake/{fmt}"):
            player.open_file()
        assert player.fileName == f"/fake/{fmt}"
