"""ЛР8, задание 2: класс с property — управляемый атрибут с валидацией и вычисляемое свойство.

Запуск: python task2_property/main.py
"""
class Temperature:
    """Температура в °C.

    Атрибут celsius объявлен как property: чтение — геттер, запись — сеттер
    с проверкой физического минимума (абсолютный нуль).
    """

    MIN_CELSIUS = -273.15

    def __init__(self, celsius: float = 0.0):
        # Присваивание идёт через сеттер property — валидация срабатывает и здесь
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """Геттер: доступ к защищённому полю _celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < self.MIN_CELSIUS:
            raise ValueError(
                f"Значение ниже абсолютного нуля: {value} < {self.MIN_CELSIUS}")
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        """Вычисляемое property: пересчитывается при каждом чтении, поля не хранит."""
        return self._celsius * 9 / 5 + 32


if __name__ == "__main__":
    t = Temperature(25)
    print("celsius:", t.celsius)                      # чтение через геттер
    print("fahrenheit:", t.fahrenheit)                # вычисляемое property

    t.celsius = 100                                   # запись через сеттер
    print("после t.celsius = 100 -> fahrenheit:", t.fahrenheit)

    try:
        t.celsius = -300                              # сеттер отклоняет значение
    except ValueError as exc:
        print("валидация сработала:", exc)
