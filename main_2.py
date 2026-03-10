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
print("-----------------------------------------------------------------------------------------------------")

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

    def __init__(self, title: str, coord_left_angle_x: int, coord_left_angle_y: int, size_horiz: int, size_vert: int,
                 color: str, state_viz: str, frame: str):

        if size_horiz > self.BORDER_Y or size_horiz < 0:
            raise ValueError("Размер по ширине, не должен выходить за рамки 0 - 1960")

        if size_vert > self.BORDER_Y or size_vert < 0:
            raise ValueError("Размер по высоте, не должен выходить за рамки 0 - 1080")

        if coord_left_angle_x > self.BORDER_Y or coord_left_angle_x < 0:
            raise ValueError("Точка верхнего лев. угла окна, не должен выходить за рамки 0 - 1960")

        if coord_left_angle_y > self.BORDER_Y or coord_left_angle_y < 0:
            raise ValueError("Точка верхнего лев. угла окна, не должен выходить за рамки 0 - 1080")

        self.title = title
        self.coord_left_angle_x = coord_left_angle_x
        self.coord_left_angle_y = coord_left_angle_y
        self.size_horiz = size_horiz
        self.size_vert = size_vert
        self.color = color
        self.state_viz = state_viz
        self.frame = frame

    def shift_horizontal(self, param: int):  # Сдвиг по горизонтали

        new_cord_left = self.coord_left_angle_x + param

        if new_cord_left + self.size_horiz > self.BORDER_X:
            self.coord_left_angle_x = self.BORDER_X - self.size_horiz  # Ставим правую границу окна вплотную к правой границе экрана (BORDER_X)

            return f"Достигнута правая граница экрана {self.BORDER_X}. Положение координаты верхнего левого угла (по горизонтали): {self.coord_left_angle_x}"

        elif new_cord_left + self.size_horiz < self.BORDER_X and new_cord_left + self.size_horiz > 0:
            self.coord_left_angle_x = new_cord_left

            return f"Положение окна сдвинуто вправо. Положение координаты верхнего левого угла (по горизонтали): {self.coord_left_angle_x}"

        elif (new_cord_left + self.size_horiz) < 0:
            self.coord_left_angle_x = 0

            return f"Достигнута левая граница экрана {self.BORDER_X}. Положение координаты верхнего левого угла (по горизонтали): {self.coord_left_angle_x}"

    def shift_vertical(self, param: int):  # Сдвиг по вертикали

        new_cord_left = self.coord_left_angle_y + param

        if new_cord_left + self.size_vert > self.BORDER_Y:
            self.coord_left_angle_y = self.BORDER_Y - self.size_vert  # Ставим верхнюю границу окна к верхней границе экрана (BORDER_Y)

            return f"Достигнута верхняя граница экрана {self.BORDER_Y}. Положение координаты верхнего левого угла (по вертикали) {self.coord_left_angle_y}"

        elif (new_cord_left + self.size_vert) < self.BORDER_Y and (new_cord_left + self.size_vert) > 0:
            self.coord_left_angle_y = new_cord_left

            return f"Положение окна сдвинуто вверх. Положение координаты верхнего левого угла (по вертикали) {self.coord_left_angle_y}"

        elif (new_cord_left + self.size_vert) < 0:
            self.coord_left_angle_y = self.size_vert

            return f"Достигнута нижняя граница экрана {self.BORDER_Y}. Положение координаты верхнего левого угла (по вертикали): {self.coord_left_angle_y}"

    def set_change_height(self, param: int):  # Изменение ширины окна

        new_height = self.size_horiz + param

        if new_height > self.BORDER_X:
            self.size_horiz = self.BORDER_X

            return f"Ширина окна равна ширине экрана {self.BORDER_X} мм."

        elif new_height < 0:  # Оставляем ширину окна без изменения
            self.size_horiz = self.size_horiz

            return f"Ширина окна, осталась без изменения {self.size_horiz} мм."

        elif new_height < self.BORDER_X and new_height > 0:

            if new_height > self.size_horiz:
                self.size_horiz = new_height

                return f"Ширина окна увеличилась, стала равной: {self.size_horiz} мм."

            else:
                self.size_horiz = new_height

                return f"Ширина окна уменьшилась, стала равной: {self.size_horiz} мм."

    def set_change_width(self, param: int):  # Изменение высоты окна

        new_width = self.size_vert + param

        if new_width > self.BORDER_Y:
            self.size_vert = self.BORDER_Y

            return f"Высота окна равна высоте экрана {self.BORDER_Y} мм."

        elif new_width < 0:  # Оставляем высоту окна без изменения, на случай введения отрицат. значений
            self.size_vert = self.size_vert

            return f"Высота окна, осталась без изменения {self.size_vert} мм."

        elif new_width < self.BORDER_Y and new_width > 0:

            if new_width > self.size_vert:
                self.size_vert = new_width

                return f"Высота окна увеличилась, стала равной: {self.size_vert} мм."

            else:
                self.size_vert = new_width

                return f"Высота окна уменьшилась, стала равной: {self.size_vert} мм."

    def set_change_color(self, new_color: str):  # Изменение цвета окна

        if not isinstance(new_color, str):
            raise ValueError("Введена не строка")

        if new_color == self.color:
            return f"Окно уже в данном цвете: {self.color}"

        else:
            self.color = new_color

            return f"Окно перекрашено в цвет: {new_color}"

    def set_change_state(self, param: str):  # Изменение состояния (видимое/не видимое) окна

        new_state = "Не видимое"

        if self.state_viz.capitalize() == param.capitalize():

            return f"Окно: {self.state_viz}"

        else:
            self.state_viz = new_state

            return f"Окно: {self.state_viz}"

    def set_change_frame(self, parm: str):  # Изменение состояния окна (с рамкой/без рамки)

        frame_lower = parm.lower()
        frames = ["с рамкой", "без рамки"]

        if frame_lower not in frames:

            return f"Недопустимое значение для рамки: '{parm}'. Допустимые значения: 'с рамкой', 'без рамки'."

        if self.frame.lower() == frame_lower:

                return f"Рамка уже установлена: {self.frame.capitalize()}"

        else:
            self.frame = frame_lower.capitalize()

            return f"Рамка окна изменена на: {self.frame}"

    def get_state(self):  # Опрос состояния.

        return f"Вид окна: {self.state_viz}. {self.frame}."

    def __str__(self):

        return f"""Создано окно. Название окна: '{self.title}';
Положение координаты верхнего левого угла (по Абсцисе X): {self.coord_left_angle_x};
Положение координаты верхнего левого угла (по Ординате Y): {self.coord_left_angle_y};
Ширина окна: {self.size_horiz} мм; Высота окна: {self.size_vert} мм;
Цвет окна: {self.color}; Состояние: {self.state_viz}; Наличие рамки: {self.frame}"""

wind = ModelWindow("Новое",100,120, 800,780,"синее","Видимое","без рамки")
print(wind)
horizont = wind.shift_horizontal(-2120)
print(horizont)
vertical = wind.shift_vertical(-3520)
print(vertical)
size_h = wind.set_change_height(127)
print(size_h)
size_v = wind.set_change_width(365)
print(size_v)
color = wind.set_change_color("красное")
print(color)
state = wind.set_change_state("не видимое")
print(state)
frame = wind.set_change_frame("С рамкой")
print(frame)
get = wind.get_state()
print(get)
print("-----------------------------------------------------------------------------------------------------")

# Задача №4.
# Создайте класс ArrayUtils, который будет содержать статические методы для выполнения различных операций над массивами
# целых чисел. Этот класс будет полезен в ситуациях, когда нужно провести стандартные операции над массивами, такие
# как расчет суммы или произведения элементов, без необходимости создания экземпляра класса.
# Операции класса:
# 1. :Метод для расчёта суммы элементов массива
# • Входные данные: массив чисел.
# • Выходные данные: сумма всех элементов массива.
# 2. :Метод для расчёта произведения элементов массива
# • Входные данные: массив чисел.
# • Выходные данные: произведение всех элементов массива.
# 3. :Метод для инверсии массива
# • Входные данные: массив чисел.
# • Выходные данные: массив с элементами в обратном порядке.
# 4. :Метод для нахождения максимального элемента в массиве
# • Входные данные: массив чисел.
# • Выходные данные: максимальное значение среди элементов массива.
# 5. :Метод для нахождения минимального элемента в массиве
# • Входные данные: массив чисел.
# • Выходные данные: минимальное значение среди элементов массива.

class ArrayUtils:

    @staticmethod
    def sum_elem_array(array: list[float]) -> float:

        if len(array) > 0:

            sum = 0
            for i in array:
                sum += i

            return sum

        return 0.0

    @staticmethod
    def mult_elem_array(array: list[float]) -> float:

        if len(array) > 0:

            multy = 1
            for i in array:
                multy *= i

            return multy

        return 0.0

    @staticmethod
    def revers_array(array: list[float]) -> list[float] | int:

        if len(array) > 0:

            return array[::-1]

        return 0

    @staticmethod
    def max_elem_array(array: list[float]) -> float:

        if len(array) > 0:

            max_elem = array[0]
            for i in array:

                if max_elem < i:
                    max_elem = i

            return max_elem

        return 0.0

    @staticmethod
    def min_elem_array(array: list[float]) -> float:

        if len(array) > 0:

            min_elem = array[0]
            for i in array:

                if i < min_elem:
                    min_elem = i

            return min_elem

        return 0.0

print(ArrayUtils.sum_elem_array([0, 7, -2, 4]))
print(ArrayUtils.mult_elem_array([-5, 4, -25]))
print(ArrayUtils.revers_array([5]))
print(ArrayUtils.max_elem_array([3, -5, -7, 0, -1]))
print(ArrayUtils.min_elem_array([2, -5, 0, 4]))
print("-----------------------------------------------------------------------------------------------------")

# Задача №6.
# Создайте класс Fraction для работы с дробями. Класс должен включать поля:
# числитель и знаменатель, оба целочисленные значения. Реализуйте методы для сложения, вычитания и умножения дробей.
# Перегрузите соответствующие операторы (+, -, *) для реализации этих операций. Каждая операция должна
# возвращать новый объект класса Fraction, представляющий результат. Добавьте методы проверки на знаменатель равный
# нулю перед выполнением операций.
# Операция вывода на экран ( __str__ ) должна отображать дробь в формате"числитель/знаменатель" или "целое число",
# если знаменатель равен 1.

class Fraction:

    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int):

        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):

        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator

        return Fraction(new_num, new_den)

    def __str__(self):

        if self.denominator == 1:

            return f"{self.numerator}"

        else:

            return f"{self.numerator}/{self.denominator}"

f1 = Fraction(5, 12)
print(f1)
f2 = Fraction(4, 17)
print(f2)
print(f1 + f2)