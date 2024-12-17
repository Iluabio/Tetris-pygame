def calcSpeed(points):
    # вычисляет уровень
    level = int(points / 10) + 1
    fall_speed = 0.27 - (level * 0.02)
    return level, fall_speed

def getNewFig():
    # возвращает новую фигуру со случайным цветом и углом поворота
    shape = random.choice(list(figures.keys()))
    newFigure = {'shape': shape,
                'rotation': random.randint(0, len(figures[shape]) - 1),
                'x': int(cup_w / 2) - int(fig_w / 2),
                'y': -2, 
                'color': random.randint(0, len(colors)-1)}
    return newFigure


