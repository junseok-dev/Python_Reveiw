def plan(time, do_it):
    print(time, do_it, "해야(가야) 합니다.")
plan("6:00 ~ 7:00", "운동")
plan("7:00 ~ 8:00", "학원")


def mul (*values):
    print(*values)
    return (5*7*9*10)

print(mul(5,7,9,10))