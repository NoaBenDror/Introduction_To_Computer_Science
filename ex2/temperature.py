def is_it_summer_yet(threshold, first_day, second_day, third_day):
    """a function that gets three days temperature and a threshold,
    and checks whether on two days (at least) out of the three
    the temperature was higher than the threshold """
    if first_day > threshold and second_day > threshold:
        return True
    if first_day > threshold and third_day > threshold:
        return True
    if second_day > threshold and third_day > threshold:
        return True
    return False

