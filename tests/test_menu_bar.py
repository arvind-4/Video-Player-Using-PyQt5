"""Tests for menu bar structure and actions."""


class TestMenuBar:
    """Menu bar contains the expected top-level menus and actions."""

    def test_file_menu_exists(self, player):
        titles = [a.text() for a in player.menuBar().actions()]
        assert "&File" in titles

    def test_preference_menu_exists(self, player):
        titles = [a.text() for a in player.menuBar().actions()]
        assert "&Preference" in titles

    def test_file_menu_has_open_action(self, player):
        file_menu = player.menuBar().actions()[0].menu()
        texts = [a.text() for a in file_menu.actions() if not a.isSeparator()]
        assert "Open..." in texts

    def test_file_menu_has_quit_action(self, player):
        file_menu = player.menuBar().actions()[0].menu()
        texts = [a.text() for a in file_menu.actions() if not a.isSeparator()]
        assert "Quit..." in texts

    def test_file_menu_has_separator(self, player):
        file_menu = player.menuBar().actions()[0].menu()
        separators = [a for a in file_menu.actions() if a.isSeparator()]
        assert len(separators) >= 1

    def test_preference_menu_has_play_action(self, player):
        pref_menu = player.menuBar().actions()[1].menu()
        texts = [a.text() for a in pref_menu.actions()]
        assert "Play" in texts

    def test_preference_menu_has_pause_action(self, player):
        pref_menu = player.menuBar().actions()[1].menu()
        texts = [a.text() for a in pref_menu.actions()]
        assert "Pause" in texts

    def test_preference_menu_has_stop_action(self, player):
        pref_menu = player.menuBar().actions()[1].menu()
        texts = [a.text() for a in pref_menu.actions()]
        assert "Stop" in texts

    def test_file_menu_action_count(self, player):
        file_menu = player.menuBar().actions()[0].menu()
        non_sep = [a for a in file_menu.actions() if not a.isSeparator()]
        assert len(non_sep) == 2  # Open, Quit

    def test_preference_menu_action_count(self, player):
        pref_menu = player.menuBar().actions()[1].menu()
        assert len(pref_menu.actions()) == 3  # Play, Pause, Stop
