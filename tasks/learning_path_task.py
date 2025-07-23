from crewai import Task
from agents.learning_path_agent import learning_path_agent

learning_path_task = Task(
    description="Create a structured learning path for the given topic using curated educational content.",
    expected_output="A detailed, step-by-step learning roadmap in markdown format.",
    agent=learning_path_agent
)
