import sys,pygame

def check_keydown_events(event,ship):



    """ 响应按键和鼠标事件"""

def update_screen(ai_settings,screen,ship):

    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()
