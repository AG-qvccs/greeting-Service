from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_location(ip: str) -> dict:
    r = requests.get(f"https://ipapi.co/{ip}/json/")
    r.raise_for_status()
    return r.json()

@app.route("/greet", methods=["GET"])
def greet():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0].strip()
    location = get_location(ip)
    city = location.get("city", "Unknown City")
    country = location.get("country_name", "Unknown Country")
    return jsonify({
        "message": f"Hello! You're connecting from {city}, {country}.",
        "ip": ip,
        "city": city,
        "country": country
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

4. Click **Commit changes → Commit directly to main**

---

## Step 3: Create `requirements.txt`

1. Click **Add file → Create new file**
2. Name it `requirements.txt`
3. Paste:
```
flask
requests
