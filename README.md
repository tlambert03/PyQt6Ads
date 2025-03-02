# PyQt6Ads

[![License](https://img.shields.io/pypi/l/PyQt6Ads.svg?color=green)](https://github.com/pyapp-kit/PyQt6Ads/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/PyQt6Ads.svg?color=green)](https://pypi.org/project/PyQt6Ads)
[![Python Version](https://img.shields.io/pypi/pyversions/PyQt6Ads.svg?color=green)](https://python.org)
[![Build](https://github.com/pyapp-kit/PyQt6Ads/actions/workflows/pypi.yml/badge.svg)](https://github.com/pyapp-kit/PyQt6Ads/actions/workflows/pypi.yml)

PyQt6 Bindings for (the amazing)
[Qt-Advanced-Docking-System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System)

[![Video Advanced
Docking](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/blob/483bb7354ace8f07b76f483ec167e84467ac3977/doc/advanced-docking_video.png)](https://www.youtube.com/watch?v=7pdNfafg3Qc)

## Installation

```sh
pip install PyQt6Ads
```

## Usage

Please see [documentation in the upstream
repo](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/blob/master/doc/user-guide.md).

See also [examples in this repo](./examples/).

The autogenerated type stubs are also useful for understanding the API.

### Minimal Example

```python
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QAction
import PyQt6Ads as ads


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # create the dock manager
        # If the parent is a QMainWindow, DockManager sets itself as the central widget.
        self.dock_manager = ads.CDockManager(self)

        # create an example widget to place inside the dock widget
        lbl = QLabel()
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        lbl.setText("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.")

        # create a dock widget with the title "Label 1"
        # and set the created label as the dock widget content
        dw = ads.CDockWidget("Label 1")
        dw.setWidget(lbl)

        # add the toggleViewAction of the dock widget to the menu
        # to give the user the possibility to show the dock widget if it has been closed
        self.menuView = self.menuBar().addMenu("View")
        self.menuView.addAction(dw.toggleViewAction())

        # add the dock widget to the top dock widget area
        self.dock_manager.addDockWidget(ads.DockWidgetArea.TopDockWidgetArea, dw)
```

## Alternatives

- **For PySide6**: See <https://github.com/mborgerson/pyside6_qtads>
- **For PyQt5**: See <https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System#pyqt5> (in the upstream repo)
