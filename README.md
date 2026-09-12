# AI/ML Task-1 — Student Performance Data Explorer

## Objective
Analyze student performance data by loading, cleaning, exploring and visualizing the dataset.

## Tools
- Python 3.12+
- Jupyter Notebook
- Pandas, NumPy, Matplotlib
- Git/GitHub

## Project Structure
```text
AI_ML_Task1_Student_Performance/
├── data/
│   └── student_performance.csv
├── notebooks/
│   └── Student_Performance_Data_Explorer.ipynb
├── src/
│   └── eda.py
├── reports/
│   ├── EDA_Report.pdf
│   └── figures/
└── screenshots/
```

## How to Run
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install numpy pandas matplotlib seaborn jupyter
jupyter notebook
```

Open `notebooks/Student_Performance_Data_Explorer.ipynb` and run all cells.

## Data Cleaning
The raw dataset intentionally contains a small number of missing values and duplicate rows so that the required cleaning steps can be demonstrated. Duplicate rows are removed and missing numeric values are filled using the median.

## EDA
The notebook includes:
- First 10 rows
- Dataset shape and columns
- Missing-value analysis
- Duplicate detection/removal
- Mean, median and mode
- Histogram
- Scatter plot
- Box plot
- Correlation heatmap
- Findings and conclusion

## Note
The student dataset in this project is a practice dataset created for Task-1 demonstration. It is not a real student's academic record.
