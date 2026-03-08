from __future__ import annotations

# Модуль №3. Задание №2

# Задача №1
class Patient:

    fio: str
    age: int
    disease: str
    data: int
    time: int

    def __init__(self, fio: str, age: int, disease: str, data: int, time: int):

        self.fio = fio
        self.age = age
        self.disease = disease
        self.data = data
        self.time = time

        if not isinstance(age, int):
            raise ValueError("Введите число")

    def data(day: int, month: str, year: int):

        if not isinstance(day, int) or (day < 1 or day > 31):
            raise ValueError("День прописывается числом, либо не может быть меньше 1 и больше 31")

        if not isinstance(year, int) or year < 2026:
            raise ValueError("Год прописывается числом, либо не может быть меньше 2026")

        return f"{day} {month} {year}"

    def time(hour: int, min: int):

        if not isinstance(hour, int) or (hour < 0 or hour > 23):
            raise ValueError("Час прописывается числом, либо не может быть меньше 0 и больше 23")

        if not isinstance(min, int) or (min < 1 or min > 59):
            raise ValueError("Минуты прописывается числом, либо не могут быть меньше 1 и больше 59")

        return f"{hour}:{min}"


    def visit_doctor(self): # Метод записи к врачу

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
data2 =Patient.data(19, "января", 2029)
time2 = Patient.time(12, 25)
p2 = Patient("Коблак Виктория Сергеевна", 18, "Кашель", data2, time2)
print(p2.visit_doctor())
print(p2)



