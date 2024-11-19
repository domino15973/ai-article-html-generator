# AI Article HTML Generator
A simple Python application that converts text articles into structured HTML content using OpenAI API.

## Overview
This application reads a text article from a file ([artykul.txt](artykul.txt)), sends it to OpenAI API for processing, and generates structured HTML content ([artykul.html](artykul.html)) with placeholder for images and descriptive prompts for each image.

- **[szablon.html](szablon.html):** A basic HTML template with styles and JavaScript for previewing any article content.
- **[podglad.html](podglad.html):** A full preview of the article with structured HTML, ready for visual inspection.

## Prerequisites
- Python 3
- Git
- OpenAI API key

## Installation
### Clone the repository:

`git clone https://github.com/domino15973/ai-article-html-generator.git`

`cd ai-article-html-generator`

### Install dependencies:

`pip install -r requirements.txt`

### Set up OpenAI API key:

`OPENAI_API_KEY=your_openai_api_key`

### Usage
**Place your article:** Save the text article you want to convert in a file named [artykul.txt](artykul.txt) in the project directory.

### Run the application:

`python main.py`

### View the output:
**Open file [artykul.html](artykul.html).**

**Template:** Open [szablon.html](szablon.html) to see the basic HTML structure ready for articles. You can use it for preview your article.
