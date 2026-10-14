import requests


def get_drivers():
    sessions = requests.get(
        "https://api.openf1.org/v1/sessions",
        params={"year": 2026}
    ).json()

    races = [
        s for s in sessions
        if s["session_name"] == "Race"
    ]

    race_session_key = races[0]["session_key"]

    drivers = requests.get(
        "https://api.openf1.org/v1/drivers",
        params={"session_key": race_session_key}
    ).json()

    return drivers


