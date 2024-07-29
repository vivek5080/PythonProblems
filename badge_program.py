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

# problems = [
#     {'id': "1", 'prob_dt': '2024-04-03', 'type': 'Hard'},
#     {'id': "2", 'prob_dt': '2024-04-04', 'type': 'Hard'},
#     {'id': "3", 'prob_dt': '2024-04-06', 'type': 'Medium'},
#     {'id': "4", 'prob_dt': '2024-04-08', 'type': 'Hard'},
#     {'id': "5", 'prob_dt': '2024-04-08', 'type': 'Hard'},
#     {'id': "6", 'prob_dt': '2024-04-10', 'type': 'Hard'},
#     {'id': "7", 'prob_dt': '2024-04-11', 'type': 'Hard'},
#     {'id': "8", 'prob_dt': '2024-04-11', 'type': 'Hard'},
#     {'id': "9", 'prob_dt': '2024-04-11', 'type': 'Hard'},
#     {'id': "10", 'prob_dt': '2024-04-13', 'type': 'Hard'},
#     {'id': "11", 'prob_dt': '2024-04-15', 'type': 'Hard'},
#     {'id': "12", 'prob_dt': '2024-04-15', 'type': 'Hard'},
#     {'id': "13", 'prob_dt': '2024-04-16', 'type': 'Hard'},
#     {'id': "14", 'prob_dt': '2024-04-17', 'type': 'Hard'},
#     {'id': "15", 'prob_dt': '2024-04-18', 'type': 'Hard'},
#     {'id': "16", 'prob_dt': '2024-04-19', 'type': 'Hard'},
#     {'id': "17", 'prob_dt': '2024-04-20', 'type': 'Hard'},
#     {'id': "18", 'prob_dt': '2024-03-31', 'type': 'Hard'},
#     {'id': "19", 'prob_dt': '2024-04-01', 'type': 'Hard'},
#     {'id': "20", 'prob_dt': '2024-04-02', 'type': 'Hard'}
# ]

problems = [
    {'id': "1", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "2", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "3", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "4", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "5", 'prob_dt': '2024-04-08', 'type': 'Hard'},
    {'id': "6", 'prob_dt': '2024-04-09', 'type': 'Hard'},
    {'id': "7", 'prob_dt': '2024-04-09', 'type': 'Hard'},
    {'id': "8", 'prob_dt': '2024-04-09', 'type': 'Hard'},
    {'id': "9", 'prob_dt': '2024-04-09', 'type': 'Hard'},
    {'id': "10", 'prob_dt': '2024-04-09', 'type': 'Medium'},
    {'id': "11", 'prob_dt': '2024-04-09', 'type': 'Medium'},
    {'id': "12", 'prob_dt': '2024-04-09', 'type': 'Medium'},
    {'id': "13", 'prob_dt': '2024-04-10', 'type': 'Medium'},
    {'id': "14", 'prob_dt': '2024-04-11', 'type': 'Hard'},
    {'id': "15", 'prob_dt': '2024-04-12', 'type': 'Hard'},
    {'id': "16", 'prob_dt': '2024-04-12', 'type': 'Hard'},
    {'id': "17", 'prob_dt': '2024-04-12', 'type': 'Medium'},
    {'id': "18", 'prob_dt': '2024-04-12', 'type': 'Medium'},
    {'id': "19", 'prob_dt': '2024-04-12', 'type': 'Medium'},
    {'id': "20", 'prob_dt': '2024-04-12', 'type': 'Hard'}
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

# Variables/flag keeping track what kind of problem is solved on given day
is_hard_processed, is_medium_processed, is_processed = False, False, False

# calculating initial or 1st day Strike based on Problem Type
if prev_type == 'Hard' and not is_hard_processed:
    gold_strikes = 1
    is_hard_processed = True
elif prev_type == 'Medium' and not is_medium_processed:
    silver_strikes = 1
    is_medium_processed = True
else:
    strikes = 1
    is_processed = True
print(f"Under Given Date : Current Date : {prev_date},Gold Strikes : {gold_strikes}, Silver Strike : {silver_strikes}")


"""
Logic without taking into account the Problem Type 
Logic Just based on consecutive day stikes or not   
"""
# for problem in problems[1:]:
#     current_dt = date.fromisoformat(problem['prob_dt'])
#     current_type = problem['type']
#     #print(current_dt, prev_date)
#     if current_dt == prev_date + timedelta(days=1):
#         strikes += 1
#         print(f"Current Date : {current_dt},Strikes : {strikes}")
#         if strikes == 5:
#             print('Badge')
#             strikes = 0
#     elif current_dt == prev_date:
#         print(f"Current Date : {current_dt},Strikes : {strikes}")
#         #pass
#     else:
#         strikes = 1
#         print(f"Current Date : {current_dt},Strikes : {strikes}")
#
#     prev_date = current_dt
#     prev_type = current_type

# for problem in problems[1:]:
#     current_dt = date.fromisoformat(problem['prob_dt'])
#     current_type = problem['type']
#     #print(current_dt, prev_date)
#     if current_dt == prev_date + timedelta(days=1):
#         if current_type == prev_type:
#             if current_type == 'Hard':
#                 gold_strikes += 1
#             elif current_type == 'Medium':
#                 silver_strikes += 1
#             else:
#                 strikes += 1
#         else:
#             if current_type == 'Hard':
#                 gold_strikes = 1
#             elif current_type == 'Medium':
#                 silver_strikes = 1
#             else:
#                 strikes = 1
#     elif current_dt == prev_date:
#         if current_type == 'Hard' and prev_type == 'Medium':
#             gold_strikes += 1
#         elif current_type == 'Medium' and prev_type == 'Hard':
#             silver_strikes += 1
#         else:
#             pass
#     else:
#         if current_type == 'Hard':
#             gold_strikes = 1
#             silver_strikes = 0
#             strikes = 0
#         elif current_type == 'Medium':
#             silver_strikes = 1
#             gold_strikes = 0
#             strikes = 0
#         else:
#             gold_strikes = 0
#             silver_strikes = 0
#             strikes = 0
#     print(f"Current Date : {current_dt},Strikes : {strikes},Silver Strikes : {silver_strikes},Gold Strikes : {gold_strikes}")
#
#     if gold_strikes == 5:
#         print('Gold Badge')
#         gold_strikes = 0
#     elif silver_strikes == 5:
#         print('Silver Badge')
#     else:
#         if strikes ==5:
#             print("Badge")
#             strikes = 0
#
#
#     prev_date = current_dt
#     prev_type = current_type

"""
Login to count Gold strikes, Silver Strike or Normal Strike
Staring from 2nd Problem in Problem set, considering it current day problem
"""
for problem in problems[1:]:
    current_dt = date.fromisoformat(problem['prob_dt'])
    current_type = problem['type']
    print(f"-" * 100)
    print(f"Current Date : {current_dt}, Current Type : {current_type}")
    print(f"-" * 100)
    if current_dt == prev_date + timedelta(days=1):

        is_hard_processed = False
        is_medium_processed = False
        is_processed = False

        if current_type == 'Hard' and not is_hard_processed:
            is_hard_processed = True
            gold_strikes += 1

        if current_type == 'Medium' and not is_medium_processed:
            is_medium_processed = True
            silver_strikes += 1
        else:
            if not is_processed:
                is_processed = True
                strikes += 1

        print(
            f"Under Subsequent Date : Current Date : {current_dt},Gold Strikes : {gold_strikes}, Silver Strike : {silver_strikes}")

    elif current_dt == prev_date:

        if not is_hard_processed and current_type == 'Hard':
            is_hard_processed = True
            gold_strikes += 1
        elif not is_medium_processed and current_type == 'Medium':
            is_medium_processed = True
            silver_strikes += 1
        else:
            if not is_processed:
                is_processed = True
                strikes += 1
        print(
            f"Under Same Date : Current Date : {current_dt},Gold Strikes : {gold_strikes}, Silver Strike : {silver_strikes}")

    else:

        if current_type == 'Hard':

            gold_strikes = 1
            silver_strikes = 0
            strikes = 0
            is_hard_processed = True
            is_medium_processed = False
            is_processed = False

        elif current_type == 'Medium':
            print(f"Current type : {current_type}")
            gold_strikes = 0
            silver_strikes = 1
            strikes = 0
            is_medium_processed = True
            is_hard_processed = False
            is_processed = False
        else:
            strikes = 1
            gold_strikes = 0
            silver_strikes = 0
            is_processed = True
            is_hard_processed = False
            is_medium_processed = False
        print(
            f"Under Different Date : Current Date : {current_dt},Gold Strikes : {gold_strikes}, Silver Strike : {silver_strikes}")

    print(f"*" * 100)
    print(f"Out of Loop : Current Date : {current_dt},Gold Strikes : {gold_strikes}, Silver Strike : {silver_strikes}")
    print(f"*" * 100)

    if gold_strikes == 5:
        print('Gold Badge')
        gold_strikes = 0
        is_hard_processed = False

    if silver_strikes == 5:
        print('Silver Badge')
        silver_strikes = 0
        is_medium_processed = False
    if strikes == 5:
        print('Bronze Badge')
        strikes = 0
        is_processed = False

    prev_date = current_dt
    prev_type = current_type
