from langchain.llms import OpenAI
from langchain.chains import SingleTurn
import os

# Initialize the LLM with your API key
llm = OpenAI(os.environ["OPENAI_API_KEY"])
chain = SingleTurn(llm)

def health_coach_conversation():
    # Greeting and asking for the user's goal
    response = chain.run("Hello! I'm your health coach. What is your fitness goal?")
    print(response)

    user_goal = None
    while not user_goal:
        user_input = input("Please tell me your fitness goal: ")
        # Check if the user input is a valid goal
        if is_valid_goal(user_input):
            user_goal = user_input
        else:
            print("I didn't quite catch that. Could you please specify your fitness goal?")

    # Once we have the goal, suggest 5 skills
    skills_response = chain.run(f"To achieve the goal of '{user_goal}', you'll need to develop these skills: ")
    print(skills_response)

    # Continue the conversation
    while True:
        user_input = input("How can I assist you further? ")
        if user_input.lower() == 'exit':
            print("Goodbye! Remember to stay focused on your goals.")
            break
        response = chain.run(user_input)
        print(response)

def is_valid_goal(goal):
    # Define criteria for a valid goal
    # Modify this function based on your specific criteria for a valid fitness goal
    return len(goal.split()) > 2  # Example: assuming a valid goal consists of more than two words

# Main Execution
if __name__ == "__main__":
    health_coach_conversation()
