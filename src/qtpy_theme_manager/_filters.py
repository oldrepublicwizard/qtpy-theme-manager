"""Minimal NoScrollEventFilter for theme selector."""
from __future__ import annotations
from qtpy.QtCore import QObject, QEvent

class NoScrollEventFilter(QObject):
    def eventFilter(self, obj, event):  # noqa: N802
        if event.type() == QEvent.Type.Wheel:
            return True
        return super().eventFilter(obj, event)
