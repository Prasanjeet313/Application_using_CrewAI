from crewai import Task
from agents.summarizer_agent import summarizer

lesson_text = """
Photosynthesis is the process by which green plants make their own food using sunlight, carbon dioxide, and water...
"""

summarization_task = Task(
    description=f"Summarize this content for a student:\n\n{lesson_text}",
    expected_output="A short paragraph summarizing the core process and significance of photosynthesis.",
    agent=summarizer
)
