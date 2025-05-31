import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk

from PIL import Image, ImageTk


from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from match import Match

# Constantes para o tamanho das cartas
CARD_WIDTH = 60
CARD_HEIGHT = 95

class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.receive_start = None
        self.receive_move = None
        
        self._main_window = tk.Tk()
        self._main_window.title("Saboteur")
        self._main_window.geometry("800x800")
        
        self.fill_window()

        self._dog_server_interface = DogActor()
        
        # Inicialização do jogador
        player_name = simpledialog.askstring("Player", "Qual o seu nome?")
        message = self._dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        self._match = Match()

        self._popup: tk.Toplevel = None

    def fill_window(self):
        self._gold_values = []
        self._gold_player1 = tk.StringVar()
        self._gold_player2 = tk.StringVar()
        self._gold_player3 = tk.StringVar()
        self._gold_player4 = tk.StringVar()
        self._gold_player5 = tk.StringVar() 
        
        self._gold_local_player = tk.StringVar()

        self._gold_player1.set("0")
        self._gold_player1.set("1")

        self._gold_values.append(self._gold_player1)
        self._gold_values.append(self._gold_player2)
        self._gold_values.append(self._gold_player3)
        self._gold_values.append(self._gold_player4)
        self._gold_values.append(self._gold_player5)
        
        self._your_team = tk.StringVar()
        self._ind_turno = tk.StringVar()
        self._vitorias_mao_remoto = tk.StringVar()
        self._vitorias_mao_local = tk.StringVar()
        self._placar_jogador_remoto = tk.StringVar()
        self._placar_jogador_local = tk.StringVar()

        for widget in self._main_window.winfo_children():
            widget.destroy()
        
        self._menu = tk.Menu(self._main_window)
        game_bar = tk.Menu(self._menu, tearoff=0)
        game_bar.add_command(
            label="Start match", 
            command=self.start_match,
        )
        game_bar.add_command(
            label="Exit", 
            command=self.quit
        )
        self._menu.add_cascade(label="Game", menu=game_bar)

        self._main_window.config(menu=self._menu)

        # Status
        self.status_label = tk.Label(self._main_window, text=self._your_team, font=("Arial", 12))
        self.status_label.pack(pady=2)
        self.status_turn_label = tk.Label(self._main_window, text=self._ind_turno, font=("Arial", 12))
        self.status_turn_label.pack(pady=2)
        
        # Frame principal
        main_frame = tk.Frame(self._main_window)
        main_frame.pack(padx=5, pady=5)
        
        # Tabuleiro
        board_frame = tk.Frame(main_frame, bd=1, relief=tk.GROOVE)
        board_frame.pack(side=tk.LEFT, padx=2)
        self.board_slots = []
        
        for row in range(5):
            row_slots = []
            for col in range(9):
                slot = tk.Frame(board_frame, width=CARD_WIDTH, height=CARD_HEIGHT, bd=1, relief=tk.RIDGE, bg="white")
                slot.grid(row=row, column=col, padx=1, pady=1)
                slot.grid_propagate(False)
                slot.bind("<Button-1>", lambda event, r=row, c=col: self.on_board_click(r, c))
                row_slots.append(slot)
            self.board_slots.append(row_slots)
        
        # Lista de Jogadores
        players_frame = tk.Frame(main_frame, bd=1, relief=tk.GROOVE)
        players_frame.pack(side=tk.LEFT, padx=2, fill=tk.Y)
        self.player_frames = []
        
        for i in range(5):
            player_container = tk.Frame(players_frame, bd=1, relief=tk.RIDGE, padx=2, pady=2)
            player_container.pack(pady=1, fill=tk.X)
            player_container.bind("<Button-1>", lambda event, idx=i: self.on_player_click(idx))
            
            label = tk.Label(player_container, text=f"Player {i+1} - Ouro: {self._gold_values[i]}", font=("Arial", 10))
            label.pack()
            
            cards_frame = tk.Frame(player_container)
            cards_frame.pack(pady=1)
            card_slots = []
            for j in range(3):
                slot = tk.Frame(cards_frame, width=CARD_WIDTH-10, height=CARD_HEIGHT-10,
                              bd=1, relief=tk.SUNKEN, bg="lightgrey")
                slot.pack(side=tk.LEFT, padx=1)
                slot.pack_propagate(False)
                card_slots.append(slot)
            self.player_frames.append({
                "container": player_container,
                "label": label,
                "card_slots": card_slots
            })
        
        # Área Inferior
        bottom_frame = tk.Frame(self._main_window)
        bottom_frame.pack(pady=5)
        
        # Mão do jogador
        self._hand_frame = tk.Frame(bottom_frame, bd=1, relief=tk.GROOVE)
        self._hand_frame.pack(side=tk.LEFT, padx=5)
        
        tk.Label(self._hand_frame, text="Mão", font=("Arial", 10)).pack()
        
         # Create the container for hand cards that will use grid
        self.hand_cards_container = tk.Frame(self._hand_frame)
        self.hand_cards_container.pack()

        #self.hand_slots = []
        self.__card_tks = []
        
        # Pilha de Descarte
        discard_frame = tk.Frame(bottom_frame, bd=1, relief=tk.GROOVE)
        discard_frame.pack(side=tk.LEFT, padx=5)
        tk.Label(discard_frame, text="Descarte", font=("Arial", 10)).pack()
        self.discard_slot = tk.Frame(discard_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
                                    bd=1, relief=tk.RIDGE, bg="white")
        self.discard_slot.pack()
        self.discard_slot.pack_propagate(False)
        self.discard_slot.bind("<Button-1>", self.on_discard_click)



    def start_match(self):
        match_status = self._match.get_match_status()

        if match_status == "sem partida em andamento":
            start_status = self._dog_server_interface.start_match(5)
            
            code = start_status.get_code()
            message = start_status.get_message()
            
            print("consegui o code")
            
            if code == "0" or code == "1":
                messagebox.showinfo(message=message)
            elif code == "2":
                print("AUUUU")
                players = start_status.get_players()
                print("BUUUU")
                move = self._match.start_match(players)
                print("fez o start_martch")
                self._dog_server_interface.send_move(move)
                game_status = self._match.get_status()
                print("fez o send_move")
                self.update_interface(game_status)
                messagebox.showinfo(message=message)

            self._match.start_round()



    def update_interface(self, game_status: dict):
        # Atualiza informações do turno
        your_turn = game_status.get("your_turn", False)
        self._ind_turno.set("Seu turno" if your_turn else "Turno do oponente")
        
        # Atualiza placar de ouro dos jogadores
        scores = game_status.get("score", [0, 0, 0, 0, 0])
        self._gold_local_player.set(f"Você - Ouro: {scores[0]}")
        self._gold_player1.set(f"Jogador 1 - Ouro: {scores[1]}")
        self._gold_player2.set(f"Jogador 2 - Ouro: {scores[2]}")
        self._gold_player3.set(f"Jogador 3 - Ouro: {scores[3]}")
        self._gold_player4.set(f"Jogador 4 - Ouro: {scores[4]}")
        
        # Atualiza time do jogador
        team = game_status.get("your_team", "Desconhecido")
        self._your_team.set(f"Seu time: {team}")
        
        if hasattr(self, 'hand_cards_container'):
            for widget in self.hand_cards_container.winfo_children():
                widget.destroy()
        else:
            self.hand_cards_container = tk.Frame(self._hand_frame)
            self.hand_cards_container.pack()
        
        # Atualiza cartas na mão do jogador
        local_player_cards = game_status.get("local_player_cards", [])
        
        for col, (card, _) in enumerate(local_player_cards):
            try:
                card_str = card.to_string()
                card_img = Image.open(f"../images/cartas/{card_str}.png")
                card_img = card_img.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
                
                card_tk = ImageTk.PhotoImage(card_img)
                self.__card_tks.append(card_tk)  # Keep reference
                
                card_label = ttk.Label(self.hand_cards_container, image=card_tk)
                card_label.image = card_tk  # Additional reference
                card_label.grid(row=0, column=col, padx=2)
                
                card_label.bind(
                    "<Button-1>", 
                    lambda event, c=col: self.on_hand_click(c)
                )
            except Exception as e:
                print(f"Erro ao carregar carta {card_str}: {e}")
        
        # Atualiza tabuleiro
        board_state = game_status.get("board", [])
        for row in range(5):
            for col in range(9):
                # Limpa o slot antes de adicionar nova carta
                for widget in self.board_slots[row][col].winfo_children():
                    widget.destroy()
                
                # Adiciona carta se existir na posição
                if row < len(board_state) and col < len(board_state[row]):
                    card = board_state[row][col]
                    if card:  # Se há uma carta nesta posição
                        try:
                            card_str = card.to_string()
                            card_img = Image.open(f"../images/cartas/{card_str}.png")
                            card_img = card_img.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
                            
                            card_tk = ImageTk.PhotoImage(card_img)
                            label = ttk.Label(self.board_slots[row][col], image=card_tk)
                            label.image = card_tk  # Mantém referência
                            label.pack()
                        except Exception as e:
                            print(f"Erro ao carregar carta no tabuleiro {row},{col}: {e}")
        
        # Atualiza descarte
        discard_pile = game_status.get("discard", [])
        for widget in self.discard_slot.winfo_children():
            widget.destroy()
        
        if discard_pile:
            try:
                top_card = discard_pile[-1]
                card_str = top_card.to_string()
                card_img = Image.open(f"../images/cartas/{card_str}.png")
                card_img = card_img.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
                
                card_tk = ImageTk.PhotoImage(card_img)
                label = ttk.Label(self.discard_slot, image=card_tk)
                label.image = card_tk
                label.pack()
            except Exception as e:
                print(f"Erro ao carregar carta no descarte: {e}")

    def receive_move(self, a_move):
        self._match.receive_move(a_move)  # Pass the move to the match
        game_status = self._match.get_status()
        self.update_interface(game_status)  # Pass the status to update

    def quit(self):
        self._main_window.destroy()

    def on_board_click(self, row, col):
        print(f"Board clicked at row {row}, column {col}")
        match_status = self._match.get_match_status()
        print("match:",match_status)
        if match_status == "in progress":
            print("cachorro belga")
            move_to_send = self._match.select_board_position(row, col)
            game_state = self._match.get_status()
            self.update_interface(game_state)
            if bool(move_to_send):
                self.dog_server_interface.send_move(move_to_send)

    def on_player_click(self, player_idx):
        print(f"Player {player_idx+1} clicked")

    def on_hand_click(self, card_idx):
        print(f"Hand card {card_idx} clicked")
        self._match.select_card(card_idx)

    def on_discard_click(self, event):
        print("Discard pile clicked")

    def receive_start(self, start_status):
        pass

        pass

    def mainloop(self):
        self._main_window.mainloop()

# Para executar a interface
if __name__ == "__main__":
    interface = PlayerInterface()
    interface.mainloop()