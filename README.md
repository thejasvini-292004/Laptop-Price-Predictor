# Laptop-Price-Predictor

This project is a Machine Learning application that predicts the price of a laptop based on its specifications like processor, RAM, storage, brand, GPU, operating system, and more. The goal is to help users estimate the market value of a laptop before buying or selling.


Features :

- Cleaned and processed dataset
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training using Random Forest, XGBoost, etc.
- Model evaluation and optimization
- Interactive web interface using Streamlit

Tech Stack:

- **Python**
- **Pandas, NumPy, Scikit-learn**
- **Matplotlib, Seaborn**
- **XGBoost, RandomForest**
- **Streamlit** for web interface

Input Features:

- Brand
- Processor (CPU)
- RAM (Size and Type)
- Storage (HDD/SSD)
- GPU
- Operating System
- Screen Size & Resolution

How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/thejasvini-292004/Laptop-Price-Predictor.git
   cd Laptop-Price-Predictor

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
