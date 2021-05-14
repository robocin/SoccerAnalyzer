import pandas as pd
from common.basic.point import Point
from common.basic.game import Game
from common.operations.measures import distance

class BallPossession:
    def __init__(self, dataFrame : Game):
        self.__leftSideTeamPossession = 0
        self.__rightSideTeamPossession = 0
        self.__currentGame = dataFrame
        self.__BALL_X_COLUMN = 10
        self.__BALL_Y_COLUMN = 11
        self.__calculate()

    def getCurrentGame(self):
        return self.__currentGame

    def __filterPlaymode(self, playmode : str):
        return self.__currentGame[self.__currentGame['playmode'] == playmode]

    def __closestPlayerSide(self,
                            cycle : int,
                            playerLeftPosition : Point,
                            playerRightPosition : Point,
                            ballPositionThisCycle : Point):
        
        currentCycle = cycle
        
        ball_x = self.__currentGame.iloc[currentCycle, self.__BALL_X_COLUMN]
        ball_y = self.__currentGame.iloc[currentCycle, self.__BALL_Y_COLUMN]
        
        ballPositionThisCycle.x = ball_x
        ballPositionThisCycle.y = ball_y

        for i in range(1,11):
            playerLeftPosition.x = self.__currentGame.loc[currentCycle, "player_l{}_x".format(i)]
            playerLeftPosition.y = self.__currentGame.loc[currentCycle, "player_l{}_y".format(i)]

            playerLeftDistance = distance(playerLeftPosition, ballPositionThisCycle)

            playerRightPosition.x = self.__currentGame.loc[currentCycle, "player_r{}_x".format(i)]
            playerRightPosition.y = self.__currentGame.loc[currentCycle, "player_r{}_y".format(i)]

            playerRightDistance = distance(playerRightPosition, ballPositionThisCycle)

            if playerLeftDistance < playerRightDistance:
                return "left"
            else:
                return "right"

            
    def __calculate(self):
        
        filteredGame = self.__filterPlaymode('play_on')

        playerLeftPosition = Point()
        playerRightPosition = Point()
        ballPositionThisCycle = Point()

        for currentCycle, row in filteredGame.iterrows():

            closestSide = self.__closestPlayerSide(currentCycle,
                                                   playerLeftPosition,
                                                   playerRightPosition,
                                                   ballPositionThisCycle)
            
            if closestSide == 'left':
                self.__leftSideTeamPossession += 1
            else:
                self.__rightSideTeamPossession += 1

    def get(self):
        total = self.__leftSideTeamPossession + self.__rightSideTeamPossession
        return [self.__leftSideTeamPossession/total, self.__rightSideTeamPossession/total]
