from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MORAD KING</title>
<style>
body {
    margin: 0;
    background: #080d18;
    color: white;
    font-family: Arial;
    text-align: center;
}
header {
    padding: 65px 15px;
    background: linear-gradient(135deg,#111d36,#153c65);
}
h1 { color: #00d9ff; font-size: 40px; }
.card {
    margin: 30px auto;
    padding: 30px;
    max-width: 450px;
    background: #121d30;
    border-radius: 18px;
}
button {
    background: #00bfe8;
    border: 0;
    padding: 14px 30px;
    border-radius: 10px;
    cursor: pointer;
}
</style>
</head>
<body>
<header>
<h1>MORAD KING</h1>
<p>مرحباً بك في موقعي الرسمي</p>
</header>
<div class="card">
<h2>من نحن؟</h2>
<p>هذا الموقع الرسمي الخاص بـ MORAD KING.</p>
<button onclick="alert('Welcome to MORAD KING!')">
اضغط هنا
</button>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
