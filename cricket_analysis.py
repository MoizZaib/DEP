import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
num_matches = 50
players = [f'Player {i+1}' for i in range(15)]
data = {
    'Match_ID': np.arange(1, num_matches + 1),
    'Player': np.random.choice(players, size=num_matches),
    'Runs': np.random.randint(0, 100, size=num_matches),
    'Wickets': np.random.randint(0, 5, size=num_matches)
}

match_data = pd.DataFrame(data)

performance = match_data.groupby('Player').agg({'Runs': 'sum', 'Wickets': 'sum'}).reset_index()
performance = performance.sort_values(by='Runs', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(performance['Player'], performance['Runs'], color='blue', label='Runs')
plt.xlabel('Players')
plt.ylabel('Total Runs')
plt.title('Total Runs Scored by Players')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(performance['Runs']):
    plt.text(index, value + 1, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.legend()
plt.show()
