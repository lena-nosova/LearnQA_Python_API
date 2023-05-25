class TestShortExample:
    def short_phrase_check(self):
       phrase = input("Set a phrase: ")
       needed_length = 15
       assert len(phrase) < needed_length, f"Phrase does not fit to the requirements"

