def get_cities(addresses):
    cities = set()
    for address in addresses:
        first_comma_index = address.find(',')
        second_comma_index = address.find(',', first_comma_index + 1)
        cities.add(address[first_comma_index+2:second_comma_index])
    return sorted(list(cities))