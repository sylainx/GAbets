from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Models.MatchsModel import MatchsModel
# models
from Models.PriorityModel import PrioritiesModel
from Models.TeamsModel import TeamsModel
from views.Admin.Matchs.MatchsView import MatchsView
# views


class AdminMatchsController(object):

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__()

        # controllers

        # views
        self.matchView = MatchsView(self.parent)

        # models
        self.team_model = TeamsModel()
        self.priority_model = PrioritiesModel()
        self.matchs_model = MatchsModel()

    def start(self, ):
        # Option to show widget
        self.matchView.show()
        # self.matchView.setVisible(True)
        # end
        self.loadLineUpsFunc() # remplir view kap genyen list match yo
        self.loadMatchsFunc()
        self.matchView.cancelBtn.clicked.connect(
            lambda: self.cancelMatchsView())
        self.matchView.category_teams_CbBx.currentIndexChanged.connect(
            lambda: self.findSelectedCategory())
        self.matchView.saveBtn.clicked.connect(lambda:self.saveRandomMatch())

        list_of_category_match = self.priority_model.show()

        if len(list_of_category_match) > 0:
            self.matchView.listTypeOfMatch(list_of_category_match)

        # show register Widget

    # end start Match ui

    def findSelectedCategory(self):
        selected_text = self.matchView.category_teams_CbBx.currentText()
        self.matchView.team_on_category_CbBx.clear()

        if selected_text is not None:
            selectedID = self.findCategoryById(selected_text)
            if selectedID:
                #
                self.list_team_selected = self.team_model.searchByCategoryId(selectedID)                
                if self.list_team_selected:
                    self.matchView.listTeamOnCategory(self.list_team_selected)                
                    list_dict_match= self.loadMatchsFunc()
                    if list_dict_match:
                        self.matchView.loadDatas(list_dict_match)


        else:
            print("Veuillez choisir une valeur correcte")

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
        Get random match and save them in DB
        '''
        # print(f"LIST Team selected: {self.list_team_selected}")
        
    
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
            
            listMatch_filter=list()
            for i in list_of_matchs:
                match_id=i[0]

                # team_model.search(...) return: (id, img, title,...)
                # pass [2] to have team 'title'
                hTeamFind = self.team_model.search(i[1])[2]
                awTeamFind = self.team_model.search(i[2])[2]

                # priority_model.search(...) return: (id, title,...)
                # pass [1] to have category 'title'
                categ = self.priority_model.search(i[3])[1]
                match_date=i[4]
                
                infoMatch_filter={
                    'match_id':match_id,
                    'home_team':hTeamFind,
                    'away_team':awTeamFind,
                    'category':categ,
                    'date_match':match_date,
                }
                listMatch_filter.append(infoMatch_filter)
            # end loop
            return listMatch_filter
        # end verification
        return False

    

    def getTeamById(self,team_id):    
        team = self.team_model.search(team_id)
        if team:
            return team

        return False

    def cancelMatchsView(self):        
        """ 
        Close Widget when called

        Arguments:
            None
        """
        
        self.matchView.close()

    def test(self):
        print("Test")
