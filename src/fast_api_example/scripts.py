import uvicorn


def start():
    uvicorn.run("fast_api_example.main:app", host="127.0.0.1", port=8000, reload=False)
