

from re import S
import rospy
import rospkg

from gpr20_msgs.msg import ControlFeedback
from gpr20_msgs.msg import GPR20AxisStatus
from std_srvs.srv import Empty, EmptyRequest
from gpr20_msgs.srv import ControlSurvey, ControlSurveyRequest

from gpr20_user_interface.survey_tab.survey_tab import SurveyTab
from gpr20_user_interface.parameters_tab.parameters_tab import ParametersTab

from PyQt5.QtWidgets import QMainWindow, QTabWidget


class RaspiUI(QMainWindow):

    def __init__(self):

        # Initializes super class
        QMainWindow.__init__(self)

        # Intializes the ROS node
        rospy.init_node("raspi_ui")

        # Sets the window title
        self.setWindowTitle("GPR-20: Raspberry Pi UI")

        # Sets the window size
        self.setFixedSize(800, 480)

        # Creates the tabs
        self.tabs = QTabWidget()

        # Creates the survey holder
        self.parameters_tab = ParametersTab(self)

        # Creates the status tab
        self.survey_tab = SurveyTab()

        # Adds survey widget to tab
        self.tabs.addTab(self.parameters_tab, "CONTROL")

        # Adds status widget to tab
        self.tabs.addTab(self.survey_tab, "STATUS")

        # Configure the tab widget to fill space
        self.tabs.tabBar().setDocumentMode(True)

        # Defines tabs as central layout
        self.setCentralWidget(self.tabs)

        # Creates the rospack instance
        rpk = rospkg.RosPack()

        # Gets the package base path
        base_path = rpk.get_path("gpr20_raspi_ui")

        # Loads the stylesheet and applies to UI
        with open(base_path + "/resources/styles.css") as f:
            self.setStyleSheet(f.read())

        # Define attributes to store coordinates
        self.x_coord = 0.0
        self.y_coord = 0.0
        self.z_coord = 0.0

        # Create the service proxy to execute survey
        self.survey_srv = rospy.ServiceProxy(
            "execute_survey",
            ControlSurvey
        )

        # Create the service proxy to stop survey
        self.stop_srv = rospy.ServiceProxy(
            "stop_survey",
            Empty
        )

        # Define the handler for receiving feedback messages
        rospy.Subscriber(
            "control_feedback",
            ControlFeedback,
            self.feedback_cb
        )

        # Define the handler for receiving X axis coordinate updates
        rospy.Subscriber(
            "/gpr20_x_axis/axis_status",
            GPR20AxisStatus,
            self.x_axis_status_cb
        )

        # Define the handler for receiving Y axis coordinate updates
        rospy.Subscriber(
            "/gpr20_y_axis/axis_status",
            GPR20AxisStatus,
            self.y_axis_status_cb
        )

        # Define the handler for receiving Z axis coordinate updates
        rospy.Subscriber(
            "/gpr20_z_axis/axis_status",
            GPR20AxisStatus,
            self.z_axis_status_cb
        )

    def start_survey(self, x_params, y_params, vna_params):

        # Execute service check and handle errors
        try:

            # Check that service is available
            rospy.wait_for_service("execute_survey", timeout=1.0)

            # Creates the request message
            request = ControlSurveyRequest(
                vna_ip=vna_params[0],
                x_start=x_params[0],
                x_stop=x_params[1],
                x_points=x_params[2],
                y_start=y_params[0],
                y_stop=y_params[1],
                y_points=y_params[2],
                f_start=vna_params[1],
                f_stop=vna_params[2],
                f_points=vna_params[3]
            )

            # Call the service and get response
            response = self.survey_srv(request)

            # Check if survey successfully started
            if response.launched:

                pass

        # Handle error if exception occurs
        except rospy.ROSException as re:
            rospy.logerr("Survey setup service is not available.")

    def stop_survey(self):
        """ Sends a cancelation request to survey. """
        # Execute in block in order to handle errors
        try:

            # Waits until service is available
            rospy.wait_for_service("stop_survey", timeout=1.0)

            # Call the service
            self.stop_srv()

            # Unlocks the survey tab as not in survey
            self.parameters_tab.unlock(on_survey=False)

        except rospy.ROSException as re:
            rospy.logerr("Survey stop service is not available.")

    def feedback_cb(self, msg):

        self.survey_tab.update_status(
            
            coordinates={
                "x-coord": self.x_coord,
                "y-coord": self.y_coord,
                "z-coord": self.z_coord
            },

            status={
                "status": msg.status_message,
                "visited": msg.visited_points,
                "remaining": msg.remaining_points,
                "completion": msg.completion,
                "time": msg.remaining_time
            }
        )

    def x_axis_status_cb(self, msg):
        """Callback for X-Axis status subscriber"""
        self.x_coord = msg.current_coordinate

    def y_axis_status_cb(self, msg):
        """Callback for Y-Axis status subscriber"""
        self.y_coord = msg.current_coordinate

    def z_axis_status_cb(self, msg):
        """Callback for Z-Axis status subscriber"""
        self.z_coord = msg.current_coordinate
