from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QMessageBox

from form.form import Ui_Form_Dialog


class FormWindow(QWidget):
    def __init__(self, parent=None):
        super(FormWindow, self).__init__()
        self.ui = Ui_Form_Dialog()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.btn_add.clicked.connect(self.get_student_from_form)
        self.ui.btn_delete.clicked.connect(self.clear_all)

    def closeEvent(self, event):
        print('Exit Form')
        self.hide()
        self.parent.show()

    @Slot()
    def get_student_from_form(self):
        data = {
            'nombre': self.ui.le_name.text(),
            'apellido': self.ui.le_last_name.text(),
            'documento': self.ui.le_dni.text()
        }
        count_before = len(self.parent.students)
        self.parent.students.append(data)
        print(self.parent.students)
        if count_before != len(self.parent.students):
            message = QMessageBox()
            message.setText(f"Se agrego el alumno {data['nombre']} exitosamente")
            message.exec()

    @Slot()
    def clear_all(self):
        self.ui.le_name.setText("")
        self.ui.le_last_name.setText("")
        self.ui.le_dni.setText("")
        message = QMessageBox()
        message.setText(f"Se limpiaron los campos")
        message.exec()
