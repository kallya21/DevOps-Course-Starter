FROM python:3.8-bookworm as base

RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev
COPY todo_app /app/todo_app

FROM base as production
ENV FLASK_ENV=production
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0", "todo_app.app:create_app()"]
EXPOSE 8000

FROM base as development
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 5000

FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]