import pandas as pd
from langchain.llms import OpenAI
#from langchain.agents import create_pandas_dataframe_agent
from langchain_experimental.agents import create_pandas_dataframe_agent

def query_agent(data, query):

    df = pd.read_csv(data)
    llm = OpenAI()
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    # A Python shell used to evaluating and executing Python commands 
    return agent.run(query)