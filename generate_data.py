import pandas as pd
import numpy as np
import os

def generate_supply_chain_data():
    np.random.seed(42)
    n = 1000
    warehouses = ['WH-Delhi', 'WH-Bengaluru', 'WH-Mumbai', 'WH-Hyderabad']
    suppliers = ['Supp-A', 'Supp-B', 'Supp-C', 'Supp-D']
    product_categories = ['Electronics', 'Industrial Parts', 'Automotive', 'Consumer Goods']

    data = {
        'shipment_id': [f"SHP-{1000+i}" for i in range(n)],
        'warehouse': np.random.choice(warehouses, n),
        'supplier': np.random.choice(suppliers, n),
        'category': np.random.choice(product_categories, n),
        'lead_time_days': np.random.randint(2, 25, n),
        'promised_lead_time': np.random.randint(5, 15, n),
        'inventory_holding_cost': np.random.uniform(500, 10000, n).round(2),
        'unit_order_quantity': np.random.randint(10, 500, n),
        'stockout_flag': np.random.choice([0, 1], n, p=[0.85, 0.15]),
        'shipment_status': np.random.choice(['Delivered', 'Delayed', 'Cancelled'], n, p=[0.75, 0.20, 0.05])
    }
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/supply_chain_data.csv', index=False)
    print("Dataset generated at data/supply_chain_data.csv")

if __name__ == '__main__':
    generate_supply_chain_data()