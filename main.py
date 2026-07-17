# game-stats-analyser.py
# Activity: Gaming Leaderborad Analyser
# Lesson: Introduction to Pandas

import pandas as pd

# PART 1 - Create a Pandas Series of top player scores
print('--- PART 1: Pandas Series ---')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'])
print(players)

# PART 2 - Create a DataFrame of gaming stats
print()
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Player': ['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'],
    'level':  [42, 38, 35, 30, 27],
    'Score':  [98500, 87200, 76400, 65100, 54800],
    'Wins':   [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)

# PART 3 - Access rows using .loc
print()
print('--- PART 3: Accessing Rows ---')
print('Row 0 (top player):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])

# PART 4 - Filter data
print()
print('--- PART 4: Filtering Data ---')
# Example: Filter rows where 'Score' column is greater than 80
# Replace 'Score' with an actual column name from your dataset
high_scores = df[df['Score'] > 80]
print('Players with scores above 80:')
print(high_scores.to_string())
print()

# PART 5 - Sort and Export data
print('--- PART 5: Sorting and Exporting ---')
# Sort by 'Score' in descending order
sorted_df = df.sort_values(by='Score', ascending=False)
print('Leaderboard sorted by highest score:')
print(sorted_df.to_string())

# Export the clean, sorted data to a new CSV file without index numbers
sorted_df.to_csv('cleaned_leaderboard.csv', index=False)
print("\nSuccessfully exported to 'cleaned_leaderboard.csv'!")
