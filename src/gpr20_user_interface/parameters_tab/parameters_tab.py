
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ip_widget import IPWidget
from parameters_widget import ParametersWidget
from step_selector_widget import StepSelectorWidget
from start_widget import StartWidget

class ParametersTab(QWidget):

  def __init__(self, parent):

    super(ParametersTab, self).__init__(parent)

    # Defines the step size attribute
    self.step_size = 1

    # Allow background color to be styled
    self.setAttribute(Qt.WA_StyledBackground, True)

    # Set widget object name
    self.setObjectName("ParametersTab")

    # Instantiate the step selector widget
    self.step_selector_widget = StepSelectorWidget(self)

    self.ip_widget = IPWidget(self)
    self.parameters_widget = ParametersWidget(self)
    self.start_widget = StartWidget(self)

    ly_panel = QVBoxLayout()
    ly_panel.addWidget(self.step_selector_widget)
    ly_panel.addWidget(self.ip_widget)
    ly_panel.addWidget(self.parameters_widget)
    ly_panel.addWidget(self.start_widget)
    
    self.setLayout(ly_panel)


  def step_size_change(self, step_size):
    """Change the step size for input widgets
    
    Args:
      step_size (int): step size for parameters values.
    """

    # Stores the step size
    self.step_size = step_size

    # Updates input widgets
    self.ip_widget.update_step_size(self.step_size)
    self.parameters_widget.update_step_size(self.step_size)


  def start_survey(self):

    # Gets x axis parameters
    x_start = self.parameters_widget.sb_x_start.value()
    x_end = self.parameters_widget.sb_x_end.value()
    x_points = self.parameters_widget.sb_x_points.value()

    # Gets y axis parameters
    y_start = self.parameters_widget.sb_y_start.value()
    y_end = self.parameters_widget.sb_y_end.value()
    y_points = self.parameters_widget.sb_y_points.value()

    # Gets the VNA parameters
    f_start = self.parameters_widget.sb_f_start.value()
    f_end = self.parameters_widget.sb_f_end.value()
    f_points = self.parameters_widget.sb_f_points.value()

    # Multiply frequency values to set them in megahertz
    f_start = f_start * 1e6
    f_end = f_end * 1e6

    # Gets the IP field values
    ip_0 = self.ip_widget.ip_edit_0.value()
    ip_1 = self.ip_widget.ip_edit_1.value()
    ip_2 = self.ip_widget.ip_edit_2.value()
    ip_3 = self.ip_widget.ip_edit_3.value()

    # Build the IP
    ip = str(ip_0) + '.' + str(ip_1) + '.' + str(ip_2) + '.' + str(ip_3)

    # Create the lists
    x_params = [x_start, x_end, x_points]
    y_params = [y_start, y_end, y_points]
    vna_params = [ip, f_start, f_end, f_points]

    # Prevents changes from user
    self.lock(on_survey=True)

    # Calls the parent class to start survey
    self.parent().parent().parent().start_survey(x_params, y_params, vna_params)


  def stop_survey(self):

    # Releases the user interface
    self.unlock(on_survey=False)

    self.parent().parent().parent().stop_survey()


  def lock(self, on_survey=False):
    """ Locks the survey tab from user inputs.
    
    """

    self.ip_widget.lock()
    self.parameters_widget.lock()
    self.step_selector_widget.lock()
    self.start_widget.lock(on_survey)


  def unlock(self, on_survey=False):
    """
    
    """
    
    self.ip_widget.unlock()
    self.parameters_widget.unlock()
    self.step_selector_widget.unlock()
    self.start_widget.unlock(on_survey)
