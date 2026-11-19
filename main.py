
import csv
import re
from pathlib import Path
from collections import Counter


# ==========================================
# 1. PROJECT SETTINGS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "feedback.csv"
RESULTS_FILE = BASE_DIR / "results.csv"
URGENT_FILE = BASE_DIR / "urgent.csv"
SUMMARY_FILE = BASE_DIR / "summary.txt"

CATEGORIES = ["taste", "hygiene", "quantity", "timing", "other"]
SENTIMENTS = ["positive", "negative", "neutral"]

HEALTH_WORDS = [
    "insect", "hair", "expired", "fell sick",
    "poochi", "mudi", "spoiled", "foreign object",
    "stone"
]

# ==========================================
# 2. CLASSIFY FEEDBACK
# ==========================================

def classify(comment):

    text = comment.lower()

    # Hygiene-related feedback
    if any(word in text for word in HEALTH_WORDS):
        category = "hygiene"
        sentiment = "negative"
        urgent = True

    # Quantity-related feedback
    elif any(word in text for word in [
        "quantity", "less food", "too little"
    ]):
        category = "quantity"
        sentiment = "negative"
        urgent = False

    # Timing-related feedback
    elif any(word in text for word in [
        "late", "delay", "time"
    ]):
        category = "timing"
        sentiment = "negative"
        urgent = False

    # Positive food feedback
    elif any(word in text for word in [
        "tasty", "delicious", "good", "excellent"
    ]):
        category = "taste"
        sentiment = "positive"
        urgent = False

    # Other feedback
    else:
        category = "taste"
        sentiment = "negative"
        urgent = False

    return {
        "category": category,
        "sentiment": sentiment,
        "urgent": urgent,
        "summary": comment[:100]
    }


# ==========================================
# 3. PARSE RESPONSE
# ==========================================

def parse_reply(reply):

    if isinstance(reply, dict):
        return reply

    try:
        import json
        return json.loads(reply)

    except (ValueError, TypeError):
        return None


# ==========================================
# 4. VALIDATE RESPONSE
# ==========================================

def is_valid(data):

    if not isinstance(data, dict):
        return False

    required_fields = {
        "category", "sentiment", "urgent", "summary"
    }

    if set(data.keys()) != required_fields:
        return False

    if data["category"] not in CATEGORIES:
        return False

    if data["sentiment"] not in SENTIMENTS:
        return False

    if type(data["urgent"]) != bool:
        return False

    if not isinstance(data["summary"], str):
        return False

    if not data["summary"].strip():
        return False

    if len(data["summary"].split()) > 12:
        return False

    return True


# ==========================================
# 5. APPLY SAFETY NET
# ==========================================

def apply_safety_net(comment, data):

    for word in HEALTH_WORDS:

        pattern = r"(?<!\w)" + re.escape(word) + r"(?!\w)"

        if re.search(pattern, comment, re.IGNORECASE):
            data["urgent"] = True
            break

    return data


# ==========================================
# 6. WRITE REPORTS
# ==========================================

def write_reports(results):

    fields = [
        "id", "date", "meal", "comment",
        "category", "sentiment", "urgent",
        "summary", "needs_manual_review"
    ]

    # Save all feedback
    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    # Save urgent feedback
    with open(URGENT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for item in results:
            if item["urgent"]:
                writer.writerow(item)

    # Create summary
    total = len(results)

    category_counts = Counter(
        item["category"] for item in results
        if not item["needs_manual_review"]
    )

    sentiment_counts = Counter(
        item["sentiment"] for item in results
        if not item["needs_manual_review"]
    )

    urgent_count = sum(item["urgent"] for item in results)
    manual_count = sum(item["needs_manual_review"] for item in results)

    with open(SUMMARY_FILE, "w", encoding="utf-8") as file:

        file.write("MESS FEEDBACK SUMMARY\n")
        file.write("=====================\n\n")

        file.write(f"Total feedback: {total}\n")
        file.write(f"Urgent feedback: {urgent_count}\n")
        file.write(f"Manual review: {manual_count}\n\n")

        file.write("CATEGORY COUNTS\n")

        for category in CATEGORIES:
            file.write(
                f"{category}: {category_counts[category]}\n"
            )

        file.write("\nSENTIMENT COUNTS\n")

        for sentiment in SENTIMENTS:
            file.write(
                f"{sentiment}: {sentiment_counts[sentiment]}\n"
            )

        percentage = (
            urgent_count / total * 100 if total else 0
        )

        file.write(
            f"\nUrgent feedback percentage: {percentage:.2f}%\n"
        )


# ==========================================
# 7. PROCESS FEEDBACK
# ==========================================

def main():

    results = []

    if not INPUT_FILE.exists():
        print("Error: feedback.csv was not found!")
        return

    with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("Error: CSV file has no column headings!")
            return

        # Normalize column headings
        reader.fieldnames = [
            name.strip().lower() for name in reader.fieldnames
        ]

        if "comment" not in reader.fieldnames:
            print("Error: No 'comment' column found!")
            print("Columns found:", reader.fieldnames)
            return

        for row in reader:

            # Normalize row keys and values
            row = {
                str(key).strip().lower(): (
                    value.strip() if isinstance(value, str) else value
                )
                for key, value in row.items()
                if key is not None
            }

            comment = row.get("comment") or ""

            print("Processing:", comment)

            # Empty feedback goes for manual review
            if not comment.strip():

                results.append({
                    "id": row.get("id", ""),
                    "date": row.get("date", ""),
                    "meal": row.get("meal", ""),
                    "comment": "",
                    "category": "other",
                    "sentiment": "neutral",
                    "urgent": False,
                    "summary": "Empty feedback",
                    "needs_manual_review": True
                })

                continue

            # Classify feedback
            reply = classify(comment)

            parsed_data = parse_reply(reply)

            # Retry once if invalid
            if not is_valid(parsed_data):
                reply = classify(comment)
                parsed_data = parse_reply(reply)

            # Manual review if still invalid
            if not is_valid(parsed_data):

                results.append({
                    "id": row.get("id", ""),
                    "date": row.get("date", ""),
                    "meal": row.get("meal", ""),
                    "comment": comment,
                    "category": "other",
                    "sentiment": "neutral",
                    "urgent": False,
                    "summary": "Could not classify",
                    "needs_manual_review": True
                })

                continue

            # Apply safety net
            final_data = apply_safety_net(
                comment, parsed_data
            )

            results.append({
                "id": row.get("id", ""),
                "date": row.get("date", ""),
                "meal": row.get("meal", ""),
                "comment": comment,
                "category": final_data["category"],
                "sentiment": final_data["sentiment"],
                "urgent": final_data["urgent"],
                "summary": final_data["summary"],
                "needs_manual_review": False
            })

    # Generate reports
    write_reports(results)

    print("\nFeedback processing completed!")
    print("Total comments processed:", len(results))
    print("Reports generated:")
    print("1. results.csv")
    print("2. urgent.csv")
    print("3. summary.txt")


# ==========================================
# 8. RUN PROJECT
# ==========================================

if __name__ == "__main__":
    main()
