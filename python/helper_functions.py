from openai import OpenAI

client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key=""
)

def print_llm_response(prompt):
    response=get_llm_response(prompt)
    print(response)
    
def get_llm_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3:8b-instruct-q2_K",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

