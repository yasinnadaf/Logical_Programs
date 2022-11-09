import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def reverse_num(i):
    """
    This function will calculate reverse of number.
    :param i:
    :return:
    """
    try:
        rev = 0
        while i > 0:
            rev = (rev * 10) + i % 10
            i = i // 10
        print(rev)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    i = int(input("enter number: "))
    reverse_num(i)