from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/info")
def get_info():
    return {"service": "lobster-skills-test", "version": "v1.0.0", "env": "test"}


@app.get("/version")
def get_version():
    return {"version": "1.0.0", "env": "test"}


@app.get("/status")
def get_status():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": "lobster",
    }


@app.get("/summary")
def get_summary():
    return {
        "service": "lobster-skills-test",
        "version": "v1.0.0",
        "env": "test",
        "routes": ["/info", "/version", "/status", "/summary", "/ui"],
    }


@app.get("/ui", response_class=HTMLResponse)
def get_ui():
    return """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>Lobster Skills Test Dashboard</title>
  <style>
    body { background: #000; color: #0ff; font-family: monospace; padding: 2rem; }
    h1 { color: #0ff; border-bottom: 1px solid #0ff; padding-bottom: 0.5rem; }
    ul { list-style: none; padding: 0; }
    li { margin: 0.5rem 0; }
    a { color: #0f0; text-decoration: none; }
    a:hover { text-decoration: underline; }
    #status-box { margin-top: 2rem; padding: 1rem; border: 1px solid #0ff; white-space: pre; }
    h2 { color: #0ff; }
  </style>
</head>
<body>
  <h1>Lobster Skills Test Dashboard</h1>
  <h2>Available Routes</h2>
  <ul>
    <li><a href="/info">/info</a> — service info</li>
    <li><a href="/version">/version</a> — version</li>
    <li><a href="/status">/status</a> — status</li>
    <li><a href="/summary">/summary</a> — summary</li>
    <li><a href="/ui">/ui</a> — this page</li>
  </ul>
  <h2>/status Live</h2>
  <div id="status-box">載入中...</div>
  <script>
    fetch('/status')
      .then(r => r.json())
      .then(data => {
        document.getElementById('status-box').textContent = JSON.stringify(data, null, 2);
      })
      .catch(e => {
        document.getElementById('status-box').textContent = 'Error: ' + e;
      });
  </script>
</body>
</html>"""
