# Mari Muraki <marimuraki@gmail.com>
# Geocode addresses to latitude/longitude, 
# using [address, city, state, zip] in CSV file

from csv import DictReader, DictWriter
from geopy import geocoders    
from sys import argv


def read_csv(input_file):
    address_file = open(input_file, 'r')
    reader = DictReader(address_file)
    return list(reader)

def generate_addresses(address_dicts):
    for address_dict in address_dicts:
        fulladdress = "{address}, {city}, {state}, {zip}" \
            .format(**address_dict)
        address_dict["fulladdress"] = fulladdress
    return address_dicts
        
def geocode_addresses(address_dicts):
    g = geocoders.GoogleV3()
    for address_dict in address_dicts:
        address, (lat, lon) = g.geocode(address_dict["fulladdress"])
        address_dict["latitude"] = lat
        address_dict["longitude"] = lon
    return address_dicts
    
def write_csv(output_file, address_dicts):
    geocoded_file = open(output_file, 'wb')
    writer = DictWriter(geocoded_file, fieldnames=address_dicts[0].keys(), \
        dialect='excel', lineterminator='\n')
    writer.writeheader()
    writer.writerows(address_dicts)
    geocoded_file.close() 


if __name__ == '__main__':
    addressdicts = read_csv(argv[1])
    output_file = argv[2]
    fulladdresses = generate_addresses(addressdicts)
    geocoded = geocode_addresses(fulladdresses)
    write_csv(output_file, geocoded)

