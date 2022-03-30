
from math import floor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel

class SurveyStatusPanel(QWidget):

    def __init__(self, parent):

        # Intialize the super class
        super(SurveyStatusPanel, self).__init__(parent)

        # Define the status box line edit
        self.le_status = QLineEdit()
        self.le_status.setEnabled(False)

        # Define the visited points line edit
        self.le_visited = QLineEdit()
        self.le_visited.setEnabled(False)

        # Define the remaining points line edit
        self.le_remaining = QLineEdit()
        self.le_remaining.setEnabled(False)

        # Define the completion line edit
        self.le_completion = QLineEdit()
        self.le_completion.setEnabled(False)

        # Define the remaining time line edit
        self.le_time = QLineEdit()
        self.le_time.setEnabled(False)

        # Create the layout for the panel
        ly_panel = QGridLayout()

        # Add the elements to  the layout
        ly_panel.addWidget(QLabel("SURVEY STATUS"), 0, 0, 1, 2, Qt.AlignCenter)
        ly_panel.addWidget(QLabel("STATUS:"), 1, 0)
        ly_panel.addWidget(self.le_status, 1, 1)
        ly_panel.addWidget(QLabel("VISITED: "), 2, 0)
        ly_panel.addWidget(self.le_visited, 2, 1)
        ly_panel.addWidget(QLabel("REMAINING: "), 3, 0)
        ly_panel.addWidget(self.le_remaining, 3, 1)
        ly_panel.addWidget(QLabel("COMPLETION: "), 4, 0)
        ly_panel.addWidget(self.le_completion, 4, 1)
        ly_panel.addWidget(QLabel("TIME: "), 5, 0)
        ly_panel.addWidget(self.le_time, 5, 1)

        # Set the layout for the panel
        self.setLayout(ly_panel)

    def update_information(self, status, visited, remaining,
                           completion, time):
        """Update the panel with information from the survey control."""
        # Update the status field with message
        self.le_status.setText(status)

        # Define the string for visited points
        visited_str = "{} points have been sampled".format(visited)

        # Update the visited points field with message
        self.le_visited.setText(visited_str)

        # Define the string for remaining points
        remaining_str = "There are {} remaining points to sample".format(
            remaining
        )

        # Update the remaining points field with message
        self.le_remaining.setText(remaining_str)

        # Define the completion string
        completion_str = "{:5.2f} % of survey completed.".format(
            completion * 100
        )

        # Set the completion string in field
        self.le_completion.setText(completion_str)

        # Define days, hours, minutes and seconds for remaning time
        days = int(floor(time / 86400))
        time_h = time - days * 86400
        hours = int(floor(time / 3600))
        time_m = time_h - hours * 3600
        minutes = int(floor(time_m / 60))
        seconds = int(time_m - minutes * 60)

        # Define the string for remaining time
        time_str ="{:d}d:{:d}h:{:d}m:{:d}s remaining".format(
            days, hours, minutes, seconds
        )

        # Update the remaining time field with value
        self.le_time.setText(time_str)
