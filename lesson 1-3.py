number = 0
while number < 100:
    number += 1
    if number >= 5 and number <= 20:
        print(number, "процентов")
    elif number % 10 == 1:
        print(number, "процент")
    else:
        print(number, "процента")
