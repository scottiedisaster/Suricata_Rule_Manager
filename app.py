from flask import Flask, request, send_from_directory ,jsonify
import os

app = Flask(__name__)

# Define the path to the Suricata rules file
RULES_FILE = '/var/lib/suricata/rules/suricata.rules'

def read_rules():
    with open(RULES_FILE, 'r') as file:
        rules = file.readlines()
    return rules

def write_rules(rules):
    with open(RULES_FILE, 'w') as file:
        file.writelines(rules)

@app.route('/api/rules', methods=['GET'])
def get_rules():
    rules = read_rules()
    return jsonify(rules)

@app.route('/api/rules', methods=['POST'])
def update_rules():
    rules = request.json
    write_rules(rules)
    return jsonify({'status': 'success'})

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
