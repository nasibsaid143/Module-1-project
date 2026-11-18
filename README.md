# Module 1 Project: NorthwoodFresh Southeast Revenue

## What is this?

An analysis for NorthwoodFresh's CFO, Sven Anderson, asking whether the apparent drop in Southeast regional revenue is a real shift or ordinary month-to-month noise, and how large it is. It is prototyped on synthetic data.

## What's in the folder

- `generate_northwoodfresh_data.py`: generates 48 rows of synthetic monthly revenue (4 regions x 12 months) with a step-down in the Southeast at month 7, and writes the CSV.
- `northwoodfresh_sales.csv`: the generated data (`region`, `month`, `revenue`).
- `northwoodfresh_analysis.ipynb`: the analysis notebook: load and inspect, summary statistics by region, distribution charts, and the Southeast before/after comparison.
- `sven_anderson_memo.md`: a one-page memo for the CFO with the findings and a recommendation.

## How to reproduce the analysis

```bash
conda activate northstar
python generate_northwoodfresh_data.py
jupyter notebook northwoodfresh_analysis.ipynb   # then Run All, top to bottom
```

## The headline finding

Southeast monthly revenue averaged $108,335 lower in months 7-12 than in months 1-6, a 22.9% drop (95% CI for the difference: $84,553 to $132,117, or roughly 18% to 28%; t-test p < 0.0001). The interval excludes zero, so the drop is very unlikely to be noise. The data is synthetic, so this demonstrates the method and is not a finding about real NorthwoodFresh revenue.
