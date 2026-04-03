"""
gTTS Voice Generation Service
Generates Hindi/English narration using gTTS and caches latest MP3.
"""

import logging
import os
from gtts import gTTS

logger = logging.getLogger(__name__)

# Get the backend directory for storing audio files
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUDIO_DIR = os.path.join(BACKEND_DIR, "audio_cache")

# Create audio directory if it doesn't exist
os.makedirs(AUDIO_DIR, exist_ok=True)
logger.info(f"Audio cache directory: {AUDIO_DIR}")


def get_audio_file_path() -> str:
    """Get the full path to the latest audio file."""
    return os.path.join(AUDIO_DIR, "latest.mp3")


def generate_voice(text: str, lang: str = "hi") -> str:
    """
    Generate voice narration using gTTS.

    Args:
        text: Text to convert to speech
        lang: Language code (default: 'hi' for Hindi)

    Returns:
        Path to generated MP3 file
    """
    if not text or not text.strip():
        raise ValueError("Text is required for TTS generation")

    try:
        logger.info(f"Generating gTTS audio for text: {text[:50]}...")
        tts = gTTS(text=text, lang=lang)
        file_path = get_audio_file_path()
        tts.save(file_path)
        file_size = os.path.getsize(file_path)
        logger.info(f"gTTS generated successfully: {file_path} ({file_size} bytes)")
        return file_path
    except Exception as e:
        logger.error(f"gTTS generation error: {e}")
        raise
