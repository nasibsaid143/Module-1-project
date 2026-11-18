# Memo: Southeast Revenue Drop

**To:** Sven Anderson, CFO, NorthwoodFresh
**Re:** Is the Southeast revenue decline real?

## Executive Summary

Southeast monthly revenue fell about 23% starting in July, from an average of $472K to $364K per month. The 95% confidence interval puts the true drop between 18% and 28%, and the chance this is random month-to-month noise is effectively nil. I recommend NorthwoodFresh open a root-cause investigation into the Southeast now, rather than wait for more months of data to confirm the drop.

## Findings

- **Effect size:** Southeast averaged $472,111 per month in months 1-6 and $363,776 in months 7-12, a difference of $108,335, or 22.9% lower.
- **Confidence interval:** The 95% CI for the difference is $84,553 to $132,117 per month (roughly 18% to 28% of the earlier average). It does not include zero.
- **Significance:** A two-sample t-test gives t = 8.93 and p = 0.0000045. Reported alone, that p-value would only say the two periods differ; the effect size and interval say by how much and how precisely.
- **Other regions:** Midwest, Northeast, and West show no comparable shift. Their monthly revenue varies by roughly 4% to 5% around a stable level, which is normal noise.
- **Distribution:** Southeast monthly revenue forms two distinct clusters, one near $480K and one near $370K, which is the signature of a step change rather than gradual drift.

**Important caveat:** This analysis was prototyped on synthetic data, not on real NorthwoodFresh data. The numbers demonstrate the method and what a result would look like. They are not a statement about actual company performance.

## Recommendation

Once real monthly revenue by region is available, rerun this same analysis on it. If the drop holds up, investigate causes in the Southeast starting in the month it began: pricing changes, lost accounts or stores, supply or delivery problems, and competitor activity.

The limitations are real. The data is synthetic, and this test shows that the level shifted but says nothing about why. No causal investigation has been done yet, so I would not attribute the drop to any specific cause or commit to a fix until that work is complete.

## AI Use Note

I used Claude for this project. I gave it the assignment spec and it wrote the data generation script, the analysis notebook, and the first drafts of this memo and the README. The first version used incorrect baselines for Midwest ($450,000) and West ($560,000); after review I corrected them to the required $510,000 and $590,000, regenerated the data, and reran the notebook. Claude ran the script and notebook and checked that the Southeast means landed near 480,000 and 370,000, that the confidence interval excluded zero, and that the p-value was tiny. I verified all the data and different claims for the region and made sure everything was worded correctly in a professional manner. I had to change certain values on the notebook and made sure the script was correct
