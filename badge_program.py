""""

This program will calculate if programmer has continuous
Strike for each day coding and awarded badge accordingly...

User awarded Gold Badge if he strikes Hard problems 5 consecutive day
User awarded Silver Badge if he strikes Medium problems 5 consecutive day
else User awarded Bronze Badge if he strikes Normal problems 5 consecutive day
"""

# Enter Python code here and hit the Run button.

from datetime import date, timedelta

#test-data
"""
Test data containing Problem set attributes like 
ProblemId, Problem solving date, and Problem Type
in unsorted Form 
"""

problems = [
    {'id': "1", 'prob_dt': '2024-04-03', 'type': 'Hard'},
    {'id': "2", 'prob_dt': '2024-04-04', 'type': 'Hard'},
    {'id': "3", 'prob_dt': '2024-04-06', 'type': 'Medium'},
    {'id': "4", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "5", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "6", 'prob_dt': '2024-04-10', 'type': 'Hard'},
    {'id': "7", 'prob_dt': '2024-04-11', 'type': 'Hard'},
    {'id': "8", 'prob_dt': '2024-04-11', 'type': 'Hard'},
    {'id': "9", 'prob_dt': '2024-04-11', 'type': 'Hard'},
    {'id': "10", 'prob_dt': '2024-04-13', 'type': 'Hard'},
    {'id': "11", 'prob_dt': '2024-04-15', 'type': 'Hard'},
    {'id': "12", 'prob_dt': '2024-04-15', 'type': 'Hard'},
    {'id': "13", 'prob_dt': '2024-04-16', 'type': 'Hard'},
    {'id': "14", 'prob_dt': '2024-04-17', 'type': 'Hard'},
    {'id': "15", 'prob_dt': '2024-04-18', 'type': 'Hard'},
    {'id': "16", 'prob_dt': '2024-04-19', 'type': 'Hard'},
    {'id': "17", 'prob_dt': '2024-04-20', 'type': 'Hard'},
    {'id': "18", 'prob_dt': '2024-03-31', 'type': 'Hard'},
    {'id': "19", 'prob_dt': '2024-04-01', 'type': 'Hard'},
    {'id': "20", 'prob_dt': '2024-04-02', 'type': 'Hard'}
]

# Sorting Problems List based on solving date in ascending order
problems = sorted(problems, key=lambda x: date.fromisoformat(x['prob_dt']), reverse=False)

# prev_date variable represents last date on which user solved problem
# Initializes prev_date variable to solving date of 1st problem of given problems set
prev_date = date.fromisoformat(problems[0]['prob_dt'])


# prev_type variable represents last problem type user solved
# Initializes prev_type variable to type of 1st problem of problems set
prev_type = problems[0]['type']

# Variables counting user strike each day
gold_strikes, silver_strikes, strikes = 0, 0, 0

# calculating initial or 1st day Strike based on Problem Type
if prev_type == 'Hard':
    gold_strikes = 1
elif prev_type == 'Medium':
    silver_strikes = 1
else:
    strikes = 1
