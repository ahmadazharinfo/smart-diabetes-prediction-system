
```text
Final_Project_Submission/
│
├── README.txt                                         # Master submission overview
│
├── Graduation_Project_Files/
│   │
│   ├── Dataset/
│   │   └── BRFSS2015.csv                              # The raw 253,680 record dataset
│   │
│   ├── Notebooks/
│   │   ├── 01_Data_Loading_and_EDA.ipynb
│   │   ├── 02_Preprocessing.ipynb
│   │   ├── 03_Baseline_Models.ipynb
│   │   ├── 04_Feature_Engineering.ipynb
│   │   ├── 05_Model_Selection_and_Tuning.ipynb
│   │   └── 06_Final_Results_and_Pipeline.ipynb
│   │
│   ├── Outputs_Folder/
│   │   ├── pipeline/
│   │   │   └── full_pipeline_bundle.pkl               # Serialized LightGBM & Scalers
│   │   ├── plots/
│   │   │   ├── 01_scaled_distributions.png
│   │   │   ├── 01_three_phase_comparison.png
│   │   │   ├── 02_smote_demo.png
│   │   │   └── 04_cm_all_thresholds.png
│   │   └── reports/
│   │       ├── final_summary.json
│   │       └── final_summary.pkl
│   │
│   └── Streamlit_App/
│       ├── app.py                                     # Web interface code
│       ├── requirements.txt                           # pandas, lightgbm, streamlit, etc.
│       └── models/
│           └── full_pipeline_bundle.pkl               # Copy of the model for the app to run
│
└── Graduation_Research_Files/
    │
    ├── PDF/
    │   ├── Final_Thesis_Smart_Diabetes_Prediction.pdf # All chapters merged into one
    │   ├── 0. PreliminaryPages.pdf
    │   ├── 1. ChapterOne_Introduction.pdf
    │   ├── 2. ChapterTwo_LiteratureReview.pdf
    │   ├── 3. ChapterThree_Methodology.pdf
    │   ├── 4. ChapterFour_ResultsAndDiscussion.pdf
    │   ├── 5. ChapterFive_ConclusionAndFutureWork.pdf
    │   ├── 6. ResearchSummary.pdf
    │   └── 7. References.pdf
    │
    └── WORD/
        ├── 0. PreliminaryPages.docx
        ├── 1. ChapterOne_Introduction.docx
        ├── 2. ChapterTwo_LiteratureReview.docx
        ├── 3. ChapterThree_Methodology.docx
        ├── 4. ChapterFour_ResultsAndDiscussion.docx
        ├── 5. ChapterFive_ConclusionAndFutureWork.docx
        ├── 6. ResearchSummary.docx
        └── 7. References.docx

```
