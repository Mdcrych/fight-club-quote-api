# Original Quotes API

Минимальный FastAPI-сервис для проверки сборки и раскатки бэкенда. Endpoint `/quote` при каждом запросе случайно возвращает одну из оригинальных русскоязычных фраз. Это не дословные цитаты из фильма или другого произведения.

## Endpoints

- `GET /` — статус сервиса
- `GET /health` — health-check
- `GET /quote` — случайная оригинальная русская фраза
- `GET /docs` — Swagger UI

## Пример ответа

```json
{
  "quote": "Не путай комфорт с жизнью.",
  "language": "ru",
  "source": "Original phrase"
}
```

## Запуск через Docker Compose

```bash
docker compose up -d --build
```

Проверка:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/quote
```

Логи:

```bash
docker compose logs -f
```

Остановка:

```bash
docker compose down
```

## Запуск без Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```
