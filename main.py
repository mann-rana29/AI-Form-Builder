from fastapi import FastAPI
from pydantic import BaseModel
from typing import  List
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
import json
from prompt_config import FORM_BUILDER_PROMPT
from schema import ElementSchema , UiStateSchema

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

app = FastAPI()

Client = AsyncOpenAI(
    api_key= API_KEY,
    base_url= BASE_URL
)

SYSTEM_INSTRUCTION = FORM_BUILDER_PROMPT

class ResponseModel(BaseModel):
    success : bool = False
    message : str
    canvas_state : List[ElementSchema] = None
    ui_state : UiStateSchema = None
    public_html : str = ""

@app.get("/")
def ping():
    return {
        "message" : "success"
    }

@app.post("/forms/generate", response_model=ResponseModel)
async def generate_form(request: str):
    response = await Client.responses.create(
        model="openai/gpt-oss-120b",
        instructions= SYSTEM_INSTRUCTION,
        input = request,
        temperature=0.2
    )

    output = response.output_text

    try:
        parsed_output = json.loads(output)
        return parsed_output

    except Exception:
        return {
            "success": False,
            "message": "Invalid AI response",
            "canvas_state" : None,
            "ui_state" : None,
            "public_html" : ""
        }


