FROM python:3.8-bookworm as base

RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev
COPY todo_app /app/todo_app

FROM base as production
ENV FLASK_ENV=production
ENV FLASK_APP=todo_app.app:create_app()
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0", "todo_app.app:create_app()"]
EXPOSE 8000

FROM base as development
ENV FLASK_ENV=development
ENV FLASK_APP=todo_app.app:create_app()
ENV FLASK_DEBUG=1
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 5000