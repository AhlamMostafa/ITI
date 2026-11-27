import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API Key not found! Check your .env file.")


client = OpenAI(api_key=api_key)
MODEL = "gpt-6-luna"
INPUT_PRICE = 0.10
OUTPUT_PRICE = 0.50
user_message = input("Enter your question: ")

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    ai_answer = response.choices[0].message.content

    print("\nAI RESPONSE")
    print(ai_answer)


    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens

    input_cost = (prompt_tokens / 1_000_000) * INPUT_PRICE
    output_cost = (completion_tokens / 1_000_000) * OUTPUT_PRICE
    total_cost = input_cost + output_cost

    print("\nTOKEN ANALYSIS")
    print(f"Model: {MODEL}")
    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Completion Tokens: {completion_tokens}")
    print(f"Total Tokens: {total_tokens}")

    print("\nCOST ANALYSIS")
    print(f"Input Cost: {input_cost:.8f}")
    print(f"Output Cost: {output_cost:.8f}")
    print(f"Total Cost: {total_cost:.8f}")

except Exception as error:
    print(f"An error occurred: {error}")
