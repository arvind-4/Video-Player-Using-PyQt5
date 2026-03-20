"""Tests for position_changed() — slider tracks playback position."""

import pytest


class TestPositionChanged:
    """Slider position mirrors the media player position."""

    def test_slider_set_to_position(self, player):
        player.slider.setRange(0, 10_000)
        player.position_changed(5000)
        assert player.slider.value() == 5000

    def test_slider_set_to_zero(self, player):
        player.slider.setRange(0, 10_000)
        player.position_changed(0)
        assert player.slider.value() == 0

    def test_slider_set_to_end(self, player):
        player.slider.setRange(0, 10_000)
        player.position_changed(10_000)
        assert player.slider.value() == 10_000

    @pytest.mark.parametrize("pos", [0, 1000, 5000, 9999, 10_000])
    def test_slider_parametrized_positions(self, player, pos):
        player.slider.setRange(0, 10_000)
        player.position_changed(pos)
        assert player.slider.value() == pos
