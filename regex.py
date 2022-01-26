# Chomsky Hierarchy Type 3, regular language.
# Regular expressions are used for parsing.

# Built-in library
import re

email = "hugo@roguh.com"

re.match("[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.(com|net|edu|io)", email)

re.match("^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+$", email)
