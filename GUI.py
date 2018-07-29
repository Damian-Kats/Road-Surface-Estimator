import sys, os, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QDesktopWidget, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from get_map import get_maps_image
from calculations import calculate_area


class MapGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.lat = QLineEdit(self)  # text box for entering latitude values
        self.long = QLineEdit(self)  # text box for entering longitude values
        self.output = QLineEdit(self)  # text box displaying the road area output

        self.initUI()  # creation of GUI

    def initUI(self):
        # Get current directory path
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        # WebEngineView of custom Google Map html file
        url = QUrl.fromLocalFile(cur_dir + "\custom_map.html")
        view = QWebEngineView()
        view.load(url)
        view.show()

        # Defining buttons for widget
        button1 = QPushButton("Calculate")
        button1.setToolTip("This button will calculate the total road surface area of your chosen region.")
        button1.resize(button1.sizeHint())

        button2 = QPushButton("Clear")
        button2.setToolTip("This button will clear the calculated result.")
        button2.resize(button1.sizeHint())

        # Connect the buttons to the relevant functions
        button1.clicked.connect(self.calculate)
        button2.clicked.connect(self.clear_area)

        # Label and area for output of surface estimate
        msg1 = QLabel('Total Road Surface Area (m^2): ', self)

        self.output.setReadOnly(True)

        # Label for asking user for input
        msg2 = QLabel('Please enter coordinates for centre of target area: ', self)

        # Labels for latitude and longitude text boxes
        latmsg = QLabel('Latitude: ')
        longmsg = QLabel('Longitude: ')

        #self.lat.textChanged.connect(self.calculate)
        #self.long.textChanged.connect(self.calculate)

        # Format of layout for widget, outer grid is 1x5. All other grids are added to the main grid rows and contain
        # the buttons and QLineEdits in either one or two columns
        outer_grid = QGridLayout()
        self.setLayout(outer_grid)

        input_grid = QGridLayout()
        self.setLayout(input_grid)

        btn_grid = QGridLayout()
        self.setLayout(btn_grid)

        text_grid = QGridLayout()
        self.setLayout(text_grid)

        outer_grid.addWidget(view, 1, 0)
        outer_grid.addWidget(msg2, 2, 0)
        outer_grid.addLayout(input_grid, 3, 0)
        outer_grid.addLayout(btn_grid, 4, 0)
        outer_grid.addLayout(text_grid, 5, 0)

        input_grid.addWidget(latmsg, 1, 1)
        input_grid.addWidget(self.lat, 1, 2)
        input_grid.addWidget(longmsg, 1, 3)
        input_grid.addWidget(self.long, 1, 4)

        btn_grid.addWidget(button1, 1, 1)
        btn_grid.addWidget(button2, 1, 2)

        text_grid.addWidget(msg1, 1, 1)
        text_grid.addWidget(self.output, 1, 2)

        # Position the GUI near the centre of the screen upon executing
        mywidget = self.frameGeometry()
        centrePoint = QDesktopWidget().availableGeometry().center()
        mywidget.moveCenter(centrePoint)
        self.setWindowTitle("Road Surface Estimation")
        self.show()

    # The calculate function is connected to the calculate button and executes functions which create the custom map
    # and do the image processing to find the road area estimate
    def calculate(self):
        start_time = time.time()
        newlat = self.lat.text()
        newlong = self.long.text()
        if newlat == '' or newlong == '':
            self.errorPopup()
            return
        if self.is_number(newlat) is False or self.is_number(newlong) is False:
            self.errorPopup2()
            return
        ctr = newlat + ',' + newlong
        #print(ctr)
        img = get_maps_image(ctr)
        road_area = str(calculate_area(img))
        self.output.setText(road_area)
        print("--- %s seconds ---" % (time.time() - start_time))

    # Clears the value from the output text box in the GUI
    def clear_area(self):
        self.output.setText("")
        print(self.output.text())

    def errorPopup(self):
        message = "Please enter values for both latitude and longitude."
        QMessageBox.about(self, "Warning", message)
        self.show()

    def errorPopup2(self):
        message = "Please enter valid float values for coordinates."
        QMessageBox.about(self, "Warning", message)
        self.show()

    def is_number(self, n):
        try:
            float(n)
            return True
        except ValueError:
            return False


def run_gui():
    app = QApplication(sys.argv)
    ex = MapGUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui()