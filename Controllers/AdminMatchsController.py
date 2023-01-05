from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import random
from Models.MatchTeams import MatchTeams
from Models.MatchsModel import MatchsModel
# models
from Models.PriorityModel import PrioritiesModel
from Models.RatioModel import RatioModel
from Models.TeamsModel import TeamsModel
from views.Admin.Matchs.MatchsView import MatchsView
# views


class AdminMatchsController(object):

    def __init__(self, parent, user_id) -> None:
        self.parent = parent
        self.user_id = user_id
        super().__init__()

        # controllers

        # views
        self.matchView = MatchsView(self.parent)

        # models
        self.team_model = TeamsModel()
        self.priority_model = PrioritiesModel()
        self.matchs_model = MatchsModel()
        self.ratios_model = RatioModel()
        self.matchs_team_model = MatchTeams()

    def start(self, ):
        # Option to show widget
        self.matchView.show()
        # self.matchView.setVisible(True)
        # end
        self.loadLineUpsFunc()  # remplir view kap genyen list match yo
        self.loadMatchsFunc()
        self.matchView.cancelBtn.clicked.connect(
            lambda: self.closeMatchsWidget())
        self.matchView.category_teams_CbBx.currentIndexChanged.connect(
            lambda: self.findSelectedCategory())
        self.matchView.saveMatchBtn.clicked.connect(
            lambda: self.saveRandomMatch())

        list_of_category_match = self.priority_model.show()

        if len(list_of_category_match) > 0:
            self.matchView.listTypeOfMatch(list_of_category_match)

        # show register Widget

    # end start Match ui

    def findSelectedCategory(self):
        """
        """
        selected_text = self.matchView.category_teams_CbBx.currentText()
        self.matchView.team_on_category_CbBx.clear()

        if selected_text:
            selectedID = self.findCategoryById(selected_text)
            if selectedID:
                #
                self.priority_id = selectedID
                self.list_team_selected = self.team_model.searchByCategoryId(
                    self.priority_id)
                if self.list_team_selected:
                    self.matchView.listTeamOnCategory(self.list_team_selected)
                    list_dict_match = self.loadMatchsFunc()
                    if list_dict_match:
                        self.matchView.loadDatas(list_dict_match)

        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Veuillez choisir une valeur correcte", QtWidgets.QMessageBox.Ok)

    def findCategoryById(self, name: str) -> int:
        """
        Get ID of a priority

        Arguments:
        - arg1 : name of priority 
        """
        p_find = self.priority_model.searchByName(name)
        if p_find:
            return list(p_find)[0]

        return None

    def saveRandomMatch(self):
        '''
        Get random list of match and save them in DB
        '''
        list_select_id = [t[0] for t in self.list_team_selected]
        random.shuffle(list_select_id)  # shuffle list

        for key, val in enumerate(list_select_id):

            if key % 2 == 1:

                home_team = list_select_id[key]
                move_team = list_select_id[key-1] # remove 1 to byPass IndexError

                list_country = ["ESPAGNE", "FRANCE",
                                "PORTUGAL", "ANGLETERRE", "HAITI"]
                country = random.choice(list_country)

                self.matchs_model.home_team_id = home_team
                self.matchs_model.move_team_id = move_team
                self.matchs_model.priority_id = self.priority_id
                self.matchs_model.country = country
                self.matchs_model.agent_id = self.user_id
                # save match in db
                match_id = self.matchs_model.save()

                # more details
                if match_id:

                    self.matchs_team_model.match_id = match_id
                    self.matchs_team_model.home_team_id = home_team
                    self.matchs_team_model.away_team_id = move_team
                    self.matchs_team_model.save()
                    # 
                    self.loadLineUpsFunc()
                    self.closeMatchsWidget()
                    
                else:
                    QtWidgets.QMessageBox.warning(
                    None, "Important", "Quelque chose s'est mal passé", QtWidgets.QMessageBox.Ok)
    # end saveRandomMatch() 

    def loadLineUpsFunc(self):
        list_dict_matchs = self.loadMatchsFunc()
        if list_dict_matchs:
            return self.matchView.showLineUpFunc(list_dict_matchs)

    def loadMatchsFunc(self):
        """
        Search a list matchs in DB.
        Loop on the result to extract for each iteration:
            - the home team
            - the away team
            - the match category
            - and the match date 
        """
        list_of_matchs = self.matchs_model.show()
        if len(list_of_matchs) > 0:

            listMatch_filter = list()
            for i in list_of_matchs:
                match_id = i[0]
                # team_model.search(...) return: (id, img, title,...)
                # pass [2] to have team 'title'
                hTeamFind = self.team_model.search(i[1])[2]
                awTeamFind = self.team_model.search(i[2])[2]

                # priority_model.search(...) return: (id, title,...)
                # pass [1] to have category 'title'
                categ = self.priority_model.search(i[3])[1]
                match_date = i[4]                
                # lister les choix de pariage
                odds = self.ratios_model.show()
                if odds:
                    dict_odds = {x[1]: x[2] for x in odds}
                else:
                    dict_odds = dict()
                # endlister les choix de pariage

                infoMatch_filter = {
                    'match_id': match_id,
                    'home_team': hTeamFind,
                    'away_team': awTeamFind,
                    'category': categ,
                    'date_match': match_date,
                }
                # ajouter la liste des odds au dict
                infoMatch_filter.update(dict_odds)
                listMatch_filter.append(infoMatch_filter)
            # end loop
            return listMatch_filter
        # end verification
        return False

    def get_match_by_id(self,matchId):
        list_matchs = self.loadMatchsFunc()
        if list_matchs:
            return next(filter(lambda x: x['match_id'] == int(matchId), list_matchs), None)

        return None
    def getTeamById(self, team_id):
        team = self.team_model.search(team_id)
        if team:
            return team

        return None

    def calculate_coefficient(self, pririotyMatch:int, t1Lvl: int, t2Lvl: int, ratioQuote):
        if pririotyMatch != None and t1Lvl !=  None and t2Lvl != None and ratioQuote  != None :
            if t1Lvl < t2Lvl:
                frac = (t2Lvl - t1Lvl) / t2Lvl
            else:
                frac = (t1Lvl - t2Lvl) / t1Lvl

            odds = (frac + pririotyMatch) / 2

            return odds

        return 100

    def closeMatchsWidget(self):
        """ 
        Close Widget when called
        Arguments:
            None
        """        
        self.matchView.close()


    def test(self):
        print("Test")
