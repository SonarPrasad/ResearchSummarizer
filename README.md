# Research Summarizer

## Description

The **Research Summarizer** is a Django-based web application designed to help users summarize research papers by extracting key information from uploaded PDFs. This project leverages AI and Natural Language Processing (NLP) techniques to generate concise summaries, making it easier for researchers, students, and professionals to grasp the main points of extensive documents quickly.

## Features

- **PDF Upload**: Users can upload PDF files containing research papers for summarization.
- **AI-Powered Summarization**: The application uses advanced AI algorithms to extract and summarize key sections of the document, including titles, abstracts, and conclusions.
- **User Authentication**: Secure login and registration functionality for users to access their summaries.
- **Responsive Design**: The application is designed to be user-friendly and responsive, ensuring compatibility with various devices.
- **Downloadable Reports**: Users can download the generated summaries in a neatly formatted Word document.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (with optional frameworks)
- **Database**: SQLite (for development)
- **AI & NLP Libraries**: LangChain, PyPDF2, etc.
- **Deployment**: Vercel

## Installation Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/SonarPrasad/ResearchSummarizer.git

2. **Navigate to the Project Directory**:

    ```bash
    cd ResearchSummarizer

3. **Set Up a Virtual Environment**:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\\Scripts\\activate`

4. **Install Required Packages**:

    Make sure you have a requirements.txt file in your project directory. If not, you can create one using:

    ```bash
    pip freeze requirements.txt

5. **Then install the packages**:

    ```bash
    pip install -r requirements.txt

6. **Create a .env File**:

    Create a .env file in the project root directory and add your environment variables. Here is an example structure:

    ```plaintext
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
    GOOGLE_CLIENT_ID=your_google_client_id_here
    GOOGLE_CLIENT_SECRET=your_google_client_secret_here

7. **Run Migrations**:

    Make sure your database is set up correctly by running migrations:

    ```bash
        python manage.py migrate

8. **Start the Development Server**:

    Finally, run the development server to test your application locally:

    ```bash
        python manage.py runserver

## Usage

Once the application is running, users can register or log in to their accounts. After logging in, they can upload research papers in PDF format and receive summarized reports based on the AI's analysis.

## Contributing

Contributions to the Research Summarizer are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (e.g., `feature-branch`).
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- Thanks to the contributors and developers of the libraries used in this project.
- Special thanks to the open-source community for their support and resources.

For more information, please contact the project maintainer or check the repository's issues for any questions or suggestions.