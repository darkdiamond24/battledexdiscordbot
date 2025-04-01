import json
import re
from flask import Flask, jsonify

app = Flask(__name__)

# Path to your HTML file
HTML_FILE_PATH = r"C:\Users\milan\OneDrive\Bureaublad\Websites\Balls\ballsabilities.html"

def extract_balls_from_html():
    """Reads the HTML file and extracts the countryball data dynamically."""
    try:
        with open(HTML_FILE_PATH, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Debugging: Print a preview of the HTML content (first 500 characters)
        print("🔍 HTML content preview:", html_content[:500])

        # Extract the const balls array from JavaScript inside the HTML
        match = re.search(r"const balls = (\[.*?\]);", html_content, re.DOTALL)
        if not match:
            print("⚠️ No 'const balls' array found in HTML.")
            return []

        balls_js = match.group(1)
        print("✅ Extracted raw JS (first 500 chars):", balls_js[:500])  # Debugging output

        # Fix JavaScript-style formatting for JSON
        balls_json = balls_js.replace("'", '"') \
                             .replace("None", "null") \
                             .replace("True", "true") \
                             .replace("False", "false")

        # Convert JS-like data to Python list safely
        balls_data = json.loads(balls_json)
        return balls_data

    except Exception as e:
        print(f"❌ Error extracting data: {e}")
        return []

@app.route('/api/abilities', methods=['GET'])
def get_abilities():
    """API endpoint to serve countryball abilities as JSON."""
    balls = extract_balls_from_html()
    return jsonify(balls)

if __name__ == '__main__':
    app.run(debug=True)
