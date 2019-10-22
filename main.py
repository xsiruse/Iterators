import hashlib
from pprint import pprint
import json
from logger import log_path


class WikiCountry:
    def __init__(self, file):
        self.url = 'https://wikipedia.org/wiki/'
        self.countries = file_read(file)

    def __iter__(self):
        return self

    def __next__(self):
        n = self.countries.__next__()
        return {'Country': n, 'link': f'{self.url}{n}'}


# def to_open(file, mode='r', encoding='utf-8'):
#     with open(file, mode, encoding=encoding) as data:
#         return data
@log_path('log.txt')
def file_read(file):
    with open(file) as countries:
        countr = json.load(countries)
        x = (country['name']['common'].replace(" ", "_") for country in countr)
        return x


@log_path('log.txt')
def result_write(src_file, dest_file):
    for wi in WikiCountry(src_file):
        with open(dest_file, 'a', encoding='utf-8') as destination:
            destination.write(f'{wi["Country"]} - [{wi["link"]}]({wi["link"]})  \n')


@log_path('log.txt')
def to_hash(dest_file):
    for line in open(dest_file):
        yield line.strip(), (hashlib.md5(str(line).encode('utf-8')).hexdigest())


@log_path('log.txt')
def main(src, dest):
    result_write(src, dest)
    pprint(list(to_hash(dest)))


if __name__ == '__main__':
    main('countries.json', 'result.md')
