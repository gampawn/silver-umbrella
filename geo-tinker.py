#!/usr/bin/env python

import pycountry, argparse

parser = argparse.ArgumentParser(
                    prog='geo-tinker.py',
                    description='a tool to tinker with pycountry',
                    epilog='try not to get hurt')

parser.add_argument('filename')
args = parser.parse_args()

geo_locations = ["AT", "AU", "BE", "BG", "BR", "CA", "CH", "CR", "DE", "DK", "ES", "FI", "FR",
                "GB", "IE", "IN", "IT", "JP", "KR", "MY", "NL", "NO", "PH", "SE", "SG", "US"
]

with open(args.filename, "r") as file:
    lines = file.readlines()

new_geo_locations = []
for line in lines:
    name = line[:-1]
    country = pycountry.countries.get(name=name)
    if country is None:
        country = pycountry.countries.get(official_name=name)
    try:
        new_geo_locations += [country.alpha_2]
    except AttributeError:
        print(f'{name} ain\'t a real country, hoss')



print(new_geo_locations)
changes = set(new_geo_locations) - set(geo_locations)
print(changes)
