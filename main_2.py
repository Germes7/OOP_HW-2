from __future__ import annotations

# Модуль №3. Задание №2

# Задача №1
class Patient:

    fio: str
    age: int
    disease: str
    data: str
    time: str

    def __init__(self, fio: str, age: int, disease: str, data: str, time: str):

        if not isinstance(age, int):
            raise ValueError("Введите число")

        self.fio = fio
        self.age = age
        self.disease = disease
        self.data = data
        self.time = time

    @staticmethod
    def data(day: int, month: str, year: int):

        if not isinstance(day, int) or (day < 1 or day > 31):
            raise ValueError("День прописывается числом, либо не может быть меньше 1 и больше 31")

        if not isinstance(year, int) or year < 2026:
            raise ValueError("Год прописывается числом, либо не может быть меньше 2026")

        return f"{day} {month} {year}"

    @staticmethod
    def time(hour: int, min: int):

        if not isinstance(hour, int) or (hour < 0 or hour > 23):
            raise ValueError("Час прописывается числом, либо не может быть меньше 0 и больше 23")

        if not isinstance(min, int) or (min < 1 or min > 59):
            raise ValueError("Минуты прописывается числом, либо не могут быть меньше 1 и больше 59")

        return f"{hour}:{min}"

    def visit_doctor(self):  # Метод записи к врачу

        return f"Пациент записан на прием, на {self.data} в {self.time}"

    def __str__(self):

        return f"""Пациент: {self.fio}, возраст {self.age} лет. Заболевание: {self.disease}.
Записан на прием к врачу, на дату: {self.data} г. в {self.time};"""


data1 = Patient.data(17, "ноября", 2026)
time1 = Patient.time(13, 20)
p1 = Patient("Иванов Сергей Львович", 48, "Температура", data1, time1)
print(p1.visit_doctor())
print(p1)
print()
data2 = Patient.data(19, "января", 2029)
time2 = Patient.time(12, 25)
p2 = Patient("Коблак Виктория Сергеевна", 18, "Кашель", data2, time2)
print(p2.visit_doctor())
print(p2)


# Задача №3.
# Создайте класс ModelWindow для работы с моделями экранных окон. В качестве полей задаются:
# заголовок окна, координаты левого верхнего угла, размер по горизонтали, размер по вертикали, цвет окна,
# состояние “видимое/невидимое”, состояние “с рамкой/без рамки”.
# Координаты и размеры указываются в целых числах.
# Реализовать операции:
# передвижения окна по горизонтали, по вертикали;
# изменение высота и/или ширины окна;
# изменение цвет окна;
# изменение состояния;
# опрос состояния.
# Операции передвижения и изменения размера должны осуществлять проверку на пересечение границ экрана.
# Границы экрана принять 1960х1080.
# Операция вывода на экран (__str__) должна аккумулировать состояние полей объекта.

class ModelWindow:

    BORDER_X = 1960
    BORDER_Y = 1080

    title: str
    coord_left_angle_x: int
    coord_left_angle_y: int
    size_horiz: int
    size_vert: int
    color: str
    state_viz: str
    frame: str

    def __init__(self, title: str, coord_left_angle_x: int, coord_left_angle_y: int, size_horiz: int, size_vert: int, color: str, state_viz: str, frame: str):

        if size_horiz > 1960 or size_horiz < 0:
            raise ValueError("Размер по ширине, не должен выходить за рамки 0 - 1960")

        if size_vert > 1080 or size_vert < 0:
            raise ValueError("Размер по высоте, не должен выходить за рамки 0 - 1080")

        if coord_left_angle_x > 1960 or coord_left_angle_x < 0:
            raise ValueError("Точка верхнего лев. угла окна, не должен выходить за рамки 0 - 1960")

        if coord_left_angle_y > 1080 or coord_left_angle_y < 0:
            raise ValueError("Точка верхнего лев. угла окна, не должен выходить за рамки 0 - 1080")

        self.title = title
        self.coord_left_angle_x = coord_left_angle_x
        self.coord_left_angle_y: coord_left_angle_y
        self.size_horiz = size_horiz
        self.size_vert = size_vert
        self.color = color
        self.state_viz = state_viz
        self.frame = frame

    def shift_horizontal(self, param: int):  # Сдвиг по горизонтали

        new_cord_left = self.coord_left_angle_x + param

        if new_cord_left + self.size_horiz > self.BORDER_X:
            self.coord_left_angle_x = self.BORDER_X - self.size_horiz  # Ставим правую границу окна вплотную к правой границе экрана (BORDER_X)

            return f"Достигнута правая граница экрана {self.BORDER_X}"

        elif new_cord_left + self.size_horiz < self.BORDER_X:
            self.coord_left_angle_x = new_cord_left

        elif (new_cord_left + self.size_horiz) < 0:
            self.coord_left_angle_x = 0

            return f"Достигнута левая граница экрана {self.BORDER_X}"

    def shift_vertical(self, param: int):  # Сдвиг по вертикали

        new_cord_left = self.coord_left_angle_y + param

        if new_cord_left + self.size_vert > self.BORDER_Y:
            self.coord_left_angle_y = self.BORDER_Y - self.size_vert  # Ставим верхнюю границу окна к верхней границе экрана (BORDER_Y)

            return f"Достигнута верхняя граница экрана {self.BORDER_Y}"

        elif new_cord_left + self.size_vert < self.BORDER_Y:
            self.coord_left_angle_y = new_cord_left

        elif (new_cord_left + self.size_vert) < 0:
            self.coord_left_angle_y = self.size_vert

            return f"Достигнута нижняя граница экрана {self.BORDER_Y}"

    def set_change_height(self, param: int):  # Изменение ширины окна

        new_height = self.size_horiz + param

        if new_height > self.BORDER_X:
            self.size_horiz = self.BORDER_X

            return f"Ширина окна равна ширине экрана {self.BORDER_X}"

        elif new_height < 0:  # Оставляем ширину окна без изменения
            self.size_horiz = self.size_horiz

        else:  # На случай введения отрицательного значения в param, т.е. уменьшаем ширину окна
            self.size_horiz = new_height

    def change_width(self):  # Изменение высоты окна
        pass

    def set_change_color(self):  # Изменение цвета окна
        pass

    def set_change_state(self):  # Изменение состояния (видимое/не видимое) окна
        pass

    def get_state(self):  # Опрос состояния
        pass

    def __str__(self):
        pass
