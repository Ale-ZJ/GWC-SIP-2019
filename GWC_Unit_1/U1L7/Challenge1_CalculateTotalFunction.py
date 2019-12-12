def main():
    a = [1, 10, 36, 101, 56, 17, 209, 13, 35, 156347.325]
    calc_total(a)

def calc_total(values):
    sum = 0
    for a in values:
        sum += a
    return sum
