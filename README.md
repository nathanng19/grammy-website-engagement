# Grammy Website Engagement Analysis
**Nathan Nguyen** | Python, pandas, Plotly, Jupyter Notebook

A Global Career Accelerator coursework portfolio analysis of Grammy and Recording Academy website engagement around the February 2022 domain split.

## Business question
How do website engagement and audience demographics differ before and after the split, and what do those patterns suggest for content strategy?

## Methods
- Segment observations before and after February 1, 2022.
- Compute pages per session and a reusable, session-weighted bounce-rate function.
- Visualize visitor traffic, engagement trends, and age demographics.
- Recommend maintaining separate sites with audience-specific content.

## Findings
| Metric | Combined site | Grammy | Recording Academy |
|---|---:|---:|---:|
| Bounce rate | 41.58% | 40.16% | 33.67% |
| Mean daily session duration (seconds) | 102.85 | 82.99 | 128.50 |

These metrics were verified against the locally downloaded course CSVs. Bounce rate divides total bounced sessions by total sessions. Duration averages daily reported values without session weighting. Pages per session counts pageviews, not unique pages.

## Run locally
Use Python 3.10 or later. From this folder:
~~~sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
~~~
On Windows, activate with .venv/Scripts/activate.
Add the four CSVs described in datasets/README.md, then open analysis.ipynb and run all cells.

## Limitations and provenance
This is an observational comparison with differing time windows and event-driven traffic. Audience shifts and other factors may explain differences; the analysis does not establish a causal effect of the split. Review missing values and zero-session rows when adapting the analysis.

The notebook was curated from my submitted coursework; assignment prompts and unfinished optional exercises were removed. Course datasets and teaching materials are not redistributed. This project does not imply employment with or endorsement by the Recording Academy.

Author: [nathanng19](https://github.com/nathanng19)
