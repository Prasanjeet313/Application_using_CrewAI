from crewai import Crew
from agents.summarizer_agent import summarizer
from agents.quiz_agent import quiz_master
from agents.tagger_agent import tagger
from agents.learning_path_agent import learning_path_agent

from tasks.summarization_task import summarization_task
from tasks.quiz_task import quiz_task
from tasks.tagger_task import tagging_task
from tasks.learning_path_task import learning_path_task

crew = Crew(
    agents=[
        summarizer,
        quiz_master,
        tagger,
        learning_path_agent
    ],
    tasks=[
        summarization_task,
        quiz_task,
        tagging_task,
        learning_path_task
    ],
    verbose=True
)
