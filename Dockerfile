FROM python:latest

WORKDIR /usr/src/sentiment_analysis_app

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN python3 -m venv .venv
RUN bash -c "source .venv/bin/activate && \
    python3 -m pip install --no-cache-dir -U pip setuptools -r requirements.txt"

CMD [ "bash", "-c", "source .venv/bin/activate && \
    uvicorn app:create_app --reload --host=0.0.0.0 --port=8000" ]
