"""Reusable Qt theme manager, catalog, and selector dialog for host-owned settings."""

from qtpy_theme_manager.theme_apply import (
    apply_style,
    apply_tooltip_style_to_app,
    get_original_style,
    get_tooltip_stylesheet,
)
from qtpy_theme_manager.theme_catalog import build_builtin_theme_configs
from qtpy_theme_manager.theme_dialog import ThemeDialog
from qtpy_theme_manager.theme_manager import ThemeManager
from qtpy_theme_manager.theme_selector_dialog import ThemeSelectorDialog
from qtpy_theme_manager.theme_types import ThemeConfig, ThemeSources

__all__ = [
    "ThemeConfig",
    "ThemeDialog",
    "ThemeManager",
    "ThemeSelectorDialog",
    "ThemeSources",
    "apply_style",
    "apply_tooltip_style_to_app",
    "build_builtin_theme_configs",
    "get_original_style",
    "get_tooltip_stylesheet",
]
