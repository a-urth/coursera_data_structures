# python3


def read_queries():
    n = int(input())
    return tuple(input().split(' ', 1) for i in range(n))


def write_responses(result):
    print('\n'.join(result))


def add_record(phone_book, phone_number, name):
    phone_book[phone_number] = name


def del_record(phone_book, phone_number):
    if phone_number in phone_book:
        del phone_book[phone_number]


def find_record(phone_book, phone_number):
    return phone_book.get(phone_number, 'not found')


def process_queries(queries):
    result, phone_book = [], {}
    for query, data in queries:
        res = globals()['{}_record'.format(query)](phone_book, *data.split())
        if res:
            result.append(res)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
