# TODO Написать 3 класса с документацией и аннотацией типов
import doctest




class City:
    def __init__(self, name: str, population: int, temperature: int):
        self.name = name
        self.population = population
        self.temperature = temperature
        """
        Создание и подготовка к работе класса "City"

        :param name: Название города
        :param population: Население города
        :param temperature: Средняя температура летом
        """
        if population <= 12000:
            raise ValueError("Население города в РФ не может быть меньше 12000.")
        if not isinstance(population, (int)):
            raise TypeError (" Количество жителей должно быть int ")

    def city_for_summer_holiday(self, diapazon_temperature: dict) -> bool:
        """
        Подходит ли город для летнего отдыха
        :param  diapazon_temperature: Min и Max значение температуры комфортной для летнего отдыха

        Пример:
        >>> city = City('Sochi', 1000000, 35)
        >>> city.city_for_summer_holiday({'min':28, 'max':37})
        Город подходит для летнего отдыха
        """
        if diapazon_temperature['min'] < self.temperature < diapazon_temperature['max']:
            print("Город подходит для летнего отдыха")
        else:
            print("Посмотрите ещё варианты")

    def undeground_in_city(self, undeground_list: list) -> bool:
        """
        Есть ли в городе метро
        :param  undeground_list: список городов РФ с метро

        Пример:
        >>> city = City('SPb', 7000000, 24)
        >>> city.undeground_in_city(['SPb', 'Msk', 'Ekb'])
        В городе SPb есть метро

        """
        if self.name  in undeground_list:
            print(f'В городе {self.name} есть метро')
        else:
            print(f'В городе {self.name} нет метро')



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()