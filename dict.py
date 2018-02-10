# A dictionary can contain multiple pairs of information
mydeets = {
    "name": "Risa Prezzano", 
    "age": "35", 
    "hobbies": ["Table Tennis", "Monument Valley", "Puzzles"], 
    "Waking Times": {"Mon": "5:30am", "Tues": "5:30am", "Wed": "5:30am", "Thurs": "5:30am", "Fri": "5:30am", "Sat": "6:30am", "Sun": "7:30am"}
}

# Print out results are stored in the dictionary
print("Hi, I'm " + mydeets["name"] + " and I was " + mydeets["age"] + " years old.")
print("I have " + str(len(mydeets["hobbies"])) + " core hobbies!")

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information
# another_actor = {"name": "Sylvester Stallone", "age": 62, "married": True, "best movies": ["Rocky", "Rocky 2", "Rocky 3"]}
# print(another_actor["name"] + " was in  " + another_actor["best movies"][0])

# A dictionary can even contain another dictionary
# film = {"title": "Interstellar", "revenues": {"United States":360, "China":250, "United Kingdom":73}}
# print(film["title"] + " made " + str(film["revenues"]["United States"]) + " in the US.")
# --------------------