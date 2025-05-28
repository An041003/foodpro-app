from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Gợi ý 3 bài tập giảm mỡ cho nam BMI 27"}
    ],
)

print(response.choices[0].message.content)
