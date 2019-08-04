import re

text = """17-120 17-121 17-122 - 131-123 12-123"""

pattern = re.compile("(^| )(\d{2}-\d{3})")

print(pattern.findall(text))
print(pattern.search(text, 6))
print(x.span())

start = 0

