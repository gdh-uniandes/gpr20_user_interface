
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class IPWidget(QWidget):

  def __init__(self, parent):

    QWidget.__init__(self, parent)

    # Creates the label
    lb_ip = QLabel("VECTOR NETWORK ANALYZER IP ADDRESS")
    lb_ip.setAlignment(Qt.AlignCenter)

    # Creates the input line edits for IP field 0
    self.ip_edit_0 = QSpinBox()
    self.ip_edit_0.setRange(0, 255)
    self.ip_edit_0.setSingleStep(1)

    # Creates the input line edits for IP field 1
    self.ip_edit_1 = QSpinBox()
    self.ip_edit_1.setRange(0, 255)
    self.ip_edit_1.setSingleStep(1)

    # Creates the input line edits for IP field 2
    self.ip_edit_2 = QSpinBox()
    self.ip_edit_2.setRange(0, 255)
    self.ip_edit_2.setSingleStep(1)

    # Creates the input line edits for IP field 3
    self.ip_edit_3 = QSpinBox()
    self.ip_edit_3.setRange(0, 255)
    self.ip_edit_3.setSingleStep(1)

    # Creates a layout for the IP
    ly_ip = QHBoxLayout()
    ly_ip.addWidget(self.ip_edit_0)
    ly_ip.addWidget(self.ip_edit_1)
    ly_ip.addWidget(self.ip_edit_2)
    ly_ip.addWidget(self.ip_edit_3)

    # Initialize the layout for widget
    ly_widget = QVBoxLayout()
    ly_widget.addWidget(lb_ip)
    ly_widget.addLayout(ly_ip)
    
    # Set the layout for widget
    self.setLayout(ly_widget)


  def lock(self):
    self.ip_edit_0.setEnabled(False)
    self.ip_edit_1.setEnabled(False)
    self.ip_edit_2.setEnabled(False)
    self.ip_edit_3.setEnabled(False)


  def unlock(self):
    self.ip_edit_0.setEnabled(True)
    self.ip_edit_1.setEnabled(True)
    self.ip_edit_2.setEnabled(True)
    self.ip_edit_3.setEnabled(True)


  def update_step_size(self, step_size):
    """Update the step size on VNA's IP address fields.
    
    Args:
      step_size (int): new step size for a single increment.
    """
    self.ip_edit_0.setSingleStep(step_size)
    self.ip_edit_1.setSingleStep(step_size)
    self.ip_edit_2.setSingleStep(step_size)
    self.ip_edit_3.setSingleStep(step_size)
