from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title="Embodix Agent Runtime", version=settings.version)


@app.get("/v1/health")
async def health() -> dict:
    return {"status": "ok", "version": settings.version}


@app.get("/v1/ready")
async def ready() -> dict:
    return {
        "ready": True,
        "checks": {
            "app_env": settings.app_env,
            "llm_provider": settings.llm_provider,
            "llm_key_configured": settings.llm_key_configured,
        },
    }


@app.post("/v1/echo")
async def echo(payload: dict) -> dict:
    text = str(payload.get("text", ""))
    return {"text": text, "length": len(text)}
