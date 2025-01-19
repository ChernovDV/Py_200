# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Flat:
    def __init__(self, count_room: int, count_family: int, square: float):
        self.count_room = count_room
        self.count_family = count_family
        self.square = square
        """
        Создание и подготовка к работе класса "Flat"

        :param count_room: Количество комнат в квартире
        :param count_family: Количество членов семьи
        :param square: Площадь квартиры
        """
        if count_room < 1:
            raise ValueError("Количество комнат не может быть меньше 1.")
        if count_family < 2:
            raise ValueError("Количество членов семьи не может быть меньше 2")

    def square_on_man(self) -> float:
        """
        Рассчитывает площадь в квартире на человека
        :return square_man: Площадь в квартире на человека
        Пример:
        >>> flat = Flat(2, 3, 60)
        >>> flat.square_on_man()
        20.0
        """
        square_man = self.square / self.count_family
        return square_man

    def flat_price(self, price_for_m2: float) -> float:
        """
        Считакм стоимость квартиры.
        :param price_for_m2: Цена за квадратный метр
        :return new_price: Стоимость квартиры
        Пример:
        >>> flat = Flat(2, 3, 60)
        >>> flat.flat_price(100000)
        6000000
        """
        all_price = self.square * price_for_m2
        return all_price


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()