import json
from datetime import datetime
from bs4 import BeautifulSoup
import requests

USERNAME = "ncyj823"
URL = f"https://github.com/users/{USERNAME}/contributions"

def fetch():
    print(f"Fetching contribution data for {USERNAME}...")
    res = requests.get(URL)
    if res.status_code != 200:
        raise Exception(f"Failed to fetch: status {res.status_code}")

    soup = BeautifulSoup(res.text, "html.parser")
    days = []

    for rect in soup.find_all("td", class_="ContributionCalendar-day"):
        date = rect.get("data-date")
        count = int(rect.get("data-count", 0))
        level = int(rect.get("data-level", 0))
        if date:
            days.append({"date": date, "count": count, "level": level})

    total_contribs = sum(d["count"] for d in days)

    data = {
        "updated_at": datetime.utcnow().isoformat(),
        "total_contributions": total_contribs,
        "days": days
    }

    with open("data/contributions.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(days)} days ({total_contribs} total contributions).")

if __name__ == "__main__":
    fetch()
