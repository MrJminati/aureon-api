import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# ✅ Use Railway dynamic port
PORT = int(os.environ.get("PORT", 8080))

# ✅ In-memory storage (we will upgrade this later to DB)
signals = []

# ✅ CORS (allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check route
@app.get("/")
def home():
    return {"status": "API running"}

# ✅ Get signals
@app.get("/signals")
def get_signals():
    return signals

# ✅ Add signal (from bot)
@app.post("/add_signal")
def add_signal(data: dict):
    try:
        signals.append(data)
        return {"status": "added"}
    except Exception as e:
        return {"error": str(e)}

# ✅ IMPORTANT: Start server correctly for Railway
if __name__ == "__main__":
    print(f"🚀 Starting server on port {PORT}")
    uvicorn.run("server:app", host="0.0.0.0", port=PORT)
