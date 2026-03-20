"""Tests for duration_changed() — slider range tracks media duration."""

import pytest


class TestDurationChanged:
    """Slider range updates when media duration changes."""

    def test_slider_max_updated(self, player):
        player.duration_changed(9000)
        assert player.slider.maximum() == 9000

    def test_slider_min_stays_zero(self, player):
        player.duration_changed(9000)
        assert player.slider.minimum() == 0

    def test_zero_duration(self, player):
        player.duration_changed(0)
        assert player.slider.minimum() == 0
        assert player.slider.maximum() == 0

    def test_large_duration(self, player):
        player.duration_changed(3_600_000)  # 1 hour in ms
        assert player.slider.maximum() == 3_600_000

    @pytest.mark.parametrize("dur", [0, 1000, 60_000, 3_600_000])
    def test_parametrized_durations(self, player, dur):
        player.duration_changed(dur)
        assert player.slider.maximum() == dur
        assert player.slider.minimum() == 0
