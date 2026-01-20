from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent

load_dotenv()

class Task(BaseModel):
    title: str
    duration_minutes: int
    priority: str

class Plan(BaseModel):
    goal: str
    tasks: List[Task]
    confidence: float

agent = Agent(
    model="openrouter:mistralai/mistral-7b-instruct",
    output_type=Plan,
    system_prompt=(
        "You are a planning AI agent. "
        "Break goals into realistic tasks with time and priority."
    ),
)

# 🔹 ADD THIS FUNCTION
def generate_plan(goal: str) -> dict:
    result = agent.run_sync(goal)
    return result.model_dump()
