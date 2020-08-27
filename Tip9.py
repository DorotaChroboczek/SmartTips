import re
import random

message = """This is the number of Anarchy Sons: 13.
And this is the number of Theirs puppies: 101.
I guess, they're not such a bustards"""


for x in message:
    if re.match(r"[0-9-]", message):
        print(x)