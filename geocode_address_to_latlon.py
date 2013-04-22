# Mari Muraki <marimuraki@gmail.com>
# Geocode addresses to latitude/longitude, 
# using [address, city, state, zip] in CSV file

from csv import DictReader
from geopy import geocoders    
from sys import argv


def read_csv(input_file):
    address_file = open(input_file, 'r')
    reader = DictReader(address_file)
    return reader

def generate_addresses(reader):
    address_list = []
    addresses = (line for line in reader)
    for address in addresses:
        fulladdress = "{address}, {city}, {state}, {zip}".format(**address)
        address_list.append(fulladdress)
    return address_list
        
def geocode_addresses(address_list):
    geocoded_list = []
    g = geocoders.GoogleV3()
    for fulladdress in address_list:
        address, (lat, lon) = g.geocode(fulladdress)
        geocoded = "%s: %.5f, %.5f" % (address, lat, lon)
        geocoded_list.append(geocoded)
    return geocoded_list
        
if __name__ == '__main__':
    readfile = read_csv(argv[1])
    fulladdress = generate_addresses(readfile)
    geocode = geocode_addresses(fulladdress)

