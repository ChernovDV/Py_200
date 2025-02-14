class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self._author!r})"

""" Производный класс бумажная книги. """
class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value:int):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError('Количество страниц должно быть положительным и > 0')

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"
""" Производный класс аудиокниги. """
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if isinstance(value, float) and value > 0:
            self._duration = value
        else:
            raise ValueError('Продолжительность аудиокниги должна быть положительной')


    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
