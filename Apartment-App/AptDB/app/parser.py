def get_cities(addresses):
    cities = set()
    for address in addresses:
        first_comma_index = address.find(',')
        second_comma_index = address.find(',', first_comma_index + 1)
        cities.add(address[first_comma_index+2:second_comma_index])
    return sorted(list(cities))

def filter_data(filter, apartments, amounts, contacts, images):
    apartments = [apt for apt in apartments if filter in apt[2]]
    apartment_ids = [apt[0] for apt in apartments]
    amounts = [amount for amount in amounts if amount[3] in apartment_ids]
    contacts = [contact for contact in contacts if contact[3] in apartment_ids]
    images = [image for image in images if image[2] in apartment_ids]

    return apartments, amounts, contacts, images