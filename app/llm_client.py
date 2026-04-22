from openai import OpenAI
from app.config import HF_TOKEN

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)