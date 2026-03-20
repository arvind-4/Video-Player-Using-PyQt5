"""Edge cases and boundary condition tests."""

from unittest.mock import MagicMock
from PyQt5.QtMultimedia import QMediaPlayer


class TestEdgeCases:
    def test_slider_min_never_exceeds_max(self, player):
        player.duration_changed(0)
        assert player.slider.minimum() <= player.slider.maximum()

    def test_position_at_boundary_zero(self, player):
        player.slider.setRange(0, 5000)
        player.position_changed(0)
        assert player.slider.value() == 0

    def test_volume_boundary_minimum(self, player):
        player.volume_slider.setValue(1)
        player.volume_changed()
        assert player.volume_label.text() == "1"

    def test_volume_boundary_maximum(self, player):
        player.volume_slider.setValue(100)
        player.volume_changed()
        assert player.volume_label.text() == "100"

    def test_repeated_stop_calls(self, player):
        player.media_player = MagicMock()
        for _ in range(5):
            player.stop_function()
        assert player.media_player.stop.call_count == 5

    def test_set_position_called_multiple_times(self, player):
        player.media_player = MagicMock()
        for pos in [0, 100, 200, 500]:
            player.set_position(pos)
        assert player.media_player.setPosition.call_count == 4

    def test_play_then_stop_sequence(self, player):
        player.media_player = MagicMock()
        player.media_player.state.return_value = QMediaPlayer.StoppedState
        player.play_video()
        player.media_player.play.assert_called_once()
        player.stop_function()
        player.media_player.stop.assert_called_once()

    def test_duration_then_position_update(self, player):
        player.duration_changed(10_000)
        player.position_changed(5_000)
        assert player.slider.maximum() == 10_000
        assert player.slider.value() == 5_000

    def test_mute_unmute_cycle(self, player):
        """setChecked drives the signal — no manual muted_checking() calls needed."""
        player.media_player = MagicMock()
        expected = [True, False, True, False]
        for state in expected:
            player.muted_checkbox.setChecked(state)
        calls = [c[0][0] for c in player.media_player.setMuted.call_args_list]
        assert calls == expected
