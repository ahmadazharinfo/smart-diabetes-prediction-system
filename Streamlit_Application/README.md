# Smart Diabetes Monitoring and Prediction System
## University of Basrah — Computer Engineering Department
**Authors:** Ahmad Azhar Almansoor | Ibrahim Madian Fadhil  
**Supervisor:** Asst. Dr. Sarah Aziz Hafidh  
**Academic Year:** 2024–2025

---

## HOW TO RUN THE APPLICATION

### Step 1 — Folder Structure
Make sure all files are in the same folder:

```
your_folder/
    app.py
    full_pipeline_bundle.pkl
    requirements.txt
```

### Step 2 — Install Dependencies
Open a terminal in the folder and run:

```bash
pip install -r requirements.txt
```

### Step 3 — Run the Application
```bash
streamlit run app.py
```

The application will open automatically in your browser at http://localhost:8501

---

## WHAT THE APPLICATION DOES

1. Accepts 21 self-reported behavioral and demographic inputs from the user
2. Applies the domain-informed feature engineering pipeline (21 → 45 features)
3. Scales features using the trained RobustScaler
4. Generates a diabetes risk probability using the tuned LightGBM model
5. Applies the clinical deployment threshold of 0.53
6. Displays a High Risk or Low Risk classification with probability score
7. Identifies key contributing risk factors from the input
8. Provides a clinical recommendation

---

## MODEL PERFORMANCE (at threshold 0.53)

| Metric | Value |
|---|---|
| Recall (Sensitivity) | 0.9064 |
| ROC-AUC | 0.8186 |
| PR-AUC | 0.4447 |
| Balanced Accuracy | 0.7228 |
| MCC | 0.3114 |
| F1-Score | 0.4066 |

---

## DISCLAIMER

This application is an academic graduation project and is intended
for educational and clinical decision support purposes only.
It does not replace laboratory diagnosis or physician evaluation.
