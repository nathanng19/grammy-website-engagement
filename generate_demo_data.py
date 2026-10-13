from pathlib import Path
import csv
from datetime import date, timedelta
from random import Random

def generate(output):
    output.mkdir(parents=True, exist_ok=True)
    rng = Random(19)
    fields = ["date", "visitors", "pageviews", "sessions", "bounced_sessions",
              "avg_session_duration_secs", "awards_week", "awards_night"]
    def rows(start, end, academy=False):
        current = start
        while current <= end:
            split = current >= date(2022, 2, 1)
            # A deliberately constructed, illustrative event on February 6.
            event = current.month == 2 and current.day == 6
            week = current.month == 2 and current.day <= 12
            visitors = rng.randint(900, 1500) if academy else rng.randint(18000, 35000)
            if event:
                visitors *= 8
            sessions = round(visitors * rng.uniform(1.05, 1.2))
            pages_per_session = rng.uniform(2.6, 3.5) if academy else rng.uniform(1.5, 2.2)
            bounce = rng.uniform(.28, .38) if academy else rng.uniform(.37, .46)
            duration = rng.randint(115, 145) if academy else rng.randint(75, 110)
            yield [current.isoformat(), visitors, round(sessions * pages_per_session),
                   sessions, round(sessions * bounce), duration, int(week), int(event)]
            current += timedelta(days=1)
    def save(name, header, records):
        with (output / name).open("w", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(header)
            writer.writerows(records)
    save("grammy_live_web_analytics.csv", fields, rows(date(2021, 1, 1), date(2023, 3, 31)))
    save("ra_live_web_analytics.csv", fields, rows(date(2022, 2, 1), date(2023, 3, 31), True))
    ages = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    save("grammys_age_demographics.csv", ["age_group", "pct_visitors"],
         zip(ages, [27, 24, 19, 14, 10, 6]))
    save("tra_age_demographics.csv", ["age_group", "pct_visitors"],
         zip(ages, [24, 26, 21, 15, 9, 5]))

if __name__ == "__main__":
    generate(Path(__file__).resolve().parent / "demo_data")
    print("Synthetic demo regenerated; no real website data used.")
