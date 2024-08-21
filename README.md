# Sentiment Analysis Web Application
Web application using [Python client for the Hugging Face Inference API](https://github.com/huggingface/hfapi) that allows users to input text and receive a sentiment analysis of their input (positive, negative or neutral).
Developed on the [FastAPI](https://fastapi.tiangolo.com) framework.  

![Static Badge](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=blue&labelColor=white)
![Static Badge](https://img.shields.io/badge/FastAPI-0.112.1-009485?logo=fastapi&labelColor=white)
![Static Badge](https://img.shields.io/badge/SQLite-white?logo=sqlite&logoColor=blue)

## Installation

### Clone repository
```console
git clone https://github.com/AlexanderGolDeluxe/sentiment-analysis-app
```

### Make a virtual environment with requirements

```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Manage environment variables

Rename file [`.env.dist`](/.env.dist) to `.env`
```console
mv .env.dist .env
```

#### Change variables according to your required parameters in `.env` file

Set your Hugging Face API token and desired AI model for sentiment analysis
```
…
HF_API_TOKEN = "hf_**********************************"
HF_MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
…
```

## Launch

```console
uvicorn app:create_app --reload
```

## Build via Docker compose

1. [Clone repository](#clone-repository)
2. [Rename file `.env.dist` to `.env`](#manage-environment-variables)
3. [Change variables according to your required parameters in `.env` file](#change-variables-according-to-your-required-parameters-in-env-file)
4.  Run following command in your console:
    ```console
    docker compose -f "docker-compose.yml" up -d --build
    ```
