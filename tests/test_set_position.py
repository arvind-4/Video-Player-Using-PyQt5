"""Tests for set_position() — forwards slider value to media player."""

import pytest
from unittest.mock import MagicMock


class TestSetPosition:
    """set_position forwards the value to media_player.setPosition()."""

    def test_calls_set_position(self, player):
        player.media_player = MagicMock()
        player.set_position(1234)
        player.media_player.setPosition.assert_called_once_with(1234)

    def test_set_position_zero(self, player):
        player.media_player = MagicMock()
        player.set_position(0)
        player.media_player.setPosition.assert_called_once_with(0)

    def test_set_position_large_value(self, player):
        player.media_player = MagicMock()
        player.set_position(99_999_999)
        player.media_player.setPosition.assert_called_once_with(99_999_999)

    def test_called_exactly_once(self, player):
        player.media_player = MagicMock()
        player.set_position(500)
        assert player.media_player.setPosition.call_count == 1

    @pytest.mark.parametrize("pos", [0, 500, 10_000, 99_999_999])
    def test_parametrized_positions(self, player, pos):
        player.media_player = MagicMock()
        player.set_position(pos)
        player.media_player.setPosition.assert_called_once_with(pos)
