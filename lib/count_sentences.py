#!/usr/bin/env python3
import ipdb

class MyString:

    def __init__(self, value = ""):
        self.set_value(value)
  
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self._value[-1] == "."
    
    def count_sentences(self):
        value = self.value
        value = value.replace('!', '.')
        value = value.replace('?', '.')
        sentences = [s for s in value.split('.') if s]
        return len(sentences)
    
    def is_exclamation(self):
        return self.value[-1] == "!"

    def is_question(self):
        return self.value[-1] == "?"

    value = property(get_value, set_value)
