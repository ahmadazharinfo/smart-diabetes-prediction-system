# Smart Diabetes Monitoring and Prediction System

**University of Basrah — Computer Engineering Department**  
**Author:** Ahmad Azhar Almansoor 
**Supervisor:** Asst. Dr. Sarah Aziz Hafidh  
**Academic Year:** 2025–2026

---

## Project Overview

A machine learning system for predicting diabetes risk using the CDC BRFSS 2015 dataset (253,680 records). The system applies a full ML pipeline — from raw data through feature engineering, model selection, and hyperparameter tuning — and exposes predictions through an interactive Streamlit web application.

**Best Model:** LightGBM (tuned) at threshold 0.53  
**Recall (Sensitivity):** 0.9064 | **ROC-AUC:** 0.8186 | **Balanced Accuracy:** 0.7228

---

## Repository Structure

```
smart-diabetes-prediction-system/
│
├── README.md
│
├── Project_Files/
│   ├── Dataset/
│   │   └── diabetes_binary_health_indicators_BRFSS2015.csv   # 253,680 records
│   │
│   ├── Notebooks/
│   │   ├── 01_Data_Loading_and_EDA.ipynb
│   │   ├── 02_Preprocessing.ipynb
│   │   ├── 03_Baseline_Models.ipynb
│   │   ├── 04_Feature_Engineering.ipynb
│   │   ├── 05_Model_Selection_and_Tuning.ipynb
│   │   ├── 06_Final_Results_and_Pipeline.ipynb
│   │   └── catboost_info/                                     # CatBoost training logs
│   │
│   ├── pipeline/
│   │   └── full_pipeline_bundle.pkl                           # Serialized LightGBM + Scalers
│   │
│   ├── plots/
│   │   ├── 01_eda/                                            # Target distribution, heatmaps, boxplots
│   │   ├── 02_imbalance/                                      # Class imbalance & SMOTE demo
│   │   ├── 03_preprocessing/                                  # Scaled feature distributions
│   │   ├── 04_baseline_models/                                # Baseline comparison, ROC/PR curves
│   │   ├── 05_feature_engineering/                            # Engineered feature distributions
│   │   ├── 06_engineered_models/                              # Orig vs engineered comparison
│   │   ├── 07_feature_importance/                             # RF importance, mutual info, combined rank
│   │   ├── 08_selected_models/                                # Three-phase comparison
│   │   ├── 09_model_comparison/                               # Global AUC heatmap
│   │   └── 10_best_model/                                     # Tuning, threshold, learning curve
│   │
│   └── research_plots/                                        # Final publication-quality figures
│       ├── 01_confusion_matrix_final.png
│       ├── 02_roc_curve_final.png
│       ├── 03_pr_curve_final.png
│       └── 07_feature_importance_final.png
│
├── Streamlit_Application/
│   ├── app.py                                                 # Web interface (29KB)
│   ├── requirements.txt                                       # All dependencies pinned
│   ├── full_pipeline_bundle.pkl                               # Model bundle for the app
│   ├── README.md                                              # App-specific run instructions
│   └── Images/                                                # App screenshots
│       ├── First_Page.png
│       ├── Second_page.png
│       ├── Third_Page.png
│       └── Third_Page_Risk.png
│
└── Graduation_Research_Files/
    ├── PDF/
    │   ├── FULL_RESEARCH_SMART_DIABETES_MONITORING_AND_PREDICTION.pdf   
    │   ├── 0. PreliminaryPages - Ahmad.pdf
    │   ├── 1. ChapterOne_Introduction.pdf
    │   ├── 2. ChapterTwo_LiteratureReview.pdf
    │   ├── 3. ChapterThree_Methodology.pdf
    │   ├── 4. ChapterFour_ResultsAndDiscussion.pdf
    │   ├── 5. ChapterFive_ConclusionAndFutureWork.pdf
    │   ├── 6. ResearchSummary.pdf
    │   ├── 7. References.pdf
    │   └── 8. Chapter_Title_Page.pdf
    │
    └── Word/
        ├── 0. PreliminaryPages - Ahmad.docx
        ├── 1. ChapterOne_Introduction.docx
        ├── 2. ChapterTwo_LiteratureReview.docx
        ├── 3. ChapterThree_Methodology.docx
        ├── 4. ChapterFour_ResultsAndDiscussion.docx
        ├── 5. ChapterFive_ConclusionAndFutureWork.docx
        ├── 6. ResearchSummary.docx
        ├── 7. References.docx
        └── 8. Chapter_Title_Page.docx
```

---

## Notebooks Overview

| # | Notebook | Description |
|---|---|---|
| 01 | Data Loading and EDA | Dataset exploration, class imbalance analysis, correlation heatmaps, feature distributions |
| 02 | Preprocessing | Missing value handling, scaling (RobustScaler), SMOTE class balancing |
| 03 | Baseline Models | Benchmarking Logistic Regression, Decision Tree, Random Forest, XGBoost, CatBoost |
| 04 | Feature Engineering | Domain-informed expansion from 21 → 45 features |
| 05 | Model Selection and Tuning | Cross-validation, hyperparameter search, threshold optimization |
| 06 | Final Results and Pipeline | LightGBM final evaluation, pipeline serialization, summary report |

---

## Streamlit Application

### Run Locally

```bash
cd Streamlit_Application
pip install -r requirements.txt
streamlit run app.py
```

The app opens at **http://localhost:8501**

### How It Works

1. Accepts **21 self-reported** behavioral and demographic inputs
2. Applies domain-informed feature engineering (21 → 45 features)
3. Scales features using the trained **RobustScaler**
4. Generates a diabetes risk probability using the tuned **LightGBM** model
5. Applies the clinical deployment threshold of **0.53**
6. Displays **High Risk / Low Risk** classification with probability score
7. Identifies key contributing risk factors
8. Provides a clinical recommendation

### App Screenshots

| Page | Description |
|---|---|
| First Page | Input form — behavioral & demographic questions |
| Second Page | Feature summary before prediction |
| Third Page | Prediction result (Low Risk) |
| Third Page Risk | Prediction result (High Risk) with risk factors |

---

## Model Performance (LightGBM @ threshold 0.53)

| Metric | Value |
|---|---|
| Recall (Sensitivity) | **0.9064** |
| ROC-AUC | 0.8186 |
| PR-AUC | 0.4447 |
| Balanced Accuracy | 0.7228 |
| MCC | 0.3114 |
| F1-Score | 0.4066 |

> High recall was prioritized — in a clinical context, missing a true diabetic case (false negative) is more costly than a false alarm.

---

## Dataset

| Property | Value |
|---|---|
| Source | CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015 |
| Records | 253,680 |
| Features | 21 behavioral and demographic indicators |
| Target | `Diabetes_binary` — 0 (No Diabetes) / 1 (Diabetes) |
| Imbalance | ~14% positive class — addressed with SMOTE |

---

## Tech Stack

| Category | Libraries |
|---|---|
| ML Models | `lightgbm==4.6.0`, `xgboost==3.2.0`, `catboost==1.2.10`, `scikit-learn==1.8.0` |
| Imbalance | `imbalanced-learn==0.14.1` |
| Data | `pandas==2.3.3`, `numpy==2.4.3` |
| Visualization | `matplotlib==3.10.8`, `seaborn==0.13.2`, `plotly==6.6.0` |
| App | `streamlit==1.55.0` |
| Utilities | `scipy==1.17.1`, `joblib==1.5.3` |

---

## Disclaimer

This project is an academic graduation submission intended for educational and clinical decision support purposes only. It does not replace laboratory diagnosis or physician evaluation.
