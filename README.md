Enterprise Supply Chain Risk Intelligence Platform

Execution Instructions
1. Initialize virtual environment: python -m venv venv
2. Activate environment: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
3. Install dependencies: pip install -r requirements.txt
4. Generate underlying dataset: python generate_data.py
5. Launch analytics application: streamlit run app.py

Streamlit Community Cloud deployment
------------------------------------
1. Push this repository to GitHub.
2. In Streamlit Community Cloud, create an app from the repository.
3. Set the main file path to `app.py`.
4. Streamlit will install the dependencies from `requirements.txt` and use the committed dataset in `data/supply_chain_data.csv`.

The dataset is already included in the repository, so running `generate_data.py` is optional for deployment.