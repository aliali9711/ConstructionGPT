import os
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

template_string = """Respond to the prompt \
that is delimited by triple backticks \
into a style that is {style}. \
The response language is {language}. \
The target country is {country}. \
Note that the target group is {target_group}. \
text: ```{text}```
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

customized_style = 'Professional engineering style related to construction domain'
customized_language = 'Arabic'
customized_country = 'Saudi Arabia'
customized_target_group = ('People who are interested in construction domain weather they are sellers of construction '
                           'materials, or engineers, or architects, or construction workers, project managers, '
                           'Construction contractors')


# customized_text = 'حدثني عن كود البناء السعودي'


# service_messages = prompt_template.format_messages(
#     style=customized_style,
#     language=customized_language,
#     country=customized_country,
#     target_group=customized_target_group,
#     text=customized_text)


# print(service_messages[0].content)
#
# service_response = chat(service_messages)
# print(service_response.content)



def generate_description_langchain(prompt, model="gpt-3.5-turbo"):
    chat = ChatOpenAI(model=model)
    messages = prompt_template.format_messages(
        style=customized_style,
        language=customized_language,
        country=customized_country,
        target_group=customized_target_group,
        text=prompt)
    return chat(messages).content

