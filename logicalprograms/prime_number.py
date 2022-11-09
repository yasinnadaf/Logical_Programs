import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def prime_check(num):
    """
    This function prints weather a number is prime or not.
    :param num:
    :return:
    """
    try:
        count = 0
        i = 1
        while i <= num:
            if num % i == 0:
                count += 1
            i = i + 1
        if count == 2:
            print("it is prime number")
        else:
            print("not a prime number")

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
        num = int(input("enter a number: "))
        prime_check(num)
