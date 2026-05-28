from fastapi import FastAPI

app = FastAPI(
    title="Support Ticket API"
)


@app.get("/")
def healthcheck():
    return {
        "status": "ok"
    }