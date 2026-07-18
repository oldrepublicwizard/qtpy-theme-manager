# Theme setup notes

This package applies themes. Saving which theme the user last picked is your job.

## Discovery

`ThemeSources` controls where themes come from:

- `qrc_prefixes` — Qt resource prefixes for QSS (default `(":/themes",)`)
- `extra_theme_dirs` — folders of VS Code-style JSON themes

```python
from qtpy_theme_manager import ThemeManager, ThemeSources

sources = ThemeSources().with_extra_dirs("/path/to/extra_themes")
manager = ThemeManager(theme_sources=sources)
```

Built-in catalog themes still show up even if QRC is empty.

## Typical host wiring

1. Build a manager (optional: custom `theme_sources`, `on_theme_error`).
2. On startup, apply whatever you stored last time.
3. Open the selector; on `theme_changed` / `style_changed`, save settings and call `apply_theme_and_style`.

```python
manager = ThemeManager(theme_sources=my_sources)
manager.apply_theme_and_style(
    my_settings.selected_theme or "sourcegraph-dark",
    my_settings.selected_style or "Fusion",
    fallback_theme="sourcegraph-dark",
    fallback_style="Fusion",
)
```

If you used to keep theme keys somewhere else, migrate them once and drop the old keys.
