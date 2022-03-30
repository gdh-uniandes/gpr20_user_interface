
from PyQt5.QtWidgets import *


class StartWidget(QWidget):

    def __init__(self, parent):

        QWidget.__init__(self, parent)

        # Creates the start button
        self.bt_start = QPushButton("START")
        self.bt_start.clicked.connect(self.parent().start_survey)
        self.bt_start.setObjectName("bt_start")

        # Creates the stop button
        self.bt_stop = QPushButton("STOP")
        self.bt_stop.clicked.connect(self.parent().stop_survey)
        self.bt_stop.setObjectName("bt_stop")
        self.bt_stop.setEnabled(False)

        # Defines the layout and adds widgets
        ly_start = QHBoxLayout()
        ly_start.addWidget(self.bt_start)
        ly_start.addWidget(self.bt_stop)

        # Sets the layout
        self.setLayout(ly_start)

    def lock(self, on_survey=False):
        self.bt_start.setEnabled(False)
        self.bt_stop.setEnabled(on_survey)

    def unlock(self, on_survey=False):
        self.bt_start.setEnabled(not on_survey)
        self.bt_stop.setEnabled(on_survey)
