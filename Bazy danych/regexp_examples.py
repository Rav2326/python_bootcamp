import re

text = """ababaabbccddabbaabb
abbbabbaabbaacca"""


pattern = re.compile("a{2}b{2}")
pattern2 = re.compile("^ab$")


print(pattern.findall(text))
print(pattern2.findall(text, re.MULTILINE))