from crewai import Agent
import os
from crewai import LLM

llm = LLM(
  model='gemini/gemini-2.5-pro',
  api_key=os.getenv("GOOGLE_API_KEY")
)

learning_path_agent = Agent(
    role="Learning Path Planner",
    goal="Create a logical learning path based on content difficulty",
    backstory="Specialist in sequencing educational content for gradual mastery.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)
