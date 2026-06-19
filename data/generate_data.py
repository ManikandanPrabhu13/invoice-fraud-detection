import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()
np.random.seed(42)

records = []

for i in range(2000):

    is_fraud = random.random() < 0.08

    if is_fraud:
        amount = round(
            random.choice([
                random.uniform(9990, 10010),
                random.uniform(1, 50),
                random.uniform(50000, 100000)
            ]),
            2
        )

        days_to_pay = random.randint(0, 1)
        duplicate = random.random() < 0.4

    else:
        amount = round(random.uniform(500, 20000), 2)
        days_to_pay = random.randint(15, 60)
        duplicate = False

    records.append({
        "invoice_id": f"INV{1000+i}",
        "supplier_id": f"SUP{random.randint(1,50)}",
        "amount": amount,
        "days_to_pay": days_to_pay,
        "num_items": random.randint(1,20),
        "weekend_submission": int(
            fake.date_this_year().weekday() >= 5
        ),
        "is_duplicate": int(duplicate),
        "is_fraud": int(is_fraud)
    })

df = pd.DataFrame(records)

df.to_csv("data/invoices.csv", index=False)

print(
    f"Dataset created: {len(df)} rows, "
    f"{df['is_fraud'].sum()} fraud cases"
)