"""Tests for quit_function()."""

from unittest.mock import MagicMock, patch


class TestQuitFunction:
    """quit_function calls sys.exit with the app's exec_() return value.

    quit_function() references the module-level `app` which only exists when
    the script is run as __main__. Inject it with patch.object(..., create=True).
    """

    def test_quit_calls_sys_exit(self, player):
        import src.main as main_module

        mock_app = MagicMock()
        mock_app.exec_.return_value = 0
        with patch.object(main_module, "app", mock_app, create=True):
            with patch("sys.exit") as mock_exit:
                player.quit_function()
        mock_exit.assert_called_once()

    def test_quit_passes_exec_return_value_to_exit(self, player):
        import src.main as main_module

        mock_app = MagicMock()
        mock_app.exec_.return_value = 42
        with patch.object(main_module, "app", mock_app, create=True):
            with patch("sys.exit") as mock_exit:
                player.quit_function()
        mock_exit.assert_called_once_with(42)
