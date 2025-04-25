
from flask import Flask, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__, static_folder='.')

@app.route('/produits')
def produits():
    df = pd.read_excel('catalogue_complet_cosmetiques_tiktok.xlsx')
    return jsonify(df.to_dict(orient='records'))

@app.route('/')
def index():
    return send_from_directory('.', 'products.html')

if __name__ == '__main__':
    app.run(debug=True)
