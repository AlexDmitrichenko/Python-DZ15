import logging
import argparse
"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет. Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа 
из вашего билета из list1 со списком выпавших чисел list2
Если совпадающих чисел нет, то выведите на экран: Совпадающих чисел нет.
Пример входных данных:
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
Пример выходных данных:
Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""
logging.basicConfig(filename='Task10_3.log',
                    filemode='w', encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()":\n{msg}', style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class LotteryGame:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def compare_lists(self):
        res = [numb for numb in self.list_a if numb in self.list_b]
        if len(res) == 0:
            logger.info(f'Совпадающих чисел нет.')
        else:
            logger.info(
                f'Совпадающие числа: {res}\n'
                f'Количество совпадающих чисел: {len(res)}')
            return res


def parse_args():
    parser = argparse.ArgumentParser(description='Лотерея')
    parser.add_argument('-list_a', type=str, nargs='*', help='Введите номера из билета через пробел')
    parser.add_argument('-list_b', type=str, nargs='*', help='Введите номера, которые выпали '
                                                             'в лотерею через пробел')
    return parser.parse_args()

# пример запуска командной строкой: python DZ15/task1.py -list_a='3 12 8 41 7 21 9 14 5 30' -list_b='9 5 6 12 14 22 17 41 8 3'

if __name__ == '__main__':

    args = parse_args()
    try:
        if len(args.list_a) != 10 or len(args.list_b) != 10:
            raise ValueError("Каждый из списков должен содержать 10 различных целых чисел")
        game = LotteryGame(args.list_a, args.list_b)
        matching_numbers = game.compare_lists()
    except ValueError as e:
        logger.error(f"DataError: {e}")
