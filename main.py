from crew_config.crew import crew

import os
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    result = crew.kickoff()
    print("\n\nFinal Crew Output:\n", result)
