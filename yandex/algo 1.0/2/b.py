a = int(input())
b = int(input())

def state_check(a, b):
    if a == b:
        state = "CONSTANT"
    elif b > a:
        state = "ASCENDING"
    elif a > b:
        state = "DESCENDING"
    return state 

def f(state, temp):
    x = int(input())
    while x != -2000000000:
        new_state = state_check(temp, x)

        if new_state == "ASCENDING" and state == "CONSTANT":
            state = "WEAKLY ASCENDING"
            
        elif new_state == "DESCENDING" and state == "CONSTANT":
            state = "WEAKLY DESCENDING"

        elif new_state == "CONSTANT" and state == "WEAKLY ASCENDING":
            state = "CONSTANT"

        elif new_state == "CONSTANT" and state == "WEAKLY DESCENDING":
            state = "CONSTANT"

        elif new_state in ["ASCENDING", "DESCENDING"] and state in ["WEAKLY ASCENDING", "WEAKLY DESCENDING"]:
            pass

        elif new_state != state:
            state = "RANDOM"

        temp = x
        x = int(input())

    return state 


state = state_check(a, b)
temp = b 

if a == -2000000000 or b == -2000000000:
    print("CONSTANT")
else:
    print(f(state, temp))


# assert Sequence([-530, -530, -530]).type == 'CONSTANT'
# assert Sequence([1, 7, 9]).type == 'ASCENDING'
# assert Sequence([1, 9, 7]).type == 'RANDOM'
# assert Sequence([2, 2, 2]).type == 'CONSTANT'
# assert Sequence([2, 2]).type == 'CONSTANT'
# assert Sequence([2, 2, 3]).type == 'WEAKLY ASCENDING'
# assert Sequence([3, 3, 2]).type == 'WEAKLY DESCENDING'
# assert Sequence([4, 3, 2]).type == 'DESCENDING'