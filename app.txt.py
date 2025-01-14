from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operation', methods=['POST'])
def perform_operation():
    try:
        data = request.json
        operation = data.get('operation', '')
        values = data.get('values', [])
        
        # Perform the requested operation
        if operation == 'SUM':
            result = sum(values)
        elif operation == 'AVERAGE':
            result = sum(values) / len(values) if len(values) > 0 else 0
        elif operation == 'MAX':
            result = max(values)
        elif operation == 'MIN':
            result = min(values)
        elif operation == 'COUNT':
            result = len(values)
        elif operation == 'TRIM':
            result = [val.strip() for val in values if isinstance(val, str)]
        elif operation == 'UPPER':
            result = [val.upper() for val in values if isinstance(val, str)]
        elif operation == 'LOWER':
            result = [val.lower() for val in values if isinstance(val, str)]
        elif operation == 'FIND_AND_REPLACE':
            find = data.get('find', '')
            replace = data.get('replace', '')
            result = [val.replace(find, replace) if isinstance(val, str) else val for val in values]
        elif operation == 'REMOVE_DUPLICATE':
            result = list(dict.fromkeys(values))  # Removes duplicates while maintaining order
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
