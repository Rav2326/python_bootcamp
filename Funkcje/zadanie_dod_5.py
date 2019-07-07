"""

Napisz funkcje, która sprawdzi, czy napis jest pangramem


"""

import string
print(string.ascii_lowercase + "ąćęłńśżźó")

def is_pangram(text, letters = string.ascii_lowercase):


    text = text.lower()
    for znak in set(text):
        if not znak.isalpah():
            text = text.replace(znak,"")


    if len(set(text)) < len(letters):
        return False
    return True

Polish_letters = letters = string.ascii_lowercase.replace("x", "").replace("v", "").replace("q", "") + "ąćęłńśżźó"

def test_is_pangram():
    assert is_pangram("the quick brown fox jump over the lazy dog") == True
    assert is_pangram("ala ma kota") == False
    assert is_pangram("Pchnąć w tę łódź jeża lub ośm skrzyń fig", alfabet) == True

