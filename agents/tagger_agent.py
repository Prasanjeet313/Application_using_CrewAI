from crewai import Agent
from crewai import LLM
import os
llm = LLM(
  model='gemini/gemini-2.5-pro',
  api_key=os.getenv("GOOGLE_API_KEY")
)

tagger = Agent(
    role="Content Tagger",
    goal="Generate relevant tags for content",
    backstory="Expert in tagging content for discoverability.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)
