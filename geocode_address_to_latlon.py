# Mari Muraki <marimuraki@gmail.com>
# Geocode addresses to latitude/longitude, 
# using [address, city, state, zip] in CSV file

from csv import DictReader
from sys import argv


def readcsv(input_file):
    address_file = open(input_file, 'r')
    reader = DictReader(address_file)
    return reader


if __name__ == '__main__':
    result = readcsv(argv[1])
