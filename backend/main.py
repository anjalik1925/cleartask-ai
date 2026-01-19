from fastapi import FastAPI
from agent import agent

app = FastAPI(title="ClearTask AI")

@app.post("/plan")
async def create_plan(goal: str):
    result = await agent.run(goal)
    return result.data
