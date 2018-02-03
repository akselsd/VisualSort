import pygame, sys

TEXT_SIZE = 20

WINDOWWIDTH = 1200
WINDOWHEIGHT = 600
HEIGHT_BOTTOM_OFFSET = 5
HEIGHT_TOP_OFFSET = 20
SELECTED_COLOR = (0,255,0)
PIVOT_COLOR = (255,0,0)
CORRECT_COLOR_MASK = (255,255,255)
HIGHLIGHTED_COLORS = [SELECTED_COLOR,PIVOT_COLOR]
TEXT_COLOR =(0,0,0)
BGCOLOR = (60, 60, 100)
FPS = 60

class GraphicHandler:


    def __init__(self, numlist):

        self.DISPLAY_SURFACE = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption("Algorithms")
        if len(numlist.numbers)>100:
            self.GAPSIZE = 0
        else:
            self.GAPSIZE = 1
        self.LINE_WIDTH = (WINDOWWIDTH - ((len(numlist.numbers) + 1) * (self.GAPSIZE))) / len(numlist.numbers)
        self.HEIGHT_SPACE_FACTOR = (WINDOWHEIGHT - (HEIGHT_TOP_OFFSET + HEIGHT_BOTTOM_OFFSET)) / len(numlist.numbers)
        self.numlist = numlist
        self.FPSCLOCK = pygame.time.Clock()
        self.display_text_bool = False
        self.text = None


    def set_display_text(self, text_to_display):
        self.display_text_bool = True
        pygame.font.init()
        font = pygame.font.SysFont("Times New Roman", TEXT_SIZE)
        self.text = font.render(text_to_display, True, TEXT_COLOR)
        self.numbers_text = font.render("Length: {}".format(len(self.numlist.numbers)), True, TEXT_COLOR)

    def display_text(self):
        assert self.text is not None, "Must set text before calling display_text()"
        self.DISPLAY_SURFACE.blit(self.text, (0,0))
        self.DISPLAY_SURFACE.blit(self.numbers_text, (0,TEXT_SIZE))

    def height_transformation(self,numbers):
        return list(map(lambda x: x * self.HEIGHT_SPACE_FACTOR + HEIGHT_BOTTOM_OFFSET, numbers))

    #bottom-left corner in (xpos,0)
    def draw_rect(self, xpos, height, color):
        rect = pygame.Rect(xpos,WINDOWHEIGHT-height,self.LINE_WIDTH,height)
        pygame.draw.rect(self.DISPLAY_SURFACE,color,rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self, *args):
        self.DISPLAY_SURFACE.fill(BGCOLOR)
        real_heights = self.height_transformation(self.numlist.numbers)
        displacement_vector = self.numlist.get_displacement_vector()
        x_pos = 0
        for i in range(len(real_heights)):

            #color mapping
            displacement_percentage = displacement_vector[i]
            if displacement_percentage<0.7:
                displacement_percentage = 0
            else:
                displacement_percentage = (10/3)*displacement_percentage-(7/3)
            adjusted_color = [x*displacement_percentage for x in CORRECT_COLOR_MASK]

            #draw
            x_pos += self.GAPSIZE
            self.draw_rect(x_pos, real_heights[i], adjusted_color)
            x_pos += self.LINE_WIDTH

        color_gen = (i for i in HIGHLIGHTED_COLORS)
        for higlighted_rects in args:
            color = color_gen.__next__()
            for index in higlighted_rects:
                x_pos = self.GAPSIZE * (index + 1) + self.LINE_WIDTH * index
                self.draw_rect(x_pos, real_heights[index], color)

        self.handle_events()

        if self.display_text_bool:
            self.display_text()

        pygame.display.update()
        self.FPSCLOCK.tick(FPS)