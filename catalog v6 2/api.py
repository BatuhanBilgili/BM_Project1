import requests
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Fetch data
url = 'https://api.football-data.org/v4/competitions/TSL/matches?season=2023'
headers = {
    'X-Auth-Token': '34540994335448c7bbfd0fa4111af14f',
    'X-Unfold-Lineups': 'true',
    'X-Unfold-Bookings': 'true',
    'X-Unfold-Subs': 'true',
    'X-Unfold-Goals': 'true'
}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")
    exit()

data = response.json()
matches = data.get('matches', [])

# Process data
data = []
for match in matches:
    matchday = match["matchday"]
    home_team = match["homeTeam"]["name"]
    away_team = match["awayTeam"]["name"]
    home_goals = match["score"]["fullTime"]["home"]
    away_goals = match["score"]["fullTime"]["away"]
    
    home_bookings = len([b for b in match.get("bookings", []) if b["team"]["name"] == home_team])
    away_bookings = len([b for b in match.get("bookings", []) if b["team"]["name"] == away_team])
    
    data.append({
        "matchday": matchday,
        "home_team": home_team,
        "away_team": away_team,
        "home_goals": home_goals,
        "away_goals": away_goals,
        "home_bookings": home_bookings,
        "away_bookings": away_bookings
    })

df = pd.DataFrame(data)

# Create labels (0 if home team wins, 1 if away team wins, 2 if draw)
df['result'] = df.apply(lambda row: 0 if row['home_goals'] > row['away_goals'] else (2 if row['home_goals'] == row['away_goals'] else 1), axis=1)

# Use the first 10 matchdays for training
train_df = df[df['matchday'] <= 10]
test_df = df[df['matchday'] > 10]

# Select features and target
X_train = train_df[["home_bookings", "away_bookings"]]
y_train = train_df["result"]

X_test = test_df[["home_bookings", "away_bookings"]]
y_test = test_df["result"]

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Add predictions to the test DataFrame for review
test_df = test_df.copy()
test_df["predicted_result"] = y_pred

# Save the data to a JSON file
with open('matches_data.json', 'w') as f:
    json.dump(test_df.to_dict(orient='records'), f, indent=4)

print("Data saved to matches_data.json")