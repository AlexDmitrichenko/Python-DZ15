"""
Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет представлять
прямоугольник с заданными шириной и высотой.
Атрибуты класса: width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
Методы класса:
__init__(self, width, height=None): Конструктор класса. Принимает ширину и высоту прямоугольника.
Если высота не указана (по умолчанию None), то считается, что прямоугольник является квадратом,
и высота устанавливается равной ширине.
perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра.
area(self): Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.
__add__(self, other): Магический метод, который определяет операцию сложения (+) для двух прямоугольников.
Принимает другой прямоугольник other. Создает новый прямоугольник, который представляет собой объединение
исходных прямоугольников по периметру. Новая ширина и высота вычисляются также на основе объединения.
Возвращает новый прямоугольник.
__sub__(self, other): Магический метод, который определяет операцию вычитания (-) одного прямоугольника из другого.
Принимает вычитаемый прямоугольник other. Создает новый прямоугольник, представляющий разницу периметров
исходных прямоугольников, и вычисляет высоту на основе этой разницы. Новая ширина вычисляется также на основе разницы.
Возвращает новый прямоугольник.
__lt__(self, other): Магический метод, который определяет операцию "меньше" (<) для двух прямоугольников.
Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше площади второго,
иначе False.
__eq__(self, other): Магический метод, который определяет операцию "равно" (==) для двух прямоугольников.
Принимает другой прямоугольник other. Возвращает True, если площади равны, иначе False.
__le__(self, other): Магический метод, который определяет операцию "меньше или равно" (<=) для двух прямоугольников.
Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше или равна
площади второго, иначе False.
__str__(self): Магический метод, возвращающий строковое представление прямоугольника. Возвращает строку,
описывающую ширину и высоту прямоугольника в виде:
Прямоугольник со сторонами 2 и 3, где первое число - это ширина, а второе - высота.
__repr__(self): Магический метод, возвращающий строковое представление прямоугольника, которое может быть
использовано для создания нового объекта такого же класса с теми же атрибутами.
Пояснение:
Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров исходных прямоугольников,
и создает новый прямоугольник.
Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.
Пример использования:
На входе:
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")
На выходе:
Периметр rect1: 30
Площадь rect2: 21
rect1 < rect2: False
rect1 == rect2: False
rect1 <= rect2: False
Периметр rect3: 50
Ширина rect4: 2
"""
import logging
import argparse

logging.basicConfig(filename='Task13_1.log',
                    filemode='w', encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno}\n'
                           '{msg}', style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class Rectangle:
    """
    Класс, представляющий прямоугольник.
    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника
    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if width < 0:
            raise ValueError("Ширина должна быть положительной, а не {}".format(width))
        if height is not None and height < 0:
            raise ValueError("Высота должна быть положительной, а не {}".format(height))
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.
        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.
        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.
        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник
        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.
        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


def parse_args():
    parser = argparse.ArgumentParser(description='Размеры прямоугольника')
    parser.add_argument('-r1_w', type=int, help='Ширина прямоугольника 1')
    parser.add_argument('-r1_h', type=int, default=None, help='Высота прямоугольника 1')
    parser.add_argument('-r2_w', type=int, help='Ширина прямоугольника 2')
    parser.add_argument('-r2_h', type=int, default=None, help='Высота прямоугольника 2')

    return parser.parse_args()


# передача параметров -r1_w=3 -r1_h=3 -r2_w=2 -r2_h=2 через Edit Configurations

if __name__ == '__main__':
    args = parse_args()
    try:
        r1 = Rectangle(args.r1_w, args.r1_h)
        logger.info(f"r1: {r1}")
        logger.info(f"r1 width: {r1.width}, height: {r1.height}")
        logger.info(f"r1 perimeter: {r1.perimeter()}")
        logger.info(f"r1 area: {r1.area()}")
        r2 = Rectangle(args.r2_w, args.r2_h)
        logger.info(f"r2: {r2}")
        logger.info(f"r2 width: {r2.width}, height: {r1.height}")
        logger.info(f"r2 perimeter: {r2.perimeter()}")
        logger.info(f"r2 area: {r2.area()}")
        r3 = r1 + r2
        logger.info(f"r3: {r3}")
        logger.info(f"r3 width: {r3.width}, height: {r3.height}")
        logger.info(f"r3 perimeter: {r3.perimeter()}")
        logger.info(f"r3 area: {r3.area()}")
        r4 = r3 - r2
        logger.info(f"r4: {r4}")
        logger.info(f"r4 width: {r4.width}, height: {r4.height}")
        logger.info(f"r4 perimeter: {r4.perimeter()}")
        logger.info(f"r4 area: {r4.area()}")
        logger.info(f"r1 < r2: {r1 < r2}")
        logger.info(f"r1 == r2: {r1 == r2}")
        logger.info(f"r1 <= r2: {r1 <= r2}")
    except ValueError as e:
        logger.error(f'DataError: {e}')