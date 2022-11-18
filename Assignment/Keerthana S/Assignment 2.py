import random

while True:
    t = random.randint(25, 200)
    print(t, "degree")
    if t > 150:
        print("Alarm is on as temperature is above 150 degree")
    else:
        print("Alarm is off as temperature is below 150 degree")
    h = random.randint(0, 100)
    print(h, "humidity")
    if h > 80:
        print("Alarm is on as temperature is above 80 percentage")
    else:
        print("Alarm is off as temperature is below 80 percentage")
