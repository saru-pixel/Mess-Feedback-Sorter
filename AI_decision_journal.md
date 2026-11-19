# AI Decision Journal
## Mess Feedback Sorter

### 1. Project Objective
To classify hostel mess feedback into categories, identify sentiment, detect urgent health-related complaints, and generate reports.

### 2. AI Design Decisions

| Decision | Reason |
|---|---|
| Five categories | Organizes feedback clearly |
| Three sentiment labels | Identifies student opinions |
| JSON response format | Makes results easy to process |
| 12-word summary limit | Keeps summaries short |
| Urgency detection | Helps identify possible food safety issues |

### 3. Validation Decisions
- Used `parse_reply()` to read responses.
- Used `is_valid()` to check response structure.
- Added one retry for invalid responses.
- Sent invalid responses for manual review.

### 4. Safety Decisions
- Added a safety net for health-related keywords.
- The safety net can increase urgency but cannot reduce it.
- Empty feedback is sent for manual review.
- The warden must review every comment in `urgent.csv`.

### 5. Testing Decisions
- Created five evaluation tests.
- Created three red-team tests.
- All eight local tests passed.

### 6. Limitations
- The current version uses rule-based sample classification instead of a live LLM.
- Keyword detection may miss unfamiliar expressions.
- Human verification is necessary for important decisions.

### 7. Future Improvements
- Connect a real LLM API.
- Improve Tanglish understanding.
- Add more evaluation cases.
- Improve classification accuracy.
- Add a dashboard for wardens.

### 8. Final Decision
The system is designed to assist the mess management team. It should not make final food safety decisions without human review.