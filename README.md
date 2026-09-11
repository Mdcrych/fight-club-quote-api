# Fight Club Quote API

Минимальный FastAPI-сервис для проверки сборки и раскатки бэкенда.

## Endpoints

- `GET /` — статус сервиса
- `GET /health` — health-check
- `GET /quote` — цитата
- `GET /docs` — Swagger UI

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
