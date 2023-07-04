def go_back_n_arq(n, test_cases):
    for i in range(n):
        m, Sf, Sn, E1, E2, E3 = test_cases[i]

        if E1 == 1:  # Timeout event
            Sf = Sn
        elif E2 > 0:  # Frames from upper layer event
            Sn = (Sn + E2) % ((2 ** m) - 1)
        elif E3 != 0:  # ACK from bottom layer event
            Sf = (Sf + E3) % ((2 ** m) - 1)
            Sn = (Sf + 1) % ((2 ** m) - 1)

        print(Sf, Sn)


# Test cases
test_cases = [
    (3, 1, 4, 0, 3, 0),
    (4, 1, 9, 0, 0, 62),
    (1, 3, 1, 0, 0, 0),
    (5, 1, 11, 0, 50, 0)
]
n = len(test_cases)

# Run the algorithm
go_back_n_arq(n, test_cases)
