# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Smartphone:
    def __init__(self, screen_size:int, model:str, price:int):
        self.model = model
        self.screen_size = screen_size
        self.price = price
        """
        Создание и подготовка к работе класса "Smartphone"
        
        :param screen_size: Размер экрана
        :param model: Модель смартфона
        :param batery: Ёмкость батареи
        """
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом.")

    def price_with_discount(self, discount:int)->float:
        """
        Рассчитывает цену со скидкой
        :param  discount: Величина скидки
        :return new_price: Цена со скидкой
        Пример:
        >>> smartphone = Smartphone(11, 'Redmi 10T', 20000)
        >>> smartphone.price_with_discount(10)
        18000.0
        """
        new_price = self.price * (100 - discount) / 100
        return new_price

    def model_in_shop(self, model_list:list)->bool:
        """
        Проверяет, доступна ли указанная модель в магазине.
        :param  model_list: перечень доступных смартфонов в магазине
        Пример:
        >>> smartphone = Smartphone(11, 'Redmi 10T', 100000)
        >>> smartphone.model_in_shop(['iPhone 14', 'Iphone 10'])
        Данная модель Redmi 10T смартфона в магазине отсутствует

        """
        if self.model not in model_list:
            print(f'Данная модель {self.model} смартфона в магазине отсутствует')
        else:
            print(f'Данная модель {self.model} смартфона в магазине есть в наличии')


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

