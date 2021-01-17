from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import warnings
from HGB_project.HGenBO_pre import XWindows
import sys
import matplotlib
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
app = QApplication(sys.argv)

xwin = XWindows()
app.exec_()
