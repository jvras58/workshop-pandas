FROM python:3.11-slim AS base

RUN pip install --no-cache-dir uvicorn

WORKDIR /app


COPY . .

RUN uv venv && uv sync

ENV PATH="/app/.venv/bin:$PATH"

CMD ["streamlit", "run", "app.py"]
