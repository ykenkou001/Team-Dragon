# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import *
from d_modules.ScreensCommnonFunc import *

class CancelScreen(QtWidgets.QWidget):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = SuperCancelScreen.SuperCancelScreen()
        self.ui.setupUi(self)