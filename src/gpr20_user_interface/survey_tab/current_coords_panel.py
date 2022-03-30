

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class CurrentCoordsPanel(QWidget):

  def __init__(self, parent):

    # Initializes the super class
    QWidget.__init__(self, parent)

    # Creates the panel layout
    ly_coords = QGridLayout()

    # Creates labels for each axis
    lb_x_axis = QLabel("X-COORD: ")
    lb_y_axis = QLabel("Y-COORD: ")
    lb_z_axis = QLabel("Z-COORD: ")

    # Adds labels to layout
    ly_coords.addWidget(QLabel("CURRENT COORDINATES"), 0, 0, 1, 2, Qt.AlignCenter)
    ly_coords.addWidget(lb_x_axis, 1, 0)
    ly_coords.addWidget(lb_y_axis, 2, 0)
    ly_coords.addWidget(lb_z_axis, 3, 0)

    # Creates line edits to display current coordinates
    self.le_x_axis = QLineEdit()
    self.le_x_axis.setEnabled(False)

    self.le_y_axis = QLineEdit()
    self.le_y_axis.setEnabled(False)

    self.le_z_axis = QLineEdit()
    self.le_z_axis.setEnabled(False)

    # Adds line edits to layout
    ly_coords.addWidget(self.le_x_axis, 1, 1)
    ly_coords.addWidget(self.le_y_axis, 2, 1)
    ly_coords.addWidget(self.le_z_axis, 3, 1)

    # Sets the layout
    self.setLayout(ly_coords)


  def update_coordinates(self, x_coord, y_coord, z_coord):
    """ Updates the current coordinates on panel """
    self.le_x_axis.setText(str(x_coord))
    self.le_y_axis.setText(str(y_coord))
    self.le_z_axis.setText(str(z_coord))
