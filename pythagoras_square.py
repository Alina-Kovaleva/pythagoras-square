day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))


def get_sum_of_all_digits(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    
    return res


def find_first_digit(p):
    while p >= 10:
        p % 10
        p //= 10

    return p


def get_number_length(che):
    res1 = 0
    while che > 0:
        res1 += 1
        che //= 10
    return res1


ch0 = get_sum_of_all_digits(day) + get_sum_of_all_digits(month)
year = get_sum_of_all_digits(year)

ch1 = ch0 + year
ch2 = get_sum_of_all_digits(ch1)
ch3 = ch1 - (find_first_digit(day) * 2)
ch4 = get_sum_of_all_digits(ch3)

chpif = get_number_length(day) + 2 + 4 + get_number_length(ch1) + get_number_length(ch2) + get_number_length(ch3) + get_number_length(
    ch4)
print(ch1, ch2, ch3, ch4)
print(chpif)


