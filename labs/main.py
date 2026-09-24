def build_roster(students):
    roster = {}
    # TODO: loop through `students` and group names by grade in `roster`
    for names,grade in students:
        if grade not in roster:
            roster[grade] = []
        roster[grade]. append(names)
    return roster
print(build_roster([("Ada", 5),("Bola", 6),("chidi",5)]))