import json
import requests
import time

MODEL = "deepseek-r1:8b"
API_URL = "http://localhost:11434/api/chat"

messages = [
    {"role": "system", "content": "Visada atsakinėk lietuviškai."}
]

def chat(prompt):
    messages.append({"role": "user", "content": prompt})
    response = requests.post(API_URL, json={
        "model": MODEL,
        "messages": messages
    }, stream=True)

    full_reply = ""
    for line in response.iter_lines():
        if line:
            obj = json.loads(line.decode("utf-8"))
            if "message" in obj and "content" in obj["message"]:
                content = obj["message"]["content"]
                print(content, end="", flush=True)
                full_reply += content

    messages.append({"role": "assistant", "content": full_reply})
    print()  # for newline after the message
    return full_reply

def preload_model():
    while True:
        try:
            response = requests.post("http://localhost:11434/api/chat", json={
                "model": "deepseek-r1:8b",
                "messages": [
                    {"role": "system", "content": "Visada atsakinėk lietuviškai."},
                    {"role": "user", "content": "Labas"}
                ]
            }, stream=True)

            for line in response.iter_lines():
                if not line:
                    continue
                obj = json.loads(line.decode("utf-8"))
                if "message" in obj:
                    print("✅ Modelis paruoštas naudoti.")
                    return True

        except requests.exceptions.ConnectionError:
            print("⏳ Ollama serveris dar nepasiekiamas...")
        except json.JSONDecodeError as e:
            print("⚠️ JSON klaida:", e)

        time.sleep(1)

def main():
    print("🔄 Įkeliu modelį į atmintį...")
    preload_model()  # Block until model is ready

    print("\n💬 Pokalbis su DeepSeek (Lietuviškai). Įveskite 'exit' išeiti.\n")
    while True:
        prompt = input("🧍 Jūs: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        reply = chat(prompt)
        print("🤖 DeepSeek:", reply)

if __name__ == "__main__":
    main()