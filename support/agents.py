from .gemini_client import Anthropic
from django.conf import settings

client = Anthropic(api_key=settings.GEMINI_API_KEY, model=settings.GEMINI_MODEL)

# support system prompt for the AI agent


# tools shema for the AI agent

# excute tools function for the AI agent


# agents loop for the AI agent
