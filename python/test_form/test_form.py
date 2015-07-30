# Copyright (c) 2015 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Test form demonstrating the various 
"""

import sgtk
from sgtk.platform.qt import QtCore, QtGui

from ..views import GroupedListView
from ..overlay_widget import ShotgunOverlayWidget, ShotgunModelOverlayWidget
from ..spinner_widget import SpinnerWidget
from ..search_widget import SearchWidget
from ..elided_label import ElidedLabel
from ..navigation import NavigationWidget, BreadcrumbWidget, Breadcrumb

from .ui.test_form import Ui_TestForm

def show_test_form():
    """
    """
    try:
        bundle = sgtk.platform.current_bundle()
        bundle.engine.show_dialog("Framework QtWidgets Test", bundle, TestForm)
    except:
        app.log_exception("Failed to create dialog for framework test form!")

class TestForm(QtGui.QWidget):
    """
    """
    def __init__(self, parent=None):
        """
        """
        QtGui.QWidget.__init__(self, parent)

        # set up the UI
        self._ui = Ui_TestForm()
        self._ui.setupUi(self)
        
        # navigation & breadcrumbs:
        