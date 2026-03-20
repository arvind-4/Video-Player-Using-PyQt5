"""Tests for muted_checking() — mute/unmute via checkbox.

Key rule: setChecked() fires the `toggled` signal which already calls
muted_checking() via the connected slot. Never call it manually.
"""

from unittest.mock import MagicMock


class TestMutedChecking:
    def test_mute_set_when_checkbox_checked(self, player):
        player.media_player = MagicMock()
        player.muted_checkbox.setChecked(True)  # signal fires → slot
        player.media_player.setMuted.assert_called_once_with(True)

    def test_mute_cleared_when_checkbox_unchecked(self, player):
        player.media_player = MagicMock()
        # Silently pre-check so unchecking actually fires toggled
        player.muted_checkbox.blockSignals(True)
        player.muted_checkbox.setChecked(True)
        player.muted_checkbox.blockSignals(False)

        player.muted_checkbox.setChecked(False)  # signal fires → slot
        player.media_player.setMuted.assert_called_once_with(False)

    def test_toggling_twice_ends_unmuted(self, player):
        player.media_player = MagicMock()
        player.muted_checkbox.setChecked(True)  # setMuted(True)
        player.muted_checkbox.setChecked(False)  # setMuted(False)
        assert player.media_player.setMuted.call_args == ((False,),)

    def test_set_muted_called_exactly_once_per_setChecked(self, player):
        player.media_player = MagicMock()
        player.muted_checkbox.setChecked(True)
        assert player.media_player.setMuted.call_count == 1

    def test_multiple_toggles_correct_call_count(self, player):
        player.media_player = MagicMock()
        for _ in range(5):
            player.muted_checkbox.setChecked(True)  # +1
            player.muted_checkbox.setChecked(False)  # +1
        assert player.media_player.setMuted.call_count == 10
