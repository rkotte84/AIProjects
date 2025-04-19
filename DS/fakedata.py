from faker import Faker

fake = Faker()

def create_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'date_of_birth': fake.date_of_birth(),
            'job': fake.job(),
            'company': fake.company(),
            'city': fake.city(),
            'country': fake.country()
        }
        data.append(record)
    return data;

print(create_fake_data(10))  # Example usage to create 10 records