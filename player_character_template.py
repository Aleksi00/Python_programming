# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Anni Niskanen
# Template for Exercise 9.5


import random


class PlayerCharacter:

    ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    SKILLS_TO_ABILITIES = {"Acrobatics" : "Dexterity", "Animal Handling" : "Wisdom", "Arcana" : "Intelligence",
                           "Athletics" : "Strength", "Deception" : "Charisma", "History" : "Intelligence",
                           "Insight" : "Wisdom", "Intimidation" : "Charisma", "Investigation" : "Intelligence",
                           "Medicine" : "Wisdom", "Nature" : "Intelligence", "Perception" : "Wisdom",
                           "Performance" : "Charisma", "Persuasion" : "Charisma", "Religion" : "Intelligence",
                           "Sleight of Hand" : "Dexterity", "Stealth" : "Dexterity", "Survival" : "Wisdom"}

    ABILITY_SCORES_TO_MODIFIERS = {1 : -5, 2 : -4, 3 : -4, 4 : -3, 5 : -3, 6 : -2, 7 : -2, 8 : -1, 9 : -1, 10 : 0,
                                   11 : 0, 12 : 1, 13 : 1, 14 : 2, 15 : 2, 16 : 3, 17 : 3, 18 : 4, 19 : 4, 20 : 5}

    def __init__(self, character_name, race, character_class, hit_die, armor_class):
        self.__name = character_name
        self.__race = race
        self.__class = character_class
        self.__hit_die = hit_die
        self.__armor_class = armor_class
        self.__level = 1
        self.__ability_scores = {}
        for ability in PlayerCharacter.ABILITIES:
            self.__ability_scores[ability] = PlayerCharacter.roll_ability_score()
        self.__max_hp = hit_die + PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[self.__ability_scores["Constitution"]]
        # Jos max_hp < 1
        self.__hp = self.__max_hp

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_class(self):
        return self.__class

    def get_level(self):
        return self.__level

    def is_downed(self):
        if self.__hp < 1:
            return True
        else:
            return False

    def get_ability_modifier(self, ability):
        if ability in PlayerCharacter.ABILITIES:
            return PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[self.__ability_scores[ability]]
        else:
            return None

    def get_skill_level(self, skill):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            return self.get_ability_modifier(PlayerCharacter.SKILLS_TO_ABILITIES[skill])
        else:
            return None

    def skill_check(self, skill, result_to_pass):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            i = PlayerCharacter.roll_die(20) + self.get_skill_level(skill)
            if i >= result_to_pass:
                return True
            else:
                return False

        else:
            return None

    def level_up(self):
        self.__level += 1
        i = PlayerCharacter.roll_die(self.__hit_die)
        self.__max_hp += i
        self.__hp += i
        return i

    def attack(self, other_character):
        i = PlayerCharacter.roll_die(20)
        s = 2
        if i >= other_character.__armor_class:
            if self.__class == "Fighter":
                s = 6
            elif self.__class == "Ranger":
                s = 8
            elif self.__class == "Wizard":
                s = 10
            elif self.__class == "Rogue":
                s = 4
            a = PlayerCharacter.roll_die(s)
            if a >= other_character.__hp:
                a = other_character.__hp
                other_character.__hp = 0
            else:
                other_character.__hp -= a
            return a
        else:
            return 0

    def heal(self):
        i = PlayerCharacter.roll_die(5)
        if i + self.__hp <= self.__max_hp:
            self.__hp+=i
        else:
            i = self.__max_hp - self.__hp
            self.__hp = self.__max_hp
        return i

    def __str__(self):
        string_1 = self.__name + ", a level "+str(self.__level) + " " + self.__race + " " + self.__class+"\n"
        string_2 = "HP: " + str(self.__hp) + "/" + str(self.__max_hp)+"\n"
        string_3 = "STR: {:2d}   DEX: {:2d}   CON: {:2d}   INT: {:2d}   WIS: {:2d}   CHA: {:2d}   ".format(self.__ability_scores["Strength"], self.__ability_scores["Dexterity"],self.__ability_scores["Constitution"],self.__ability_scores["Intelligence"],self.__ability_scores["Wisdom"],self.__ability_scores["Charisma"])
        k = string_1 + string_2 + string_3
        return k
    @staticmethod
    def roll_die(die_sides):
        return random.randint(1, die_sides)

    @staticmethod
    def roll_ability_score():
        roll_results = [PlayerCharacter.roll_die(6) for i in range(4)]  # throwing 4 6-sided dies
        smallest = 1000  # just some very large value
        for result in roll_results:  # choosing 3 largest results
            if result < smallest:
                smallest = result
        roll_results.remove(smallest)  # removing smallest result
        roll_sum = sum(roll_results)  # adding 3 largest results
        return roll_sum
