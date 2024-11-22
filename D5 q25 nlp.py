import openai

openai.api_key = "your_api_key_here"

prompt = "Write a story about a brave knight."

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100
)

print(response.choices[0].text.strip())
