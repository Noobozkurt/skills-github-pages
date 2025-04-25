from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route('/produits')
def get_produits():
    df = pd.read_csv("catalogue_complet_cosmetiques_tiktok.csv")
    return jsonify(df.to_dict(orient="records"))

@app.route('/')
def index():
    return send_from_directory('.', 'products.html')