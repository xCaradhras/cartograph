from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QToolBar, QToolButton, QMenu, QMessageBox
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window, set its title, size, and initialize UI components.
        """
        super().__init__()
        self.setWindowTitle("Cartograph")
        self.setWindowIcon(QIcon("resources/logo_sqare.ico"))
        self.setGeometry(100, 100, 800, 600)

        self.initUI()
        self.initMenuBar()

    def initUI(self):
        """
        Set up the central widget and layout for the main window.
        """
        layout = QVBoxLayout()

        label = QLabel("Welcome to the PyQt6 Application!")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def initMenuBar(self):
        """
        Create and add a menu bar with actions and a dropdown menu to the main window.
        """
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        # Add various buttons to the file menu
        open_action = QAction("Open", self)
        open_action.setStatusTip("Say Hello")
        open_action.triggered.connect(self.say_hello)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.setStatusTip("Save the current document")
        file_menu.addAction(save_action)

        quit_action = QAction("Quit", self)
        quit_action.setStatusTip("Quit the application")
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        # Options menu
        options_menu = menubar.addMenu("Options")
        action_option1 = QAction("Option 1", self)
        action_option1.triggered.connect(lambda: print("Option 1 selected"))
        options_menu.addAction(action_option1)
        action_option2 = QAction("Option 2", self)
        action_option2.triggered.connect(lambda: print("Option 2 selected"))
        options_menu.addAction(action_option2)

        # Help menu
        help_menu = menubar.addMenu("Help")

        # Project page action
        project_page = QAction("Project Page", self)
        project_page.setStatusTip("Visit the project page")
        project_page.triggered.connect(self.open_project_page)
        help_menu.addAction(project_page)

        # About action
        help_action = QAction("About", self)
        help_action.setStatusTip("About this application")
        help_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(help_action)

    def say_hello(self):
        """
        Print a hello message to the console when the toolbar action is triggered.
        """
        print("Opening something!")

    def open_project_page(self):
        """
        Open the project page in a web browser.
        """
        import webbrowser
        project_page_url = r"https://github.com/xCaradhras/cartograph"
        webbrowser.open(project_page_url)
        
    def show_about_dialog(self):
        """
        Show a modal popup with information about the application.
        """
        QMessageBox.information(self, "About Cartograph", "Cartograph\nVersion 1.0\nLicense: GPLv3")
        