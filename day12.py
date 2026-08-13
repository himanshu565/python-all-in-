# Q1 Deleting Dictionary Values
names_dict = {"jack": "bronson", "jill": "mcarty", "joe": "denver"}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

# Q2 We need to display on our players' screens what the most common enemy in a given area of the game map is.

# Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

# If there are no enemies, return the Python None value (not a string). If there are multiple enemies with the same highest count, return the first one found.

# enemies_dict is a dictionary of name -> count. Example:

def get_most_common_enemy(enemies_dict):
    pass


run_cases = [
    ({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}, "soldier"),
    ({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5}, "gremlin"),
]

submit_cases = run_cases + [
    ({"jackal": 2, "gremlin": 7}, "gremlin"),
    ({"jackal": 3}, "jackal"),
    ({}, None),
    ({"kobold": 5, "soldier": 5, "gremlin": 5, "dragon": 5}, "kobold"),
    ({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}, "dragon"),
    ({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}, "gremlin"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expected: {expected_output}")
    result = get_most_common_enemy(input1)
    if result == "None":
        print('Actual: "None"')
    else:
        print(f"Actual: {result}")
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
