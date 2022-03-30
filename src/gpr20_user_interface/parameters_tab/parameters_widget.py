
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class ParametersWidget(QWidget):

  def __init__(self, parent):

    QWidget.__init__(self, parent)

    # Creates the grid layout
    ly_parameters = QGridLayout()

    # Creates the x start input field
    self.sb_x_start = QSpinBox()
    self.sb_x_start.setRange(0, 800)
    self.sb_x_start.setValue(50)
    self.sb_x_start.setSingleStep(1)
    
    self.sb_x_end = QSpinBox()
    self.sb_x_end.setRange(0, 800)
    self.sb_x_end.setValue(550)
    self.sb_x_end.setSingleStep(1)

    self.sb_x_points = QSpinBox()
    self.sb_x_points.setRange(2, 7000)
    self.sb_x_points.setValue(2)

    self.sb_y_start = QSpinBox()
    self.sb_y_start.setRange(0, 700)
    self.sb_y_start.setValue(50)

    self.sb_y_end = QSpinBox()
    self.sb_y_end.setRange(0, 700)
    self.sb_y_end.setValue(550)

    self.sb_y_points = QSpinBox()
    self.sb_y_points.setRange(2, 7000)
    self.sb_y_points.setValue(2)

    self.sb_f_start = QSpinBox()
    self.sb_f_start.setRange(600, 6000)
    self.sb_f_start.setValue(600)

    self.sb_f_end = QSpinBox()
    self.sb_f_end.setRange(600, 6000)
    self.sb_f_end.setValue(6000)

    self.sb_f_points = QSpinBox()
    self.sb_f_points.setRange(2, 4000)
    self.sb_f_points.setValue(512)

    # Adds the labels
    ly_parameters.addWidget(QLabel("START"), 0, 1)
    ly_parameters.addWidget(QLabel("END"), 0, 2)
    ly_parameters.addWidget(QLabel("POINTS"), 0, 3)
    ly_parameters.addWidget(QLabel("X: "), 1, 0, Qt.AlignRight)
    ly_parameters.addWidget(QLabel("Y: "), 2, 0, Qt.AlignRight)
    ly_parameters.addWidget(QLabel("F: "), 3, 0, Qt.AlignRight)

    # Adds the input fields
    ly_parameters.addWidget(self.sb_x_start, 1, 1)
    ly_parameters.addWidget(self.sb_x_end, 1, 2)
    ly_parameters.addWidget(self.sb_x_points, 1, 3)
    ly_parameters.addWidget(self.sb_y_start, 2, 1)
    ly_parameters.addWidget(self.sb_y_end, 2, 2)
    ly_parameters.addWidget(self.sb_y_points, 2, 3)
    ly_parameters.addWidget(self.sb_f_start, 3, 1)
    ly_parameters.addWidget(self.sb_f_end, 3, 2)
    ly_parameters.addWidget(self.sb_f_points, 3, 3)

    # Sets the colums stretch
    ly_parameters.setColumnStretch(0, 1)
    ly_parameters.setColumnStretch(1, 5)
    ly_parameters.setColumnStretch(2, 5)
    ly_parameters.setColumnStretch(3, 5)

    # Sets the paramters layout
    self.setLayout(ly_parameters)


  def lock(self):
    self.sb_x_start.setEnabled(False)
    self.sb_x_end.setEnabled(False)
    self.sb_x_points.setEnabled(False)
    self.sb_y_start.setEnabled(False)
    self.sb_y_end.setEnabled(False)
    self.sb_y_points.setEnabled(False)
    self.sb_f_start.setEnabled(False)
    self.sb_f_end.setEnabled(False)
    self.sb_f_points.setEnabled(False)


  def unlock(self):
    self.sb_x_start.setEnabled(True)
    self.sb_x_end.setEnabled(True)
    self.sb_x_points.setEnabled(True)
    self.sb_y_start.setEnabled(True)
    self.sb_y_end.setEnabled(True)
    self.sb_y_points.setEnabled(True)
    self.sb_f_start.setEnabled(True)
    self.sb_f_end.setEnabled(True)
    self.sb_f_points.setEnabled(True)


  def update_step_size(self, step_size):
    
    self.sb_x_start.setSingleStep(step_size)
    self.sb_x_end.setSingleStep(step_size)
    self.sb_x_points.setSingleStep(step_size)
    self.sb_y_start.setSingleStep(step_size)
    self.sb_y_end.setSingleStep(step_size)
    self.sb_y_points.setSingleStep(step_size)
    self.sb_f_start.setSingleStep(step_size)
    self.sb_f_end.setSingleStep(step_size)
    self.sb_f_points.setSingleStep(step_size)
