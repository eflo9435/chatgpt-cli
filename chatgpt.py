#!/usr/bin/env python3

import sys
import os
from dotenv import load_dotenv

def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY is not set.")
        print("Set it in the .env file.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: chatgpt \"your prompt here\"")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    print("Prompt received:")
    print(prompt)
    print("API key loaded successfully.")

if __name__ == "__main__":
    main()
