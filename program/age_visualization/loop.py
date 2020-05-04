from .percent import *
from .number import *

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
            "topicName": "Return",
            "fonction": 0
        }
    ]

    while True:
        print("\nAge Visualization : ")
        for index in range(len(topics)):
            print(f"{index + 1}. {topics[index]['topicName']}")
        choice = int(input("\nChoose your topic :\n"), 10) - 1
        if choice >= len(topics):
            print("Invalid input")
        elif choice == len(topics) - 1:
            break
        else:
            topics[choice]['fonction']()    