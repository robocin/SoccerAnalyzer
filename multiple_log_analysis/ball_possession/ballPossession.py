import pandas as pd
from analyzer_common.common.basic.point import Point
from analyzer_common.common.basic.game import Game
from analyzer_common.common.operations.measures import distance

class BallPossession:
    """
        Used to calculate the simple ball possession of the game.

        BallPossession(dataFrame)

        Attributes
        ----------
            private:
                leftSideTeamPossession : int
                    amount of cycles the left team was closest to the ball

                rightSideTeamPossession : int
                    amount of cycles the right team was closest to the ball

                currentGame : common.basic.game.Game
                    a Game object of the current game

                BALL_X_COLUMN : int
                    ball x position in the dataframe

                BALL_Y_COLUMN : int
                    ball y position in the dataframe

        Methods
        -------
            private:
                filterPlaymode(playmode : str) -> None
                    filters the currentGame dataframe and returns a filtered copy

                closestPlayerSide(cycle : int,
                                playerLeftPosition : common.basic.point.Point,
                                playerRightPosition : common.basic.point.Point,
                                ballPositionThisCycle : common.basic.point.Point) -> str
                    returns the closest player of the ball in the cycle passed as argument

                calculate() -> None
                    populates the leftSideTeamPossession and rightSideTeamPossession

            public:
                getCurrentGame() -> pandas.Dataframe
                    returns the dataframe of the current game being analyzed

                get() -> [a,b]
                    returns the leftSideTeamPossession(a) and rightSideTeamPossession(b) in percentual

                newGame(game : DataFrame)
                    updates the object with new game and calculates the new ball possession

    """
    def __init__(self, dataFrame : Game):
        self.__leftSideTeamPossession = 0
        self.__rightSideTeamPossession = 0
        self.__currentGame = dataFrame
        self.__BALL_X_COLUMN = 10
        self.__BALL_Y_COLUMN = 11
        self.__calculate()

    def newGame(self, dataFrame : Game):
        self.__currentGame = dataFrame
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

        closestRight = 1000
        closestLeft = 1000

        for i in range(1, 11):
            playerLeftPosition.x = self.__currentGame.loc[currentCycle, "player_l{}_x".format(i)]
            playerLeftPosition.y = self.__currentGame.loc[currentCycle, "player_l{}_y".format(i)]

            playerLeftDistance = distance(playerLeftPosition, ballPositionThisCycle)

            if playerLeftDistance <= closestLeft:
                closestLeft = playerLeftDistance

            playerRightPosition.x = self.__currentGame.loc[currentCycle, "player_r{}_x".format(i)]
            playerRightPosition.y = self.__currentGame.loc[currentCycle, "player_r{}_y".format(i)]

            playerRightDistance = distance(playerRightPosition, ballPositionThisCycle)

            if playerRightDistance <= closestRight:
                closestRight = playerRightDistance

        if closestLeft < closestRight:
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
