import pandas as pd
sessions = pd.read_json(
    "https://api.openf1.org/v1/sessions?year=2026&country_name=Monaco&session_name=Race"
)
session_key = sessions.iloc[0]["session_key"]
drivers = pd.read_json(
    f"https://api.openf1.org/v1/drivers?session_key={session_key}"
)
driver_names = drivers["full_name"].tolist()
print(drivers[["full_name", "team_name", "headshot_url"]])
