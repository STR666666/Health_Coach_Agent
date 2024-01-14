import os
import sys
from typing import List, Union
from utils.readkey import set_env
set_env()

from langchain.tools import DuckDuckGoSearchRun
from serpapi.google_search import GoogleSearch
cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

MAX_TRY = 10
from utils.readkey import set_env

set_env()

def duck(input_text):
    # I can later compare which website provide better/higher accuracy. Also, based on user preference, I need to personalize the plan for each individual.
    search = DuckDuckGoSearchRun()
    search_results = search.run(f"{input_text}")
    return search_results

def google_search(query):
    params = {
        "engine": "google",
        "q": f"{query}",
        "api_key": os.environ["SERPAPI_API_KEY"]
    }
    for _ in range(MAX_TRY):
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
        except BaseException:
            continue
        break
    return results
