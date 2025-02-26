from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load CSV data
def load_data():
    df = pd.read_csv('dump.csv')
    df.columns = df.columns.str.strip()  # Remove spaces around column names
    return df

data = load_data()

# API to get the list of indices
@app.route('/api/indices')
def get_indices():
    return jsonify(data['index_name'].dropna().unique().tolist())

# API to get data for a selected index
@app.route('/api/index/<name>')
def get_index_data(name):
    index_data = data[data['index_name'] == name].to_dict(orient='records')
    return jsonify(index_data)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
