import requests
import sseclient  # pip install sseclient-py
import json

REMOTE_IP = "52.25.231.171"
url = "http://52.25.231.171:5000/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

history = []

while True:
    user_message = input("> ")
    history.append({"role": "user", "content": user_message})
    data = {
        "mode": "instruct",
        "stream": True,
        "messages": history
    }

    stream_response = requests.post(url, headers=headers, json=data, verify=False, stream=True)
    client = sseclient.SSEClient(stream_response)

    assistant_message = ''
    for event in client.events():
        payload = json.loads(event.data)
        chunk = payload['choices'][0]['message']['content']
        assistant_message += chunk
        print(chunk, end='')

    print()
    history.append({"role": "assistant", "content": assistant_message})