from flask import Flask, render_template, request
import pandas as pd
from rapidfuzz import process

app = Flask(__name__)

# Load the Excel file and clean column names
df = pd.read_excel("data/HSN_Master_Data.xlsx")
df.columns = df.columns.str.strip()  # remove extra spaces from headers

# Check for proper column names
if 'HSNCode' not in df.columns or 'Description' not in df.columns:
    raise ValueError("Excel file must contain 'HSNCode' and 'Description' columns.")

# Ensure HSNCode is treated as string
df['HSNCode'] = df['HSNCode'].astype(str)

# Validate HSN code
def validate_hsn(code):
    result = {"code": code}

    if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
        result["status"] = "Invalid Format"
        result["message"] = "HSN code must be numeric and 2, 4, 6, or 8 digits."
        return result

    if code not in df['HSNCode'].values:
        result["status"] = "Invalid"
        result["message"] = "HSN code not found in master dataset."
        return result

    parents = [code[:i] for i in [2, 4, 6] if i < len(code)]
    parent_exists = [p for p in parents if p in df['HSNCode'].values]

    description = df[df['HSNCode'] == code]['Description'].values[0]
    result["status"] = "Valid"
    result["message"] = f"Description: {description}"
    result["parents"] = parent_exists
    return result

# Suggest HSN code based on description
def suggest_hsn(description):
    choices = df['Description'].tolist()
    matches = process.extract(description, choices, limit=3)

    suggestions = []
    for match in matches:
        desc, score, idx = match
        suggestions.append({
            "hsn": df.iloc[idx]['HSNCode'],
            "description": desc,
            "score": score
        })
    return suggestions

# Web route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    suggestions = None

    if request.method == "POST":
        hsn_input = request.form.get("hsn_code")
        desc_input = request.form.get("description")

        if hsn_input:
            result = validate_hsn(hsn_input)
        if desc_input:
            suggestions = suggest_hsn(desc_input)

    return render_template("index.html", result=result, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
