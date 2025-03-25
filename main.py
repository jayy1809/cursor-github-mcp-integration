from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(
    title="Cursor GitHub MCP Integration",
    description="A FastAPI application created and pushed to GitHub using Cursor Agent",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Returns a warm welcome message."""
    return {
        "message": "Welcome to a FastAPI application created by Cursor Agent!",
        "details": "This application was created and pushed to GitHub directly by Cursor Agent using GitHub MCP integration",
        "repository": "https://github.com/jayy1809/cursor-github-mcp-integration"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)