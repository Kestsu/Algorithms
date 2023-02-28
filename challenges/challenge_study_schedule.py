def study_schedule(permanence_period, target_time):

    contador = 0
    try:
        for permanent in permanence_period:
            if permanent[0] <= target_time and permanent[1] >= target_time:
                contador += 1
        return contador
    except TypeError:
        return None


if __name__ == '__main__':
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1))
