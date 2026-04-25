from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

signals = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API running"}

@app.get("/signals")
def get_signals():
    return signals

@app.post("/add_signal")
def add_signal(data: dict):
    signals.append(data)
    return {"status": "added"}
