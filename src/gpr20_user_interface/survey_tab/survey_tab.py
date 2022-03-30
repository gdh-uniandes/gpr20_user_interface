

from current_coords_panel import CurrentCoordsPanel
from survey_status_panel import SurveyStatusPanel

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class SurveyTab(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        # Allow background color to be styled
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Set widget object name
        self.setObjectName("SurveyTab")

        # Instantiates the current coordinates panel
        self.current_coords_panel = CurrentCoordsPanel(self)
        self.survey_status_panel = SurveyStatusPanel(self)

        # Creates the panel layout
        ly_status = QVBoxLayout()

        # Adds the current coords panel to layout
        ly_status.addWidget(self.current_coords_panel)
        ly_status.addWidget(self.survey_status_panel)

        # Sets the panel layout
        self.setLayout(ly_status)

    def update_status(self, coordinates, status):
        """ Updates the status tab with survey data.

        Args:
          coordinates (dict): dictionary with the current coordinates of
            positioner.
          status (dict): dictionary with the status values of survey.

        """
        # Update current coordinates in corresponding panel
        self.current_coords_panel.update_coordinates(
            coordinates["x-coord"], coordinates["y-coord"], coordinates["z-coord"]
        )

        # Update survey status in corresponding panel
        self.survey_status_panel.update_information(
            status["status"], status["visited"], status["remaining"],
            status["completion"], status["time"]
        )
