stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append("Edinburgh Waverley")
print(stops)

stops.insert(0, "Glasgow Queen St")
print(stops)

stops.insert(4, "Polmont")
print(stops)

index = stops.index("Linlithgow")
print(index)

stops.remove('Livingston')
print(stops)

del stops[2]
print(stops)

number_of_stops = len(stops)
print(number_of_stops)