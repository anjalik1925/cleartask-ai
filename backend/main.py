from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import agent

app = FastAPI(title="ClearTask AI")

# ✅ CORS (required for frontend on Vercel/Lovable)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow all frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check (optional but useful)
@app.get("/")
def root():
    return {"status": "ClearTask AI backend running"}

# ✅ Main agent endpoint
@app.post("/plan")
async def create_plan(goal: str):
    result = await agent.run(goal)
    return result.data
