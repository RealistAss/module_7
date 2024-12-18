def is_prime(func):
    def wrapper(*nums):
        result = func(*nums)
        if result < 2:
            print('sostavnoe')
            return
        for div in range(2, result):
            if result % div == 0:
                print('sostavnoe')
                break
        else:
            print('prostoe')

        print(result)


    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 5)



