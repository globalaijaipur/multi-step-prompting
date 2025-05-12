from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(override=True)

import os
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

openai = OpenAI();

# STEP 1: Initialize the multi-step prompting process
# Multi-step prompting allows for more controlled and focused AI responses
# by breaking down complex tasks into manageable sequential steps

messages = [{"role": "user", "content": "Pick a business area that might be worth exploring for an Agentic AI opportunity. Respond only with the business area."}]

# STEP 2: Execute the first prompt to get a focused response
# This demonstrates how multi-step prompting can guide the AI to provide
# specific, targeted outputs rather than lengthy, unfocused responses

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

# STEP 3: Extract and use the output from the first step
# Each step in multi-step prompting builds upon previous responses,
# creating a chain of reasoning that leads to more coherent results

business_idea = response.choices[0].message.content
print("Business Idea: "+business_idea)

# STEP 4: Create a follow-up prompt that builds on the previous response
# This demonstrates how multi-step prompting enables contextual continuity
# while maintaining tight control over the direction of the conversation

messages = [{"role": "user", "content": f"Present a pain point in the area of {business_idea} which is challenging & could be solved by an Agentic AI. Respond only with the pain point."}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

# STEP 5: Process intermediate results to maintain the prompting chain
# Multi-step prompting allows for validation and refinement at each stage
# before proceeding to the next logical step in the reasoning process

pain_point = response.choices[0].message.content
print("Pain Point: "+pain_point)

# STEP 6: Formulate the final prompt that synthesizes previous outputs
# The power of multi-step prompting is evident in how it can guide the AI
# to build comprehensive solutions through a series of focused interactions

messages = [{"role": "user", "content": f"Present the Agentic AI solution to the pain point of {pain_point} in the area of {business_idea}. Respond only with the solution."}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

# STEP 7: Deliver the final output of the multi-step prompting process
# This approach results in more relevant, coherent, and useful AI-generated content
# than could be achieved with a single, complex prompt

solution = response.choices[0].message.content
print("Solution: "+solution)