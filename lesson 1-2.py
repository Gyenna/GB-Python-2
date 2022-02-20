row_power_three = []
number = 1
while number < 1000:
    if number % 2 == 1:
        row_power_three.append(number ** 3)
    number = number + 1
print(row_power_three)
sum_row1 = 0
for number_power_three in row_power_three:
    k = number_power_three
    y = 0
    while number_power_three >= 1:
        y += number_power_three % 10
        number_power_three = number_power_three // 10
    if y % 7 == 0:
        sum_row1 += k
print(sum_row1)
sum_row2 = 0
for number_power_three in row_power_three:
    number_power_three += 17
    k = number_power_three
    y = 0
    while number_power_three >= 1:
        y += number_power_three % 10
        number_power_three = number_power_three // 10
    if y % 7 == 0:
        sum_row2 += k
print(sum_row2)
