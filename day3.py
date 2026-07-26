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

# A 1 in binary is the same as True, while 0 is False. So really a bitwise operation is just a bunch of logical operations that are completed in tandem by column.
# example:
# 0 & 0 = 0
# 1 & 1 = 1
# 1 & 0 = 0

# Binary Notation
# When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number. 0b10 is two in binary, but 10 without the 0b prefix is simply ten.

# 0b0101 is 5
# 0b0111 is 7

# 0b0101 & 0b0111
#  equals 5

# binary_five = 0b0101
# binary_seven = 0b0111
# binary_five & binary_seven
#  equals 5

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    user_create_permissions = can_create_guild & user_permissions
    return user_create_permissions


def get_review_bits(user_permissions):
    user_review = can_review_guild & user_permissions
    return user_review


def get_delete_bits(user_permissions):
    user_delete = can_delete_guild & user_permissions
    return user_delete

def get_edit_bits(user_permissions):
    user_get = can_edit_guild & user_permissions
    return user_get



student = ...
run_cases = [
    (get_create_bits, 0b1000, 0b1010, True),
    (get_review_bits, 0b0100, 0b1001, False),
    (get_delete_bits, 0b0010, 0b0110, True),
    (get_edit_bits, 0b0001, 0b1110, False),
]

submit_cases = run_cases + [
    (get_create_bits, 0b1000, 0b0111, False),
    (get_review_bits, 0b0100, 0b0110, True),
    (get_delete_bits, 0b0010, 0b1101, False),
    (get_edit_bits, 0b0001, 0b0011, True),
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


# Bitwise “|” Operator
# Q3 A 1 in binary is the same as True, while 0 is False. So a bitwise operation is just a bunch of logical operations that are completed in tandem. When two binary numbers are "or"ed together, the result has a 1 in any place where either of the input numbers has a 1 in that place.

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    guild_perms = glorfindel | galadriel | elendil | elrond
    return guild_perms




run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
]

submit_cases = run_cases + [
    (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
    (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = calculate_guild_perms(input1, input2, input3, input4)
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


# Q3 Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.

# For example:

# data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
# print(data_a)

def binary_string_to_int(num_servers, num_players, num_admins):
    num1 = int(num_servers ,2)
    num2 = int(num_players, 2)
    num3 = int(num_admins , 2)
    return num1,num2,num3


run_cases = [
    ("1", "10", "1010", (1, 2, 10)),
    ("101", "11", "10100", (5, 3, 20)),
    ("111", "1011", "11010", (7, 11, 26)),
]

submit_cases = run_cases + [
    ("0", "0", "0", (0, 0, 0)),
    ("1111", "1111", "1111", (15, 15, 15)),
    ("101010", "110011", "101010", (42, 51, 42)),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = binary_string_to_int(input1, input2, input3)
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

