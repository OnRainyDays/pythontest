
import pygame,sys

from settings import Settings

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Tnvasion")


    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #每次循环时都会重绘屏幕
        screen.fill(ai_settings.bg_color)
         #让最近绘制的屏幕可见
        pygame.display.flip()
run_game()
