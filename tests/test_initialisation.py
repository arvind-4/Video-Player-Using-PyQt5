"""Tests for widget creation and initial state."""

from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtMultimediaWidgets import QVideoWidget


class TestInitialisation:
    """Verify every widget is created with the correct initial state."""

    def test_player_is_qmainwindow(self, player):
        assert isinstance(player, QMainWindow)

    def test_media_player_created(self, player):
        assert player.media_player is not None

    def test_video_widget_created(self, player):
        assert isinstance(player.video_widget, QVideoWidget)

    def test_play_button_created_and_disabled(self, player):
        assert player.play_button is not None
        assert player.play_button.isEnabled() is False

    def test_stop_button_created_and_disabled(self, player):
        assert player.stop_button is not None
        assert player.stop_button.isEnabled() is False

    def test_slider_initial_range(self, player):
        assert player.slider.minimum() == 0
        assert player.slider.maximum() == 0

    def test_volume_slider_range(self, player):
        assert player.volume_slider.minimum() == 1
        assert player.volume_slider.maximum() == 100

    def test_volume_slider_default_value(self, player):
        assert player.volume_slider.value() == 70

    def test_volume_slider_initially_disabled(self, player):
        assert player.volume_slider.isEnabled() is False

    def test_volume_label_initial_text(self, player):
        assert player.volume_label.text() == "70"

    def test_muted_checkbox_initially_disabled(self, player):
        assert player.muted_checkbox.isEnabled() is False

    def test_muted_checkbox_initially_unchecked(self, player):
        assert player.muted_checkbox.isChecked() is False

    def test_label_widget_created(self, player):
        assert isinstance(player.label, QLabel)

    def test_player_has_central_widget(self, player):
        assert player.centralWidget() is not None
