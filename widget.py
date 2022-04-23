#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Python 3 Compatibility
from __future__ import division
from __future__ import print_function

<<<<<<< Updated upstream
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import Qt

    
class Dock(QtGui.QDockWidget):
=======
from PyQt6 import QtCore
from PyQt6 import QtGui

from PyQt6 import QtWidgets


class Dock(QtWidgets.QDockWidget):
>>>>>>> Stashed changes
    """ dock """
    def __init__(self, widget, title, lock=False):
        QtGui.QDockWidget.__init__(self, title)
        if lock:
            self.setTitleBarWidget(QtGui.QWidget())
            self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.setWidget(widget)

    def lock(self, state):
        if state:
            if self.isFloating():
                self.setTitleBarWidget(None)
                self.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
            else:
                self.setTitleBarWidget(QtGui.QWidget())
                self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        else:
            self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
            self.setTitleBarWidget(None)
            self.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
<<<<<<< Updated upstream
            
    
class Label(QtGui.QLabel):
=======


class Label(QtWidgets.QLabel):
>>>>>>> Stashed changes
    """ Label """
    def __init__(self, tooltip):
        QtGui.QLabel.__init__(self)
        self.setToolTip(tooltip)
<<<<<<< Updated upstream
        
    
class Button(QtGui.QToolButton):
=======


class Button(QtWidgets.QToolButton):
>>>>>>> Stashed changes
    """ button """
    def __init__(self, tooltip, icon, connection, checkable=False):
        QtGui.QToolButton.__init__(self)
        self.setToolTip(tooltip)
        self.setAutoRaise(True)
        self.setCheckable(checkable)
        if isinstance(icon, QtGui.QIcon):
            self.setIcon(icon)
        elif type(icon) is str:
            self.setIconSize(QtCore.QSize(24, 24)) 
            self.setIcon(QtGui.QIcon(QtGui.QPixmap(icon)))
        self.clicked.connect(connection)


class Background(QtGui.QPixmap):
    """ background of the scene"""
    def __init__(self, size, arg=16):
        QtGui.QPixmap.__init__(self, size)
        self.fill(QtGui.QColor(0, 0, 0, 0))
        if type(arg) is int and arg:
            p = QtGui.QPainter(self)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 30))
            bol = True
            for x in range(0, size.width(), arg):
                for y in range(0, size.height(), arg*2):
                    if bol:
                        p.fillRect (x, y, arg, arg, brush)
                    else:
                        p.fillRect (x, y+arg, arg, arg, brush)
                bol = not bol
        elif type(arg) is str:
            brush = QtGui.QBrush(QtGui.QPixmap(arg))
            p = QtGui.QPainter(self)
            p.fillRect (0, 0, size.width(), size.height(), brush)


class Viewer(QtGui.QScrollArea):
    """ QScrollArea you can move with midbutton"""
    resyzing = QtCore.pyqtSignal(tuple)
    def __init__ (self):
<<<<<<< Updated upstream
        QtGui.QScrollArea.__init__(self)
        
=======
        QtWidgets.QScrollArea.__init__(self)

>>>>>>> Stashed changes
    def event(self, event):
        """ capture middle mouse event to move the view """
        # clic: save position
        if   (event.type() == QtCore.QEvent.Type.MouseButtonPress and
              event.button() == QtCore.Qt.MidButton):
            self.mouseX, self.mouseY = event.x(), event.y()
            return True
        # drag: move the scrollbars
        elif (event.type() == QtCore.QEvent.MouseMove and
              event.buttons() == QtCore.Qt.MidButton):
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - (event.x() - self.mouseX))
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - (event.y() - self.mouseY))
            self.mouseX, self.mouseY = event.x(), event.y()
            return True
        elif (event.type() == QtCore.QEvent.Resize):
            self.resyzing.emit((event.size().width(), event.size().height()))
        return QtGui.QScrollArea.event(self, event)
