import re

pattern2 = re.compile(r"#([A-Za-z0-9$%#@]{7,}[0-9])")

password = 'asldflask%#7'

check = pattern2.fullmatch(password)
print(check)
