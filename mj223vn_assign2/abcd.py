def to_four_digit_str(a, b, c, d):
    to_str = str(a) + str(b) + str(c) + str(d)
    return to_str


for a in range(1, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(1, 9):
                if (1000*a + 100*b + 10*c + d) * 4 == 1000*d + 100*c + 10*b + a:
                    print("The digits we are loking for is:", to_four_digit_str(a, b, c, d))
