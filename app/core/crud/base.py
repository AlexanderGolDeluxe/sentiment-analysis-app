import hfapi
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import HF_API_TOKEN, HF_MODEL_NAME
from app.core.models import UserPhrase
from app.core.schemas import UserPhraseCreate


@logger.catch(reraise=True)
def get_text_classification(text: str):
    """
    Performs sentiment classification of `text` using a trained HF model
    """
    hf_client = hfapi.Client(api_token=HF_API_TOKEN)

    return hf_client.text_classification(text, model=HF_MODEL_NAME)


@logger.catch(reraise=True)
async def save_text_classification_to_db(
        session: AsyncSession, phrase: str, classification: list[dict]
    ):
    """
    Saves `phrase` and
    its sentiment scores (positive, negative, neutral) to database
    """
    analyzed_user_phrase = dict(phrase=phrase)
    for sentiment_row in classification:
        analyzed_user_phrase[sentiment_row["label"] + "_score"] = (
            sentiment_row["score"])

    user_phrase_row = UserPhrase(
        **UserPhraseCreate(**analyzed_user_phrase).model_dump()
    )
    session.add(user_phrase_row)
    await session.commit()


@logger.catch(reraise=True)
async def get_sentiment_by_phrase(session: AsyncSession, phrase: str):
    """
    Returns sentiment classification of `phrase` using a HF model and
    writes results to DB
    """
    sentiment = None
    classification = get_text_classification(phrase)
    if isinstance(classification, list) and classification and classification[0]:
        classification = classification[0]
        if "score" in classification[0]:
            sentiment = max(
                classification, key=lambda stmt: stmt["score"]
            )["label"]
            await save_text_classification_to_db(
                session, phrase, classification)

    return sentiment or classification
