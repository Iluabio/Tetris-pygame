def pauseScreen():
        pause = pg.Surface((600, 500), pg.SRCALPHA)   
        pause.fill((0, 0, 255, 127))                        
        display_surf.blit(pause, (0, 0))


def txtObjects(text, font, color):
    surf = font.render (text, True, color)
    return surf, surf.get_rect()


def showText(text):
    titleSurf, titleRect = txtObjects(text, big_font, title_color)
    titleRect.center = (int(window_w / 2) - 3, int(window_h / 2) - 3)
    display_surf.blit(titleSurf, titleRect)
   
    pressKeySurf, pressKeyRect = txtObjects('Нажмите любую клавишу для продолжения', basic_font, title_color)
    pressKeyRect.center = (int(window_w / 2), int(window_h / 2) + 100)
    display_surf.blit(pressKeySurf, pressKeyRect)

    while checkKeys() == None:
        pg.display.update()
        fps_clock.tick()


def drawTitle():
    titleSurf = big_font.render('Тетрис Lite', True, title_color)
    titleRect = titleSurf.get_rect()
    titleRect.topleft = (window_w - 425, 30)
    display_surf.blit(titleSurf, titleRect)
    

def drawInfo(points, level):

    pointsSurf = basic_font.render(f'Баллы: {points}', True, txt_color)
    pointsRect = pointsSurf.get_rect()
    pointsRect.topleft = (window_w - 550, 180)
    display_surf.blit(pointsSurf, pointsRect)

    levelSurf = basic_font.render(f'Уровень: {level}', True, txt_color)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (window_w - 550, 250)
    display_surf.blit(levelSurf, levelRect)

    pausebSurf = basic_font.render('Пауза: пробел', True, info_color)
    pausebRect = pausebSurf.get_rect()
    pausebRect.topleft = (window_w - 550, 420)
    display_surf.blit(pausebSurf, pausebRect)
    
    escbSurf = basic_font.render('Выход: Esc', True, info_color)
    escbRect = escbSurf.get_rect()
    escbRect.topleft = (window_w - 550, 450)
    display_surf.blit(escbSurf, escbRect)


def drawFig(fig, pixelx=None, pixely=None):
    figToDraw = figures[fig['shape']][fig['rotation']]
    if pixelx == None and pixely == None:    
        pixelx, pixely = convertCoords(fig['x'], fig['y'])

    #отрисовка элементов фигур
    for x in range (fig_w):
        for y in range (fig_h):
            if figToDraw[y][x] != empty:
                drawBlock(None, None, fig['color'], pixelx + (x * block), pixely + (y * block))


def drawnextFig(fig):  # превью следующей фигуры
    nextSurf = basic_font.render('Следующая:', True, txt_color)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (window_w - 150, 180)
    display_surf.blit(nextSurf, nextRect)
    drawFig(fig, pixelx=window_w-150, pixely=230)


def convertCoords(block_x, block_y):
    return (side_margin + (block_x * block)), (top_margin + (block_y * block))


def drawBlock(block_x, block_y, color, pixelx=None, pixely=None):
    #отрисовка квадратных блоков, из которых состоят фигуры
    if color == empty:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(block_x, block_y)
    pg.draw.rect(display_surf, colors[color], (pixelx + 1, pixely + 1, block - 1, block - 1), 0, 3)
    pg.draw.rect(display_surf, lightcolors[color], (pixelx + 1, pixely + 1, block - 4, block - 4), 0, 3)
    pg.draw.circle(display_surf, colors[color], (pixelx + block / 2, pixely + block / 2), 5)