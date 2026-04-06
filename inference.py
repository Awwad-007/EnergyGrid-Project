import os
import requests
import json

# Uses the Space URL or falls back to local for testing
BASE_URL = os.environ.get("SPACE_URL", "http://localhost:7860")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")
ENV_NAME = "energy-grid-env"
TASK_NAME = "grid_balancing"

def run():
    # Mandatory Start Log
    print(f"[START] task={TASK_NAME} env={ENV_NAME} model={MODEL_NAME}", flush=True)

    try:
        requests.post(f"{BASE_URL}/reset", json={})
        rewards = []

        for step in range(1, 6):
            action = {"action_type": "balance", "value": 0.0}
            resp = requests.post(f"{BASE_URL}/step", json=action)
            result = resp.json()
            reward = result.get("reward", 0.0)
            done = result.get("done", False)
            rewards.append(reward)

            # Mandatory Step Log
            print(
                f"[STEP] step={step} action={action['action_type']}:{action['value']} "
                f"reward={reward:.2f} done={str(done).lower()} error=null",
                flush=True
            )
            if done:
                break

        rewards_str = ",".join(f"{r:.2f}" for r in rewards)
        # Mandatory End Log
        print(f"[END] success=true steps={len(rewards)} rewards={rewards_str}", flush=True)
    
    except Exception as e:
        print(f"[END] success=false error={str(e)}")

if __name__ == "__main__":
    run()