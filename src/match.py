from Player import Player

class Match:
    def __init__(self):
        self._local_player = Player()
        self._local_remoteplayer1 = Player()
        self._local_remoteplayer2 = Player()
        self._local_remoteplayer3 = Player()
        self._local_remoteplayer4 = Player()
        self._remotePlayers = []
        self._match_status = str = "sem partida em andamento"
        self._deck = []
        self.current_round = 0
        self.board = []
        for i in range(5):
            board = 9*[None]
        self._adjacencyMatrix = [0]*15
        for i in range(15):
            self._adjacencyMatrix[i] = [0]*27

    def selectPlayer(self,id):
        player = self._remotePlayers[id] 
        return player
    
    def getPlayer(self):
        return self._local_player
    
    def checkRepair():
        pass        
    def prepareMove():
        pass
    def popCardFromDeck():
        pass
    def receiveMove(self, move: dict):
        pass
    
    def removeCardFromPosition(self):
        pass
    
    def updateAdjacencyMatrix(self):
        pass
        
    def setCardToPosition(self):
        pass
    
    def selectedBordPosition(self, cord: tuple[int, int]):
        pass
    
    def isPositionEmpty(self) -> bool:
        pass
    
    def verifyAdjacentPositions(self) -> bool:
        pass
    
    def verifyPath(self) -> list[tuple[int, int]]:
        pass
    
    def revealTreasures(self):
        pass
    
    def discardSelectedCard(self):
        pass
    
    def selectCard(self, position: int):
        pass
    
    def hasCardSelected(self) -> bool:
        pass
    
    def endRound(self):
        pass
    
    def distributeGold(self):
        pass
    
    def clearBoard(self):
        pass
    
    def restoreDeck(self):
        pass
    
    def displayWinner(self):
        pass
    
    def startRound(self):
        pass
    
    def shiftId(self):
        pass
    
    def setPlayersHands(self):
        pass
    
    def setDeck(self):
        pass
    
    def startMatch(self):
        pass
    
    def receive_start(self, players: list[str]):
        self._match_status = "em progresso"
        self._local_player.reset()
        self._local_player.initilize(players[0][1])
        for i in range(4):
            self.player.reset()
            self.player.initialize(players[i][1])
        
        if int(jogadores[0][2]) == 1:
            self._jogador_local.troca_turno()
        else:
            self._jogador_remoto.troca_turno()
            
    
    def placeGoalCardsOnBoard(self):
        pass
    
    def rotateCard(self):
        pass