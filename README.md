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

### Create Matrix GIF

**You: Make a 512x512 gif with falling green Matrix letters. Assume no fonts. 90 frames 5fps. No talk, just go.**

_Alright, here's the code to generate a 512x512 gif with falling green matrix letters. We'll be using the Python Imaging Library (PIL) to generate the gif frames. To install it, run the command `!pip3 install pillow` in the terminal if it's not installed._

_This code will generate a gif with 90 frames at 5fps. You can adjust the variables at the beginning of the code to change the parameters of the gif, such as the background color, the font size, and the characters used for the falling letters._

```
import random

from PIL import Image, ImageDraw

# Set up variables
width = 512
height = 512
fps = 5
frames = 90
background = (0, 0, 0)
falling_letters = []
letter_size = 10

# Generate unicode matrix letters
matrix_letters = [chr(x) for x in range(256) if chr(x) not in ['ヽ', 'ヾ', 'オ']]

# Generate initial positions for the letters
for i in range(100):
    x = random.randint(0, width-10)
    y = random.randint(-height, 0)
    letter = random.choice(matrix_letters)
    falling_letters.append({"x": x, "y": y, "letter": letter})

# Generate frames
images = []
for i in range(frames):
    # Create image
    image = Image.new('RGB', (width, height), background)
    draw = ImageDraw.Draw(image)
    
    # Draw falling letters
    for letter in falling_letters:
        # Update y position
        letter["y"] += letter_size
        # Draw letter
        draw.text((letter["x"], letter["y"]), letter["letter"], fill=(0, 255, 0))
        
        # Reset letter if it has fallen off the screen
        if letter["y"] > height:
            letter["y"] = random.randint(-height, 0)
            letter["x"] = random.randint(0, width-10)
            letter["letter"] = random.choice(matrix_letters)
    
    # Add image to list of frames
    images.append(image)
    
# Save gif
images[0].save('matrix.gif', save_all=True, append_images=images[1:], duration=200, loop=0)
print('saved to matrix.gif')
```

`Output: saved to matrix.gif`

![matrix](data/matrix.gif)

### OpenAI Completion

**You: Please start a conversation with openai and print the response. Read the API key from `openai_api_key.txt`.**

_Sure, I can help you with that. To read the API key from `openai_api_key.txt`, I need to read the contents from it. Here's the code:_

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
