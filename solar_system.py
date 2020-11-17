class Manager():
    """
    класс менеджера приложения
    """`

    def __init__(self, list_of_buttons):
    """
    запускается менеджер и интерфейс
    """
    pass

    def set_file_from(self, file_from):
    """
    функция, устанавливающая файл, откуда будут считываться данные для тел
    обязательна к выполнению в начале работы приложения
    """
    pass

    def process(self):
    """
    итерируемый через каждые dt времени код: перемещение планет, обновление
    их параметров, отрисовка, обработка событий на кнопках
    """
    pass

    def move_obj(self):
    """
    метод перемещения всех планет и обновления их параметров
    """
    pass

    def react_events(self, events):
    """
    метод обработки событий по всем кнопкам
    """
    pass

    def draw(self, screen):
    """
    отрисовка всех объектов на screen
    """
    pass

    def start(self):
    """
    запуск новых тел при изменении поля менеджера file_from
    """
    pass