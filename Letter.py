class Letter:
    letter = ""
    iterator = 0

    def __init__(self, letter = None):
        self.letter = letter
        self.iterator+= 1

    def __iterate__(self):
        self.iterator+=1

