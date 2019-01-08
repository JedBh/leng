import sys

class Knightproblem:
    def __init__(self, width, height):
        # base

        self.width = width
        self.height = height
        self.board = []
        self.initial_board()

    def initial_board(self):
        # initializes board

        for i in range(self.height):
            self.board.append([0]*self.width)

    def show_board(self):
        # shows current board

        for row in self.board:
            print(row)
        

    def knight_moves(self, pos):
        # possible moves for knight

        possible_position = []
        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in knight_moves:
            new_x = pos[0] + move[0]
            new_y = pos[1] + move[1]

            if (new_x >= self.height):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.width):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_position.append((new_x, new_y))

        return possible_position

    def srt_empty_sq(self, land):
     
        square_list = self.knight_moves(land)
        empty_squares = []

        for square in square_list:
            np_value = self.board[square[0]][square[1]]
            if np_value == 0:
                empty_squares.append(square)

        counts = []
        for empty in empty_squares:
            count = [empty, 0]
            moves = self.knight_moves(empty)
            for i in moves:
                if self.board[i[0]][i[1]] == 0:
                    count[1] += 1
            counts.append(count)

        counts_sort = sorted(counts, key = lambda a: a[1])
        sorted_neighbours = [a[0] for a in counts_sort]
        return sorted_neighbours

    def init_tour(self, count, path, land):
        print("First instance: ")
        self.board[land[0]][land[1]] = count
        self.show_board()

    def tour(self, count, path, land):
        self.board[land[0]][land[1]] = count
        

        if count == self.width * self.height: 
            print("Final instance: ")
            self.show_board()
            sys.exit(1)

        else:
            sorted_squares = self.srt_empty_sq(land)
            for square in sorted_squares:
                self.tour(count + 1, path, square)

x, y = [int(i) for i in input("Enter the x and the y for the knight's position: ").split()]
print(x, y)

attiach = Knightproblem(8, 8)
attiach.init_tour(1, [], (y - 1, x - 1))
attiach.tour(1, [], (y - 1, x - 1))
attiach.show_board()