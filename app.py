from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load Excel data
df = pd.read_excel("your_excel_file.xlsx")  # Ensure 'your_excel_file.xlsx' is in the same directory

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()  # Get search query from URL
    results = df[df['Name'].str.lower().str.contains(query, na=False)]  # Filter data
    return jsonify(results.to_dict(orient='records'))  # Return results as JSON

if __name__ == '__main__':
    app.run(debug=True)
