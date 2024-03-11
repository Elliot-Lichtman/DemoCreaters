import pygame

pygame.init()

def drawConnect4Board(board, screen):
    colors = {
        "white": (255, 255, 255),
        "red": (192, 0, 0),
        "yellow": (248, 187, 2),
        "black": (0, 0, 0)
    }

    #screen.fill((50, 50, 150))
    screen.fill((240, 240, 240))

    for row in range(6):
        for col in range(7):
            pygame.draw.circle(screen, (0, 0, 0), (75+col*100, 100+row*100), 47)
            pygame.draw.circle(screen, colors[board[row][col]], (75 + col*100, 100+row*100), 45)

            if board[row][col] == "yellow":
                font = pygame.font.Font("freesansbold.ttf", 60)
                text = "P"
                text = font.render(text, True, colors["white"])
                textBox = text.get_rect()
                textBox.center = (75 + col*100, 100 + row*100)
                screen.blit(text, textBox)

            if board[row][col] == "red":
                font = pygame.font.Font("freesansbold.ttf", 60)
                text = "C"
                text = font.render(text, True, colors["white"])
                textBox = text.get_rect()
                textBox.center = (75 + col*100, 100 + row*100)
                screen.blit(text, textBox)
    pygame.draw.circle(screen, (0, 0, 0), (20, 30), 2)

    pygame.draw.circle(screen, (0, 0, 0), (730, 670), 2)



def connect4():

    screen = pygame.display.set_mode((750, 700))



    board = [
        ["white", "white", "white", "white", "white", "white", "white"],
        ["white", "white", "white", "white", "white", "white", "white"],
        ["white", "white", "white", "white", "white", "white", "white"],
        ["white", "white", "white", "white", "white", "white", "white"],
        ["white", "white", "white", "white", "white", "white", "white"],
        ["white", "white", "white", "white", "white", "white", "white"],
        ["white", "white", "white", "white", "white", "white", "white"]
    ]

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                print(pos)

                row = abs(pos[1] - 55) // 100
                col = abs(pos[0] - 30) // 100

                if board[row][col] == "white":
                    board[row][col] = "red"
                elif board[row][col] == "red":
                    board[row][col] = "yellow"
                else:
                    board[row][col] = "white"

        drawConnect4Board(board, screen)

        pygame.display.update()

#connect4()

def drawOthelloBoard(board, screen):

    buffer = 50

    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "green" : (8,148,100)
    }

    screen.fill(colors["green"])

    for col in range(9):

        pygame.draw.line(screen, (0, 0, 0), (col*75 + buffer, 0 + buffer), (col*75 + buffer, 600 + buffer))

    for row in range(9):

        pygame.draw.line(screen, (0, 0, 0), (0 + buffer, row*75 + buffer), (600 + buffer, row*75 + buffer))

    for row in range(8):
        for col in range(8):
            if board[row][col] == "possible":
                pygame.draw.circle(screen, (0, 0, 0), (37.5 + buffer + col * 75, 37.5 + buffer + row * 75), 34)
                pygame.draw.circle(screen, colors["green"], (37.5 + buffer + col * 75, 37.5 + buffer + row * 75), 33)
            elif board[row][col] != "green":
                #pygame.draw.circle(screen, (0, 0, 0), (37.5+col*75, 37.5+row*75), 34)
                pygame.draw.circle(screen, colors[board[row][col]], (37.5 + buffer + col * 75, 37.5 + buffer + row * 75), 33)


    pygame.draw.circle(screen, (0, 0, 0), (buffer-20, buffer-20), 2)

    pygame.draw.circle(screen, (0, 0, 0), (buffer+620, buffer+620), 2)

class Button():

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text


    def draw(self, screen):

        font = pygame.font.Font("freesansbold.ttf", 30)

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height))

        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(self.x - self.width / 2+1, self.y - self.height / 2+1, self.width-2, self.height-2))


        text = font.render(self.text, True, (0, 0, 0))
        textBox = text.get_rect()
        textBox.center = (self.x, self.y)
        screen.blit(text, textBox)

    def detectPress(self, x, y):

        if abs(x - self.x) <= self.width/2 and abs(y - self.y) <= self.height/2:

            return True

        return False




colorDictionary = {"background": (152, 140, 132),
                   " ": (188,173,159),
                   "2": (238, 228, 218),
                   "4": (238, 225, 201),
                   "8": (243,178,122),
                   "16": (247, 149, 100),
                   "32":(247,125,95),
                   "64": (248,92,60),
                   "128+":(237,208,115),
                   "blackText":(119,110,101),
                   "whiteText":(248, 246, 242)
                   }

textColorDictionary = {
  " " : colorDictionary["blackText"],
  "2" : colorDictionary["blackText"],
  "4" : colorDictionary["blackText"],
  "8+" : colorDictionary["whiteText"]
}

font = pygame.font.Font("freesansbold.ttf", 60)


def copyList(list):
    newList = []
    for item in list:
        newList.append(item)
    return newList


class Tile:
    def __init__(self, x, y):
        self.color = colorDictionary[" "]
        self.value = " "
        self.x = x
        self.y = y
        self.textColor = colorDictionary["blackText"]

    def setValue(self, valueStr):
        self.value = valueStr
        try:
            self.color = colorDictionary[valueStr]
        except:
            self.color = colorDictionary["128+"]

        try:
            self.textColor = textColorDictionary[valueStr]
        except:
            self.textColor = textColorDictionary["8+"]

    def doubleValue(self):

        if self.value == " ":
            self.value = "2"

            self.color = colorDictionary["2"]

            self.textColor = textColorDictionary["2"]

            return

        self.value = str(int(self.value) * 2)

        if self.value == "8":
            self.textColor = colorDictionary["whiteText"]

            self.color = colorDictionary["8"]

        elif int(self.value) >= 128 and int(self.value) < 4096:
            self.color = colorDictionary["128+"]

        elif int(self.value) >= 4096:
            self.color = colorDictionary[" "]

            self.value = " "
            return

        else:
            try:
                self.color = colorDictionary[self.value]
            except:
                self.color = colorDictionary["empty tile"]

    def draw(self, screen):
        # I added a few more parameters to the rectangle command, don't worry about them. They just make the corners rounded

        pygame.draw.rect(screen, self.color, pygame.Rect(self.x - 70, self.y - 70, 140, 140), border_top_left_radius=10,
                         border_top_right_radius=10, border_bottom_left_radius=10, border_bottom_right_radius=10)

        text = font.render(self.value, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        screen.blit(text, textRect)


class Game:
    def __init__(self):
        self.board = []

        currentX = 110
        currentY = 110

        for r in range(4):
            row = []
            for t in range(4):
                row.append(Tile(currentX, currentY))
                currentX += 160
            self.board.append(copyList(row))
            currentY += 160
            currentX = 110

        self.score = 0


    def draw(self, screen):
        screen.fill(colorDictionary["background"])
        for row in self.board:
            for tile in row:
                tile.draw(screen)

        pygame.draw.circle(screen, (0, 0, 0), (20, 20), 2)
        pygame.draw.circle(screen, (0, 0, 0), (680, 680), 2)



def create2048():
    screen = pygame.display.set_mode((700, 700))

    game = Game()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 20) // 160
                col = (pos[0] - 20) // 160

                game.board[row][col].doubleValue()




        game.draw(screen)
        pygame.display.update()



def othello():

    screen = pygame.display.set_mode((700, 700))


    board = [
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
        ["green", "green", "green", "green", "green", "green", "green", "green"],
    ]

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 75
                col = (pos[0] - 50) // 75

                if board[row][col] == "green":
                    board[row][col] = "white"
                elif board[row][col] == "white":
                    board[row][col] = "black"
                elif board[row][col] == "black":
                    board[row][col] = "possible"
                else:
                    board[row][col] = "green"

        drawOthelloBoard(board, screen)

        pygame.display.update()

def drawSudokuBoard(board, hBoard, screen):

    font = pygame.font.Font("freesansbold.ttf", 50)

    buffer = 50

    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "w": (255, 255, 255),
        "r": (255, 200, 200),
        "b": (200, 230, 255),
        "y": (255, 255, 200),
        "g": (200, 255, 200)

    }

    screen.fill(colors["white"])


    for row in range(9):
        for col in range(9):

            pygame.draw.rect(screen, colors[hBoard[row][col]], pygame.Rect(buffer + col*75, buffer+row*75, 75, 75))

            text = board[row][col]

            text = font.render(text, True, (0, 0, 0))

            textBox = text.get_rect()

            textBox.center = (37.5 + buffer + col*75, 37.5 + buffer + row * 75)

            screen.blit(text, textBox)


    pygame.draw.circle(screen, (0, 0, 0), (buffer-20, buffer-20), 2)

    pygame.draw.circle(screen, (0, 0, 0), (buffer+700, buffer+700), 2)

    for col in range(10):

        if col % 3 == 0:
            thickness = 3
        else:
            thickness = 1

        pygame.draw.line(screen, (0, 0, 0), (col*75 + buffer, 0 + buffer), (col*75 + buffer, 675 + buffer), thickness)

    for row in range(10):

        if row % 3 == 0:
            thickness = 3
        else:
            thickness = 1


        pygame.draw.line(screen, (0, 0, 0), (0 + buffer, row*75 + buffer), (675 + buffer, row * 75 + buffer), thickness)

def sudoku():

    screen = pygame.display.set_mode((775, 775))

    board = [
        ["6", "8", " ", "2", " ", " ", "1", " ", " "],
        ["9", " ", " ", "6", "8", "7", " ", " ", " "],
        [" ", "2", " ", "9", " ", " ", " ", "6", "8"],
        [" ", " ", " ", " ", "9", " ", "4", " ", "3"],
        ["3", " ", "9", " ", " ", "6", " ", "5", "1"],
        [" ", " ", " ", "3", " ", "5", "9", "2", " "],
        [" ", "9", "8", "1", " ", " ", "7", " ", "4"],
        ["1", " ", "2", "4", "7", " ", "6", " ", " "],
        ["7", " ", "4", "5", " ", "8", " ", " ", " "],
    ]

    hBoard = [
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ]

    running = True

    selectedSquare = [0, 0]

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                try:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    else:
                        value = chr(event.key)

                        if value in ("123456789 "):
                            board[selectedSquare[0]][selectedSquare[1]] = value
                        else:
                            hBoard[selectedSquare[0]][selectedSquare[1]] = value

                except:
                    pass


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 75
                col = (pos[0] - 50) // 75

                selectedSquare = [row, col]

        drawSudokuBoard(board, hBoard, screen)

        pygame.display.update()


o = pygame.image.load("O.png")
x = pygame.image.load("X.png")
grid = pygame.image.load("TicTacToeGrid.png")

grid = pygame.transform.scale(grid, (600, 600))
x = pygame.transform.scale(x, (150, 150))
o = pygame.transform.scale(o, (150, 150))

def drawTicTacToeBoard(board, screen):

    screen.fill((255, 255, 255))
    screen.blit(grid, (50, 50))

    for row in range(3):
        for col in range(3):

            if board[row][col] == "X":
                screen.blit(x, (60 + 215*col, 60 + 210*row))

            elif board[row][col] == "O":
                screen.blit(o, (60 + 215*col, 60 + 210*row))

    pygame.draw.circle(screen, (0, 0, 0), (40, 40), 2)
    pygame.draw.circle(screen, (0, 0, 0), (660, 660), 2)


def ticTacToe():
    screen = pygame.display.set_mode((700, 700))

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 200
                col = (pos[0] - 50) // 200

                if board[row][col] == " ":
                    board[row][col] = "X"
                elif board[row][col] == "X":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = " "

        drawTicTacToeBoard(board, screen)

        pygame.display.update()

def drawBoggleBoard(board, hBoard, screen):

    font = pygame.font.Font("freesansbold.ttf", 50)

    buffer = 50

    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "1": (255, 255, 255),
        "2": (255, 200, 200),
        "3": (200, 230, 255),
        "4": (255, 255, 200),
        "5": (200, 255, 200)

    }

    screen.fill(colors["white"])


    for row in range(4):
        for col in range(4):

            pygame.draw.rect(screen, colors[hBoard[row][col]], pygame.Rect(buffer + col*75, buffer+row*75, 75, 75))

            text = board[row][col]

            text = font.render(text, True, (0, 0, 0))

            textBox = text.get_rect()

            textBox.center = (37.5 + buffer + col*75, 37.5 + buffer + row * 75)

            screen.blit(text, textBox)


    pygame.draw.circle(screen, (0, 0, 0), (buffer-20, buffer-20), 2)

    pygame.draw.circle(screen, (0, 0, 0), (buffer+320, buffer+320), 2)

    for col in range(5):

        pygame.draw.line(screen, (0, 0, 0), (col*75 + buffer, 0 + buffer), (col*75 + buffer, 300 + buffer), 3)

    for row in range(5):

        pygame.draw.line(screen, (0, 0, 0), (0 + buffer, row*75 + buffer), (300 + buffer, row * 75 + buffer), 3)

def boggle():

    screen = pygame.display.set_mode((400, 400))

    board = [
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
    ]

    hBoard = [
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
    ]

    running = True

    selectedSquare = [0, 0]

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                try:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    else:
                        value = chr(event.key)

                        if value not in ("123456789 "):
                            board[selectedSquare[0]][selectedSquare[1]] = value.upper()
                        else:
                            hBoard[selectedSquare[0]][selectedSquare[1]] = value

                except:
                    pass


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 75
                col = (pos[0] - 50) // 75

                selectedSquare = [row, col]

        drawBoggleBoard(board, hBoard, screen)

        pygame.display.update()


class Square:

    def __init__(self, sideLength, x, y):
        self.sideLength = sideLength
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.value = " "
        self.colorDictionary = {"green": (108, 172, 100), "yellow": (204, 180, 85), "gray": (124, 124, 124)}

    def draw(self, screen):
        text = self.value

        if self.color == (255, 255, 255):
            pygame.draw.rect(screen, (0, 0, 0), (self.x - self.sideLength / 2, self.y - self.sideLength / 2, self.sideLength, self.sideLength))
            pygame.draw.rect(screen, self.color, (self.x - self.sideLength / 2 + 1, self.y - self.sideLength / 2 + 1, self.sideLength-2, self.sideLength-2))
            text = font.render(text, True, (0, 0, 0))

        else:
            pygame.draw.rect(screen, self.color, (self.x-self.sideLength/2, self.y-self.sideLength/2, self.sideLength, self.sideLength))
            text = font.render(text, True, (255, 255, 255))

        textBox = text.get_rect()
        textBox.center = (self.x, self.y)
        screen.blit(text, textBox)

    def changeColor(self):
        if self.color == self.colorDictionary["green"]:
            self.color = self.colorDictionary["gray"]

        elif self.color == (255, 255, 255):
            self.color = self.colorDictionary["yellow"]

        elif self.color == self.colorDictionary["yellow"]:
            self.color = self.colorDictionary["green"]

        else:
            self.color = (255, 255, 255)



class Wordle:

    def __init__(self):
        self.squareGrid = []

        currentX = 100
        currentY = 100

        for r in range(6):
            row = []
            for s in range(5):
                row.append(Square(80, currentX, currentY))
                currentX += 90
            self.squareGrid.append(copyList(row))
            currentY += 90
            currentX = 100

        self.firstEmptySquare = [0, 0]

        self.colorDictionary = {"green" : (108,172,100), "yellow" : (204,180,85), "gray" : (124, 124, 124)}

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for row in self.squareGrid:
            for square in row:
                square.draw(screen)

        pygame.draw.circle(screen, (0, 0, 0), (40, 40), 2)
        pygame.draw.circle(screen, (0, 0, 0), (520, 610), 2)

    def typeLetter(self, letter):

        self.squareGrid[self.firstEmptySquare[0]][self.firstEmptySquare[1]].value = letter

        if self.firstEmptySquare[1] == 4:
            self.firstEmptySquare[0] += 1
            self.firstEmptySquare[1] = 0

        else:
            self.firstEmptySquare[1] += 1

    def delete(self):

        if self.firstEmptySquare[1] == 0:
            self.firstEmptySquare[0] -= 1
            self.firstEmptySquare[1] = 4

        elif self.firstEmptySquare[1] > 0:
            self.firstEmptySquare[1] -= 1

        self.squareGrid[self.firstEmptySquare[0]][self.firstEmptySquare[1]].value = " "


def wordle():
    game = Wordle()

    screen = pygame.display.set_mode((560, 650))

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                try:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    else:
                        value = chr(event.key)

                        game.typeLetter(value.upper())

                except:
                    pass


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 90
                col = (pos[0] - 50) // 90

                game.squareGrid[row][col].changeColor()

        game.draw(screen)

        pygame.display.update()

images = {
    "b": pygame.image.load("Bomb.png"),
    "f": pygame.image.load("Flag.png"),
    "h": pygame.image.load("Hidden.png"),
    "r": pygame.image.load("Revealed.png"),
}

for image in images.keys():
    images[image] = pygame.transform.scale(images[image], (75, 75))

def drawMinesweeperBoard(board, boardText, screen):

    screen.fill((200, 200, 200))

    buffer = 50

    font = pygame.font.Font("freesansbold.ttf", 50)

    colors = {
        "1": (0, 0, 255),
        "2": (0, 150, 0),
        "3": (255, 0, 0),
        "4": (0, 0, 100),
        " ": (0, 0, 0)
    }

    for row in range(9):
        for col in range(9):
            try:
                screen.blit(images[board[row][col]], (buffer + 75*col, buffer + 75*row))
            except:
                pass

            if boardText[row][col] in "1234 ":
                text = font.render(boardText[row][col], True, (colors[boardText[row][col]]))

                rect = text.get_rect()

                rect.center = (buffer + 75*col + 75/2, buffer+75*row + 75/2)

                screen.blit(text, rect)

            else:
                try:
                    screen.blit(images[boardText[row][col]], (buffer + 75*col, buffer + 75*row))
                except:
                    pass



    pygame.draw.circle(screen, (0, 0, 0), (buffer - 20, buffer - 20), 2)

    pygame.draw.circle(screen, (0, 0, 0), (buffer + 700, buffer + 700), 2)


def minesweeper():

    screen = pygame.display.set_mode((775, 775))

    selectedSquare = [0, 0]

    board = [
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"],
        ["h", "h", "h", "h", "h", "h", "h", "h", "h"]
    ]

    boardText = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                try:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if chr(event.key) in "123456fb ":
                        boardText[selectedSquare[0]][selectedSquare[1]] = chr(event.key)

                    else:
                        board[selectedSquare[0]][selectedSquare[1]] = chr(event.key)

                except:
                    pass


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 75
                col = (pos[0] - 50) // 75

                selectedSquare = [row, col]

        drawMinesweeperBoard(board, boardText, screen)

        pygame.display.update()

def drawMaze(board, hBoard, screen):

    font = pygame.font.Font("freesansbold.ttf", 50)

    buffer = 50

    colors = {
        "w": (255, 255, 255),
        "b": (0, 0, 0),
        "r": (255, 100, 100),
        "g": (100, 255, 100),
        "u": (100, 100, 255),
        "h": (124, 124, 124)

    }

    screen.fill(colors["w"])


    for row in range(5):
        for col in range(4):

            pygame.draw.rect(screen, colors[hBoard[row][col]], pygame.Rect(buffer + col*75, buffer+row*75, 75, 75))



    pygame.draw.circle(screen, (0, 0, 0), (buffer-20, buffer-20), 2)

    pygame.draw.circle(screen, (0, 0, 0), (buffer+325, buffer+395), 2)

    for col in range(5):

        pygame.draw.line(screen, (0, 0, 0), (col*75 + buffer, 0 + buffer), (col*75 + buffer, 375 + buffer), 3)

    for row in range(6):

        pygame.draw.line(screen, (0, 0, 0), (0 + buffer, row*75 + buffer), (300 + buffer, row * 75 + buffer), 3)

    for row in range(5):
        for col in range(5):

            if board[row][col] == "h":
                pygame.draw.rect(screen, colors["h"], pygame.Rect(buffer + col*75, buffer+row*75, 75, 75))

def maze():

    screen = pygame.display.set_mode((400, 475))

    board = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
    ]

    hBoard = [
        ["r", "w", "w", "w", "w"],
        ["w", "b", "w", "b", "b"],
        ["w", "b", "w", "b", "w"],
        ["w", "b", "b", "b", "w"],
        ["w", "w", "w", "g", "g"],
    ]

    running = True

    selectedSquare = [0, 0]

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                try:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    else:
                        value = chr(event.key)

                        if value in "wbrgu":
                            hBoard[selectedSquare[0]][selectedSquare[1]] = value

                        else:
                            board[selectedSquare[0]][selectedSquare[1]] = value

                except:
                    pass


            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 75
                col = (pos[0] - 50) // 75

                selectedSquare = [row, col]

        drawMaze(board, hBoard, screen)

        pygame.display.update()

WQueen = pygame.image.load("White Queen.png")
WQueen = pygame.transform.scale(WQueen, (80, 80))

def drawBackground(screen):
    # Colors in the black squares

    colors = {
        "dark" : (90, 60, 50),
        "light" : (200, 170, 160)
    }

    colors = {
        "dark" : (209, 138, 71),
        "light" : (252,205,157)
    }


    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, colors["dark"], pygame.Rect(50, 50, 640, 640))


    # ignore the janky booleans this just alternates squares
    color = True
    startRow = True
    for r in range(8):
        if startRow:
            color = True
            startRow = False
        else:
            color = False
            startRow = True
        for c in range(8):
            if color:
                color = False
                pygame.draw.rect(screen, colors["light"], pygame.Rect(50+r * 80, 50+c * 80, 80, 80))
            else:
                color = True

    """for r in range(9):
        pygame.draw.line(screen, (0, 0, 0), (50, 50+r*80), (690, 50 + r*80), 2)


    for c in range(9):
        pygame.draw.line(screen, (0, 0, 0), (50+c*80, 50), (50 + c*80, 690), 2)"""

# This function will draw the pieces on top of the board in the right squares. The input is the board as a string
def drawPieces(board, screen):
    pieceCounter = 0
    for piece in board:
        # calculate the row and col of the square. We can use this to get the coords we want for the image.
        col = pieceCounter % 8
        row = pieceCounter // 8
        if piece == "A":
            screen.blit(WQueen, (50+80*col, 50+80*row))

        pieceCounter += 1

def drawChessBoard(board, screen):

    drawBackground(screen)

    drawPieces(board, screen)

    pygame.draw.circle(screen, (0, 0, 0), (30, 30), 2)
    pygame.draw.circle(screen, (0, 0, 0), (720, 720), 2)

def chess():

    screen = pygame.display.set_mode((740, 740))

    board = "GGGGAGGGGAGGGGGGGGGAGGGGGGGGGGAGGGAGGGGGGGGGGGGAGGGGGAGGAGGGGGGG"

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                row = (pos[1] - 50) // 80
                col = (pos[0] - 50) // 80

                if board[row*8 + col] == "G":
                    newBoard = ""
                    counter = 0

                    for letter in board:
                        if counter == row*8 + col:
                            newBoard += "A"
                        else:
                            newBoard += letter
                        counter += 1

                    board = newBoard

                else:
                    newBoard = ""
                    counter = 0

                    for letter in board:
                        if counter == row * 8 + col:
                            newBoard += "G"
                        else:
                            newBoard += letter

                        counter += 1

                    board = newBoard

        drawChessBoard(board, screen)
        pygame.display.update()

coin = pygame.image.load("Coin.png")
coin = pygame.transform.scale(coin, (75, 75))

def drawCoinGame(screen, coins):

    screen.fill((255, 255, 255))

    for c in range(12):
        if coins[c] % 3 == 0:
            screen.blit(coin, (c*85 + 50, 100-37.5))
        elif coins[c] % 3 == 1:
            pygame.draw.circle(screen, (0, 0, 0), (c*85 + 87.5, 100), 37.5)
            pygame.draw.circle(screen, (255, 255, 255), (c*85 + 87.5, 100), 35)

    pygame.draw.circle(screen, (0, 0, 0), (20, 40), 2)
    pygame.draw.circle(screen, (0, 0, 0), (1100, 160), 2)

def coinGame():
    screen = pygame.display.set_mode((1120, 200))

    running = True
    coins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                index = (pos[0] - 50) // 85

                coins[index] += 1

        drawCoinGame(screen, coins)
        pygame.display.update()

def main():

    screen = pygame.display.set_mode((500, 600))

    buttons = []

    buttons.append(Button(250, 50, 400, 45, "Connect Four"))

    buttons.append(Button(250, 100, 400, 45, "Othello"))

    buttons.append(Button(250, 150, 400, 45, "2048"))

    buttons.append(Button(250, 200, 400, 45, "Sudoku"))

    buttons.append(Button(250, 250, 400, 45, "Wordle"))

    buttons.append(Button(250, 300, 400, 45, "Boggle"))

    buttons.append(Button(250, 350, 400, 45, "Tic Tac Toe"))

    buttons.append(Button(250, 400, 400, 45, "Minesweeper"))

    buttons.append(Button(250, 450, 400, 45, "Maze"))

    buttons.append(Button(250, 500, 400, 45, "8 Queens"))

    buttons.append(Button(250, 550, 400, 45, "Coin Game"))

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                for button in buttons:
                    if button.detectPress(pos[0], pos[1]):
                        if button.text == "Connect Four":
                            connect4()
                            screen = pygame.display.set_mode((500, 600))
                        elif button.text == "Othello":
                            othello()
                            screen = pygame.display.set_mode((500, 600))
                        elif button.text == "2048":
                            create2048()
                            screen = pygame.display.set_mode((500, 600))
                        elif button.text == "Sudoku":
                            sudoku()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "Tic Tac Toe":
                            ticTacToe()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "Boggle":
                            boggle()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "Wordle":
                            wordle()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "Minesweeper":
                            minesweeper()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "Maze":
                            maze()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "8 Queens":
                            chess()
                            screen = pygame.display.set_mode((500, 600))

                        elif button.text == "Coin Game":
                            coinGame()
                            screen = pygame.display.set_mode((500, 600))


        screen.fill((100, 200, 255))

        for button in buttons:
            button.draw(screen)

        pygame.display.update()

main()