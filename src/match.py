from Player import Player

class Match:
    def __init__(self):
        """ self._jogador_local = Jogador()
        self._jogador_remoto = Jogador()

        self._mesa = Mesa()

        self._pontos_jogador_local: int = 0
        self._pontos_jogador_remoto: int = 0

        self._pedido_em_andamento: bool = False
        self._qual_pedido: str = ""
        self._infos_popup: dict = dict()
        self._status_partida: str = "sem partida em andamento"

        self._truco: Truco = Truco()
        self._envido: Envido = Envido()
        self._flor: Flor = Flor()
        self._flor_ou_envido_ja_ocorreu: bool = False
        self._truco_ja_ocorreu: bool = False"""
        self._local_player = Player()
        self._remote_player1 = Player()
        self._remote_player2 = Player()
        self._remote_player3 = Player()
        self._remote_player4 = Player()
        
        self._local_player_points: int = 0
        self._remote_player1_points: int = 0
        self._remote_player2_points: int = 0
        self._remote_player3_points: int = 0
        self._remote_player4_points: int = 0

        self._remote_players = []
        self._remote_players.append(self._remote_player1)
        self._remote_players.append(self._remote_player2)
        self._remote_players.append(self._remote_player3)
        self._remote_players.append(self._remote_player4)
        
        self._match_status : str = "sem partida em andamento"
        self._deck = []
        self.current_round = 0
        self.board = []
        for i in range(5):
            board = 9*[None]
        self._adjacencyMatrix = [0]*15
        for i in range(15):
            self._adjacencyMatrix[i] = [0]*27

    def get_status(self):
        game_status = dict()

        end_of_match = self.verify_end_match()
        game_status["winner"] = end_of_match

        score = (self._local_player_points,self._remote_player1,self._remote_player2,self._remote_player3,self._remote_player4)
        game_status["score"] = score

        local_player_cards = self._local_player.get_cards()
        game_status["local_player_cards"] = local_player_cards

        remote_player1_cards = self._remote_player1.get_cards()  
        game_status["remote_player1_cards"] = remote_player1_cards  

        remote_player2_cards = self._remote_player2.get_cards()  
        game_status["remote_player2_cards"] = remote_player2_cards

        remote_player3_cards = self._remote_player3.get_cards()  
        game_status["remote_player3_cards"] = remote_player3_cards

        remote_player4_cards = self._remote_player3.get_cards()  
        game_status["remote_player4_cards"] = remote_player4_cards

        your_turn = self._local_player.get_turn()  
        game_status["your_turn"] = your_turn  

        return game_status

    def get_match_status(self):
        return self._match_status

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
    def receive_move(self, move: dict):
        move_type = move["move_type"]
        if move_type == "BUILD":
            self.receive_build(move)
        elif move_type == "UNBLOCK":
            self.receive_unblock(move)
        elif move_type == "BLOCK":
            self.receive_block(move)
        elif move_type == "DESTROY":
            self.receive_destroy(move)
        elif move_type == "new_hand":
            self.receive_new_hand(move)
        if move["match_status"] == "next":
            self._local_player.switch_turn()
            self._remote_player1.switch_turn()
            self._remote_player2.switch_turn()
            self._remote_player3.switch_turn()
            self._remote_player4.switch_turn()
    
    
    def receive_build(self, move:dict):
        carta_jogada, id_jogador = move["BUILD"]

    
    
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
    
    def start_match(self):
        pass
    
    def receive_start(self, players: list[str]):
        pass
    def placeGoalCardsOnBoard(self):
        pass
    
    def rotateCard(self):
        pass