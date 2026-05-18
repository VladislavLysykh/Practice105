# Password Generator - Microservices Demo

## Architecture
- **Nginx**: Reverse proxy and static frontend server
- **Frontend**: HTML/JS UI served by Nginx
- **Backend (Flask)**: API endpoint for generating password tasks
- **Worker (Python)**: Long-running password generation service
- **Redis**: Task queue and result storage

## Run

docker compose up -d

## How it works
- Frontend submits generation request to backend API
- Backend creates task in Redis and returns task_id
- Worker picks up task from Redis queue
- Worker generates password (simulated 2s delay)
- Frontend polls for result and displays password

----
## Проверка работоспособности

### Клонируем репозиторий
1. git clone https://github.com/SoftwareEngineering2026/Practice105.git
2. cd Practice105/SerovAA/

### Создаём структуру и файлы (скопируй вышеуказанные файлы)

### Запускаем
docker compose up -d

### Проверяем
curl http://localhost:8080/api/generate -X POST -H "Content-Type: application/json" -d '{"length": 16, "use_digits": true, "use_special": true}'

### Останавливаем
docker compose down

----
## Особенности решения:

✅ Одна точка входа — Nginx на порту 8080

✅ Все сервисы в одной сети Docker

✅ Worker выполняет "длительные задачи" (generation с delay)

✅ Готово к запуску одной командой docker compose up

✅ Полностью микросервисный (frontend, backend, worker, redis)
