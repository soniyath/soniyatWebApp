from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Yatharth Soni - Sheridan!"

# For local testing only:
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
