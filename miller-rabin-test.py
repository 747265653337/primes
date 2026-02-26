import random

def miller_rabin_test(self, num_to_check, amnt_of_checks=40):

    # remove the 2 base cases, which interfere with the algorithm
    if num_to_check == 2 or num_to_check == 3:
        return True

    # remove obvious cases
    if num_to_check % 2 == 0:
        return False

    # ha I can now asign multiple variables on one line
    r, d = 0, num_to_check - 1

    # get r and d for: num_to_check = 2^r * d + 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(amnt_of_checks):
        a = random.randint(2, num_to_check - 2)
        x = pow(a, d, num_to_check)
        # if num_to_check is a prime it passes for nearly all bases
        if x == 1 or x == num_to_check - 1:
            continue
        # if it didn't it should pass this test
        for _ in range(r - 1):
            x = pow(x, 2, num_to_check)
            if x == num_to_check - 1:
                break
        else:
            return False
    return True
