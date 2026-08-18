from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the AI model and tokenizer designed for analyzing code
MODEL_NAME = "microsoft/codebert-base"

print("Loading AI model... Please wait a moment.")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
print("AI Model loaded successfully!")

def scan_code(code_snippet: str):
    """
    Analyzes code to detect potential security vulnerabilities.
    """
    # 1. Convert source code text into numbers the AI understands
    inputs = tokenizer(code_snippet, return_tensors="pt", truncation=True, max_length=512)
    
    # 2. Pass the code through the AI model
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
    
    # 3. Read the AI's detection confidence
    vulnerable_prob = probabilities[0][1].item()
    is_vulnerable = vulnerable_prob > 0.5

    # Simple heuristic checks to tag common vulnerabilities
    detected_types = []
    lowered_code = code_snippet.lower()
    
    if "select " in lowered_code and "where" in lowered_code and "+" in lowered_code:
        detected_types.append("SQL Injection")
    if "strcpy" in lowered_code or "gets(" in lowered_code or "memcpy" in lowered_code:
        detected_types.append("Buffer Overflow")
    if "<script>" in lowered_code or "innerhtml" in lowered_code:
        detected_types.append("Cross-Site Scripting (XSS)")

    return {
        "is_vulnerable": is_vulnerable or len(detected_types) > 0,
        "risk_score": round(max(vulnerable_prob, 0.85 if detected_types else 0.1) * 100, 2),
        "vulnerability_types": detected_types if detected_types else (["Generic Risk"] if is_vulnerable else ["None Detected"]),
        "status": "DANGER: Security Risk Found!" if (is_vulnerable or detected_types) else "SAFE: No Vulnerabilities Detected"
    }

# Quick local test run
if __name__ == "__main__":
    test_code = "query = 'SELECT * FROM users WHERE username = ' + user_input"
    print("\nTesting Scanner with code sample...")
    result = scan_code(test_code)
    print(f"Status: {result['status']}")
    print(f"Risk Score: {result['risk_score']}%")
    print(f"Detected Risks: {', '.join(result['vulnerability_types'])}\n")