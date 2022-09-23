x = 2
y = "one"

try:
    z = x + y
except TypeError:
    print("You can't sum number with string")
except:
    print("uh oh! Call Helppppppp")
finally:
    print("You've tried something neat")


def asking_age():
    age = input("How old are you? ")
    try:
        age = float(age)
    except ValueError:
        print("You should type only numbers.")
        age = asking_age()
    except:
        print("uh oh")

    return age


result_one = asking_age()
result_two = asking_age()

print(result_one, result_two)
