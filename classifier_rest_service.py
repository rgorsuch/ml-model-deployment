#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:29:19 2022

@author: ryan.gorsuch
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:18:11 2022

@author: ryan.gorsuch
"""
import numpy as np
import pickle
from flask import Flask, request


app = Flask(__name__)

local_classifier = pickle.load(open("classifier.pickle", "rb"))
local_scaler = pickle.load(open("sc.pickle", "rb"))

@app.route("/model", methods=["POST"])
def hello_model():
    request_data = request.get_json(force=True)
    #model_name = request_data["model"]
    age = request_data["age"]
    salary = request_data["salary"]
    prediction = local_classifier.predict(
        local_scaler.transform(
            np.array([[age, salary]])
        )
    )
    probability = local_classifier.predict_proba(
        local_scaler.transform(
            np.array([[age, salary]])
        )
    )[:,1]

    return f"The prediction is {prediction}\n"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
