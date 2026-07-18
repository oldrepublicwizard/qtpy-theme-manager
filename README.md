# qtpy-theme-manager

Apply QSS / palette / style themes to a `QApplication`. Can scan QRC and VS Code-style JSON theme packs.

The host app owns persistence (what the user last picked). There's a short note in `THEME_MIGRATION.md` if you're moving an older theme setup over.

## Install

```bash
pip install git+https://github.com/oldrepublicwizard/qtpy-theme-manager.git
pip install qtpy PyQt5
```

```python
from qtpy_theme_manager import ThemeManager  # see package for exact symbols
```

Or grab a wheel from [Releases](https://github.com/oldrepublicwizard/qtpy-theme-manager/releases).

## License

LGPL-3.0-or-later
