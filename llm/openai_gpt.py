import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def ask_llm(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that retrieves and analyzes cryptocurrency data."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

# Simulate interaction
def interact_with_llm(question):
    if "Bitcoin" in question:
        data = query_crypto_prices("Bitcoin")
    elif "Ethereum" in question:
        data = query_crypto_prices("Ethereum")
    else:
        return "I can only retrieve data for Bitcoin and Ethereum right now."

    analysis_prompt = f"The following data was retrieved from the database: {data}. Analyze this data and provide a summary."
    return ask_llm(analysis_prompt)

if __name__ == "__main__":
    question = "What is the latest price of Bitcoin?"
    print(interact_with_llm(question))
