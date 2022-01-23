import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Model


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1900, 900)

        # Product Button
        self.buttonP = QPushButton(self)
        self.buttonP.setGeometry(10, 10, 250, 100)
        self.buttonP.setText('Add Products')
        self.buttonP.setStyleSheet('font-size:30px')

        # Vehicles Button
        self.buttonV = QPushButton(self)
        self.buttonV.setGeometry(1640, 10, 250, 100)
        self.buttonV.setText('Add Vehicles')
        self.buttonV.setStyleSheet('font-size:30px')

        # Product Window
        self.ProductWindow = ProductWindow()

        # Vehicles Window
        self.VehiclesWindow = VehiclesWindow()

        # Button Event
        self.buttonP.clicked.connect(self.ProductWindow.show)
        self.buttonV.clicked.connect(self.VehiclesWindow.show)
        self.ProductWindow.buttonAddProduct.clicked.connect(self.AddProduct)
        self.VehiclesWindow.buttonAddVehicle.clicked.connect(self.AddVehicle)

        #Run Button
        self.buttonRun = QPushButton(self)
        self.buttonRun.setGeometry(780, 770, 250, 100)
        self.buttonRun.setText('Run')
        self.buttonRun.setStyleSheet('background-color:green; font-size:30px')
        self.buttonRun.clicked.connect(self.Run)

        # Product Table
        self.ProductTable = QTableWidget(self)
        self.ProductTable.setGeometry(10, 120, 900, 290)
        self.ProductTable.setColumnCount(7)
        self.ProductTable.setRowCount(0)
        self.ProductTable.setHorizontalHeaderLabels(['Product Name', 'Radius', 'Height','Weight','Quantity','Add','Delete'])
        self.ProductTable.setColumnWidth(0, 200)
        self.ProductTable.setColumnWidth(1, 200)
        self.ProductTable.setColumnWidth(2, 100)
        self.ProductTable.setColumnWidth(3, 100)
        self.ProductTable.setColumnWidth(4, 100)
        self.ProductTable.setColumnWidth(5, 100)
        self.ProductTable.setColumnWidth(6, 100)
        self.ProductTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ProductTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ProductTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ProductTable.setShowGrid(False)
        self.ProductTable.setStyleSheet('font-size:10px, font-weight:bold')

        # Vehicle Table
        self.VehicleTable = QTableWidget(self)
        self.VehicleTable.setGeometry(990, 120, 900, 290)
        self.VehicleTable.setColumnCount(9)
        self.VehicleTable.setRowCount(0)
        self.VehicleTable.setHorizontalHeaderLabels(['Vehicle Name','Vehicle Type','Length', 'Width', 'Height','Max Weight','Quantity','Add','Delete'])
        self.VehicleTable.setColumnWidth(0, 100)
        self.VehicleTable.setColumnWidth(1, 100)
        self.VehicleTable.setColumnWidth(2, 100)
        self.VehicleTable.setColumnWidth(3, 100)
        self.VehicleTable.setColumnWidth(4, 100)
        self.VehicleTable.setColumnWidth(5, 100)
        self.VehicleTable.setColumnWidth(6, 100)
        self.VehicleTable.setColumnWidth(7, 100)
        self.VehicleTable.setColumnWidth(8, 100)
        self.VehicleTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.VehicleTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.VehicleTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.VehicleTable.setShowGrid(False)
        self.VehicleTable.setStyleSheet('font-size:10px, font-weight:bold')

        #The Used Products Table
        self.Qlabel = QLabel(self)
        self.Qlabel.setGeometry(10, 400, 700, 100)
        self.Qlabel.setText('The Used Products')
        self.Qlabel.setStyleSheet('font-size:20px')
        self.UsedProductTable = QTableWidget(self)
        self.UsedProductTable.setGeometry(10, 470, 700, 200)
        self.UsedProductTable.setColumnCount(6)
        self.UsedProductTable.setRowCount(0)
        self.UsedProductTable.setHorizontalHeaderLabels(['Product Name', 'Radius', 'Heigth', 'Weight','Quantity','Delete'])
        self.UsedProductTable.setColumnWidth(0, 200)
        self.UsedProductTable.setColumnWidth(1, 100)
        self.UsedProductTable.setColumnWidth(2, 100)
        self.UsedProductTable.setColumnWidth(3, 100)
        self.UsedProductTable.setColumnWidth(4, 100)
        self.UsedProductTable.setColumnWidth(5, 100)
        self.UsedProductTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.UsedProductTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.UsedProductTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.UsedProductTable.setShowGrid(False)
        self.UsedProductTable.setStyleSheet('font-size:10px, font-weight:bold')

        #The Used Vehicles Table
        self.Qlabel = QLabel(self)
        self.Qlabel.setGeometry(1720, 400, 700, 100)
        self.Qlabel.setText('The Used Vehicles')
        self.Qlabel.setStyleSheet('font-size:20px')
        self.UsedVehicleTable = QTableWidget(self)
        self.UsedVehicleTable.setGeometry(1090, 470, 800, 200)
        self.UsedVehicleTable.setColumnCount(8)
        self.UsedVehicleTable.setRowCount(0)
        self.UsedVehicleTable.setHorizontalHeaderLabels(['Vehicle Name','Vehicle Type','Length', 'Width', 'Height','Max Weight','Quantity','Delete'])
        self.UsedVehicleTable.setColumnWidth(0, 100)
        self.UsedVehicleTable.setColumnWidth(1, 100)
        self.UsedVehicleTable.setColumnWidth(2, 100)
        self.UsedVehicleTable.setColumnWidth(3, 100)
        self.UsedVehicleTable.setColumnWidth(4, 100)
        self.UsedVehicleTable.setColumnWidth(5, 100)
        self.UsedVehicleTable.setColumnWidth(6, 100)
        self.UsedVehicleTable.setColumnWidth(7, 100)
        self.UsedVehicleTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.UsedVehicleTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.UsedVehicleTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.UsedVehicleTable.setShowGrid(False)
        self.UsedVehicleTable.setStyleSheet('font-size:10px, font-weight:bold')

        #Delete Button all items of Product Table
        self.buttonDeleteProduct = QPushButton(self)
        self.buttonDeleteProduct.setGeometry(10, 690, 200, 50)
        self.buttonDeleteProduct.setText('Delete All Products')
        self.buttonDeleteProduct.setStyleSheet('font-size:20px')
        self.buttonDeleteProduct.setStyleSheet('font-weight:bold')
        self.buttonDeleteProduct.setStyleSheet('background-color:red')
        self.buttonDeleteProduct.clicked.connect(self.DeleteAllProductFromUsed)

        #Delete Button all items of Vehicle Table
        self.buttonDeleteVehicle = QPushButton(self)
        self.buttonDeleteVehicle.setGeometry(1690, 690, 200, 50)
        self.buttonDeleteVehicle.setText('Delete All Vehicles')
        self.buttonDeleteVehicle.setStyleSheet('font-size:20px')
        self.buttonDeleteVehicle.setStyleSheet('font-weight:bold')
        self.buttonDeleteVehicle.setStyleSheet('background-color:red')
        self.buttonDeleteVehicle.clicked.connect(self.DeleteAllVehiclesFromUsed)

    def Run(self):
        data = {}
        data["i"] = []
        data["k"] = []
        data["j"] = []
        data["l"] = []

        data["pRadius"] = []
        data["pHeight"] = []
        data["pMass"] = []

        data["vLength"] = []
        data["vHeight"] = []
        data["vWide"] = []
        data["vMass"] = []

        for row in range(self.UsedVehicleTable.rowCount()):
            for j in range(int(self.UsedVehicleTable.item(row, 6).text())):
                data["j"].append(j)
                data["vLength"].append(int(self.UsedVehicleTable.item(row, 2).text()))
                data["vHeight"].append(int(self.UsedVehicleTable.item(row, 4).text()))
                data["vWide"].append(int(self.UsedVehicleTable.item(row, 3).text()))
                data["vMass"].append(int(self.UsedVehicleTable.item(row, 5).text()))


        for row in range(self.UsedProductTable.rowCount()):
            for i in range(int(self.UsedProductTable.item(row,4).text())):
                data["i"].append(i)
                data["k"].append(i)
                data["pRadius"].append(int(self.UsedProductTable.item(row, 1).text()))
                data["pHeight"].append(int(self.UsedProductTable.item(row, 2).text()))
                data["pMass"].append(int(self.UsedProductTable.item(row, 3).text()))

            
        Model.CreateModel(data)

    def AddProduct(self):
        ProductName = self.ProductWindow.ProductName.text()
        ProductRadius = self.ProductWindow.ProductRadius.text()
        ProductHeight = self.ProductWindow.ProductHeight.text()
        ProductWeight = self.ProductWindow.ProductWeight.text()
        if ProductName == '' or ProductRadius == '' or ProductHeight == '' or ProductWeight == '':
            self.ErrorMessage = QMessageBox.warning(self, 'Error', 'Please fill all the blanks')
        else:
            self.ProductQuantity = QLineEdit(self)
            self.ProductQuantity.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
            self.DeleteButton = QPushButton(self)
            self.DeleteButton.setText('Delete')
            self.DeleteButton.setStyleSheet('font-size:20px')
            self.DeleteButton.setStyleSheet('font-weight:bold')
            self.DeleteButton.setStyleSheet('background-color:red')
            self.DeleteButton.clicked.connect(self.DeleteProduct)
            self.AddButton = QPushButton(self)
            self.AddButton.setText('Add')
            self.AddButton.setStyleSheet('font-size:20px')
            self.AddButton.setStyleSheet('font-weight:bold')
            self.AddButton.setStyleSheet('background-color:green')
            self.AddButton.clicked.connect(self.AddProductToUsed)
            self.ProductTable.setRowCount(self.ProductTable.rowCount() + 1)
            self.ProductTable.setItem(self.ProductTable.rowCount() - 1, 0, QTableWidgetItem(ProductName))
            self.ProductTable.setItem(self.ProductTable.rowCount() - 1, 1, QTableWidgetItem(ProductRadius))
            self.ProductTable.setItem(self.ProductTable.rowCount() - 1, 2, QTableWidgetItem(ProductHeight))
            self.ProductTable.setItem(self.ProductTable.rowCount() - 1, 3, QTableWidgetItem(ProductWeight))
            self.ProductTable.setCellWidget(self.ProductTable.rowCount() - 1, 4, self.ProductQuantity)
            self.ProductTable.setCellWidget(self.ProductTable.rowCount() - 1, 5, self.AddButton)
            self.ProductTable.setCellWidget(self.ProductTable.rowCount() - 1, 6, self.DeleteButton)
            self.ProductWindow.close()

    # Add Button for Product table to The used Products Table
    def AddProductToUsed(self):
        #if the quantity is empty not add the product and show an error message
        if QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).text()).text() == '' or QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).text()).text() == 'Quantity is Empty' or QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).text()).text() == '0':
            QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).setStyleSheet('background-color:red'))
            QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).setPlaceholderText('Quantity is Empty'))
        else:
            QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).setStyleSheet('background-color:white'))
            self.DeleteButton = QPushButton(self)
            self.DeleteButton.setText('Delete')
            self.DeleteButton.setStyleSheet('font-size:20px')
            self.DeleteButton.setStyleSheet('font-weight:bold')
            self.DeleteButton.setStyleSheet('background-color:red')
            self.DeleteButton.clicked.connect(self.DeleteProductFromUsed)
            self.UsedProductTable.setRowCount(self.UsedProductTable.rowCount() + 1)
            self.UsedProductTable.setItem(self.UsedProductTable.rowCount() - 1, 0, QTableWidgetItem(self.ProductTable.item(self.ProductTable.currentRow(), 0).text()))
            self.UsedProductTable.setItem(self.UsedProductTable.rowCount() - 1, 1, QTableWidgetItem(self.ProductTable.item(self.ProductTable.currentRow(), 1).text()))
            self.UsedProductTable.setItem(self.UsedProductTable.rowCount() - 1, 2, QTableWidgetItem(self.ProductTable.item(self.ProductTable.currentRow(), 2).text()))
            self.UsedProductTable.setItem(self.UsedProductTable.rowCount() - 1, 3, QTableWidgetItem(self.ProductTable.item(self.ProductTable.currentRow(), 3).text()))
            self.UsedProductTable.setItem(self.UsedProductTable.rowCount() - 1, 4, QTableWidgetItem(self.ProductTable.cellWidget(self.ProductTable.currentRow(), 4).text()))
            self.UsedProductTable.setCellWidget(self.UsedProductTable.rowCount() - 1, 5, self.DeleteButton)

    # Delete button for Product Table
    def DeleteProduct(self):
        try:
            self.ProductTable.removeRow(self.ProductTable.currentRow())
        except:
            pass

    # Delete button for The used Product Table
    def DeleteProductFromUsed(self):
        try:
            self.UsedProductTable.removeRow(self.UsedProductTable.currentRow())
        except:
            pass

    # Delete all item of The used Product Table
    def DeleteAllProductFromUsed(self):
        self.UsedProductTable.setRowCount(0)


    # Add Vehicle Button
    def AddVehicle(self):
        VehicleName = self.VehiclesWindow.VehicleName.text()
        VehicleLength = self.VehiclesWindow.VehicleLength.text()
        VehicleWidth = self.VehiclesWindow.VehicleWidth.text()
        VehicleHeight = self.VehiclesWindow.VehicleHeight.text()
        VehicleWeight = self.VehiclesWindow.VehicleWeight.text()

        if VehicleName == '' or VehicleLength == '' or VehicleWidth == '' or VehicleHeight == '' or VehicleWeight == '' or self.VehiclesWindow.radioButtonC.isChecked() == False and self.VehiclesWindow.radioButtonT.isChecked() == False:
            self.ErrorMessage = QMessageBox.warning(self,'Error','Please fill all the blanks')
        else:
            self.VehicleQuantity = QLineEdit(self)
            self.VehicleQuantity.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
            self.DeleteButton = QPushButton(self)
            self.DeleteButton.setText('Delete')
            self.DeleteButton.setStyleSheet('font-size:20px')
            self.DeleteButton.setStyleSheet('font-weight:bold')
            self.DeleteButton.setStyleSheet('background-color:red')
            self.DeleteButton.clicked.connect(self.DeleteVehicle)
            self.AddButton = QPushButton(self)
            self.AddButton.setText('Add')
            self.AddButton.setStyleSheet('font-size:20px')
            self.AddButton.setStyleSheet('font-weight:bold')
            self.AddButton.setStyleSheet('background-color:green')
            self.AddButton.clicked.connect(self.AddVehicleToUsed)
            self.VehicleTable.setRowCount(self.VehicleTable.rowCount() + 1)
            self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 0, QTableWidgetItem(VehicleName))
            if self.VehiclesWindow.radioButtonT.isChecked():
                self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 1, QTableWidgetItem('Truck'))
            elif self.VehiclesWindow.radioButtonC.isChecked():
                self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 1, QTableWidgetItem('Container'))
            self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 2, QTableWidgetItem(VehicleLength))
            self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 3, QTableWidgetItem(VehicleWidth))
            self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 4, QTableWidgetItem(VehicleHeight))
            self.VehicleTable.setItem(self.VehicleTable.rowCount() - 1, 5, QTableWidgetItem(VehicleWeight))
            self.VehicleTable.setCellWidget(self.VehicleTable.rowCount() - 1, 6, self.VehicleQuantity)
            self.VehicleTable.setCellWidget(self.VehicleTable.rowCount() - 1, 7, self.AddButton)
            self.VehicleTable.setCellWidget(self.VehicleTable.rowCount() - 1, 8, self.DeleteButton)
            self.VehiclesWindow.close()

    # Add Vehicle Button for The used Vehicle Table
    def AddVehicleToUsed(self):
        
        if QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).text()).text() == '' or QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).text()).text() == 'Quantity is Empty' or QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).text()).text() == '0':
            QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).setStyleSheet('background-color:red'))
            QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).setPlaceholderText('Quantity is Empty'))
        else:
            QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).setStyleSheet('background-color:white'))
            self.DeleteButton = QPushButton(self)
            self.DeleteButton.setText('Delete')
            self.DeleteButton.setStyleSheet('font-size:20px')
            self.DeleteButton.setStyleSheet('font-weight:bold')
            self.DeleteButton.setStyleSheet('background-color:red')
            self.DeleteButton.clicked.connect(self.DeleteVehicleFromUsed)
            self.UsedVehicleTable.setRowCount(self.UsedVehicleTable.rowCount() + 1)
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 0, QTableWidgetItem(self.VehicleTable.item(self.VehicleTable.currentRow(), 0).text()))
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 1, QTableWidgetItem(self.VehicleTable.item(self.VehicleTable.currentRow(), 1).text()))
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 2, QTableWidgetItem(self.VehicleTable.item(self.VehicleTable.currentRow(), 2).text()))
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 3, QTableWidgetItem(self.VehicleTable.item(self.VehicleTable.currentRow(), 3).text()))
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 4, QTableWidgetItem(self.VehicleTable.item(self.VehicleTable.currentRow(), 4).text()))
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 5, QTableWidgetItem(self.VehicleTable.item(self.VehicleTable.currentRow(), 5).text()))
            self.UsedVehicleTable.setItem(self.UsedVehicleTable.rowCount() - 1, 6, QTableWidgetItem(self.VehicleTable.cellWidget(self.VehicleTable.currentRow(), 6).text()))
            self.UsedVehicleTable.setCellWidget(self.UsedVehicleTable.rowCount() - 1, 7, self.DeleteButton)

    # Delete button for Vehicle Table
    def DeleteVehicle(self):
        try:
            self.VehicleTable.removeRow(self.VehicleTable.currentRow())
        except:
            pass

    # Delete button for The used Vehicle Table
    def DeleteVehicleFromUsed(self):
        try:
            self.UsedVehicleTable.removeRow(self.UsedVehicleTable.currentRow())
        except:
            pass
    
    # Delete all Vehicles from Used Vehicles Table
    def DeleteAllVehiclesFromUsed(self):
        self.UsedVehicleTable.setRowCount(0)





        


class ProductWindow(QWidget):
    def __init__(self):
        super(ProductWindow, self).__init__()
        self.resize(500, 300)

        # Product Name
        self.label = QLabel(self)
        self.label.setGeometry(10, 25, 150, 50)
        self.label.setText('Product Name:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.ProductName = QLineEdit(self)
        self.ProductName.setGeometry(220, 32, 180, 30)
        self.ProductName.setStyleSheet('font-size:20px')

        # Product Size Radius
        self.label = QLabel(self)
        self.label.setGeometry(14, 75, 190, 50)
        self.label.setText('Product Size Radius:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.ProductRadius = QLineEdit(self)
        self.ProductRadius.setPlaceholderText('Radius (cm)')
        self.ProductRadius.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.ProductRadius.setGeometry(220, 82, 150, 30)
        self.ProductRadius.setStyleSheet('font-size:20px')

        # Product Size Height
        self.label = QLabel(self)
        self.label.setGeometry(14, 125, 190, 50)
        self.label.setText('Product Size Height:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.ProductHeight = QLineEdit(self)
        self.ProductHeight.setPlaceholderText('Height (cm)')
        self.ProductHeight.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.ProductHeight.setGeometry(220, 132, 150, 30)
        self.ProductHeight.setStyleSheet('font-size:20px')


        # Product Weight
        self.label = QLabel(self)
        self.label.setGeometry(6, 175, 170, 50)
        self.label.setText('Product Weight:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.ProductWeight = QLineEdit(self)
        self.ProductWeight.setPlaceholderText('Weight (kg)')
        self.ProductWeight.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.ProductWeight.setGeometry(220, 182, 150, 30)
        self.ProductWeight.setStyleSheet('font-size:20px')


        # Add Product Button
        self.buttonAddProduct = QPushButton(self)
        self.buttonAddProduct.setGeometry(10, 240, 150, 50)
        self.buttonAddProduct.setText('Add Product')
        self.buttonAddProduct.setStyleSheet('font-size:20px')
        self.buttonAddProduct.setStyleSheet('font-weight:bold')
        self.buttonAddProduct.setStyleSheet('background-color:green')      






class VehiclesWindow(QWidget):
    def __init__(self):
        super(VehiclesWindow, self).__init__()
        self.resize(500, 400)

        # Vehicle Name
        self.label = QLabel(self)
        self.label.setGeometry(10, 25, 150, 50)
        self.label.setText('Vehicle Name:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.VehicleName = QLineEdit(self)
        self.VehicleName.setGeometry(220, 32, 180, 30)
        self.VehicleName.setStyleSheet('font-size:20px')

        # Vehicle Size Length
        self.label = QLabel(self)
        self.label.setGeometry(14, 75, 190, 50)
        self.label.setText('Vehicle Size Length:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.VehicleLength = QLineEdit(self)
        self.VehicleLength.setPlaceholderText('Length (cm)')
        self.VehicleLength.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.VehicleLength.setGeometry(220, 82, 150, 30)
        self.VehicleLength.setStyleSheet('font-size:20px')

        # Vehicle Size Width
        self.label = QLabel(self)
        self.label.setGeometry(10, 125, 190, 50)
        self.label.setText('Vehicle Size Width:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.VehicleWidth = QLineEdit(self)
        self.VehicleWidth.setPlaceholderText('Width (cm)')
        self.VehicleWidth.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.VehicleWidth.setGeometry(220, 132, 150, 30)
        self.VehicleWidth.setStyleSheet('font-size:20px')

        # Vehicle Size Height
        self.label = QLabel(self)
        self.label.setGeometry(14, 175, 190, 50)
        self.label.setText('Vehicle Size Height:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.VehicleHeight = QLineEdit(self)
        self.VehicleHeight.setPlaceholderText('Height (cm)')
        self.VehicleHeight.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.VehicleHeight.setGeometry(220, 182, 150, 30)
        self.VehicleHeight.setStyleSheet('font-size:20px')

        # Vehicle Weight
        self.label = QLabel(self)
        self.label.setGeometry(4, 225, 170, 50)
        self.label.setText('Vehicle Weight:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')
        self.VehicleWeight = QLineEdit(self)
        self.VehicleWeight.setPlaceholderText('Max Weight (kg)')
        self.VehicleWeight.setValidator(QRegExpValidator(QRegExp("[0-9]{1,5}")))
        self.VehicleWeight.setGeometry(220, 232, 170, 30)
        self.VehicleWeight.setStyleSheet('font-size:20px')

        # Vehicle Type
        self.label = QLabel(self)
        self.label.setGeometry(-4, 275, 170, 50)
        self.label.setText('Vehicle Type:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:20px')

        self.radioButtonT = QRadioButton(self)
        self.radioButtonT.setGeometry(200, 275, 170, 50)
        self.radioButtonT.setText('Truck')
        self.radioButtonT.setStyleSheet('font-size:20px')

        self.radioButtonC = QRadioButton(self)
        self.radioButtonC.setGeometry(300, 275, 170, 50)
        self.radioButtonC.setText('Container')
        self.radioButtonC.setStyleSheet('font-size:20px')

        # Add Vehicle Button
        self.buttonAddVehicle = QPushButton(self)
        self.buttonAddVehicle.setGeometry(10, 325, 150, 50)
        self.buttonAddVehicle.setText('Add Vehicle')
        self.buttonAddVehicle.setStyleSheet('font-size:20px')
        self.buttonAddVehicle.setStyleSheet('font-weight:bold')
        self.buttonAddVehicle.setStyleSheet('background-color:green')
