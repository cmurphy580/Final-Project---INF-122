from src.view.irender import IRender

class TetrisRender(IRender):
    def __init__(self):
        # Initialize any required attributes or data structures for Tetris rendering

    def render(self):
        # Implement the rendering logic for the Tetris game here

    # def draw_next_shape(self, screen, shape):
    #     font = pygame.font.SysFont('comicsans', 30)
    #     label = font.render('Next Shape', 1, (255, 255, 255))
    #
    #     sx = Constants.TOP_LEFT_X + Constants.PLAY_WIDTH + 50
    #     sy = Constants.TOP_LEFT_Y + Constants.PLAY_HEIGHT / 2 - 100
    #     format = shape.shape[shape.rotation % len(shape.shape)]
    #
    #     for i, line in enumerate(format):
    #         row = list(line)
    #         for j, column in enumerate(row):
    #             if column == '0':
    #                 pygame.draw.rect(screen, shape.color,
    #                                  (sx + j * 30, sy + i * 30, 30, 30), 0)
    #
    #     screen.blit(label, (sx + 10, sy - 30))

