import os
import logging
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("application.log"),
        logging.StreamHandler()
    ]
)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("API key missing. Ensure OPENAI_API_KEY is set in the .env file.")
    raise ValueError("API key missing")

client = OpenAI(api_key=api_key)


def read_article(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File {file_path} does not exist.")
        raise FileNotFoundError(f"File {file_path} not found.")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        logging.info(f"Successfully read the file {file_path}")
        return content
    except Exception as e:
        logging.error(f"Error reading the file {file_path}: {e}")
        raise


def generate_html_from_article(article_text):
    prompt = (
        "Convert the following article into structured HTML content suitable for a web page. "
        "Use appropriate HTML tags to organize the content. Indicate suggested places for images with "
        "<img src='image_placeholder.jpg' alt='Description for image generation'> tags. "
        "Each image tag should have an accurate alt attribute describing the visual context. "
        "Include captions for images under each image tag using appropriate HTML tags. "
        "Only return content to be placed within <body> tags. Do not include <html>, <head>, or <body> tags."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an assistant that generates HTML content."},
                {"role": "user", "content": prompt + "\n\n" + article_text}
            ]
        )
        html_content = response.choices[0].message.content.strip()
        logging.info("HTML content successfully generated using OpenAI API")
        return html_content
    except OpenAIError as e:
        logging.error(f"Error during OpenAI API call: {e}")
        raise


def save_html_to_file(html_content, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
        logging.info(f"HTML content successfully saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving to file {output_file}: {e}")
        raise


def main(file_path="artykul.txt", output_file="artykul.html"):
    try:
        article_text = read_article(file_path)

        html_content = generate_html_from_article(article_text)

        save_html_to_file(html_content, output_file)
        logging.info("Process completed successfully.")
    except Exception as e:
        logging.error(f"Main process failure: {e}")


if __name__ == "__main__":
    main()
