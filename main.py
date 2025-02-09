import pygame, sys
from pygame.locals import *
#定义Trivia类
class Trivia(object):
    def __init__(self, filename):
        #初始化属性设置
        self.date = []
        self.current =0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]
        #问答数据读取
        f = open(filename, "r", encoding="utf-8")
        trivia_date = f.readlines()
        f.close()
        #问答数据存储
        for text_line in trivia_date:
            self.date.append(text_line.strip())
            self.total += 1
    #问题及答案显示
    def show_question(self):
        print_text(font1, 260, 5, "问答竞赛")
        print_text(font2, 200, 480, "请按下(1~4)按键来选择答案", purple)
        print_text(font2, 630, 5, "得分", purple)
        print_text(font2, 635, 25, str(self.score), purple)

        self.correct = int(self.date[self.current+5])

        question = self.current // 6 + 1
        print_text(font1, 5, 80, f"问题{question}")
        print_text(font2, 20, 120, self.date[self.current], yellow)

        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct] = green
            print_text(font1, 300, 380, "正确", green)
            print_text(font2, 210, 420, "请按下Enter键前往下一题", green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wronganswer] = red
            self.colors[self.correct] = green
            print_text(font1, 300, 380, "错误", red)
            print_text(font2, 210, 420, "请按下Enter键前往下一题", red)
        print_text(font1, 5, 170, "选项")
        print_text(font2, 20, 210, f"1- {self.date[self.current+1]}", self.colors[0])
        print_text(font2, 20, 240, f"2- {self.date[self.current+2]}", self.colors[1])
        print_text(font2, 20, 270, f"3- {self.date[self.current+3]}", self.colors[2])
        print_text(font2, 20, 300, f"4- {self.date[self.current+4]}", self.colors[3])
    #玩家答案正误判断
    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number
    #下一个问题属性处理
    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0
#文本打印函数
def print_text(font, x, y, text, color=(255, 255, 255), shadow=True):
    if shadow:
        imgText = font.render(text, True, (0, 0, 0))
        screen.blit(imgText, (x - 2, y -2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))
#初始化pygame
pygame.init()
screen = pygame.display.set_mode((700, 550))
pygame.display.set_caption("问答竞赛")
font1 = pygame.font.Font("klxqt.ttf", 40)
font2 = pygame.font.Font("klxqt.ttf", 24)
white = 255, 255, 255
black = 0, 0, 0
cyan = 0, 255, 255
yellow = 255, 255, 0
blue = 0, 0, 250
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0
#实例化Trivia对象
trivia = Trivia("trivia_date.txt")
#主循环代码
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(0)
            elif event.key == pygame.K_2:
                trivia.handle_input(1)
            elif event.key == pygame.K_3:
                trivia.handle_input(2)
            elif event.key == pygame.K_4:
                trivia.handle_input(3)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()
    #填充屏幕
    screen.fill((0, 0, 250))
    #加载问题及选项
    trivia. show_question()
    #更新界面
    pygame.display.update()
                

                
            
