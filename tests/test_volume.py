"""Tests for volume_changed() — label and value sync."""

import pytest


class TestVolumeChanged:
    """Volume label stays in sync with the slider value."""

    def test_label_updates_to_slider_value(self, player):
        player.volume_slider.setValue(50)
        player.volume_changed()
        assert player.volume_label.text() == "50"

    def test_label_updates_to_minimum(self, player):
        player.volume_slider.setValue(1)
        player.volume_changed()
        assert player.volume_label.text() == "1"

    def test_label_updates_to_maximum(self, player):
        player.volume_slider.setValue(100)
        player.volume_changed()
        assert player.volume_label.text() == "100"

    def test_value_attribute_is_set(self, player):
        player.volume_slider.setValue(42)
        player.volume_changed()
        assert player.value == 42

    @pytest.mark.parametrize("vol", [1, 25, 50, 75, 99, 100])
    def test_label_reflects_parametrized_values(self, player, vol):
        player.volume_slider.setValue(vol)
        player.volume_changed()
        assert player.volume_label.text() == str(vol)
