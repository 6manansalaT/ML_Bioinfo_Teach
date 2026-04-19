import os
from Agent.model import llm
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rich.console import Console
from rich.markdown import Markdown
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

'''
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
'''

console = Console(record=True)

async def main(user_topic):
    instruction = (
        f"Explain the machine learning concepts behind {user_topic}. "
        "Find 2-3 peer-reviewed relevant papers on PubMed to illustrate "
        "how this is used in real Bioinformatics research and in recent applications."
        )

    # 1. pubmed MCP server (IO transfer)
    server_params = StdioServerParameters(
        command = "npx",
        args = ["-y", "@cyanheads/pubmed-mcp-server"],
        env = os.environ.copy()
    )
    # 2. load MCP server tools
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            mcp_tools = await load_mcp_tools(session)
            system_prompt = """You are an expert Bioinformatics AI Tutor.
Help the user understand Machine Learning concepts in Bioinformatics.
Always cite real papers from PubMed when explaining a topic.
Explain clearly and accurately, and keep the response educational."""

            agent = create_agent(
                model=llm,
                tools=mcp_tools,
                system_prompt=system_prompt,
            )

            
            try:
                result = await agent.ainvoke(
                    {
                        "messages": [
                            {"role": "user", "content": instruction}
                        ]
                    }
                )
                console.print("\n[bold green]--- Study Results ---[/bold green]")
                final_message = result["messages"][-1].text
                console.print(Markdown(final_message))
                res_string = console.export_text()
                return res_string

            except Exception as e:
                console.print(f"[bold red]Error during execution:[/bold red] {e}")
