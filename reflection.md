# Project Reflection – Mess Feedback Sorter

## Introduction

The Mess Feedback Sorter is a Python-based project designed to organize student feedback about hostel food. Its main purpose is to help mess management identify common complaints and recognize possible food safety issues.

## Project Development

During this project, I learned how to use Python to read CSV files, process feedback, classify comments, and generate reports. I divided the program into functions such as `classify()`, `parse_reply()`, `is_valid()`, `apply_safety_net()`, and `write_reports()`.

The program reads student comments from `feedback.csv` and organizes them into five categories: taste, hygiene, quantity, timing, and other. It also identifies sentiment as positive, negative, or neutral.

## Validation and Safety

One important part of the project was response validation. I used validation checks to ensure that classification results contained the required fields and correct data types.

I also implemented a safety net that identifies health-related keywords such as insect, hair, expired, and stone. This safety net can increase an urgency flag but cannot reduce it.

Empty or invalid feedback is directed for manual review. The warden must examine every complaint in `urgent.csv` before deciding what action to take.

## Testing

I created five evaluation tests to check the classification of different feedback comments. All five tests passed.

I also created three red-team tests covering hidden instructions, Tanglish feedback, and empty feedback. All three local tests passed, giving a total of eight successful tests.

## Challenges and Learning

Initially, I faced problems with Python setup, CSV reading, and report generation. I solved these issues by checking the input file, correcting the code, and testing the program repeatedly.

I learned the importance of modular programming, input validation, error handling, and human supervision.

## Limitations and Future Improvements

The current version uses rule-based sample classification rather than a live LLM API. Keyword-based classification may not understand every expression or context. In the future, I would like to connect a real LLM, improve Tanglish understanding, and develop a dashboard for mess management.

## Conclusion

This project helped me understand how AI-related concepts and Python programming can be applied to a practical problem. I also learned that automated systems should support human decisions rather than replace human judgment.