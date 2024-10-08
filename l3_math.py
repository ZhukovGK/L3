import math as m


# Осуществляем ввод радиуса в см с клавиатуры
user_radius = int(input(
    "Добрый день! Введите радиус круга в сантиметрах, и я посчитаю много интересных вещей, связанных с этим радиусом: "))

PI = 3.14 # задаем значение числа пи

# считаем длину окружности и площадь круга
round_len = 2 * user_radius * PI # длина окружности равна двум радиусам, умноженным на число пи
round_sqr = user_radius ** 2 * PI # площадь круга равна квадрату радиуса на число пи

# вычисляем сторону вписанных фигур
inner_square_side = user_radius # сторона вписанного квадрата равна радиусу
inner_triangle_side = user_radius * m.sqrt(3) # сторона вписанного треугольника равна радиус на корень из 3

# вычисляем стороны описанных фигур
outer_square_side = user_radius * 2 # сторона описанного квадрата = диаметр
# сторона описанного треугольника равна четыре радиуса на корень из 3 или четыре стороны вписанного треугольника
outer_triange_side = inner_triangle_side * 4 
outer_oktagon_side = user_radius * m.sqrt(2) # сторона описанного восьмиугольникагольника равна радиус на корень из 2

# вывод всего посчитанного в см и в м
print("Длина окружности = ", round_len, "см и ", round_len / 100,"м")
print("Площадь круга = ", round_sqr, "см2 и ", round_sqr / 10000,"м2")
print("Сторона вписанного в окружность квадрата = ", inner_square_side, "см и ", inner_square_side / 100,"м")
print("Сторона вписанного в окружность равностороннего треугольника = ", inner_triangle_side, "см и ", inner_triangle_side / 100,"м")
print("Сторона описанного вокруг окружности квадрата = ", outer_square_side, "см и ", outer_square_side / 100,"м")
print("Сторона описанного вокруг окружности равностороннего треугольника = ", outer_triange_side, "см и ", outer_triange_side / 100,"м")
print("Сторона описанного вокруг окружности восьмиугольника = ", outer_oktagon_side, "см и ", outer_oktagon_side / 100,"м")