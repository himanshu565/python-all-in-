# Q1 Fix the award_enchantments function. It calculates the strength of the enchantment – 5 times the total number of quests completed – and prints a message for the player. But we need to make sure this happens only once for every three quests that we iterate over within the loop! Only count the quests in the loop, don't worry about the total number of quests being divisible by 3

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter +=1
        if counter < 3:
            continue
        enchantment_strength = quest_number * 5
        counter = 0
        print(f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!")


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)


main()

# T2 No-Index Syntax
# In my opinion, Python has the most elegant syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:

trees = ["oak", "pine", "maple"]
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple 
# tree, the variable declared using the in keyword, directly accesses the value in the list rather than the index of the value. If we don't need to update the item and only need to access its value then this is a more clean way to write the code.

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True
            

    # don't touch below this line

    return found
    
run_cases = [
    (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
    (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
]

submit_cases = run_cases + [
    ([], False),
    (["Leather Scraps"], True),
    (["Potion", "Healing Potion"], False),
    (["Leather scraps"], False),
    (["Leather", "Scraps"], False),
    (["Potion", "Leather Scraps", "Healing Potion", "Iron Breastplate"], True),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = contains_leather_scraps(input1)
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
