import numpy as np


def multiply_list(x):
    list_of_x = list(map(int, x.split()))
    if len(list_of_x) == 0:
        return 0
    else:
        return np.prod(list_of_x)


def count_common_chars(word):
    common_char = []
    word_split = word.split()
    for i in word_split[0]:
        if i in word_split[-1]:
            common_char.append(i)

    return common_char




def sum_divsible_by_k(n, k):
    if k == 0:
        return -1
    else:

        numbers = range(n + 1)

        list_of_divisible = []
        for i in numbers:

            if i % k == 0:
                list_of_divisible.append(i)
            else:
                continue

    if sum(list_of_divisible) == 0:
        return -1
    else:
        return sum(list_of_divisible)


def highest_common_factor(num1, num2):
    smaller = 0

    if num1 < num2:
        smaller = num1
    else:
        smaller = num2

    highest_commonr_factor = 0
    for i in range(1, smaller + 1):
        if (num1 % i == 0) & (num2 % i == 0):
            highest_common_factor = i

    return highest_common_factor


def get_minimum(my_list):
    return min(my_list)


def rename_col(df, name_old, name_new):
    dataframe = df

    dataframe = dataframe.rename(columns={name_old: name_new})

    return dataframe


import pandas as pd
import statistics


def standard_deviation(nums):
    my_series = pd.Series(nums)
    return statistics.stdev(my_series)


import pandas as pd
import numpy


def correlation_sum(string):
    spaced = ' '.join(string)
    list_convert = spaced.split()

    if len(list_convert) != 9:
        return 0
    else:
        my_array = np.asarray(list_convert).reshape(3, 3).astype(int)

        my_df = pd.DataFrame(my_array)

        corr_df = my_df.corr()

        return corr_df
