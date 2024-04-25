import json
import random
from flask import Flask

property_with_scores_json = "./mock_data/property_with_scores.json"

app = Flask(__name__)


@app.route('/get-properties')
def get_properties_with_scores():
    with open(property_with_scores_json, 'r') as json_file:
        data = json.load(json_file)
    return data


@app.route('/get-property')
def get_random_property_with_score():
    return random.choice(get_properties_with_scores())


def get_matching_score_from_property(property: dict):
    return property["matching"]["score"]


def get_matching_status_from_property(property: dict):
    return property["matching"]["status"]


app.run(debug=True)
