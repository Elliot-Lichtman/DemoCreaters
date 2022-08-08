import pygame

pygame.init()


def drawConnect4Board(board, screen):

    screen.fill((50, 50, 150))

    for row in range(6):
        for col in range(7):
            pygame.draw.circle(screen, board[row][col], (75 + col*100, 100+row*100), 45)



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

    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "green" : (50, 150, 50)
    }

    screen.fill(colors["green"])

    for col in range(8):

        pygame.draw.line(screen, (0, 0, 0), (col*75, 0), (col*75, 600))

    for row in range(8):

        pygame.draw.line(screen, (0, 0, 0), (0, row*75), (600, row*75))

        for col in range(8):
            if board[row][col] == "possible":
                pygame.draw.circle(screen, (0, 0, 0), (37.5 + col * 75, 37.5 + row * 75), 34)
                pygame.draw.circle(screen, colors["green"], (37.5 + col * 75, 37.5 + row * 75), 33)
            elif board[row][col] != "green":
                #pygame.draw.circle(screen, (0, 0, 0), (37.5+col*75, 37.5+row*75), 34)
                pygame.draw.circle(screen, colors[board[row][col]], (37.5+col*75, 37.5+row*75), 33)


class Button():

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text


    def draw(self, screen):

        font = pygame.font.Font("freesansbold.ttf", 60)

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






def othello():

    screen = pygame.display.set_mode((600, 600))

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

                row = pos[1] // 75
                col = pos[0] // 75

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

main()
