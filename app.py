import random

from fastapi import FastAPI

app = FastAPI(title="Original Quotes API", version="1.1.0")

QUOTES = [
    "Вещи, которыми ты владеешь, не должны владеть тобой.",
    "Страх не исчезает. Ты просто перестаёшь давать ему команды.",
    "Перемены начинаются не с правильных слов, а с поступка.",
    "Не путай комфорт с жизнью.",
    "Иногда нужно потерять привычное, чтобы увидеть себя.",
    "Свобода начинается там, где заканчивается желание всем понравиться.",
    "Ты не обязан быть удобной версией себя.",
]


@app.get("/", tags=["service"])
def root() -> dict[str, str]:
    return {"service": "original-quotes-api", "status": "ok"}


@app.get("/quote", tags=["quote"])
def get_quote() -> dict[str, str]:
    return {
        "quote": random.choice(QUOTES),
        "language": "ru",
        "source": "Original phrase",
    }


@app.get("/health", tags=["service"])
def health() -> dict[str, str]:
    return {"status": "healthy"}
