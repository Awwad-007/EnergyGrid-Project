from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI()

# Simple in-memory state
state = {"step": 0, "grid_load": 0.5, "done": False}

class Action(BaseModel):
    action_type: str        # e.g. "increase_load", "decrease_load", "balance"
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
    # Simple reward: closer to 0.5 load = better
    if action.action_type == "balance":
        state["grid_load"] = 0.5
        reward = 1.0
    elif action.action_type == "increase_load":
        state["grid_load"] = min(1.0, state["grid_load"] + action.value)
        reward = -0.2
    else:
        state["grid_load"] = max(0.0, state["grid_load"] - action.value)
        reward = -0.1

    done = state["step"] >= 5
    state["done"] = done
    return {
        "observation": {"grid_load": state["grid_load"], "step": state["step"]},
        "reward": round(reward, 2),
        "done": done,
        "info": {}
    }

@app.get("/health")
def health():
    return {"status": "healthy"}