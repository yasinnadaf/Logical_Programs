import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def fibonacci_series(num):
    """
    This function calculated fibonacci series
    :param num:
    :return:
    """
    try:
        a = 0
        b = 1
        c = 0
        while c <= num:
            print(c)
            a = b
            b = c
            c = a + b
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    num = int(input("enter a number: "))
    fibonacci_series(num)