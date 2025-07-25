from openai import OpenAI

def think(api_key, content, model = "gpt-4"):
    client = OpenAI(api_key = api_key)
    
    newline = "\n"
    user_prompt = (
    "Summarize this repo:\n" +
    newline.join([f"{key}: {value}" for key, value in content.items()]) +
    f"\n\nREADME: {content.get('readme', 'README not available')}"
    )
    
    response = client.chat.completions.create(
        model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant tasked with summarizing respositories based on the following information. Focus on strengths and weaknesses so they can be compared."},
            {"role": "user", "content": user_prompt}
        ]
    )

    summary = response.choices[0].message.content
    
    return summary

def compare(api_key):
    pass