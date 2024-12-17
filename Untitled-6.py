def stopGame():
    pg.quit()
    sys.exit()


def checkKeys():
    quitGame()

    for event in pg.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def quitGame():
    for event in pg.event.get(QUIT): # проверка всех событий, приводящих к выходу из игры
        stopGame() 
    for event in pg.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            stopGame() 
        pg.event.post(event)



