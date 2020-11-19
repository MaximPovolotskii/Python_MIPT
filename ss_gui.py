class Button():
    """
    класс кнопки
    параметры: координаты на экране, прямоугольник формы, подпись, цвет
    """
    def __init__(self, role, coordinates, rectangle, caption, colour):
        self.coord = coordinates
        self.rectangle = rectangle
        self.caption = caption
        self.colour = colour
        self.role = role
        pass

    def click(point):
        """
        проверяет, находится ли point внутри прямоугольника кнопки
        """
        flag = False
        if self.coord[0] < point[0]:
            if self.coord[0] + self.rectangle[0] > point[0]:
                if self.coord[1] < point[1]:
                    if self.coord[1] + self.rectangle[1] > point[1]:
                        flag = True
        return flag
        pass

    def handle_events(self, events):
        """
        обработчик событий с кнопкой
        """
        done = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.click(event.pos) == True:
                    button.function()
        return done
        pass
