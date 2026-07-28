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

