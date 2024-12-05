import uvicorn


def start() -> None:
    uvicorn.run("fast_api_example.app:app", host="127.0.0.1", port=8000, reload=False)
