import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

CARD_WIDTH = 60
CARD_HEIGHT = 84

class SaboteurGame(DogPlayerInterface,tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Saboteur - Interface Tkinter")
        
        # Adicionando a barra de menu
        menubar = tk.Menu(self)
        
        # Menu Game
        game_menu = tk.Menu(menubar, tearoff=0)
        game_menu.add_command(label="Start Match", command=self.start_match)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Game", menu=game_menu)
        
        # Configurar a barra de menu na janela principal
        self.config(menu=menubar)
        
        # Status: indica se o jogador local é sabotador ou não
        self.status_label = tk.Label(self, text="Você é um Sabotador!", font=("Arial", 14))
        self.status_label.pack(pady=5)
        
        # Restante do seu código original...
        # Frame principal que conterá o tabuleiro e a lista de jogadores
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)
        
        # ----- Tabuleiro -----
        board_frame = tk.Frame(main_frame, bd=2, relief=tk.GROOVE)
        board_frame.pack(side=tk.LEFT, padx=10)
        self.board_slots = []  # Armazenar referência para cada slot
        
        for row in range(5):
            row_slots = []
            for col in range(9):
                slot = tk.Frame(board_frame, width=CARD_WIDTH, height=CARD_HEIGHT, bd=1, relief=tk.RIDGE, bg="white")
                slot.grid(row=row, column=col, padx=2, pady=2)
                slot.grid_propagate(False)
                # Evento de clique no slot do tabuleiro
                slot.bind("<Button-1>", lambda event, r=row, c=col: self.on_board_click(r, c))
                row_slots.append(slot)
            self.board_slots.append(row_slots)
        
        # ----- Lista de Jogadores -----
        players_frame = tk.Frame(main_frame, bd=2, relief=tk.GROOVE)
        players_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)
        self.player_frames = []
        
        for i in range(5):
            # Cada jogador possui um frame contêiner que será clicável como um todo.
            player_container = tk.Frame(players_frame, bd=2, relief=tk.RIDGE, padx=5, pady=5)
            player_container.pack(pady=5, fill=tk.X)
            # Vincula o clique no frame do jogador
            player_container.bind("<Button-1>", lambda event, idx=i: self.on_player_click(idx))
            
            # Label informando o nome do jogador e a quantidade de ouro
            label = tk.Label(player_container, text=f"Player {i+1} - Ouro: 0", font=("Arial", 12))
            label.pack()
            
            # Frame para comportar 3 slots de cartas (estes slots não possuem eventos individuais)
            cards_frame = tk.Frame(player_container)
            cards_frame.pack(pady=5)
            card_slots = []
            for j in range(3):
                slot = tk.Frame(cards_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
                                bd=1, relief=tk.SUNKEN, bg="lightgrey")
                slot.pack(side=tk.LEFT, padx=3)
                slot.pack_propagate(False)
                card_slots.append(slot)
            self.player_frames.append({
                "container": player_container,
                "label": label,
                "card_slots": card_slots
            })
        
        # ----- Área Inferior: Mão do Jogador e Pilha de Descarte -----
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(pady=10)
        
        # Mão do jogador com 6 slots
        hand_frame = tk.Frame(bottom_frame, bd=2, relief=tk.GROOVE)
        hand_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(hand_frame, text="Mão do Jogador", font=("Arial", 12)).pack(pady=2)
        self.hand_slots = []
        cards_container = tk.Frame(hand_frame)
        cards_container.pack(pady=5)
        for i in range(6):
            slot = tk.Frame(cards_container, width=CARD_WIDTH, height=CARD_HEIGHT,
                            bd=1, relief=tk.RIDGE, bg="white")
            slot.pack(side=tk.LEFT, padx=4)
            slot.pack_propagate(False)
            slot.bind("<Button-1>", lambda event, idx=i: self.on_hand_click(idx))
            self.hand_slots.append(slot)
        
        # Pilha de Descarte
        discard_frame = tk.Frame(bottom_frame, bd=2, relief=tk.GROOVE)
        discard_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(discard_frame, text="Pilha de Descarte", font=("Arial", 12)).pack(pady=2)
        self.discard_slot = tk.Frame(discard_frame, width=CARD_WIDTH, height=CARD_HEIGHT,
                                      bd=1, relief=tk.RIDGE, bg="white")
        self.discard_slot.pack(pady=5)
        self.discard_slot.pack_propagate(False)
        self.discard_slot.bind("<Button-1>", self.on_discard_click)

        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
    
    def start_match(self):
        """Função chamada quando o usuário seleciona Start Match no menu"""
        start_status = self.dog_server_interface.start_match(5)
        message = start_status.get_message()
        messagebox.showinfo(message = message)
    
    # Função chamada ao clicar em um slot do tabuleiro
    def on_board_click(self, row, col):
        print(f"Clicou no tabuleiro na linha {row + 1}, coluna {col + 1}")
    
    # Função chamada ao clicar no contêiner de um jogador
    def on_player_click(self, player_index):
        print(f"Clicou no contêiner do Player {player_index + 1}")
    
    # Função chamada ao clicar em um slot da mão do jogador
    def on_hand_click(self, slot_index):
        print(f"Clicou no slot {slot_index + 1} da mão do jogador")
    
    # Função chamada ao clicar na pilha de descarte
    def on_discard_click(self, event):
        print("Clicou na pilha de descarte")

if __name__ == "__main__":
    app = SaboteurGame()
    app.mainloop()
