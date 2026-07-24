# Q1.Complete the total_xp function. It accepts two integers as input:

# level
# xp_to_add
# There are 100 xp per level. total_xp should convert the current level to xp, then add this current xp to the xp_to_add argument and return the player's total xp. For example:

# If a player is level 1 and gains 100 xp, they have 200 total xp.
# If a player is level 2 and gains 250 xp, they have 450 total xp.
# If a player is level 170 and gains 590 xp, they have 17590 total xp.


level = 0
def total_xp(level, xp_to_add):
    current_xp = level*100 + xp_to_add
    xp_to_add = xp_to_add + current_xp
    return current_xp
    


run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expected: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
