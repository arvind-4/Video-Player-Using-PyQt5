"""Integration tests for signal–slot wiring."""

from unittest.mock import MagicMock
from PyQt5.QtMultimedia import QMediaPlayer


class TestSignalSlotWiring:
    """Verify UI signals are routed to the correct slots."""

    def test_play_button_click_calls_play(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.play_button.setEnabled(True)
        player.play_button.click()
        player.media_player.play.assert_called_once()

    def test_stop_button_click_calls_stop(self, player):
        player.media_player = MagicMock()
        player.stop_button.setEnabled(True)
        player.stop_button.click()
        player.media_player.stop.assert_called_once()

    def test_volume_slider_value_change_updates_label(self, player):
        player.volume_slider.setValue(33)
        assert player.volume_label.text() == "33"

    def test_slider_moved_sets_position(self, player):
        player.media_player = MagicMock()
        player.slider.setRange(0, 10_000)
        player.slider.sliderMoved.emit(7500)
        player.media_player.setPosition.assert_called_with(7500)

    def test_muted_checkbox_toggle_calls_set_muted(self, player):
        player.media_player = MagicMock()
        player.muted_checkbox.setEnabled(True)
        player.muted_checkbox.setChecked(True)
        player.media_player.setMuted.assert_called_with(True)
