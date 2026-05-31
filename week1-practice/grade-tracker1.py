grades = {
    "Ali": 70,
    "Sara": 45,
    "Shaima": 90,
    "Rayyan":80 ,
    "Mohammed": 60,
    "Alaa": 98,
    "Ron": 20,
    "Zenaida": 15,
}

for name, score in grades.items():
    if score >= 50: 
        print(f"{name}, you passed! Congrats!")
    elif score < 50: 
        print(f"{name}, you failed")


highest = max(grades.values())
print(highest)

lowest = min(grades.values()) 
print(lowest)

average = sum(grades.values())/len(grades)
print(average)

for name, score in grades.items(): 
    if score == highest:
        print(name)
