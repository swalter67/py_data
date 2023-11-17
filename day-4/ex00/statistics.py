from typing import Any

from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    args_list = list(args)
    total = 0
    values = []
    num_args = len(args)

    if num_args == 0:
        print("ERROR")
        return

    for arg in args_list:
        total += arg
        values.append(arg)

    mean = total / num_args

    values.sort()

    median_index = num_args // 2
    if num_args % 2 == 0:
        median = (values[median_index - 1] + values[median_index]) / 2
    else:
        median = values[median_index]

    q1_index = num_args // 4
    q3_index = q1_index * 3
    quartile = [float(values[q1_index]), float(values[q3_index])]

    variance_total = sum((value - mean) ** 2 for value in values)
    variance = variance_total / num_args
    std_deviation = variance ** 0.5

    result = {"mean": mean, "median": median, "quartile": quartile,
              "std": std_deviation, "var": variance}

    for key, value in kwargs.items():
        if value in result:
            print(f"{value} : {result[value]}")
        else:
            print("ERREUR")    