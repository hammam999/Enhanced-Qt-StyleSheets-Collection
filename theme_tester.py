#!/usr/bin/env python3
"""
QSS Theme Tester - PyQt6 Application
Application to test and display all templates QSS
"""

import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QFont

class ThemeTesterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_theme = None
        self.themes = self.load_available_themes()
        self.init_ui()
        
    def load_available_themes(self):
        """Download list of available templates"""
        themes = {}
        theme_dir = Path(__file__).parent
        
        theme_files = [
            'MacOS-Enhanced.qss', 'MaterialDark-Enhanced.qss', 'Ubuntu-Enhanced.qss',
            'MacOS.qss', 'MaterialDark.qss', 'Ubuntu.qss', 'ElegantDark.qss',
            'AMOLED.qss', 'Aqua.qss', 'ManjaroMix.qss', 'ConsoleStyle.qss', 'NeonButtons.qss'
        ]
        
        for theme_file in theme_files:
            theme_path = theme_dir / theme_file
            if theme_path.exists():
                theme_name = theme_file.replace('.qss', '').replace('-', ' ')
                themes[theme_name] = str(theme_path)
                
        return themes
    
    def init_ui(self):
        """User Interface Setup"""
        self.setWindowTitle("QSS Theme Tester - Template Testing Qt")
        self.setGeometry(100, 100, 1200, 800)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Template selection bar
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Choose a template:")
        theme_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Default template", None)
        for theme_name, theme_path in self.themes.items():
            self.theme_combo.addItem(theme_name, theme_path)
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        main_layout.addLayout(theme_layout)
        
        # Tabs
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        self.create_basic_controls_tab()
        self.create_input_controls_tab()
        self.create_display_controls_tab()
        self.create_container_controls_tab()
        
        # Status bar
        self.statusBar().showMessage("Ready - select a template to test")
    
    def create_basic_controls_tab(self):
        """Basic controls"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Buttons
        buttons_group = QGroupBox("Buttons")
        buttons_layout = QGridLayout(buttons_group)
        
        normal_btn = QPushButton("Normal Button")
        default_btn = QPushButton("Default Button")
        default_btn.setDefault(True)
        disabled_btn = QPushButton("Disabled Button")
        disabled_btn.setEnabled(False)
        
        buttons_layout.addWidget(normal_btn, 0, 0)
        buttons_layout.addWidget(default_btn, 0, 1)
        buttons_layout.addWidget(disabled_btn, 0, 2)
        
        layout.addWidget(buttons_group)
        
        # Checkboxes
        checkboxes_group = QGroupBox("Checkboxes")
        checkboxes_layout = QVBoxLayout(checkboxes_group)
        
        cb1 = QCheckBox("Checked")
        cb1.setChecked(True)
        cb2 = QCheckBox("Unchecked")
        cb3 = QCheckBox("Disabled")
        cb3.setEnabled(False)
        
        checkboxes_layout.addWidget(cb1)
        checkboxes_layout.addWidget(cb2)
        checkboxes_layout.addWidget(cb3)
        
        layout.addWidget(checkboxes_group)
        
        # Radio buttons
        radio_group = QGroupBox("Radio buttons")
        radio_layout = QVBoxLayout(radio_group)
        
        rb1 = QRadioButton("Option 1")
        rb1.setChecked(True)
        rb2 = QRadioButton("Option 2")
        rb3 = QRadioButton("Disabled")
        rb3.setEnabled(False)
        
        radio_layout.addWidget(rb1)
        radio_layout.addWidget(rb2)
        radio_layout.addWidget(rb3)
        
        layout.addWidget(radio_group)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "Basic controls")
    
    def create_input_controls_tab(self):
        """Input controls"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Text fields
        text_group = QGroupBox("Text fields")
        text_layout = QGridLayout(text_group)
        
        text_layout.addWidget(QLabel("Text field:"), 0, 0)
        line_edit = QLineEdit("Text example")
        text_layout.addWidget(line_edit, 0, 1)
        
        text_layout.addWidget(QLabel("Password field:"), 1, 0)
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        password_edit.setText("password")
        text_layout.addWidget(password_edit, 1, 1)
        
        layout.addWidget(text_group)
        
        # Text area
        text_area_group = QGroupBox("Text area")
        text_area_layout = QVBoxLayout(text_area_group)
        
        text_edit = QTextEdit()
        text_edit.setPlainText("Text example")
        text_edit.setMaximumHeight(100)
        text_area_layout.addWidget(text_edit)
        
        layout.addWidget(text_area_group)
        
        # Dropdown lists
        combo_group = QGroupBox("Dropdown lists")
        combo_layout = QGridLayout(combo_group)
        
        combo_layout.addWidget(QLabel("Dropdown list:"), 0, 0)
        combo_box = QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        combo_layout.addWidget(combo_box, 0, 1)
        
        combo_layout.addWidget(QLabel("Spin box:"), 1, 0)
        spin_box = QSpinBox()
        spin_box.setRange(0, 100)
        spin_box.setValue(50)
        combo_layout.addWidget(spin_box, 1, 1)
        
        layout.addWidget(combo_group)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "Input controls")
    
    def create_display_controls_tab(self):
        """Display controls"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Sliders and progress bars
        sliders_group = QGroupBox("Sliders and progress bars")
        sliders_layout = QGridLayout(sliders_group)
        
        sliders_layout.addWidget(QLabel("Horizontal slider:"), 0, 0)
        h_slider = QSlider(Qt.Orientation.Horizontal)
        h_slider.setValue(30)
        sliders_layout.addWidget(h_slider, 0, 1)
        
        sliders_layout.addWidget(QLabel("Progress bar:"), 1, 0)
        progress_bar = QProgressBar()
        progress_bar.setValue(45)
        sliders_layout.addWidget(progress_bar, 1, 1)
        
        layout.addWidget(sliders_group)
        
        # Lists and tables
        lists_group = QGroupBox("Lists and tables")
        lists_layout = QHBoxLayout(lists_group)
        
        # List
        list_widget = QListWidget()
        list_widget.addItems([f"Item {i+1}" for i in range(5)])
        list_widget.setMaximumHeight(120)
        lists_layout.addWidget(list_widget)
        
        # Table
        table_widget = QTableWidget(3, 2)
        table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2"])
        table_widget.setMaximumHeight(120)
        
        for i in range(3):
            for j in range(2):
                table_widget.setItem(i, j, QTableWidgetItem(f"Cell {i+1},{j+1}"))
        
        lists_layout.addWidget(table_widget)
        
        layout.addWidget(lists_group)
        layout.addStretch()
        
        self.tab_widget.addTab(tab, "Display controls")
    
    def create_container_controls_tab(self):
        """Containers"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Splitters
        splitter_group = QGroupBox("Splitters")
        splitter_layout = QVBoxLayout(splitter_group)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(QLabel("Left part"))
        splitter.addWidget(QLabel("Right part"))
        splitter.setMaximumHeight(80)
        splitter_layout.addWidget(splitter)
        
        layout.addWidget(splitter_group)
        
        # Toolboxes
        toolbox_group = QGroupBox("Toolboxes")
        toolbox_layout = QVBoxLayout(toolbox_group)
        
        toolbox = QToolBox()
        toolbox.setMaximumHeight(150)
        
        page1 = QWidget()
        page1_layout = QVBoxLayout(page1)
        page1_layout.addWidget(QLabel("Page 1 content"))
        toolbox.addItem(page1, "Basic tools")
        
        page2 = QWidget()
        page2_layout = QVBoxLayout(page2)
        page2_layout.addWidget(QLabel("Page 2 content"))
        toolbox.addItem(page2, "Advanced tools")
        
        toolbox_layout.addWidget(toolbox)
        layout.addWidget(toolbox_group)
        
        # Nested tabs
        nested_group = QGroupBox("Nested tabs")
        nested_layout = QVBoxLayout(nested_group)
        
        nested_tabs = QTabWidget()
        nested_tabs.setMaximumHeight(120)
        
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(QLabel("Tab 1 content"))
        nested_tabs.addTab(tab1, "Tab 1")
        
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(QLabel("Tab 2 content"))
        nested_tabs.addTab(tab2, "Tab 2")
        
        nested_layout.addWidget(nested_tabs)
        layout.addWidget(nested_group)
        
        layout.addStretch()
        self.tab_widget.addTab(tab, "Containers")
    
    def change_theme(self, theme_name):
        """Change the theme"""
        if theme_name == "Default template":
            QApplication.instance().setStyleSheet("")
            self.current_theme = None
            self.statusBar().showMessage("Default template applied")
            return
        
        theme_path = self.themes.get(theme_name)
        if theme_path and os.path.exists(theme_path):
            try:
                with open(theme_path, 'r', encoding='utf-8') as f:
                    stylesheet = f.read()
                QApplication.instance().setStyleSheet(stylesheet)
                self.current_theme = theme_name
                self.statusBar().showMessage(f"Theme applied: {theme_name}")
            except Exception as e:
                self.statusBar().showMessage(f"Error loading theme: {str(e)}")
        else:
            self.statusBar().showMessage(f"Theme not found: {theme_name}")

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QSS Theme Tester")
    app.setApplicationVersion("1.0")
    
    window = ThemeTesterWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
