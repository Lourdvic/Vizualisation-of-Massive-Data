import age_visualization

print("COVID_19 Big Data Visualization")

topics = [
    {
        "topicName": "Age visualization",
        "fonction": age_visualization.loop
    },
    {
        "topicName": "Quit",
        "fonction": quit
    }
]

def mainLoop():
    while True:
        print("\nMenu : ")
        for index in range(len(topics)):
            print(f"{index + 1}. {topics[index]['topicName']}")
        choice = int(input("\nChoose your topic :\n"), 10) - 1
        if choice >= len(topics) + 1:
            print("Invalid input")
        else:
            topics[choice]['fonction']()

mainLoop()