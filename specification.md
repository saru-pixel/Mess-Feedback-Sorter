# MESS FEEDBACK SORTER
### Project Specification
**CIT AI-Native Engineering Programme – Semester 1**

## 1. Problem Statement
The hostel mess committee receives many student food feedback comments in English, Tamil and Tanglish. Reading every comment manually takes time. Important hygiene complaints may be missed among ordinary food complaints.

## 2. Project Objective
To develop a console-based Python application that uses a Large Language Model (LLM) to classify student feedback, identify possible health risks and generate reports automatically.

## 3. Input Specification
The application reads a CSV file named `feedback.csv`.

The CSV contains four fields:
- id – Unique feedback ID
- date – Feedback date
- meal – Breakfast, Lunch or Dinner
- comment – Original student feedback

The input file contains at least 20 comments.

## 4. LLM Output Specification
For every non-empty comment, the LLM must return valid JSON with exactly four fields:

- category: taste, hygiene, quantity, timing or other
- sentiment: positive, negative or neutral
- urgent: true or false
- summary: A short description containing 12 words or fewer

## 5. Urgency Rules
A comment is urgent only when it indicates a possible food health risk, such as:
- Foreign objects in food
- Insects or hair in food
- Expired food
- Stale or spoiled food
- Someone falling sick after eating

Ordinary taste, quantity and timing complaints are never urgent, regardless of how strongly they are expressed.

## 6. Python Validation Rules
The Python program checks every LLM response.

- Check that all four field names are correct.
- Check that all values follow the allowed rules.
- Retry once if the response is invalid.
- If the second response is invalid, mark it as `needs_manual_review`.
- Empty comments are sent directly to manual review without calling the LLM.

## 7. Safety Net
Python checks the original comment for health-risk keywords such as insect, hair, expired, fell sick, poochi and mudi.

If a health-risk keyword is detected, the urgent field is set to true, even if the LLM returns false.

The safety net can increase urgency but must never reduce it.

## 8. Output Files
The application generates three files:

1. `results.csv` – Contains every feedback comment and its classification labels.
2. `urgent.csv` – Contains only urgent comments along with their original text.
3. `summary.txt` – Contains category counts, percentage of negative comments and the urgent feedback list.

## 9. Human Responsibility
The application only labels and sorts feedback. It does not make final decisions.

The warden reads every comment in `urgent.csv`, verifies the concern and decides what action should be taken. The mess committee reviews the overall feedback summary.

## 10. Expected Outcome
The project aims to reduce manual feedback sorting, identify potential food safety concerns more quickly and help the mess committee understand student feedback efficiently.