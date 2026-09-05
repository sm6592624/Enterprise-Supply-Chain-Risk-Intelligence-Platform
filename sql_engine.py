from pathlib import Path

import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "supply_chain_data.csv"

def run_sql_queries():
    conn = sqlite3.connect(':memory:')
    df = pd.read_csv(DATA_FILE)
    df.to_sql('supply_chain', conn, index=False, if_exists='replace')

    query = """
    WITH WarehouseRisk AS (
        SELECT
            warehouse,
            COUNT(shipment_id) AS total_shipments,
            SUM(CASE WHEN shipment_status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_shipments,
            AVG(lead_time_days - promised_lead_time) AS avg_delay_days,
            SUM(inventory_holding_cost) AS total_holding_cost
        FROM supply_chain
        GROUP BY warehouse
    )
    SELECT
        warehouse,
        total_shipments,
        delayed_shipments,
        ROUND((CAST(delayed_shipments AS FLOAT) / total_shipments) * 100, 2) AS delay_rate_pct,
        ROUND(avg_delay_days, 2) AS avg_delay_days,
        ROUND(total_holding_cost, 2) AS total_holding_cost,
        DENSE_RANK() OVER (ORDER BY (CAST(delayed_shipments AS FLOAT) / total_shipments) DESC) AS risk_rank
    FROM WarehouseRisk;
    """
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

if __name__ == '__main__':
    print(run_sql_queries())