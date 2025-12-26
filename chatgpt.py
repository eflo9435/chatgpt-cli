#!/usr/bin/env python3

import sys
import os
from dotenv import load_dotenv
from openai import OpenAI

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

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content
        print("\nChatGPT response:\n")
        print(reply)

    except Exception as e:
        print("Error communicating with OpenAI:")
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
