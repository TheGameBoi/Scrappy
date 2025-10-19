def dark_mode_stylesheet():
    return """
    QWidget {
        background-color: #2E2E2E;
        color: #FFFFFF;
        font-size: 14px;
    }
    QLineEdit {
        background-color: #3A3A3A;
        border: 1px solid #5A5A5A;
        border-radius: 5px;
        padding: 5px;
        color: #FFFFFF;
    }
    QPushButton {
        background-color: #4A4A4A;
        border: 1px solid #5A5A5A;
        border-radius: 5px;
        padding: 5px;
        color: #FFFFFF;
    }
    QPushButton:hover {
        background-color: #5A5A5A;
    }
    QComboBox {
        background-color: #3A3A3A;
        border: 1px solid #5A5A5A;
        border-radius: 5px;
        padding: 5px;
        color: #FFFFFF;
    }
    QLabel {
        color: #FFFFFF;
    }
    """