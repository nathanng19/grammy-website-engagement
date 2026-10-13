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

## Original coursework findings
| Metric | Combined site | Grammy | Recording Academy |
|---|---:|---:|---:|
| Bounce rate | 41.58% | 40.16% | 33.67% |
| Mean daily session duration (seconds) | 102.85 | 82.99 | 128.50 |

These metrics were verified against the locally downloaded course CSVs. Bounce rate divides total bounced sessions by total sessions. Duration averages daily reported values without session weighting. Pages per session counts pageviews, not unique pages.

## Run locally
The notebook now runs with included **synthetic demonstration data**. No course-server access or CSV download is needed. Synthetic values are invented and do not reproduce the coursework findings above.

Use Python 3.10 or later. From this folder:
~~~sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
~~~
On Windows Command Prompt, activate with .venv\Scripts\activate.bat; in PowerShell, use .\.venv\Scripts\Activate.ps1.
Open analysis.ipynb from the repository root and run all cells. The first cell prints which dataset is being used. To rerun the original coursework analysis instead, add all four CSVs described in datasets/README.md. A partial set produces a clear error rather than mixing real and demo data.

To regenerate the synthetic CSVs, run python generate_demo_data.py. The generator uses only the Python standard library and a fixed random seed.

## Limitations and provenance
This is an observational comparison with differing time windows and event-driven traffic. Audience shifts and other factors may explain differences; the analysis does not establish a causal effect of the split. Review missing values and zero-session rows when adapting the analysis.

The notebook was curated from my submitted coursework; assignment prompts and unfinished optional exercises were removed. Original course datasets and teaching materials are not redistributed. The included demo data is newly generated and entirely synthetic. This project does not imply employment with or endorsement by the Recording Academy.

Author: [nathanng19](https://github.com/nathanng19)
