"""Smoke import test."""

def test_import():
    import os
    os.environ.setdefault('QT_API', 'pyqt5')
    from qtpy_theme_manager import ThemeManager, ThemeSources
    assert ThemeManager is not None
