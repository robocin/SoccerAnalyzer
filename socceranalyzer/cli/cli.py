



class CLI:
    def __init__(self, path:str = ".") -> None:
        self.__folder_path = path
        self.__team_left = TeamData()
        self.__team_right = TeamData()
        self.__filenames = []
        
        self.__time_start = time.time()
        self._get_filenames()
        self._get_team_names()
        self._get_goal_balance()
        self.__time_end = time.time()

    def _get_filenames(self):
        print(f'socceranalyzer.{CONTEXT}: searching for game logs in {self.__folder_path}/')

        os.chdir(self.__folder_path)
        for logname in glob.glob("*.rcg"):
            self.__filenames.append(logname)

        print(f'socceranalyzer.{CONTEXT}: {len(self.__filenames)} logs read')

    def __is_valid_file(self, logname: str):
        if("null" not in logname):
            return True

        print(f'socceranalyzer.{CONTEXT}: invalid file {logname}')
        return False
    
    def __had_penalti_shotout(self, logname):
        team_left = logname.split('-')[3].split('.')[0]   
        return False if team_left.count('_') == 1 else True

    def _get_team_dict(self, team_name):
        if(self.__team_left.data["name"] == team_name):
            return self.__team_left
        else:
            return self.__team_right

    # TODO: Refactor for split array usage
    def _get_team_names(self):
        for logname in self.__filenames:
            if self.__is_valid_file(logname):
                if not self.__had_penalti_shotout(logname):
                    team_right = logname.split('-')[3].split('.')[0]
                    team_left = logname.split('-')[1] 

                    team_left_name = team_left[:-2]
                    team_right_name = team_right[:-2]

                    self.__team_left.data["name"] = team_left_name
                    self.__team_right.data["name"] = team_right_name 
                    break

    def _update_team_scores(self, logname, left_team, right_team):

        team_left_splitted = left_team.split('_')
        team_right_splitted = right_team.split('_')

        team_left_name = team_left_splitted[0]
        team_right_name = team_right_splitted[0]

        team_left_score = team_left_splitted[1]
        team_right_score = team_right_splitted[1]

        if(self.__had_penalti_shotout(logname)):
            team_left_penalti_score = team_left_splitted[2]
            team_right_penalti_score = team_right_splitted[2]
        else:
            team_left_penalti_score = 0
            team_right_penalti_score = 0
        
        self._get_team_dict(team_left_name).data["score_count"] += int(team_left_score)
        self._get_team_dict(team_left_name).data["score_adv"] += int(team_right_score)
        self._get_team_dict(team_left_name).data["penalti_score"] += int(team_left_penalti_score)

        self._get_team_dict(team_right_name).data["score_count"] += int(team_right_score)
        self._get_team_dict(team_right_name).data["score_adv"] += int(team_left_score)
        self._get_team_dict(team_right_name).data["penalti_score"] += int(team_right_penalti_score)

        if int(team_left_score) > int(team_right_score):
            self._get_team_dict(team_left_name).data["victory"] += 1
            self._get_team_dict(team_right_name).data["defeat"] += 1
        elif int(team_left_score) < int(team_right_score):
            self._get_team_dict(team_left_name).data["defeat"] += 1
            self._get_team_dict(team_right_name).data["victory"] += 1
        else:
            self._get_team_dict(team_left_name).data["draw"] += 1
            self._get_team_dict(team_right_name).data["draw"] += 1

    def _get_goal_balance(self):
        print(f'socceranalyzer.{CONTEXT}: interpreting game logs...')
        for logname in self.__filenames:
            if("null" not in logname):
                left_team = logname.split('-')[1]
                right_team = logname.split('-')[3].split('.')[0]

                self._update_team_scores(logname, left_team, right_team)

    def log(self):
        total_games = len(self.__filenames)
        time_span = self.__time_end - self.__time_start
        
        print(f'socceranalyzer.{CONTEXT}: read {total_games} games of {self.__team_left.data["name"]} x {self.__team_right.data["name"]} in {time_span} seconds', "")
        print("\n")
        print(f'==================================== Debug ===================================')
        print(self.__team_left.data)
        print(self.__team_right.data)
        print("\n")

        print(f'==================================== Detail ===================================')
        print(f'{self.__team_left.data["name"]} victories: {(self.__team_left.data["victory"]/total_games)*100}%')
        print(f'{self.__team_left.data["name"]} defeats: {(self.__team_left.data["defeat"]/total_games)*100}%')
        print(f'Draws: {(self.__team_left.data["draw"]/total_games)*100}%')
        print(f'Goals scored: {self.__team_left.data["score_count"]}')
        print(f'Goal balance: {self.__team_left.data["score_count"] - self.__team_left.data["score_adv"]}')
        print(f'Score/taken ratio: {(self.__team_left.data["score_count"] / self.__team_left.data["score_adv"])}')
        print(f'Score per game: {(self.__team_left.data["score_count"]/total_games)}')
        print("\n")

        print(f'================================== Overall ================================')
        print(f'{self.__team_left.data["name"]} victories: {(self.__team_left.data["victory"]/total_games)*100}%')
        print(f'{self.__team_right.data["name"]} victories: {(self.__team_right.data["victory"]/total_games)*100}%')
        print(f'Draws: {(self.__team_left.data["draw"]/total_games)*100}%')

  
CONTEXT='CLI'