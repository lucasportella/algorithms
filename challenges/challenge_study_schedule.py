def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    counter = 0
    for c in permanence_period:
        if type(c[0]) != int or type(c[1]) != int:
            return None
        if target_time in c or (c[0] < target_time and c[1] > target_time):
            counter += 1
    return counter
