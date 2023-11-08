FROM python:3.8-bookworm
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev
COPY todo_app /app/todo_app
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0", "todo_app.app:create_app()"]
EXPOSE 8000