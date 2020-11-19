from ss_objects import Body
from ss_draw import draw_objects
from ss_io import get_data
import numpy as np
import pygame


FILE = 'test.txt'


class Manager():
    """
    класс менеджера приложения
    """
    def __init__(self, dt, list_of_buttons=[]):
        """
        запускается менеджер и интерфейс
        """
        self.list_of_obj = []
        self.dt = dt 
        pass

    def set_file_from(self, file_from):
        """
        функция, устанавливающая файл, откуда будут считываться данные для тел
        обязательна к выполнению в начале работы приложения
        """
        data = get_data(file_from)
        for i in range(len(data)):
            m = data[i][0]
            r = data[i][1]
            colour = data[i][2]
            q = data[i][3]
            v = data[i][4]
            obj = Body(m, r, colour, q, v)
            self.list_of_obj.append(obj)
        

    def process(self, events, screen):
        """
        итерируемый через каждые dt времени код: перемещение планет, обновление
        их параметров, отрисовка, обработка событий на кнопках
        """
        done = self.react_events(events)
        self.move_obj()
        self.draw(screen)
        return done

    def move_obj(self):
        """
        метод перемещения всех планет и обновления их параметров
        """
        for obj in self.list_of_obj:
            obj.move(self.list_of_obj, self.dt)
    
    def react_events(self, events):
        """
        метод обработки событий по всем кнопкам
        """
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True
        return done

    def draw(self, screen):
        """
        отрисовка всех объектов на screen
        """
        for obj in self.list_of_obj:
            draw_objects(screen, self.list_of_obj)

    def start(self):
        """
        запуск новых тел при изменении поля менеджера file_from
        """

pygame.init()
screen = pygame.display.set_mode([800, 600])
done = False
clock = pygame.time.Clock()

manager = Manager(dt=1)

"""
пока костыль с пробными телами, потому что в ss_io и set_file_from
какой-то лютый баг с индексом массива t_data
"""

body1 = Body(5*10**13, 10, (0, 0, 0), [300, 300], [0, 3])
body2 = Body(5*10**13, 10, (0, 0, 0), [100, 300], [0, -3])
manager.list_of_obj.append(body1)
manager.list_of_obj.append(body2)

"""
manager.set_file_from(FILE)
"""

while not done:
    clock.tick(20)
    screen.fill([255, 255, 255])
    done = manager.process(pygame.event.get(), screen)
    pygame.display.flip()


pygame.quit()
