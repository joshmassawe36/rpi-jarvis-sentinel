import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

def _encode_image(image_path: str) -> str:
    """Read an image file and return its base64-encoded string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_scene(image_path: str) -> str:
    """
    Send an image to GPT-4 Vision and return a short natural-language
    description of what's in the scene.

    Reads the API key from the OPENAI_API_KEY environment variable
    (via a local .env file or the shell environment) — never hardcode
    the key in source code.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY environment variable not set. "
            "Create a .env file with OPENAI_API_KEY=your-key-here, "
            "or run: export OPENAI_API_KEY='your-key-here'"
        )

    client = OpenAI(api_key=api_key)

    base64_image = _encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o",  
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are Jarvis, a vigilant AI sentinel monitoring a desk "
                            "through a camera. Motion has just been detected and you're "
                            "reporting what you observe. Speak directly, like a calm, "
                            "alert security presence — brief, observant, and a little "
                            "formal, the way a butler-bodyguard hybrid would announce "
                            "a status update. One or two short sentences. Do not describe "
                            "yourself or explain that you are an AI — just report what you "
                            "see, in character, as if announcing it out loud to the room."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=150,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python vision_analysis.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    print(f"Analyzing {image_path}...")

    description = analyze_scene(image_path)
    print("\nJarvis sees:")
    print(description)