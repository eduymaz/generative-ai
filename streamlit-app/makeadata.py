import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Parameters
data_size = 50
names_female = ["Ayşe Demir", "Elif Şahin", "Canan Aydın", "Deniz Korkmaz", "Selin Aksoy", "Melis Kurt", "İrem Uçar", "Tuğba Yalçın", "Esra Koç", "Simge Yıldırım", "Aslı Karaca", "Nilay Er", "Betül Acar", "Hande Gül", "Selda Yılmaz", "Ayça Güneş", "Deniz Korkut", "Melike Kurt", "Tuğçe Yalçın", "Sevgi Polat"]
names_male = ["Ali Yılmaz", "Mehmet Kaya", "Ahmet Güneş", "Emre Yıldız", "Barış Öz", "Onur Polat", "Serkan Ekin", "Kerem Arslan", "Levent Duran", "Volkan Çetin", "Ömer Akın", "Harun Yavuz", "Alper Şen", "Erkan Kılıç", "Faruk Demir", "İlker Aydın", "Emrah Yıldız", "Baran Öz", "Serhat Ekin"]
categories = ["Electronics", "Fashion", "Home", "Books", "Sports", "Beauty"]
genders = ["Female", "Male"]

# Helper Functions
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

data = []
for i in range(1, data_size + 1):
    gender = random.choice(genders)
    if gender == "Female":
        name = random.choice(names_female)
    else:
        name = random.choice(names_male)
    age = random.randint(22, 46)
    total_spent = random.randint(800, 4200)
    num_transactions = random.randint(6, 32)
    last_purchase_date = random_date(datetime(2025, 3, 20), datetime(2025, 5, 22)).strftime("%Y-%m-%d")
    preferred_category = random.choice(categories)
    data.append({
        "customer_id": i,
        "name": name,
        "age": age,
        "gender": gender,
        "total_spent": total_spent,
        "num_transactions": num_transactions,
        "last_purchase_date": last_purchase_date,
        "preferred_category": preferred_category
    })

df = pd.DataFrame(data)
df.to_csv("customers2.csv", index=False)
print("customers.csv is made.")
