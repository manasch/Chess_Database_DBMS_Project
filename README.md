# Chess Database Management

## Setup

- Start MySQL on XAMPP
- Install python dependencies
    ```bash
    pip install -r requirements.txt
    ```
- Source setup.sql and chess.sql
    ```
    mysql -u root
    source setup.sql
    source src/sql/chess.sql
    ```
- Start streamlit
    ```bash
    streamlit run ./src/app.py
    ```

