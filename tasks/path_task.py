from crewai import Task

def path_task(agent, content):
    return Task(
        description="Based on the following lesson content, suggest a 3-step learning path that builds on this material:\n\n" + content,
        agent=agent,
        expected_output="A 3-step learning plan with brief explanations."
    )
