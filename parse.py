from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template for extracting specific information from the text content
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the OllamaLLM model
model = OllamaLLM(model="llama3.2:1b")

def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt template from the provided template
    prompt = ChatPromptTemplate.from_template(template)
    
    # Create a chain of the prompt and model
    chain = prompt | model
    
    # List to store the parsed results
    parsed_result = []
    
    # Iterate over each chunk of DOM content
    for i, chunk in enumerate(dom_chunks, start=1):
        # Invoke the chain with the current chunk and parse description
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        
        # Print a message indicating the progress of parsing
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        
        # Append the response to the parsed results list
        parsed_result.append(response)
    
    # Join the parsed results into a single string and return
    return "\n".join(parsed_result)