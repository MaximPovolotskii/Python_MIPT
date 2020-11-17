class Body():
    """
    класс физических тел в симуляции: планет и звёзд
    базовые параметры: масса, радиус, цвет, координаты (массив), скорость (массив)
    """
    def __init__(self, mass, radius, colour, coordinates, velocities):
        pass

    def move(self, list_of_obj):
        """
        метод движения тела
        для координат выполняется = скорость * dt + ускорение * dt^2 / 2,
        ускорение считается по всем другим телам из list_of_obj с помощью calc_force
        для скоростей выполняется = ускорение * dt
        """
        pass
    
    def calc_force(self, another_body):
        """
        метод, рассчитывающий силу взаимодействия между данным телом и некоторым другим
        """
        pass
