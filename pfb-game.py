import sys
from random import shuffle


class pfb_game(object):
    """ Select the requested number of secret digits """
    def __init__(self, length=3):
        self._length = length
        self._digits = [x for x in range(10)]
        shuffle(self._digits)
        self._digits = self._digits[0:self._length]

    def print_pfb(self):
        """ Print out the contents of the generated pfb """
        for x in self._digits:
            print("{} ".format(x), end="")
        print("")

    def digit_count(self):
        return len(self._digits)

    def check_pfb(self, guess):
        """ Given a guess, print out the corresponding P's F's and B's that
            indicate how close the guess is to the secret set.
            If the guess is correct, return True, otherwise return False.
        """
        index = 0
        match = 0
        answer = ""
        for g in guess:
            if self._digits[index] == g:
                answer = answer + 'F '
                match = match + 1

            elif g in self._digits:
                answer = answer + 'P '

            else:
                answer = answer + 'B '

            index = index + 1

        print(answer)
        if match == self.digit_count():
            return True

        return False

    def get_next_guess(self):
        """ Request the next guess from the player """
        print("Enter your next guess:")
        guess = list(map(int, sys.stdin.readline().split()))

        while len(guess) != self.digit_count():
            print("Need {} digits with a space between each".
                  format(self.digit_count()))
            print("Enter your next guess:")
            guess = list(map(int, sys.stdin.readline().split()))

        return guess


def print_intro():
    """ Print out the game rules """
    welcome = """
                 Welcome to Pico Fermi Bagel, or PFB.
    Pico Fermi Bagel is a logic game where one player (I the computer)
    secretly chooses a set of digits from the numbers 0 - 9.  You (the other
    player) try to guess what digits I have selected and in what order they
    are in.  For each digit in the set you guess, I give you a positional
    awnser that indicates the following:
    B:  This digit is not one of the digits I have selected.
    P:  This digit is one I have selected, but it's not in the right place.
    F:  This digit is one I have selected, and it's in the right place.

    Let's do an example, let's say I secretly pick "2 4 6" as my set.
    You first guess "1 2 3".
    I respond with:
    1 2 3
    B P B
    From this, you can tell that "1" and "3" are not part of the set as they
    have "B" under them.  You also know that "2" is present, but it's not in
    proper position.
    Let's say your next guess is: "2 4 5"
    I respond with:
    2 4 5
    F F B
    Ah!  Your getting close.  "2" and "4" are correct, and in the correct
    places, it's just the last place you need to discover.  Let's say your
    next guess is: "2 4 6".
    I respond with"
    2 4 6
    F F F
    And, the game is over, you found the set I picked.

    Now that you know the rules, pick a size for digits in my secret set
    3, 4 or 5, and let's play a round.
    """

    print(welcome)


if __name__ == '__main__':
    print_intro()
    digits = 0
    while digits < 3 or digits > 5:
        digits = int(input("Enter 3, 4, or 5 for the number of digits: "))

    pfb = pfb_game(digits)
    success = False
    while not success:
        guess = pfb.get_next_guess()
        success = pfb.check_pfb(guess)
