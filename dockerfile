FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pip-tools

# Instalar dependências do pyproject.toml
RUN pip-compile pyproject.toml --output-file=requirements.txt && \
    pip install --no-cache-dir -r requirements.txt


CMD ["streamlit", "run", "app.py"]
