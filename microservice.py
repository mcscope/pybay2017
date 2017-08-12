# #!/usr/bin/env python
"""PyBay vprof remote profiling example

First of all launch vprof in remote mode:

    vprof -r

and launch this script:

    python microservice.py fetch 9001

Then you can profile the fetch handler

    curl http://127.0.0.1:9001/profile/fetch

and

curl 127.0.0.1:9001/profile/fetch
"""

from flask import Flask, redirect
import os
import random
from vprof import runner
import sys

FETCH_URL = "http://localhost:9001/fetch"
RENDER_URL = "http://localhost:9002/render"
role = sys.argv[1]
app = Flask(role)


@app.route("/fetch")
def fetch():
    FORTUNE_DIR = "/usr/local/Cellar/fortune/9708/share/games/fortunes/"

    all_fortunes = []
    for filename in os.listdir(FORTUNE_DIR):

        path = os.path.join(FORTUNE_DIR, filename)

        if not os.path.isfile(path) or path.endswith(".dat"):
            continue

        with open(path, 'r') as fortune_file:
            new_fortunes = parse_fortunes(fortune_file)
            all_fortunes.extend(new_fortunes)

    return random.choice(all_fortunes)


@app.route('/profile/fetch', methods=['GET', 'POST'])
def profiler_handler():
    try:
        runner.run(fetch, 'cmhp')
    except:
        import traceback
        traceback.print_exc(file=sys.stdout)

    return redirect('/')


def parse_fortunes(lines):
    FORTUNE_SEPERATOR = "%\n"
    fortunes = []
    current_fortune_lines = []
    for line in lines:
        if line == FORTUNE_SEPERATOR:
            found_fortune = "".join(current_fortune_lines)
            if found_fortune not in served_fortunes:
                fortunes.append(found_fortune)
            current_fortune_lines = []
        else:
            current_fortune_lines.append(line)
    return fortunes

served_fortunes = []


if __name__ == '__main__':
    app.run(port=int(sys.argv[2]))
