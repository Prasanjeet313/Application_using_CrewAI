from crewai import Agent
from crewai import LLM
import os
llm = LLM(
  model='gemini/gemini-2.5-pro',
  api_key=os.getenv("GOOGLE_API_KEY")
)

summarizer = Agent(
    role="Summarizer",
    goal="Summarize educational content clearly",
    backstory="Expert at breaking down complex topics for students.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)
