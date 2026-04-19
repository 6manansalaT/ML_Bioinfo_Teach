from langchain_core.prompts import ChatPromptTemplate
from rich.console import Console
from rich.markdown import Markdown

def build_agent(user_question):

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert {domain} consultant with 10+ years of experience."),
        ("human", "Provide a detailed analysis of: {topic} with a focus of educating users on machine learning concepts under bioinformatics tools.")
    ])

    from Agent.model import llm

    # Chain the prompt with the model
    chain = prompt | llm

    # Generate output with specific parameters
    result = chain.invoke({
        "domain": "bioinformatics, computer science, computational biology, machine learning",
        "topic": user_question
    })

    if isinstance(result.content,list):
        #join text blocks to avoid text cut off
        full_text = "".join([block['text'] for block in result.content if block['type'] == 'text'])
    else: 
        full_text = result.content

    # print with rich
    console = Console(record=True)
    console.print(Markdown(full_text))
    res_string = console.export_text()

    return res_string