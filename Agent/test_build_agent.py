import os
import asyncio
from model import llm
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rich.console import Console
from rich.markdown import Markdown
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

console = Console()

async def main():
    user_topic = input("🧬 What ML Bioinformatics topic would you like to learn about today? ")
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
            except Exception as e:
                console.print(f"[bold red]Error during execution:[/bold red] {e}")

if __name__ == "__main__":
    asyncio.run(main())


