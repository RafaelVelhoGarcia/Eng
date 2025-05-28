import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

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
        self.status_label = tk.Label(self._main_window, text="Você é um Sabotador!", font=("Arial", 12))
        self.status_label.pack(pady=2)
        
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
            
            label = tk.Label(player_container, text=f"Player {i+1} - Ouro: 0", font=("Arial", 10))
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
        hand_frame = tk.Frame(bottom_frame, bd=1, relief=tk.GROOVE)
        hand_frame.pack(side=tk.LEFT, padx=5)
        tk.Label(hand_frame, text="Mão", font=("Arial", 10)).pack()
        self.hand_slots = []
        cards_container = tk.Frame(hand_frame)
        cards_container.pack()
        for i in range(6):
            slot = tk.Frame(cards_container, width=CARD_WIDTH, height=CARD_HEIGHT,
                          bd=1, relief=tk.RIDGE, bg="white")
            slot.pack(side=tk.LEFT, padx=2)
            slot.pack_propagate(False)
            slot.bind("<Button-1>", lambda event, idx=i: self.on_hand_click(idx))
            self.hand_slots.append(slot)
        
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
        start_status = self._dog_server_interface.start_match(5)
        messagebox.showinfo(message=start_status.get_message())

    def quit(self):
        self._main_window.destroy()

    def on_board_click(self, row, col):
        print(f"Board clicked at row {row}, column {col}")

    def on_player_click(self, player_idx):
        print(f"Player {player_idx+1} clicked")

    def on_hand_click(self, card_idx):
        print(f"Hand card {card_idx} clicked")

    def on_discard_click(self, event):
        print("Discard pile clicked")

    def receive_start(self, start_status):
        pass

    def receive_move(self, a_move):
        pass

    def mainloop(self):
        self._main_window.mainloop()

# Para executar a interface
if __name__ == "__main__":
    interface = PlayerInterface()
    interface.mainloop()