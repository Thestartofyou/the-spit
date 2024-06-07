import openai

# Function to get the most talked about penny stocks
def get_most_talked_about_penny_stocks(api_key, query="most talked about penny stocks"):
    openai.api_key = api_key
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that provides the most talked-about penny stocks."},
            {"role": "user", "content": query}
        ]
    )
    
    # Extract the response text
    response_text = response['choices'][0]['message']['content']
    
    # Extracting the top 6 mentioned penny stocks from the response
    # (Assuming the response is in a list format)
    penny_stocks = response_text.split('\n')[:6]
    
    return penny_stocks

# Example usage
if __name__ == "__main__":
    api_key = "your-openai-api-key"
    penny_stocks = get_most_talked_about_penny_stocks(api_key)
    for i, stock in enumerate(penny_stocks, start=1):
        print(f"{i}. {stock}")
