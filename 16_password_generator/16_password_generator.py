import string
import random
import time

def main():
    weak_password = ""
    strong_password = ""

    # Get requirements to create the password
    amount_characters = int(input("How many characters the password must have? "))
    check_answer = input("Do you want a WEAK or STRONG password? ")

    def check_path(check_answer):
        if check_answer.lower() == "weak":
            random_word = weak_random_word()
            weak_password = weak_password_generator(random_word)
            print("Ok. Wait a second while I create a WEAK PASSWORD...")
            time.sleep(2)
            print(weak_password)
        else:
            strong_password = strong_password_generator()
            print("Ok. Wait a second while I create a STRONG PASSWORD...")
            time.sleep(2)
            print(strong_password)

    # Picking a random word for weak password
    def weak_random_word():
        list1 = ["pug", "shepperd", "heeler", "greyhound", "bulldog", "malamute", "foxhound", "husky", "dobermann", "collie"]
        list2 = ["siamese", "ragdoll", "birman", "sphynx", "burmese", "chartreux", "peterbald", "snowshoe", "ragamuffin", "chausie"]

        defining_list = random.randint(1, 2)

        if defining_list == 1:
            random_word = list1[random.randint(0, 9)]
            return random_word
        else:
            random_word = list2[random.randint(0, 9)]
        return random_word

    # Generator WEAK PASSWORD logic
    def weak_random_word():
        list1 = ["pug", "heeler", "husky", "collie", "poodle", "hound"]
        list2 = ["red", "blue", "green", "black", "gray", "pink", "white"]

        defining_list = random.randint(1, 2)

        if defining_list == 1:
            random_word = list1[random.randint(0, len(list1))]
            return random_word.capitalize()
        else:
            random_word = list2[random.randint(0, len(list2))]
        return random_word.capitalize()

    def weak_password_generator(random_word):
        characters_counter = len(random_word)
        weak_password = random_word
        special = input("Include special characters [YES] or [NO]? ")

        # a-z, A-Z, 0-9
        while characters_counter < amount_characters:
            if special.lower().startswith("y"):
                weak_password += random.choice(string.digits + string.punctuation)
            else:
                weak_password += random.choice(string.digits)
            characters_counter += 1

        return weak_password

    # Generator STRONG PASSWORD logic
    def strong_password_generator():
        characters_counter = 0
        password = ""

        # a-z, A-Z, 0-9
        while characters_counter < amount_characters:
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
            characters_counter += 1

        return password

    check_path(check_answer)

if __name__ == "__main__":
    main()