"""Tests for palette / colour setup."""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


class TestPaletteSetup:
    """Palette colour is applied to the window."""

    def test_window_palette_colour_is_black(self, player):
        colour = player.palette().color(QPalette.Window)
        assert colour == Qt.black

    def test_palette_object_stored(self, player):
        assert player.p is not None
