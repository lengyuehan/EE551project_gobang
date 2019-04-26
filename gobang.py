import tkinter.messagebox
import tkinter as tk


class Game:

    CORS_COLS: int = 35
    X_ORIGIN_COOR = 32
    Y_ORIGIN_COOR = 38

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('GOBANG')
        self.root.geometry('560x620')
        self.canvas = ''
        self.chess_turn_canvas = ''
        self.var = ''
        self.restart_button = ''
        self.chess_size = 13
        self.piece_color = 'black'
        self.coo_x = [i for i in range(self.X_ORIGIN_COOR, 523, self.CORS_COLS)]
        self.coo_y = [i for i in range(self.Y_ORIGIN_COOR, 529, self.CORS_COLS)]
        self.coo_black = []
        self.coo_white = []
        self.state = 1
        self.click_x = 0
        self.click_y = 0

    def draw(self):
        self.canvas = tk.Canvas(self.root, bg="Burlywood", width=540, height=540)
        self.canvas.grid(row=2, column=0, columnspan =3)
        self.canvas.bind("<Button-1>", self.coor_back)

        for i in range(15):
            self.canvas.create_line(self.X_ORIGIN_COOR, (self.CORS_COLS * i + self.Y_ORIGIN_COOR), 522, (self.CORS_COLS * i + self.Y_ORIGIN_COOR))
            self.canvas.create_line((self.CORS_COLS * i + self.X_ORIGIN_COOR), self.Y_ORIGIN_COOR, (self.CORS_COLS * i + self.X_ORIGIN_COOR), 528)

        star_point = [(3, 3), (3, 11), (11, 3), (11, 11), (7, 7)]
        for x, y in star_point:
            self.canvas.create_oval(self.CORS_COLS * x + 28, self.CORS_COLS * y + 33, self.CORS_COLS * x + 36, self.CORS_COLS * y + 41, fill="black")

        self.chess_turn_canvas = tk.Canvas(self.root, width=100, height=40)
        self.chess_turn_canvas.grid(row=0, column=0)
        self.chess_turn_canvas.create_oval(23 - self.chess_size, 28 - self.chess_size, 23 + self.chess_size, 28 + self.chess_size, fill=self.piece_color, tags=('display_turn'))
        self.var = tk.StringVar()
        self.var.set('Black')
        turn_label = tk.Label(self.root, textvariable=self.var, width=12, anchor=tk.W, font=("Arial", 14))
        turn_label.grid(row=1, column=0)

        self.restart_button = tk.Button(self.root, text='Restart', width=6, height=1, command=self.game_restart)
        self.restart_button.grid(row=0, column=2, columnspan=2)

        for i in self.coo_x:
            for j in self.coo_y:
                self.canvas.create_oval(i - self.chess_size, j - self.chess_size, i + self.chess_size, j + self.chess_size, width=0, tags=(str(i), str(j)))

    def coor_back(self, event):
        self.click_x = event.x
        self.click_y = event.y
        self.coor_judge()

    def show_turn(self, color):
        self.piece_color = color
        self.chess_turn_canvas.delete('display turn')
        self.chess_turn_canvas.create_oval(23 - self.chess_size, 28 - self.chess_size, 23 + self.chess_size, 28 + self.chess_size, fill=self.piece_color, tags=("display turn"))

    def game_restart(self):
        self.state = 1
        self.var.set("Black")
        self.show_turn("black")
        self.canvas.delete("pieces")
        self.coo_black = []
        self.coo_white = []

    def winner_message(self):
        self.message = ""
        if self.state == -1:
            self.message = 'White Win! Congratulations!'
        else:
            self.message = 'Black Win! Congratulations!'
        self.result = tk.messagebox.showinfo("Game Over", self.message)

    def put_piece(self, piece_color):
        self.canvas.create_oval(self.click_x - self.chess_size, self.click_y - self.chess_size, self.click_x + self.chess_size, self.click_y + self.chess_size, fill=piece_color, tags=("pieces"))
        if piece_color == "white":
            self.coo_white.append((self.click_x, self.click_y))
        elif piece_color == "black":
            self.coo_black.append((self.click_x, self.click_y))

    def coor_judge(self):
        coor = self.coo_black + self.coo_white
        item = self.canvas.find_closest(self.click_x, self.click_y)
        tags_tuple = self.canvas.gettags(item)
        if len(tags_tuple) > 1:
            tags_list = list(tags_tuple)
            coor_list = tags_list[:2]
            try:
                for i in range(len(coor_list)):
                    coor_list[i] = int(coor_list[i])
            except ValueError:
                pass
            else:
                coor_tuple = tuple(coor_list)
                (self.click_x, self.click_y) = coor_tuple
                if ((self.click_x, self.click_y) not in coor) and (self.click_x in self.coo_x) and (self.click_y in self.coo_y):
                    if self.state != 0:
                        if self.state == 1:
                            self.put_piece("black")
                            self.show_turn("white")
                            self.var.set("White")
                            self.judge("black")
                        elif self.state == -1:
                            self.put_piece("white")
                            self.show_turn("black")
                            self.var.set("Black")
                            self.judge("white")
                        self.state *= -1

    def judge(self, piece_color):
        if piece_color == "black":
            self.to_check(self.coo_black)
        elif piece_color == "white":
            self.to_check(self.coo_white)

    def to_check(self, coor):
        if self.check(coor):
            self.winner_message()
            self.game_restart()
            self.state = -1

    def check(self, coor):
        for x in self.coo_x:
            for y in self.coo_y:
                if ((x, y) in coor) and ((x+self.CORS_COLS, y) in coor) and ((x+2*self.CORS_COLS, y) in coor) and ((x+3*self.CORS_COLS, y) in coor) and ((x+4*self.CORS_COLS, y) in coor):
                    return True
                elif((x, y) in coor) and ((x, y+1*self.CORS_COLS) in coor) and ((x, y+2*self.CORS_COLS) in coor) and ((x, y+3*self.CORS_COLS) in coor) and ((x, y+4*self.CORS_COLS) in coor):
                    return True
                elif((x, y) in coor) and ((x+1*self.CORS_COLS, y+1*self.CORS_COLS) in coor) and ((x+2*self.CORS_COLS, y+2*self.CORS_COLS) in coor) and ((x+3*self.CORS_COLS, y+3*self.CORS_COLS) in coor) and ((x+4*self.CORS_COLS, y+4*self.CORS_COLS) in coor):
                    return True
                elif((x, y) in coor) and ((x+1*self.CORS_COLS, y-1*self.CORS_COLS) in coor) and ((x+2*self.CORS_COLS, y-2*self.CORS_COLS) in coor) and ((x+3*self.CORS_COLS, y-3*self.CORS_COLS) in coor) and ((x+4*self.CORS_COLS, y-4*self.CORS_COLS) in coor):
                    return True
                else:
                    pass


game = Game()
game.draw()
game.root.mainloop()
