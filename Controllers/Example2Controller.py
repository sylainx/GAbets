import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from model import Model
from view import View

class Controller:

    
    def __init__(self):

        # Créer l'application Qt
        self.qt_app = QApplication(sys.argv)

        # Créer le modèle
        self.model = Model()

        # Créer la vue
        self.view = View()

        # Connecter les signaux de la vue aux slots du contrôleur
        self.view.button_clicked.connect(self.button_clicked)
        self.view.item_selected.connect(self.item_selected)

        # Afficher la fenêtre principale
        self.view.show()

        # Exécuter l'application Qt
        sys.exit(self.qt_app.exec_())

    def button_clicked(self):
        # Traiter le clic sur le bouton
        result = self.model.do_something()
        self.view.set_result(result)

    def item_selected(self, item):
        # Traiter la sélection d'un élément dans la liste
        data = self.model.get_item_data(item)
        self.view.display_item_data(data)
