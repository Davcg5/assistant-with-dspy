import os

from fastapi import FastAPI
import dspy
import uvicorn

from assistant.routers import endpoints as assistant_endpoints

API_KEY = os.environ.get("GEMINI_API_KEY")

tags_metadata = [
    {
        "name": "Assistant"
    }
]

gemini = dspy.Google(
    "models/gemini-1.0-pro",
    api_key=API_KEY,
    temperature=0
    )



dspy.settings.configure(lm=gemini, max_tokens=3096)
app = FastAPI(title="Assistant", openapi_tags=tags_metadata)
app.include_router(assistant_endpoints.router)


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
