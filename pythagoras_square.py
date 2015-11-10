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


def count_the_number_of_each_digit(digit):
    control_array = [0,0, 0, 0, 0, 0, 0, 0, 0, 0]
    while digit > 0:
        res = digit % 10
        digit //= 10

        if res == 0:
            control_array[0] += 1
        elif res == 1:
            control_array[1] += 1
        elif res == 2:
            control_array[2] += 1
        elif res == 3:
            control_array[3] += 1
        elif res == 4:
            control_array[4] += 1
        elif res == 5:
            control_array[5] += 1
        elif res == 6:
            control_array[6] += 1
        elif res == 7:
            control_array[7] += 1
        elif res == 8:
            control_array[8] += 1
        else:
            control_array[9] += 1

    return control_array


def count_array(mas1, mas2, mas3, mas4, mas5, mas6, mas7):
    res_mas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 10):
        res_mas[i] += mas1[i] + mas2[i] + mas3[i] + mas4[i] + mas5[i] + mas6[i] + mas7[i]
    return res_mas


ch0 = get_sum_of_all_digits(day) + get_sum_of_all_digits(month)
ch0_0 = get_sum_of_all_digits(year)

ch1 = ch0 + ch0_0
ch2 = get_sum_of_all_digits(ch1)
ch3 = ch1 - (find_first_digit(day) * 2)
ch4 = get_sum_of_all_digits(ch3)

chpif = get_number_length(day) + 2 + 4 + get_number_length(ch1) + get_number_length(ch2) + get_number_length(
    ch3) + get_number_length(
    ch4)

print(count_array(count_the_number_of_each_digit(day),
                  count_the_number_of_each_digit(month),
                  count_the_number_of_each_digit(year),
                  count_the_number_of_each_digit(ch1),
                  count_the_number_of_each_digit(ch2),
                  count_the_number_of_each_digit(ch3),
                  count_the_number_of_each_digit(ch4)))
#print(ch4)
#print(count_the_number_of_each_digit(ch4))
