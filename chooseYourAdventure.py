
text = [["Welcome to choose your own adventure!", ["Press 1 to begin", 1], ["Press 2 to begin anyway", 1]],

        ["You are walking down a dark jungle path with two of your trusty adventurers. Suddenly, one of"
        " them lets out a shriek and is pulled into the dark leaves. What do you do?", ["Press 1 to go after him", 2],
            ["Press 2 to leave him, he slowed us down anyway", 3]],

        ["You cautiously approach the spot where he disappeared and move through the leaves."
        "You see a boot on the ground and pick it up. There is blood on the boot, and some black fur."
        "What do you do?", ["Turn on your flashlight", 4], ["Yell his name", 5]],

        ["You continue on your journey and come to a river. There is a rickety bridge across"
        "The river is too fast to cross without a bridge. What do you do?",
            ["Brave the ghetto bridge", 2], ["Try to find a way around", 2]],

        ["You turn on your flashlight and see the enormous shape. It turns around and standing before you is "
        "the largest gorilla you've ever seen. It tears you and your friends to shreds. You die",
            ["Press one to start over", 0], ["Press two to also go back", 2]]]


class Story:
    def __init__(self, texts):
        self.texts = texts
        self.num = 0

    def play(self, number):
        print(self.texts[number][0])
        print(self.texts[number][1][0])
        print(self.texts[number][2][0])

    def play_story(self):
        self.play(self.num)
        choice = input("Your choice: ")
        if not choice:
            return False
        if choice == "1":
            self.num = self.texts[0][1][1]
            self.play(self.num)
        elif choice == "2":
            self.num = self.texts[0][1][1]
            self.play(self.num)






def main():
    story1 = Story(text)

    while True:
        if not story1.play_story():
            print("Done")
            break


main()