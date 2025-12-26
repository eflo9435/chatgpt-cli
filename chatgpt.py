#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: chatgpt \"your prompt here\"")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    print("Prompt received:")
    print(prompt)

if __name__ == "__main__":
    main()
