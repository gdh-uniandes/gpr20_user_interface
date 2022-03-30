

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class StepSelectorWidget(QWidget):

  def __init__(self, parent):

    # Initializes the super class
    QWidget.__init__(self, parent)

    # Creates the label
    lb_step_size = QLabel("STEP SIZE SELECTOR")
    lb_step_size.setAlignment(Qt.AlignCenter)
    lb_step_size.setObjectName("lb_step_size")

    # Creates the first button
    self.bt_step_0 = QPushButton("100")
    self.bt_step_0.setObjectName("bt_step_size")
    self.bt_step_0.setCheckable(True)

    self.bt_step_1 = QPushButton("10")
    self.bt_step_1.setObjectName("bt_step_size")
    self.bt_step_1.setCheckable(True)

    self.bt_step_2 = QPushButton("1")
    self.bt_step_2.setObjectName("bt_step_size")
    self.bt_step_2.setCheckable(True)
    self.bt_step_2.setChecked(True)

    # Creates the button group
    bt_group = QButtonGroup(self)
    bt_group.setExclusive(True)
    bt_group.addButton(self.bt_step_0, 100)
    bt_group.addButton(self.bt_step_1, 10)
    bt_group.addButton(self.bt_step_2, 1)

    # Connects the butttons to slot
    bt_group.buttonClicked[int].connect(self.parent().step_size_change)

    # Adds label and buttons to layout
    ly_buttons = QHBoxLayout()
    ly_buttons.addWidget(self.bt_step_0)
    ly_buttons.addWidget(self.bt_step_1)
    ly_buttons.addWidget(self.bt_step_2)

    # Create the layout for widget
    ly_widget = QVBoxLayout()
    ly_widget.addWidget(lb_step_size)
    ly_widget.addLayout(ly_buttons)

    # Sets widget layout
    self.setLayout(ly_widget)


  def lock(self):
    """Locks the panel from being changed"""

    self.bt_step_0.setEnabled(False)
    self.bt_step_1.setEnabled(False)
    self.bt_step_2.setEnabled(False)


  def unlock(self):
    """Unlocks the panel for an user to interact"""
    
    self.bt_step_0.setEnabled(True)
    self.bt_step_1.setEnabled(True)
    self.bt_step_2.setEnabled(True)
