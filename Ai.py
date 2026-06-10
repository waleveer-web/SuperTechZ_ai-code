import sys

from dotenv import load_dotenv
from huggingface_hub import InferenceClient, get_token

load_dotenv()

token = get_token()
if not token:
    print("Error: Hugging Face token not found.", file=sys.stderr)
    print(
        "\nSet for this PowerShell session:\n"
        '  $env:HF_TOKEN = "hf_..."\n'
        "\nOr add to `.env`:\n"
        "  HF_TOKEN=hf_...\n"
        "\nOr run once: huggingface-cli login\n"
        "\nGet a token: https://huggingface.co/settings/tokens",
        file=sys.stderr,
    )
    sys.exit(1)

client = InferenceClient(api_key=token)
completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Thinking",
    messages=[
        {
            "role": "user",
            "content": "richest man in world"
        }
    ],
)

message = completion.choices[0].message
print(message.content)