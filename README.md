# 🧾 HSN Code Validation & Suggestion Agent

This project is a web-based tool that validates and suggests HSN (Harmonized System of Nomenclature) codes using a master dataset. It is useful for businesses and professionals who deal with GST filings, invoices, and product classification in India.

---

## 📌 Features

- ✅ **HSN Code Validation** — Checks if an entered HSN code exists in the master dataset.
- 🧠 **HSN Code Suggestions** — Uses fuzzy matching to recommend possible HSN codes based on product description.
- 📊 **Parent Code Tracing** — Displays parent codes if the provided code is a sub-code.
- 🖥️ **User-Friendly Interface** — Built with Flask and Bootstrap for ease of use.

---

## 🛠️ Tech Stack

| Layer        | Technologies Used             |
|--------------|-------------------------------|
| **Frontend** | HTML, Bootstrap, Jinja2       |
| **Backend**  | Python (Flask)                |
| **Data**     | Excel (`HSN_Master_Data.xlsx`)|
| **Library**  | Pandas, FuzzyWuzzy, Openpyxl  |

---

## 🚀 How It Works

1. User enters an **HSN code** and/or a **product description**.
2. The system:
   - Validates the HSN code against the master dataset.
   - Suggests similar codes using `fuzzywuzzy` based on the description.
3. Results are shown on the same page, including validation status and recommendations.

---

## 📂 Project Structure

```
├── app.py                  # Flask backend with validation and suggestion logic
├── HSN_Master_Data.xlsx    # Master Excel file of HSN codes
├── templates/
│   └── index.html          # Frontend form and result rendering

---

## 🧪 Requirements

Install dependencies using pip:

```bash
pip install flask pandas openpyxl fuzzywuzzy python-Levenshtein
```

---

## ▶️ Running the Project

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

---

## 📥 Input Fields

- **HSN Code**: Optional. 8-digit classification code.
- **Product Description**: Optional. Free text like `live horses`.

---

## ✅ Output

- **Validation Result**: Status, message, and parent codes (if any).
- **Suggestions**: List of 5 best-matching HSN codes with similarity scores.

---

## 📌 Example

### Input:
- HSN Code: `01011010`
- Description: `live horses`

### Output:
- ✔️ Code is valid.
- 💡 Suggestions:
  - 01011010 — Live horses (Score: 100)
  - 01019000 — Other animals (Score: 82)
  - ...

---

## 📄 License

This project is open-source and free to use under the MIT License.

---

## 🙋‍♂️ Author

Developed by [S.Keerthi Bushan].  
For queries or collaboration, feel free to reach out!
