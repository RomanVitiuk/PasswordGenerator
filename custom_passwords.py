from random import sample
import re
from string import ascii_letters, digits, punctuation
import sys


def gen_pass(lenght):
    letters = ascii_letters + digits + punctuation
    pattern = r"[a-zA-Z0-9\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]+"
    while True:
        password = "".join(sample(letters, int(lenght)))
        if re.fullmatch(pattern, password):
            return password


if len(sys.argv) == 1:
    pass_len = 8
else:
    pass_len = int(sys.argv[1])

print(gen_pass(lenght=pass_len))

