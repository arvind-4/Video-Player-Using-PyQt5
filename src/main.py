"""Video player."""

import pathlib
import sys

from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QColor, QIcon, QKeySequence, QPalette
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSlider,
    QStyle,
    QVBoxLayout,
    QWidget,
)

ROOT = pathlib.Path(__file__).parent.parent


class VideoPlayer(QMainWindow):
    """Video player class."""

    def __init__(self) -> None:
        """Initialize the video player."""
        super().__init__()
        self.main()

    def main(self) -> None:
        """Initialize the UI and media player."""
        self._setup_palette()
        self._setup_media_player()
        self._setup_menu()
        self._setup_ui()
        self._connect_signals()

    def _setup_palette(self) -> None:
        """Set the palette of the application."""
        self.p = self.palette()
        self.p.setColor(QPalette.Window, Qt.black)
        self.setPalette(self.p)

    def _setup_media_player(self) -> None:
        """Set the media player of the application."""
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

    def _setup_menu(self) -> None:
        """Set the menu of the application."""
        file_menu = self.menuBar().addMenu("&File")
        open_action = QAction(QIcon(str(ROOT / "images/open.png")), "Open...", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        file_menu.addSeparator()

        quit_action = QAction(QIcon(str(ROOT / "images/close.png")), "Quit...", self)
        quit_action.setShortcut(QKeySequence.Close)
        quit_action.triggered.connect(self.quit_function)
        file_menu.addAction(quit_action)

        pref_menu = self.menuBar().addMenu("&Preference")

        play_action = QAction(QIcon(str(ROOT / "images/play.png")), "Play", self)
        play_action.triggered.connect(self.play_video)
        pref_menu.addAction(play_action)

        pause_action = QAction(QIcon(str(ROOT / "images/pause.png")), "Pause", self)
        pause_action.triggered.connect(self.media_player.pause)
        pref_menu.addAction(pause_action)

        stop_action = QAction(QIcon(str(ROOT / "images/stop.png")), "Stop", self)
        stop_action.triggered.connect(self.media_player.stop)
        pref_menu.addAction(stop_action)

    def _setup_ui(self) -> None:
        """Set the UI of the application."""
        self.video_widget = QVideoWidget()

        self.play_button = QPushButton()
        self.play_button.setEnabled(False)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        self.stop_button = QPushButton()
        self.stop_button.setEnabled(False)
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(1, 100)
        self.volume_slider.setValue(70)
        self.volume_slider.setEnabled(False)

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        self.volume_label = QLabel("70")

        self.muted_checkbox = QCheckBox()
        self.muted_checkbox.setEnabled(False)
        self.muted_checkbox.setIcon(
            self.style().standardIcon(QStyle.SP_MediaVolumeMuted)
        )

        self._setup_layout()

    def _setup_layout(self) -> None:
        """Set the layout of the UI."""
        wid = QWidget(self)
        self.setCentralWidget(wid)

        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.slider)
        control_layout.addWidget(self.volume_label)
        control_layout.addWidget(self.volume_slider)
        control_layout.addWidget(self.muted_checkbox)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addLayout(control_layout)

        wid.setLayout(layout)

    def _connect_signals(self) -> None:
        """Connect the signals of the UI."""
        self.play_button.clicked.connect(self.play_video)
        self.stop_button.clicked.connect(self.stop_function)
        self.slider.sliderMoved.connect(self.set_position)

        self.volume_slider.sliderMoved.connect(self.media_player.setVolume)
        self.volume_slider.valueChanged.connect(self.volume_changed)

        self.muted_checkbox.toggled.connect(self.muted_checking)

        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.stateChanged.connect(self.logo_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

    def open_file(self) -> None:
        """Open the file."""
        self.fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Open",
            ".",
            "Files (*.mp4 *.flv *.ts *.mts *.avi *.wav *.mp3 *.mkv)",
            QDir.homePath(),
        )

        if self.fileName != "":
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.fileName)))
            self.play_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.muted_checkbox.setEnabled(True)
            self.volume_slider.setEnabled(True)
            self.play_video()

    def play_video(self) -> None:
        """Play the media player."""
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()

        else:
            self.media_player.play()

    def logo_changed(self) -> None:
        """Change the logo of the media player."""
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def volume_changed(self) -> None:
        """Set the volume of the media player."""
        self.value = self.volume_slider.value()
        self.volume_label.setText(str(self.value))

    def muted_checking(self) -> None:
        """Check the mute status of the media player."""
        if self.muted_checkbox.isChecked():
            self.media_player.setMuted(True)
        else:
            self.media_player.setMuted(False)

    def stop_function(self) -> None:
        """Stop the media player."""
        self.media_player.stop()

    def quit_function(self) -> None:
        """Quit the application."""
        sys.exit(app.exec_())

    def position_changed(self, position: int) -> None:
        """Set the position of the media player."""
        self.slider.setValue(position)

    def duration_changed(self, duration: int) -> None:
        """Set the duration of the media player."""
        self.slider.setRange(0, duration)

    def set_position(self, position: int) -> None:
        """Set the position of the media player."""
        self.media_player.setPosition(position)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Media Player --Arvind")
    app.setWindowIcon(QIcon(str(ROOT / "images/icon.png")))
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(192, 192, 192))
    palette.setColor(QPalette.WindowText, Qt.yellow)
    palette.setColor(QPalette.Base, QColor(255, 255, 0))
    palette.setColor(QPalette.AlternateBase, QColor(64, 128, 128))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.darkMagenta)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, QColor(255, 128, 128))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; "
        "background-color: #2a82da; "
        "border: 1px solid white; }"
    )
    player = VideoPlayer()
    player.resize(480, 360)
    player.show()
    sys.exit(app.exec_())
