# streamlit-nlp-categorization
This is a Streamlit application for categorizing indirect spend data using Natural Language Processing (NLP). The app allows you to upload a CSV file of spend data, processes the file using a pre-trained `spaCy` model, and categorizes the spend based on the description and items.

## How to Run the Project

### Installation:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/streamlit-nlp-categorization.git
    ```
    
2. Navigate into the project directory:
    ```bash
    cd streamlit-nlp-categorization
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the necessary spaCy model:
    ```bash
    python -m spacy download en_core_web_md
    ```

5. Run the app:
    ```bash
    streamlit run app.py
    ```

### Usage:

- Upload a CSV file with the columns `Description` and `Items`.
- The app will process the data and categorize it into predefined categories.
- You can download the categorized CSV file.

## Example:

| Date       | Supplier          | Description             | Items                           | Amount  | Currency | Department   | Category        |
|------------|-------------------|-------------------------|---------------------------------|---------|----------|--------------|-----------------|
| 2023-09-01 | Staples           | Purchase of stationery  | Pen, Pencil, Notepad, Eraser    | 500.00  | USD      | Admin        | Office Supplies |
| 2023-09-02 | TechCorp          | Monthly server fees     | Cloud Hosting                   | 1200.00 | USD      | IT           | IT Services     |
