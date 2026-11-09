import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
ventana = QWidget()
ventana.show()
sys.exit(app.exec_())