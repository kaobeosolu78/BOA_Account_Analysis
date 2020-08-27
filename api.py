from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QFormLayout, QLineEdit, QPushButton, QMainWindow, QAction, QListWidget
from get import finance
import sys

class plot_sel(QWidget):
    def __init__(self):
        self.fin = finance()

        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        # label
        title = QLabel("Which plot would you like?")
        grid.addWidget(title,0,0)

        # input
        count = 0
        self.lb = QListWidget()
        for p in ["month","all","highest"]:
            self.lb.insertItem(count, p)
            count += 1
        self.lb.clicked.connect(lambda: self.pick_plot())
        grid.addWidget(self.lb,1,0)

        # gen settings
        self.setLayout(grid)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Schedule')
        self.show()

    def pick_plot(self):
        self.close()
        item = self.lb.currentItem().text()
        self.fin.plot(item)


class dt_range(QWidget):
    def __init__(self):
        self.fin = finance()

        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        # labels
        title = QLabel("")
        grid.addWidget(title, 0, 0)

        title = QLabel("Start Date: ")
        grid.addWidget(title, 1, 0)

        title = QLabel("End Date: ")
        grid.addWidget(title, 2, 0)

        # inputs
        self.start = QLineEdit("04/27/2019")#"mon/day/year")
        grid.addWidget(self.start, 1, 1)

        self.end = QLineEdit("04/27/2020")#"mon/day/year")
        grid.addWidget(self.end, 2, 1)

        # buttons
        submit = QPushButton("Get Amount")
        submit.clicked.connect(lambda: self.get_rng(grid))
        grid.addWidget(submit, 3, 0)

        cancel = QPushButton("Cancel")
        cancel.clicked.connect(lambda: self.close())
        grid.addWidget(cancel, 3, 1)

        # gen settings
        self.setLayout(grid)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Schedule')
        self.show()

    def get_rng(self, grid):
        temp = self.fin.get_range(datetime.datetime.strptime(self.start.text(), "%m/%d/%Y"), datetime.datetime.strptime(self.end.text(), "%m/%d/%Y"))
        title = QLabel(str(temp))
        grid.addWidget(title, 0, 0)

class home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # wid = QWidget(self)
        # self.setCentralWidget(wid)
        grid = QGridLayout()

        # menus
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        disp = QAction("Display", self)
        disp.triggered.connect(lambda: self.display())
        filemenu.addAction(disp)

        rng = QAction("Date Range", self)
        rng.triggered.connect(lambda: self.range())
        filemenu.addAction(rng)


        # gen settings
        # wid.setLayout(grid)
        self.setLayout(grid)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Schedule')
        self.show()

    def disp(self):
        self.next = plot_sel()

    def range(self):
        self.next = dt_range()


def main():
    app = QApplication(sys.argv)
    a = home()
    sys.exit(app.exec_())

main()
