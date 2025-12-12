
import ollama
res = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": "hi"}]
)

print(res)
