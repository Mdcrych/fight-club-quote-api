from fastapi import FastAPI

app = FastAPI(title="Fight Club Quote API", version="1.0.0")

QUOTE = "The first rule of Fight Club is: you do not talk about Fight Club."


@app.get("/", tags=["service"])
def root() -> dict[str, str]:
    return {"service": "fight-club-quote-api", "status": "ok"}


@app.get("/quote", tags=["quote"])
def get_quote() -> dict[str, str]:
    return {"quote": QUOTE, "source": "Fight Club"}


@app.get("/health", tags=["service"])
def health() -> dict[str, str]:
    return {"status": "healthy"}
