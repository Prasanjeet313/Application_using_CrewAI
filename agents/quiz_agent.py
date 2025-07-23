from crewai import Agent
from crewai import LLM
import os
llm = LLM(
  model='gemini/gemini-2.5-pro',
  api_key=os.getenv("GOOGLE_API_KEY")
)

quiz_master = Agent(
    role="Quiz Master",
    goal="Create short multiple choice quizzes",
    backstory="Creates effective MCQs for students based on content.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)
