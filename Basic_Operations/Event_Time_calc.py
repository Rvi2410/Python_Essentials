hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins =  mins + dura
print(mins)
hour = hour + mins // 60
print(hour)
mins = mins % 60
print(mins)
print("End Time of the event " + str(hour) +":" + str(mins))
