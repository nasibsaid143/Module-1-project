"""Generate synthetic monthly revenue data for NorthwoodFresh.

Four regions, 12 months each (48 rows). Southeast steps down from a
480,000 baseline (months 1-6) to a 370,000 baseline (months 7-12).
Every other region holds a single baseline all year.

Baselines: Northeast 520,000, Midwest 510,000, West 590,000.
"""

import numpy as np
import pandas as pd

# Reproducible seed
np.random.seed(42)

# Baseline monthly revenue by region.
# Southeast holds two values: (months 1-6, months 7-12).
BASELINES = {
    "Northeast": 520000,
    "Midwest": 510000,
    "West": 590000,
    "Southeast": {"before": 480000, "after": 370000},
}

NOISE_PCT = 0.05  # std dev = 5% of the baseline
N_MONTHS = 12
STEP_MONTH = 7    # Southeast drops starting in month 7

rows = []
for region, baseline in BASELINES.items():
    for month in range(1, N_MONTHS + 1):
        if region == "Southeast":
            base = baseline["before"] if month < STEP_MONTH else baseline["after"]
        else:
            base = baseline
        # Draw inside the loop so every month gets its own random value
        revenue = np.random.normal(loc=base, scale=NOISE_PCT * base)
        rows.append({"region": region, "month": month, "revenue": round(revenue, 2)})

df = pd.DataFrame(rows, columns=["region", "month", "revenue"])
df["revenue"] = df["revenue"].round(2)

df.to_csv("northwoodfresh_sales.csv", index=False)

# Verification block
se = df[df["region"] == "Southeast"]
print("=" * 50)
print("VERIFICATION")
print("=" * 50)
print(f"Total rows: {len(df)}")
print("\nMean revenue per region:")
print(df.groupby("region")["revenue"].mean().round(2).to_string())
print(f"\nSoutheast mean, months 1-6:  {se[se['month'] <= 6]['revenue'].mean():,.2f}")
print(f"Southeast mean, months 7-12: {se[se['month'] >= 7]['revenue'].mean():,.2f}")
print("=" * 50)
