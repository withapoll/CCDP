import pandas as pd
from sqlalchemy import create_engine
from faker import Faker

#need url for postgres
DATABASE_URL = "postgresql://username:password@localhost:5432/doubleb_db" 
engine = create_engine(DATABASE_URL)
fake = Faker()

customers_data = []
for _ in range(1000):
    customers_data.append({
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'registration_date': fake.date_this_year()
    })

df = pd.DataFrame(customers_data)
df.to_sql('customers', con=engine, if_exists='append', index=False)