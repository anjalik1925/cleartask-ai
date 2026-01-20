from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import generate_plan

app = FastAPI()

# CORS (frontend allowed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://clear-plan-git-main-anjali-kumaris-projects-6faf437e.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Models ----------
class PlanRequest(BaseModel):
    goal: str

# ---------- Routes ----------

# Health check ONLY
@app.get("/")
def health():
    return {"status": "ClearTask AI backend running"}

# REAL API (this is what frontend uses)
@app.post("/plan")
def plan(req: PlanRequest):
    result = generate_plan(req.goal)

    return {
        "goal": result["goal"],
        "tasks": result["tasks"],
        "confidence": result["confidence"],
    }
