
# * slowest algorithm ever written
print([2]+[number for number in range(3, int(input('amount:'))+1, 2) if not any([(number % factor == 0) for factor in range(3,round(number**0.5+1), 2)])])