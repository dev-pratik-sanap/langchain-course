from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


def main():
    # Access the environment variable
    google_api_key = os.getenv("GOOGLE_API_KEY")

    if google_api_key:
        print(f"Google API Key: {google_api_key}")
    else:
        print("Google API Key not found in environment variables.")


if __name__ == "__main__":
    main()
