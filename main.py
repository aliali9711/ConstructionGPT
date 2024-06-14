from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai_api import generate_description
from pydantic import BaseModel
import openai



# Initialize FastAPI
app = FastAPI()

# Configure CORS to allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add the origin of your React app
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict HTTP methods if needed
    allow_headers=["*"],  # You can restrict headers if needed
)


# Define your data model for the request body
class Ask(BaseModel):
    ask: str
    model: str


@app.post("/add")
async def add_product_description(request: Ask):
    # description = generate_description(request.ask, request.model)
    description = generate_description(request.ask, request.model)

    return {"output": description}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="localhost", port=7001, log_level="debug")
