# Mari Muraki <marimuraki@gmail.com>
# Geocode addresses to latitude/longitude, 
# using [address, city, state, zip] in CSV file

from csv import DictReader
from sys import argv


def read_csv(input_file):
    address_file = open(input_file, 'r')
    reader = DictReader(address_file)
    return reader

def generate_addresses(reader):
    addresses = (line for line in reader)
    for address in addresses:
        fulladdress = "{address}, {city}, {state}, {zip}".format(**address)
        return fulladdress
    
    
if __name__ == '__main__':
    readfile = read_csv(argv[1])
    fulladdress = generate_addresses(readfile)

