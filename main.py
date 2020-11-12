import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from menu.menu import Ui_MainWindow
#from canjear_cheque.exchange_cheque_form_dialog import
#from crear_cheque.create_cheque_form_dialog import
#from depositar.deposit_form_dialog import
#from retirar.withdraw_form_dialog import
#from tutorial.tutorial_dialog import



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        pathToMoney = open(r'C:\Users\manue\Desktop\ArduinQt5\saldo', 'r')

        self.usuariosRegistrados = {
            'id' : "0",
            'nombre': "MANUEL FERRERAS",
            'contrasena': "123",
            'saldo': pathToMoney.readline()
        }

        # Attributes
        # Guardo las ventanas como atributos
        #self.canjearCheque = (parent=self)
        #self.crearCheque = (parent=self)
        #self.depositar = (parent=self)
        #self.retirar = (parent=self)
        #self.tutorial = (parent=self)

        # Configuracion de los botones de la main window
        self.ui.btn_deposit.clicked.connect(self.open_depositar)
        self.ui.btn_withdraw.clicked.connect(self.open_retirar)
        self.ui.btn_cheque.clicked.connect(self.open_canjear)
        self.ui.btn_generate.clicked.connect(self.open_crear)
        self.ui.btn_tutorial.clicked.connect(self.open_tutorial)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_close_session.clicked.connect(self.cerrar_sesion)



    @Slot()
    def open_canjear(self):  # Muestra la ventana para canjear un cheque y oculta la main window
        self.canjearCheque.show()
        self.hide()

    @Slot()
    def open_crear(self):  # Muestra la ventana para crear un cheque y oculta la main window
        self.crearCheque.show()
        self.hide()

    @Slot()
    def open_depositar(self):  # Muestra la ventana de depositar plata y oculta la main window
        self.depositar.show()
        self.hide()

    @Slot()
    def open_retirar(self):  # Muestra la ventana de retirar plata y oculta la main window
        self.retirar.show()
        self.hide()

    @Slot()
    def open_tutorial(self):  # Muestra el tutorial y oculta la main window
        self.tutorial.show()
        self.hide()

    @Slot()
    def exit(self):  # Sale de la aplicacion
        sys.exit(app.exec_())

    @Slot()
    def cerrar_sesion(self):
        # TODO Permitir al usuario cerrar sesion y volvver a la pantalla de verificacion de tarjeta.
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
