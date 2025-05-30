import random

from player import Player

class Match:
    def __init__(self):
        self._cards: list[Cards] = None
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
        self._current_round = 0

        self.selected_location = None


        self._board = []
        for i in range(5):
            self._board.append(9*[None])
        
        self._adjacencyMatrix = [0]*15
        for i in range(15):
            self._adjacencyMatrix[i] = [0]*27

    def get_turn_player(self):
        if self._local_player.get_turn():
            return self._local_player
        elif self._remote_player1.get_turn():
            return self._remote_player1
        elif self._remote_player2.get_turn():
            return self._remote_player2
        elif self._remote_player3.get_turn():
            return self._remote_player3
        elif self._remote_player4.get_turn():
            return self._remote_player4
        else:
            return None


    def start_match(self, players: list[str]) :
        print("match constructor")
        self._match_status = "in progress"

        self._local_player.reset()
        self._local_player.initialize(players[0][1])

        self._remote_player1.reset()
        self._remote_player1.initialize(players[1][1])

        self._remote_player2.reset()
        self._remote_player2.initialize(players[2][1])

        self._remote_player3.reset()
        self._remote_player3.initialize(players[3][1])

        self._remote_player4.reset()
        self._remote_player4.initialize(players[4][1])

        move = self.start_new_hand()

        if int(players[0][2]) == 1:
            self._local_player.switch_turn()
        elif int(players[1][2]) == 1 :
            self._remote_player1.switch_turn()
        elif int(players[2][2]) == 1 :
            self._remote_player2.switch_turn()
        elif int(players[3][2]) == 1 :
            self._remote_player3.switch_turn()
        else:
            self._remote_player4.switch_turn()
        
        return move
    
    def start_round(self):
        


    def start_new_hand(self):
        self.clean_board()
        cards = self.distribuir_cartas()
        random.shuffle(self._cards)
        local_player_cards = cards[0]
        remote_player1_cards = cards[1]
        remote_player2_cards = cards[2]
        remote_player3_cards = cards[3]
        remote_player4_cards = cards[4]

        self._local_player.receive_cards(local_player_cards)
        self._remote_player1.receive_cards(remote_player1_cards)
        self._remote_player2.receive_cards(remote_player2_cards)
        self._remote_player3.receive_cards(remote_player3_cards)
        self._remote_player4.receive_cards(remote_player4_cards)

        move = {
            "move_type": "new_hand",
            "local_player_cards": [remote_player1_cards,
                                   remote_player2_cards,remote_player3_cards,
                                   remote_player4_cards],
            "remote_player_cards": local_player_cards,
            "match_status": "progress",
        }

        return move

    def distribuir_cartas(self):
        players_cards = []
        for i in range(5):
            temp_cards = []
            for j in range(6):
                card = self._cards.pop()
                temp_cards.append(card)
            players_cards.append(temp_cards)

        return players_cards
    
    def clean_board(self):
        # melhorar isso aqui
        self._cartas_jogadas = [[]]

    def get_status(self):
        game_status = dict()

        end_of_match = self.verify_end_match()
        game_status["winner"] = end_of_match

        score = (self._local_player_points,self._remote_player1_points,self._remote_player2_points,self._remote_player3_points,self._remote_player4_points)
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
    def select_board_position(self,grid_line,grid_column):
        """
        Coloca uma carta no tabuleiro do jogo Saboteur
        :param grid_line: linha do tabuleiro onde a carta será colocada
        :param grid_column: coluna do tabuleiro onde a carta será colocada
        :param card: carta a ser colocada no tabuleiro
        :return: dicionário com informações da jogada ou None se movimento inválido
        """
        turn_player = self.get_turn_player()
        #arrumar essa bomba
        card = turn_player.selected_card
        move_info = {}
        # Verifica se a posição está dentro dos limites do tabuleiro
        if grid_line > 10 or grid_column > 6:
            self.match_status = 3  #    waiting piece or origin selection (first action)
            self.regular_move = False
        else:
            # Verifica se a posição está adjacente a cartas já colocadas (exceto para a primeira jogada)
            if self.verify_adjacent_positions(grid_line, grid_column):
                # Coloca a carta no tabuleiro
                self._board[grid_line][grid_column] = card
                turn_player.remove_card_from_hand(card)
                self.update_adjacency_matrix(grid_line,grid_column)
            
            # Verifica se completou um caminho até o ouro
            if self.check_path_to_gold():
                move_info["game_status"] = "gold_found"
                self.game_status = "gold_found"
                self.update_scores()
            else:
                move_info["game_status"] = "next_turn"
                self.pass_turn_to_next_player()
                self.game_status = "waiting_card_selection"
            
            # Prepara informações da jogada para enviar aos outros jogadores
            move_info["player"] = turn_player.id
            move_info["card_type"] = card.card_type
            move_info["card_direction"] = card.direction if hasattr(card, 'direction') else None
            move_info["position_line"] = grid_line
            move_info["position_column"] = grid_column
            
        return move_info
    
    def verify_adjacent_positions(self,line,colum):
        if(line+1 > 8): 
            north = None
        else:
            north = self._board[line+1][colum]
        if(line-1 < 0):
            south = None
        south = self._board[line-1][colum]
        east = self._board[line][colum-1]
        west = self._board[line][colum+1]


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
    
    def select_card(self, position: int):
        turn_player = self.get_turn_player()
        self.regular_move = True
        hands_card = turn_player.get_cards
        card = hands_card[position]        
        turn_player.set_selected_card(card)
        self.match_status = 4  #   move occurring (waiting second action)
        
    def get_match_status():

        
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
    
    def shiftId(self):
        pass
    
    def setPlayersHands(self):
        pass
    
    def setDeck(self):
        pass
    
    def receive_start(self, players: list[str]):
        pass
    def placeGoalCardsOnBoard(self):
        pass
    
    def rotateCard(self):
        pass