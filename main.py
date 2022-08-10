import pygame

pygame.init()


def drawConnect4Board(board, screen):

    screen.fill((50, 50, 150))

    for row in range(6):
        for col in range(7):
            pygame.draw.circle(screen, board[row][col], (75 + col*100, 100+row*100), 45)

    pygame.draw.circle(screen, (0, 0, 0), (20, 30), 2)

    pygame.draw.circle(screen, (0, 0, 0), (730, 670), 2)



def connect4():

    screen = pygame.display.set_mode((750, 700))

    colors = {
        "white" : (255, 255, 255),
        "red" : (255, 100, 100),
        "yellow" : (200, 200, 100)
    }

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
        "green" : (50, 150, 50)
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


    pygame.draw.circle(screen, (0, 0, 0), (buffer, buffer), 2)

    pygame.draw.circle(screen, (0, 0, 0), (buffer+600, buffer+600), 2)

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

def main():

    screen = pygame.display.set_mode((500, 500))

    font = pygame.font.Font("freesansbold.ttf", 60)

    buttons = []

    buttons.append(Button(250, 100, 400, 100, "Connect Four"))

    buttons.append(Button(250, 250, 400, 100, "Othello"))

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
                        elif button.text == "Othello":
                            othello()

        screen.fill((100, 100, 100))

        for button in buttons:
            button.draw(screen)

        pygame.display.update()


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

            elif event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE:
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

    colors = {
        "white" : (255, 255, 255),
        "black" : (0, 0, 0),
        "green" : (0, 1, 0),
        "possible" : (0, 0, 0)
    }

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

def main():

    screen = pygame.display.set_mode((500, 500))

    buttons = []

    buttons.append(Button(250, 50, 400, 45, "Connect Four"))

    buttons.append(Button(250, 100, 400, 45, "Othello"))

    buttons.append(Button(250, 150, 400, 45, "2048"))

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
                            screen = pygame.display.set_mode((500, 500))
                        elif button.text == "Othello":
                            othello()
                            screen = pygame.display.set_mode((500, 500))
                        elif button.text == "2048":
                            create2048()
                            screen = pygame.display.set_mode((500, 500))

        screen.fill((100, 100, 100))

        for button in buttons:
            button.draw(screen)

        pygame.display.update()

main()
