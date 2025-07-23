from crewai import Task
from agents.tagger_agent import tagger

tagging_task = Task(
    description="Generate 5 relevant hashtags based on the content summary and quiz.",
    expected_output="#photosynthesis, #biology, #greenplants, #science, #chlorophyll",
    agent=tagger
)
