# 🍽️ Mess Feedback Sorter

**CIT AI-Native Engineering Programme | Semester 1 | Assessment 5**

A Python-based AI-powered feedback classification system that analyses hostel mess feedback in English, Tamil, and Tanglish using a Large Language Model (LLM).

## 📌 Project Overview

The Mess Feedback Sorter is a console-based Python application designed to automatically classify hostel mess feedback.

It identifies feedback categories, detects sentiment, and flags potential food safety risks. The system helps the mess committee organise student feedback and allows the warden to identify urgent health-related complaints.

The application uses an LLM for classification and Python for validation, safety checks, counting, and report generation.

## 🎯 Objectives

- Automatically classify hostel mess feedback.
- Identify positive, negative, and neutral comments.
- Detect potential food hygiene and safety risks.
- Support English, Tamil, and Tanglish feedback.
- Generate organised reports for the mess committee and warden.
- Ensure reliable output through validation and a safety net.

## ⚙️ Technologies Used

- Python
- Large Language Model (LLM) API
- CSV Module
- JSON
- Exception Handling
- Git and GitHub
- VS Code

## 📂 Project Structure

```text
Mess-Feedback-Sorter/
│
├── feedback.csv
├── main.py
├── results.csv
├── urgent.csv
├── summary.txt
├── system_prompt.txt
├── README.md
├── .gitignore
│
├── specification/
├── testing/
├── reports/
└── reflection/
```

*The folder structure above is a suggested organisation; adjust it to match your actual repository files.*

## 🔍 How It Works

1. **Input:** Reads hostel mess feedback from `feedback.csv`.
2. **Classification:** Sends valid comments to the LLM.
3. **Parsing:** Extracts the JSON response.
4. **Validation:** Checks the required field names and allowed values.
5. **Retry:** Retries invalid responses once.
6. **Safety Net:** Checks health-risk keywords and ensures urgent feedback is flagged.
7. **Report Generation:** Generates three output files.

## 🏷️ Classification Categories

| Field | Allowed Values |
|---|---|
| Category | Taste, Hygiene, Quantity, Timing, Other |
| Sentiment | Positive, Negative, Neutral |
| Urgent | True, False |
| Summary | Maximum 12 words |

## 🚨 Safety Features

- Empty comments are sent directly for manual review.
- Invalid LLM responses are retried once.
- Failed validation results are marked for manual review.
- Health-risk keywords can automatically raise the urgency flag.
- The safety net never reduces urgency.
- A human decision-maker reviews every comment in `urgent.csv`.

## 📄 Output Files

| File | Description |
|---|---|
| `results.csv` | All feedback with classification labels |
| `urgent.csv` | Urgent feedback with original comments |
| `summary.txt` | Category counts, negative percentage, and urgent list |

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/saru-pixel/Mess-Feedback-Sorter.git
```

### 2. Open the project folder

```bash
cd Mess-Feedback-Sorter
```

### 3. Install required dependencies

Install the Python packages required by your implementation.

For example:

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Store your LLM API key in an environment variable or a local `.env` file. Never upload your API key to GitHub.

### 5. Run the program

```bash
python main.py
```

*Replace `main.py` or the installation commands if your actual project uses different filenames or dependencies.*

## 🧪 Testing

The project includes:

- Five evaluation test cases.
- Three red-team test cases.
- Instruction-hiding test.
- Tanglish feedback test.
- Empty comment test.
- JSON validation and retry testing.
- Urgent keyword safety-net testing.

## 👩‍⚖️ Human Judgment Framework

The system only classifies and organises feedback. It does not make decisions about disciplinary action or food safety responses.

**Human Checkpoint:** The warden reads every comment in `urgent.csv` and decides the appropriate action.

## 💡 Expected Benefits

- Saves time in manually reading feedback.
- Improves identification of potential food safety risks.
- Organises student feedback systematically.
- Supports multilingual feedback.
- Helps the mess committee understand recurring complaints.

## ⚠️ Limitations

- LLM classifications may not always be accurate.
- Keyword-based safety checks may miss unfamiliar expressions.
- Internet access may be required for API communication.
- Human verification is necessary before taking action.

## 👩‍🎓 Academic Information

**Institution:** Coimbatore Institute of Technology, Coimbatore

**Programme:** Five Years Integrated M.Sc. Artificial Intelligence and Machine Learning

**Programme:** CIT AI-Native Engineering Programme

**Semester:** 1

**Assessment:** Assessment 5 – Capstone Project

**Project Title:** Mess Feedback Sorter

## 📌 Conclusion

The Mess Feedback Sorter demonstrates how Python and Large Language Models can be combined to organise hostel mess feedback efficiently. By integrating structured classification, response validation, safety checks, and human oversight, the system supports better feedback management and responsible AI engineering.

---

**Developed as part of the CIT AI-Native Engineering Programme – Semester 1.**