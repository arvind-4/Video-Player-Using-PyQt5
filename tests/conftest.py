"""Shared fixtures for all VideoPlayer tests."""

import sys
import pytest
from PyQt5.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qapp():
    """Create a single QApplication for the entire test session."""
    app = QApplication.instance() or QApplication(sys.argv)
    yield app


@pytest.fixture
def player(qapp):
    """Return a fresh VideoPlayer instance for each test."""
    from src.main import VideoPlayer

    vp = VideoPlayer()
    yield vp
    vp.close()
