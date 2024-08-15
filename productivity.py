'''

RBI - How to automate trading

Research 
 # Google Scholar - Trading strategies 
 # Discord - Quant_strategies

Backtest
 # To see if they work in the past
 # 95% of strategies  fail 
 # 5% of strategies work!

Implement
 # With small size to a bot

 4 Hours - Algo Trading Bootcamp
 1 Hour - Muay Thai
 0.5 Hours Gym
 0.25 Hours Sauna

 # Prompt to learn more about any code

 # Please explain the concepts in this code with 3 analogies and 3 coding examples. 
 # I'm learning how to code and need to understand these concepts perfectly

'''
import json
import time
from datetime import datetime, timedelta
from termcolor import cprint
import random

def load_tasks():
    with open('/Users/arman/Desktop/Moon_Dev/Productivity_App/tasks.json', 'r') as f:
        tasks = json.load(f)
    return tasks 

def get_tasks_schedule(tasks):
    task_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
       end_time = task_start_time + timedelta(minutes=minutes)
       schedule.append((task, task_start_time, end_time))
       task_start_time = end_time  # Update the start time for the next task
    return schedule

def main():
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    current_index = 0

    while True:
        now = datetime.now()
        current_task, start_time, end_time = schedule[current_index]
        remaining_time = end_time - now
        remaining_minutes = int(remaining_time.total_seconds() // 60)

        print('')

        for index, (task, s_time, e_time) in enumerate(schedule):
            if index < current_index:
                # Task is completed
                print(f'{task} done: {e_time.strftime("%H:%M")}')
            elif index == current_index:
                # Current Task
                if remaining_minutes < 2:
                    cprint(f'{task} < 2m left!', 'white', 'on_red', attrs=['blink'])
                elif remaining_minutes < 5:
                    cprint(f'{task} - {remaining_minutes} mins', 'white', 'on_red')
                else:
                    cprint(f'{task} - {remaining_minutes} mins', 'white', 'on_blue')
            else:
                print(f'{task} @ {s_time.strftime("%H:%M")}')

        list_of_reminders = [
            "I have a 1000 Percent Algo",
            "Time is irrelevant, keep swimming",
            "Everyday I get better",
            "Rest at the end",
            "Jobs not finished",
            "Deal was already made",
            "Best Algo Trader in the World"
        ]

        random_reminder = random.choice(list_of_reminders)
        print('💫 ' + random_reminder)

        if now >= end_time:
            current_index += 1
            if current_index >= len(schedule):
                cprint("All Tasks Completed", 'white', 'on_green')
                break

        time.sleep(15)

main()

# /Users/arman/Desktop/Moon_Dev/Productivity_App/productivity.py