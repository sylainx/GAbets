from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant
from PyQt5.QtWidgets import QListView, QApplication

class MyListModel(QAbstractListModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return self._data[index.row()]
        return QVariant()

    def rowCount(self, index: QModelIndex = QModelIndex()):
        return len(self._data)



class MyController:
    def __init__(self, app: QApplication):
        self._app = app
        self._view = QListView()
        self._model = MyListModel(['item1', 'item2', 'item3'])
        self._view.setModel(self._model)
        self._view.show()

    def run(self):
        self._app.exec_()

if __name__ == '__main__':
    app = QApplication([])
    controller = MyController(app)
    controller.run()
