#!/usr/bin/env python
"""Implements Unix Fortune as a microservice"""
import os
import os.path
import random
from flask import Flask

app = Flask("fortune")

FORTUNE_DIR = "/usr/local/Cellar/fortune/9708/share/games/fortunes/"


@app.route("/")
def fetch_fortune():
    return random.choice(get_all_fortunes())


def get_all_fortunes():
    import pudb
    pudb.set_trace()  # breakpoint 31c0f251 //

    all_fortunes = []
    for filename in os.listdir(FORTUNE_DIR):

        path = os.path.join(FORTUNE_DIR, filename)

        if not os.path.isfile(path) or path.endswith(".dat"):
            continue

        with open(path, 'r') as fortune_file:
            all_fortunes.extend(parse_fortunes(fortune_file))

    return all_fortunes


def parse_fortunes(fortune_file):
    FORTUNE_SEPERATOR = "%\n"
    complete_fortunes = []
    current_fortune = []

    for line in fortune_file.readlines():
        if line != FORTUNE_SEPERATOR:
            current_fortune.append(line)
        else:
            complete_fortunes.append("".join(current_fortune))

    return complete_fortunes

if __name__ == '__main__':
    app.run(port=9000)
