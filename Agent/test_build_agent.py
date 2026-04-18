from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert {domain} consultant with 10+ years of experience."),
    ("human", "Provide a detailed analysis of: {topic} with a focus of educating users on machine learning concepts under bioinformatics tools.")
])

from model import llm

# Chain the prompt with the model
chain = prompt | llm

# Generate output with specific parameters
result = chain.invoke({
    "domain": "bioinformatics, computer science, computational biology",
    "topic": "can you explain to me what is a SVM, ML, BERT, and embedding?" # this can be the user input
})

print(result.content)