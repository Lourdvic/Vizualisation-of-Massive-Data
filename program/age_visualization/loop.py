from .percent import *
from .number import *
from .treemap_by_region import *
from .treemap_by_age import *
import sys

def loop():
    topics = [
        {
            "topicName": "Number of persons by age (Scatter plot)",
            "fonction": number
        },
        {
            "topicName": "Percent of persons by age (Scatter plot)",
            "fonction": percent
        },
        {
            "topicName": "Treemap by region (Treemap)",
            "fonction": treemap_by_region
        },
        {
            "topicName": "Treemap by age (Treemap)",
            "fonction": treemap_by_age
        },
        {
            "topicName": "Return",
            "fonction": 0
        },
        {
            "topicName": "Quit",
            "fonction": sys.exit
        }
    ]

    while True:
        print("\nAge Visualization : ")
        for index in range(len(topics)):
            print(f"{index + 1}. {topics[index]['topicName']}")
        choice = int(input("\nChoose your topic :\n"), 10) - 1
        if choice >= len(topics):
            print("Invalid input")
        elif choice == len(topics) - 2:
            break
        else:
            topics[choice]['fonction']()