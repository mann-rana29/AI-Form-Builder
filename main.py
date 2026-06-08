from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import  List, Optional
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
import json
from prompt_config import FORM_BUILDER_PROMPT
from schema import CanvasElement , UiStateSchema
from urllib.parse import quote

with open("templates.json", "r", encoding="utf-8") as f:
    TEMPLATES = json.load(f)


load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

app = FastAPI()

#temporary storage for forms
FORM_STORE = {}

Client = AsyncOpenAI(
    api_key= API_KEY,
    base_url= BASE_URL
)

SYSTEM_INSTRUCTION = FORM_BUILDER_PROMPT

class RequestModel(BaseModel):
    query : str

class ResponseModel(BaseModel):
    success: bool = False
    message: str

    canvas_state: Optional[List[CanvasElement]] = None

    ui_state: Optional[UiStateSchema] = None

    public_html: str = ""

@app.get("/")
def ping():
    return {
        "message" : "success"
    }

@app.post("/forms/generate", response_model=ResponseModel)
async def generate_form(request: RequestModel):
    response = await Client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": request.query}
        ],
        temperature=0.5,
        max_tokens=4000
    )

    output = response.choices[0].message.content

    # Strip markdown code blocks if present
    if output.startswith("```"):
        # Remove ```json or ``` from start and ``` from end
        output = output.strip()
        if output.startswith("```json"):
            output = output[7:]  # Remove ```json
        elif output.startswith("```"):
            output = output[3:]  # Remove ```
        if output.endswith("```"):
            output = output[:-3]  # Remove trailing ```
        output = output.strip()

    try:
        parsed_output = json.loads(output)

        FORM_STORE[1] = parsed_output
        
        return parsed_output

    except Exception as e:
        print(f"JSON parsing error: {e}")
        print(f"Failed to parse: {output}")
        return {
            "success": False,
            "message": f"Invalid AI response: {str(e)}",
            "canvas_state" : None,
            "ui_state" : None,
            "public_html" : ""
        }

@app.get("/form/preview/1")
async def preview_form():

    form = FORM_STORE.get(1)

    if not form:
        return HTMLResponse(
            content = "<h1>Form not found</h1>",
            status_code=404
        )
    
    return HTMLResponse(
        content= form["public_html"],
        status_code=200
    )

@app.get("/templates")
async def get_templates():
    cards = ""

    for index, template in enumerate(TEMPLATES):

        encoded_prompt = quote(template["prompt"])

        cards += f"""
        <div
            style="
                border:1px solid #ddd;
                padding:20px;
                margin-bottom:20px;
                border-radius:10px;
            "
        >

            <h2>{template["topic"]}</h2>

            <p>{template["prompt"]}</p>

            <a
                href="/generate-preview?prompt={encoded_prompt}"
                target="_blank"
            >
                <button
                    style="
                        padding:10px 20px;
                        cursor:pointer;
                    "
                >
                    Generate Form
                </button>
            </a>

        </div>
        """

    return HTMLResponse(f"""
    <html>

    <head>
        <title>AI Form Templates</title>
    </head>

    <body
        style="
            font-family: Arial;
            max-width: 900px;
            margin:auto;
            padding:40px;
        "
    >

        <h1>AI Form Templates</h1>

        {cards}

    </body>

    </html>
    """)


#Only for geneating templates
@app.get("/generate-preview")
async def generate_preview(prompt: str):

    response = await Client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=4000
    )

    output = response.choices[0].message.content

    if output.startswith("```"):

        output = output.strip()

        if output.startswith("```json"):
            output = output[7:]

        elif output.startswith("```"):
            output = output[3:]

        if output.endswith("```"):
            output = output[:-3]

        output = output.strip()

    try:

        parsed_output = json.loads(output)

        return HTMLResponse(
            content=parsed_output["public_html"]
        )

    except Exception as e:

        return HTMLResponse(
            content=f"""
            <h1>Failed To Generate Form</h1>

            <pre>{str(e)}</pre>

            <pre>{output}</pre>
            """,
            status_code=500
        )