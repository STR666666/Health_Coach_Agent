import os
import re
import gradio as gr
from typing import List, Union
from utils.readkey import set_env
set_env()

# Importing langchain related modules
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.tools import DuckDuckGoSearchRun
from langchain.schema import AgentAction, AgentFinish
from langchain.chat_models import ChatOpenAI
from utils.tools import duck
from recommender.recommender_template import CustomPromptTemplate, CustomOutputParser
from prompts.persona import REACT_TEMPLATE
from recommender.recommender_agent import Recommender

# Set up the tools available to the agent
tools = [
    Tool(
        name="Search bodybuilding",
        func=duck,
        description="Useful for answering medical and pharmacological questions"
    )
]

output_parser = CustomOutputParser()
prompt = CustomPromptTemplate(
            template=REACT_TEMPLATE,
            tools=tools,
            input_variables=["input", "intermediate_steps"]
        )

# Setup for the agent and its execution
output_parser = CustomOutputParser()
llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"])
llm_chain = LLMChain(llm=llm, prompt=prompt)
tool_names = [tool.name for tool in tools]

agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=output_parser,
    stop=["\nObservation:"],
    allowed_tools=tool_names
)

agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

rec = Recommender()

# Greeting message for the chatbot
greeting = """
Start personalized your goal! And we can work towards it together!
"""

rec.agent_exec(agent_executor)

with gr.Blocks() as demo:
    gr.Markdown('# Health Coach Agent')
    gr.Markdown(greeting)
    with gr.Row():
        with gr.Column():
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Talk to me!")
            clear = gr.ClearButton([msg, chatbot])

        # When the user submits their message, process it and update the chatbot
        msg.submit(rec.respond_to_input, inputs=msg, outputs=[msg, chatbot])

# Launch the Gradio app
demo.launch()