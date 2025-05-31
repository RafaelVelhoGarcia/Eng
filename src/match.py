import random

from goal_card import GoalCard

from card import Card

from path_card import PathCard

from player import Player

class Match:
    def __init__(self):
        self._deck: list[Card] = None
        self.reset_deck()

        self._round = 0

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

        self._visMatrix = [0]*15
        for i in range(15):
            self._visMatrix[i] = [0]*27


    def reset_deck(self):
        self._deck = []  # Clear the deck before resetting
        # x1 cards (7 in the image)
        for i in range(7):
            self._deck.append(PathCard(i, True, True, True, True, True, True))
        
        # x2 cards (3 in the image)
        for i in range(3):
            self._deck.append(PathCard(i, True, True, False, False, True, True))
        
        # x3 cards (4 in the image - 1 in row 3 and 3 in row 4)
        for i in range(4):
            self._deck.append(PathCard(i, True, True, False, True, True, True))
        
        # x4 cards (2 in the image - first and fifth in first row)
        for i in range(2):
            self._deck.append(PathCard(i, True, True, True, False, False, True))
        
        # x5 cards (3 in the image - second, third, and sixth in first row)
        for i in range(30):
            self._deck.append(PathCard(i, True, True, True, False, True, True))
        
        # x6 cards (1 in the image - second in third row)
        self._deck.append(PathCard(0, True, False, False, True, True, True))
        print("Encheu ")
        print(self._deck)
        print("._.")
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
        pass


    def start_new_hand(self):
        random.shuffle(self._deck)
        cards = self.distribuir_cartas()
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
        print("distriboi cartas")
        self.reset_deck()
        players_cards = []

        for i in range(5):
            temp_cards = []
            for j in range(6):
                card = self._deck.pop()
                temp_cards.append(card)
            players_cards.append(temp_cards)

        return players_cards
    
    def clean_board(self):
        # melhorar isso aqui
        self._board = []
        for i in range(5):
            self._board.append(9*[None])

    def verify_end_match(self):
        if self._round == 3:
            # acabousse tudo
            return 1
        else:
            # A partida ainda não terminou.
            return 0


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
        print("cheguei no select_board_pos")
        """
        Coloca uma carta no tabuleiro do jogo Saboteur
        :param grid_line: linha do tabuleiro onde a carta será colocada
        :param grid_column: coluna do tabuleiro onde a carta será colocada
        :param card: carta a ser colocada no tabuleiro
        :return: dicionário com informações da jogada ou None se movimento inválido
        """
        turn_player = self.get_turn_player()
        #arrumar essa bomba
        card_tuple = turn_player.get_selected_card()

        if isinstance(card_tuple, tuple):
            card_only = card_tuple[0]

        move_info = {}
        # Verifica se a posição está dentro dos limites do tabuleiro
        if grid_line > 10 or grid_column > 6:
            self.match_status = 3  #    waiting piece or origin selection (first action)
            self.regular_move = False
        else:
            # Verifica se a posição está adjacente a cartas já colocadas (exceto para a primeira jogada)
            if self.verify_adjacent_positions(grid_line, grid_column):
                print("passou pelo verify adjacente position")
                # Coloca a carta no tabuleiro
                self._board[grid_line][grid_column] = card_only
                turn_player.remove_card_from_hand(card_tuple)
                self.update_adjacency_matrix(grid_line,grid_column,card_only)
            
            # Verifica se completou um caminho até o ouro
            if self.check_path_to_gold():
                move_info["game_status"] = "gold_found"
                self.game_status = "gold_found"
                self.update_scores(grid_line,grid_column)
            else:
                print("não achou ouro segue o bAILE")

                move_info["game_status"] = "next_turn"
                print("proximo metodo nem existe")
                self.pass_turn_to_next_player()
                self.game_status = "waiting_card_selection"
            
            # Prepara informações da jogada para enviar aos outros jogadores
            move_info["player"] = turn_player.get_player_id()
            move_info["card_type"] = card_tuple.card_type
            move_info["card_direction"] = card_tuple.direction if hasattr(card_tuple, 'direction') else None
            move_info["position_line"] = grid_line
            move_info["position_column"] = grid_column
            
        return move_info
    
    def pass_turn_to_next_player():
        


    def check_path_to_gold(self):
        """Check if there's a valid path from the given position to a gold card using BFS."""
        line = 2
        column = 0
        def in_board(l, c):
            """Check if coordinates are within board boundaries."""
            return 0 <= l < 15 and 0 <= c < 27
        
        # Directions: north, south, east, west
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        # Initialize visited matrix
        vis_matrix = [[0 for _ in range(27)] for _ in range(15)]
        
        # Convert logical coordinates to board matrix coordinates
        new_line = 3 * line + 1  # Center of the card
        new_column = 3 * column + 1
        
        queue = [(new_line, new_column)]
        vis_matrix[new_line][new_column] = 1
        
        while queue:
            current_l, current_c = queue.pop(0)
            
            # Check if current position is a gold card
            if self.is_gold_card(current_l, current_c):
                return True
            
            # Explore all four directions
            for dl, dc in directions:
                nl = current_l + dl
                nc = current_c + dc

                # Check if neighbor is within bounds and not visited
                if in_board(nl, nc) and vis_matrix[nl][nc] == 0:
                    # Check if there's a valid path between current cell and neighbor
                    if (self._adjacencyMatrix[nl][nc] == 1):
                        vis_matrix[nl][nc] = 1
                        queue.append((nl, nc))
        
        return False

    def is_gold_card(self, l, c):
        """Check if the given position contains a gold card."""
        card = self._board[l // 3][c // 3]
        return isinstance(card, GoalCard) and card.is_gold()

    def update_adjacency_matrix(self,line,colum,card):
        new_line = 3*line
        new_colum = 3*colum
        if (self._board[line][colum].get_north()):
            self._adjacencyMatrix[line+1][colum] = 1
        if (self._board[line][colum].get_south()):
            self._adjacencyMatrix[line-1][colum] = 1
        if (self._board[line][colum].get_east()):
            self._adjacencyMatrix[line][colum-1] = 1
        if (self._board[line][colum].get_west()):
            self._adjacencyMatrix[line][colum+1] = 1

    def verify_adjacent_positions(self,line,colum):
        current_card = self._board[line][colum]
        if(line+1 > 5): 
            north = None
        else:
            north = self._board[line+1][colum]
        if(line-1 < 0):
            south = None
        else:
            south = self._board[line-1][colum]
        if colum-1 < 0:
            east = None
        else:
            east = self._board[line][colum-1]
        if colum+1 > 8:
            west = None
        else:
            west = self._board[line][colum+1]
        
        if (north == None or not(north.get_south() ^ current_card.get_north())):
            if (south == None or not(south.get_north() ^ current_card.get_south())):
                if (east == None or not(east.get_west() ^ current_card.get_east())):
                    if (west == None or not(west.get_east() ^ current_card.get_west())):
                        return True
        return False

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
        hands_card = turn_player.get_cards()
        card = hands_card[position]        
        turn_player.set_selected_card(card)
        self.match_status = 4  #   move occurring (waiting second action)
        print("Fez tudo em select card")
        print(turn_player.get_cards())
        
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