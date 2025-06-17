import openai
import config

# Set up OpenAI client
client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

# Load input text
def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Generate summary
def summarize_text(text):
    prompt = f"""
You are an expert academic assistant. Summarize the following academic text in three parts:
1. Bullet-point summary
2. Rewritten abstract
3. Key takeaways (in plain language for students)

Text:
{text}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("📘 Academic Paper Summarizer")
    text = load_text("sample.txt")
    result = summarize_text(text)
    print("\n📄 Summary Output:\n")
    print(result)
