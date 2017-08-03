#!/usr/bin/env python
"""Implements Unix Fortune using 3 microservices and an API"""
import sys
from flask import Flask, request, render_template_string
import requests

FETCH_URL = "http://localhost:9001/fetch"
RENDER_URL = "http://localhost:9002/render"
role = sys.argv[1]
app = Flask(role)


@app.route("/")
def main():

    fortunes = []
    for _ in range(0, 3):
        fortunes.append(requests.get(FETCH_URL).content)

    return requests.post(RENDER_URL, data={'fortunes': fortunes}).content


@app.route("/fetch")
def fetch():
    return requests.get("http://mcscope.com/fortune").content


@app.route("/render", methods=["POST"])
def render():
    fortune_template = "<div style='margin:100px;'> {{fortune}} </div>"
    fortune_divs = [render_template_string(fortune_template, fortune=fortune)
                    for fortune in request.form.getlist("fortunes")]

    body_template = """
    <html>
        <body>
            <div style="width:50%; margin:auto; margin-top:100px;">
                {{"".join(fortune_divs)}}
            </div>
        </body>
    </html>
    """
    return render_template_string(body_template, fortune_divs=fortune_divs)

if __name__ == '__main__':
    app.run(port=int(sys.argv[2]), debug=True)
