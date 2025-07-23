from crewai import Task
from agents.quiz_agent import quiz_master

quiz_task = Task(
    description="Create 3 multiple choice questions from the summary created by the Summarizer.",
    expected_output="3 questions with 4 options each and one correct answer marked.",
    agent=quiz_master
)
