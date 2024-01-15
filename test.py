# from langchain.llms import OpenAI
# from langchain.chains import SingleTurn
# import os

# # Initialize the LLM with your API key
# llm = OpenAI(os.environ["OPENAI_API_KEY"])
# chain = SingleTurn(llm)

# def health_coach_conversation():
#     # Greeting and asking for the user's goal
#     response = chain.run("Hello! I'm your health coach. What is your fitness goal?")
#     print(response)

#     user_goal = None
#     while not user_goal:
#         user_input = input("Please tell me your fitness goal: ")
#         # Check if the user input is a valid goal
#         if is_valid_goal(user_input):
#             user_goal = user_input
#         else:
#             print("I didn't quite catch that. Could you please specify your fitness goal?")

#     # Once we have the goal, suggest 5 skills
#     skills_response = chain.run(f"To achieve the goal of '{user_goal}', you'll need to develop these skills: ")
#     print(skills_response)

#     # Continue the conversation
#     while True:
#         user_input = input("How can I assist you further? ")
#         if user_input.lower() == 'exit':
#             print("Goodbye! Remember to stay focused on your goals.")
#             break
#         response = chain.run(user_input)
#         print(response)

# def is_valid_goal(goal):
#     # Define criteria for a valid goal
#     # Modify this function based on your specific criteria for a valid fitness goal
#     return len(goal.split()) > 2  # Example: assuming a valid goal consists of more than two words

# # Main Execution
# if __name__ == "__main__":
#     health_coach_conversation()

# recommender_system.py
import os
import sys
from utils.readkey import set_env
set_env()

from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, AgentExecutor
from prompts.persona import PERSONA_TEMPLATE


# 1. Set up LangChain with your chosen LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"]) # Adjust model and temperature as needed

# 2. Define a function for the conversation flow
def health_coach_conversation():
    user_goal = None
    while not user_goal:
        greeting = llm("Greet the user and ask what their health goal is.")
        print(greeting)
        user_response = input("Enter your goal: ")
        if user_response.lower() != "":
            user_goal = user_response

    skills = llm(f"List 5 skills that are essential to achieve the goal of {user_goal}.")
    print("Here are 5 skills that will help you achieve your goal:")
    print(skills)

    # 3. Continue the conversation normally
    while True:
        user_input = input("What would you like to talk about? ")
        response = llm(user_input)
        print(response)

# 4. Start the conversation
health_coach_conversation()