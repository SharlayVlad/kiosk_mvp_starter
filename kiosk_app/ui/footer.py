
from __future__ import annotations

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QSizePolicy, QWidget


class Footer(QWidget):
    DEFAULT_NOTE = "для навигации используйте сенсорный экран"

    def __init__(self, theme: dict, navigation_text: str | None = None, qr_text: str = "") -> None:
        super().__init__()
        self.setStyleSheet(
            f"background:{theme['footer_bg']}; color:{theme['muted']};"
            f"border-top:1px solid {theme['border']};"
        )

        self.note = QLabel(navigation_text or self.DEFAULT_NOTE)
        self.note.setAlignment(Qt.AlignCenter)
        self.note.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.note.setStyleSheet("font-size:18px; font-weight:600; background: transparent;")

        self.qr = QLabel()
        self.qr.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.qr.setMinimumSize(88, 88)
        self.qr.setStyleSheet("background: transparent;")
        self.qr.setVisible(False)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(24, 12, 24, 12)
        layout.setSpacing(12)
        layout.addStretch(1)
        layout.addWidget(self.note, 0, Qt.AlignVCenter)
        layout.addStretch(1)
        layout.addWidget(self.qr, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.set_qr(qr_text)

    def set_qr(self, text: str) -> None:
        self.qr.clear()
        text = (text or "").strip()
        if not text:
            self.qr.setVisible(False)
            return
        try:
            import qrcode
            from PIL.ImageQt import ImageQt

            img = qrcode.make(text)
            qim = ImageQt(img)
            pix = QPixmap.fromImage(qim)
            self.qr.setPixmap(
                pix.scaled(QSize(88, 88), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
            self.qr.setVisible(True)
        except Exception:
            self.qr.setVisible(False)

