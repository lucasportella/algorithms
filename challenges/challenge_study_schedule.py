def input_check(input):
    if type(input[0]) == int and type(input[1]) == int:
        return True
    return False

def study_schedule(permanence_period, target_time='missing'):
    if target_time == 'missing' or type(target_time) != int: return None
    counter = 0
    for c in permanence_period:
        if not input_check(c): return None
        if target_time in c or (c[0] < target_time and c[1] > target_time):
            counter += 1
    return counter
