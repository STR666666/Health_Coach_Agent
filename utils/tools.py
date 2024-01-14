from typing import List, Union
from utils.readkey import set_env
set_env()
from langchain.tools import DuckDuckGoSearchRun

def duck(input_text):
    # I can later compare which website provide better/higher accuracy. Also, based on user preference, I need to personalize the plan for each individual.
    search = DuckDuckGoSearchRun()
    search_results = search.run(f"site:bodybuilding.com {input_text}")
    return search_results