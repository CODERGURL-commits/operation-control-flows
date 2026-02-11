# This is a simple code grader that determines whether you have passed or not.

def score_grade(score):

    if score == 100:
        print("Pass")
    if score > 96:
        print("pass")
    elif score > 92:
        print("pass")
    elif score > 89:
        print("tried")
    elif score > 86:
        print("meeting expectation")
    elif score > 82:
        print("can do better!")
    else:
        print("fail")


score_grade(55)
