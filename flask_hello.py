#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:18:11 2022

@author: ryan.gorsuch
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/model", methods=["POST"])
def hello_model():
    request_data = request.get_json(force=True)
    model_name = request_data["model"]
    return f"You requested the {model_name} model"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
