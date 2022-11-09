import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def is_perfect(num):
    """
    This function is check number is perfect or not.
    param num:int
    :return:
    """
    try:
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    result = is_perfect(num)
    if result:
        print('yes its perfect number ')
    else:
        print('no its not a perfect number')