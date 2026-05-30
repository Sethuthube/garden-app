"""
Garden Advice App

This program gives basic gardening advice based on the selected month
and season. It is designed as a simple beginner-friendly app for
gardening enthusiasts.
"""

MONTHS = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]

SEASONS = ["spring", "summer", "autumn", "winter"]


def get_month_advice(month):
    """Return gardening advice based on the month."""
    month = month.lower()

    if month in ["december", "january", "february"]:
        return "Water plants regularly and protect them from extreme heat."
    if month in ["march", "april", "may"]:
        return "Prepare soil, remove weeds, and plant cool-season crops."
    if month in ["june", "july", "august"]:
        return "Protect sensitive plants from frost and reduce watering."
    if month in ["september", "october", "november"]:
        return "Plant new flowers, vegetables, and refresh garden beds."

    return "Invalid month entered. Please enter a valid month."


def get_season_advice(season):
    """Return gardening advice based on the season."""
    season = season.lower()

    if season == "spring":
        return "Spring is ideal for planting, pruning, and preparing garden beds."
    if season == "summer":
        return "Summer requires regular watering and pest monitoring."
    if season == "autumn":
        return "Autumn is good for composting, clearing leaves, and soil preparation."
    if season == "winter":
        return "Winter is best for protecting plants and planning the next season."

    return "Invalid season entered. Please enter spring, summer, autumn, or winter."


def main():
    """Run the garden advice program."""
    print("Welcome to the Garden Advice App")

    month = input("Enter the current month: ")
    season = input("Enter the current season: ")

    print("\nMonth advice:")
    print(get_month_advice(month))

    print("\nSeason advice:")
    print(get_season_advice(season))


if __name__ == "__main__":
    main()