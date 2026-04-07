from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI()

# THE FIX: Bypasses the 403 Forbidden wall for the Scaler bot
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {"step": 0, "grid_load": 0.5, "done": False}

class Action(BaseModel):
    action_type: str
    value: Optional[float] = 0.0

@app.get("/")
def home():
    return {"status": "Smart Grid API is Live"}

@app.post("/reset")
def reset(body: dict = {}):
    state["step"] = 0
    state["grid_load"] = round(random.uniform(0.3, 0.8), 2)
    state["done"] = False
    return {
        "observation": {"grid_load": state["grid_load"], "step": 0},
        "reward": 0.0,
        "done": False,
        "info": {}
    }

@app.post("/step")
def step(action: Action):
    state["step"] += 1
    if action.action_type == "balance":
        state["grid_load"] = 0.5
        reward = 1.0
    else:
        state["grid_load"] = max(0.0, state["grid_load"] - 0.1)
        reward = -0.1
    done = state["step"] >= 5
    return {
        "observation": {"grid_load": state["grid_load"], "step": state["step"]},
        "reward": round(reward, 2),
        "done": done,
        "info": {}
    }