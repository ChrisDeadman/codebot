# 🤖 Codebot: An Interactive Code Assistant

Codebot is a Python-based interactive code assistant that leverages OpenAI's ChatCompletion API to help users write and execute code snippets.
Users can chat with the assistant, ask questions, and receive responses in the form of code and explanations.
The application automatically detects code blocks within the response, executes them, and displays the results to the user.

**Note:** This application requires an OpenAI API key. Please follow OpenAI's guidelines for usage and safety.

## 🌟 Key features

- Chat-like interaction with GPT-3.5 Turbo using OpenAI's API
- Automatic detection and execution of code blocks within the AI's response
- Colored output for improved readability
- Message history managed using a cyclic buffer for efficient token count management
- Option to reset or clear the conversation history
- Easy to set up with a local server for code execution

## 📦 Build and run `python-executor` container

```
# build
docker build -t deads-inc/python-executor python-executor

# run
docker run --rm -d -p 8080:8080 -v ./data:/data --name python-executor deads-inc/python-executor

# test
curl -X POST -H "Content-Type: text/plain" -d $'print(1+2)' http://localhost:8080/execute
```

## 🛠️ Prepare Codebot Environment

```
# create venv
python -m venv .venv --system-site-packages

# activate venv
source .venv/bin/activate

# install dependencies
pip install -r codebot/requirements.txt

# configure openai API key
echo "your_api_key" > data/openai_api_key.txt
```

## 🏃‍♀️ Run Codebot

`python codebot/codebot.py`

## 💡Usage Examples

### Hello World

**You: Print "Hello, World!"**

_Sure, here's a simple Python code to print "Hello, World!" to the console:_

```
print("Hello, World!")
```

`Output: Hello, World!`

### OpenAI Completion

**You: Please start a conversation with openai and print the response. Read the API key from `openai_api_key.txt`.**

_Sure, I can help you with that. To read the API key from `openai_api_key.txt`, I need to check if the file exists and then read the contents from it. Here's the code:_

```
import os
import openai

with open('openai_api_key.txt') as f:
    api_key = f.read().strip()

# Now we can use the API key to start a conversation with OpenAI
openai.api_key = api_key
response = openai.Completion.create(
    engine="davinci",
    prompt="Hello, how are you today?",
    max_tokens=20
)

print(response.choices[0].text.strip())
```

_Make sure to add your API key in the `openai_api_key.txt` file for this code to work. After running it, you should see a response from OpenAI to the prompt "Hello, how are you today?"_

`Output: Where are you today? No, why are you here today? Why is the most subjective of words`
