from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from scanner import scan_code

app = FastAPI(title="AI Code Security Scanner")

def get_html_page(code: str = "", result_html: str = "") -> str:
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Code Security Scanner</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f8; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        textarea {{ width: 100%; height: 180px; font-family: monospace; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }}
        button {{ background-color: #007bff; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-top: 10px; }}
        button:hover {{ background-color: #0056b3; }}
        .result {{ margin-top: 20px; padding: 15px; border-radius: 5px; }}
        .danger {{ background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }}
        .safe {{ background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>🛡️ AI Code Vulnerability Scanner</h2>
        <p>Paste your Python, C++, or JS code below to check for security bugs:</p>
        <form method="post" action="/scan">
            <textarea name="code" placeholder="Paste code here...">{code}</textarea><br>
            <button type="submit">Scan Code</button>
        </form>
        {result_html}
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return get_html_page()

@app.post("/scan", response_class=HTMLResponse)
async def scan(request: Request):
    form_data = await request.form()
    code = form_data.get("code", "")
    
    result = scan_code(code)
    css_class = "danger" if result["is_vulnerable"] else "safe"
    
    result_html = f"""
    <div class="result {css_class}">
        <h3>{result['status']}</h3>
        <p><strong>Risk Score:</strong> {result['risk_score']}%</p>
        <p><strong>Detected Vulnerabilities:</strong> {', '.join(result['vulnerability_types'])}</p>
    </div>
    """
    return get_html_page(code=code, result_html=result_html)