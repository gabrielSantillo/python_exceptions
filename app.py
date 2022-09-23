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