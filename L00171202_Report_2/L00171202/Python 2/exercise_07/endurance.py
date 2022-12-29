def get_endurance(fuel: float, consumption: float):
    endurance = 0
    if consumption < 0:
        print("Consumption cannot be negative, Please correct and try again")
        return None

    if fuel < 0:
        print("Fuel cannot be negative, Please correct and try again")
        return None

    try:
        endurance = fuel/consumption
    except ZeroDivisionError as err:
        print(err, 'Error,' , 'Consumption cannot be zero', )
        return None
    except ValueError as err:
        print('input validation issue, Please correct before proceeding')
        return None

    return endurance

if __name__ == '__main__':
    print(get_endurance(10,0))
    print(get_endurance(0,0))
    print(get_endurance(0,10))
    print(get_endurance(-10,4.0))
    print(get_endurance(10,-4))