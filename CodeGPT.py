import json
# Install required dependencies
# ! pip install clarifai
# ! pip install -upgrade langchain
# ! pip install --upgrade typing-extensions


# Please login and get your API key from  https://clarifai.com/settings/security
from getpass import getpass
# CLARIFAI_PAT = getpass()
CLARIFAI_PAT = "6dd0327cc2a145f6987b487a76e03f43" # User's Personal Access Tokens of Clarifai

# Import the required modules
from langchain.llms.clarifai import Clarifai
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List

USER_ID = "openai"
APP_ID = "chat-completion"
MODEL_ID = "GPT-4"

# Initialize a Clarifai LLM
clarifai_llm = Clarifai(
    pat=CLARIFAI_PAT, user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID,
)

# Define your desired data structure.
class CODEGPT(BaseModel):
    code: str = Field(description="""This field requires a code snippet to be generated related to the query asked by the user.""")
    description: str = Field(description="""This Field Provides a short description about the code generated format dhould be: "Latex".""")
    input: str = Field(description="""This field requires an example input to be used for the code.""")
    expected_output: str = Field(description="""This field requires an expected output which the generated code must output given the genrated input.""")
    
    # You can add custom validation logic easily with Pydantic.
    # _args = []
    # @validator('code', 'input', 'expected_output')
    # def is_the_code_working(cls,value,values,config,field):
    #     _args.append(value)
    #     pass


# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=CODEGPT)

prompt = PromptTemplate(
    template="""Answer the user query.
    \n{format_instructions}\n{query}\n""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# And a query intended to prompt a language model to populate the data structure.
def GPT_run(query):
    _input = prompt.format_prompt(query=query)
    output = clarifai_llm(_input.to_string())
    out = parser.parse(output)


    
    # json_object = json.dumps(output, indent=4)
    # with open("out.json", "w") as outfile:
        # outfile.write(json_object)
    # print("OUTPUT\n",out)

    return out


# print("INPUT:\n",_input.to_string())
# print("OUTPUT:\n",output)






