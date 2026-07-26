#  Q1 Let's complete the unlock_achievement function. It accepts 3 arguments:

# before_xp: int
# ach_xp: int
# ach_name: str
# It should return 2 values:

# The player's xp after the achievement is unlocked (The sum of before_xp and ach_xp)
# An alert message that says "Achievement Unlocked: ACHIEVEMENT_NAME", where ACHIEVEMENT_NAME is the name of the achievement
# Let's start by running the code in its current state. You should see an error like this:
def unlock_achievement(before_xp, ach_xp, ach_name):
    totalxp = before_xp + ach_xp
    alert = f"Achievement Unlocked: {ach_name}"
    return totalxp , alert
    

run_cases = [
    (100, 20, "Speedster", (120, "Achievement Unlocked: Speedster")),
    (200, 50, "Killer", (250, "Achievement Unlocked: Killer")),
]

submit_cases = run_cases + [
    (100, 50, "Unstoppable", (150, "Achievement Unlocked: Unstoppable")),
    (400, 75, "Gnarly", (475, "Achievement Unlocked: Gnarly")),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = unlock_achievement(input1, input2, input3)
    print(f"Expected: {expected_output}")
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


# Q3 Complete each of the get_XXX_bits functions. Simply use the bitwise & operation on the input of the user's permission bits and the appropriate guild permission bits variable, and return the resulting bits for them to be checked by the tests.

# 4 values have been provided, use the appropriate one for each function:

# can_create_guild
# can_review_guild
# can_delete_guild
# can_edit_guild


can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    pass


def get_review_bits(user_permissions):
    pass


def get_delete_bits(user_permissions):
    pass


def get_edit_bits(user_permissions):
    pass


run_cases = [
    (student.get_create_bits, 0b1000, 0b1010, True),
    (student.get_review_bits, 0b0100, 0b1001, False),
    (student.get_delete_bits, 0b0010, 0b0110, True),
    (student.get_edit_bits, 0b0001, 0b1110, False),
]

submit_cases = run_cases + [
    (student.get_create_bits, 0b1000, 0b0111, False),
    (student.get_review_bits, 0b0100, 0b0110, True),
    (student.get_delete_bits, 0b0010, 0b1101, False),
    (student.get_edit_bits, 0b0001, 0b0011, True),
]


def test(func, perm_bit, user_permissions, expected_output):
    print("---------------------------------")
    print(f"Testing {func.__name__}")
    print(f"Inputs: {user_permissions:04b}")
    print(f"Expecting: {expected_output}")
    result = func(user_permissions) == perm_bit
    print(f"Actual:    {result}")
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
