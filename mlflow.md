# Wine Quality Prediction - ML Project
---
## 🚀 Why I Switched from DVC to MLflow

Initially, I used **DVC** to version control datasets and model files, and to manage reproducible ML pipelines.

However, as the project matured, I needed:

- Native **experiment tracking**
- **Model registry** with version control
- Easier **deployment integrations**


## **MLflow** is a User Interface allows you to model tracking, experimenting, logging, you'll have model registry.

**MLflow** provided these features more natively and aligned better with the current stage of development. While DVC is powerful for data and pipeline versioning, MLflow simplifies **experiment tracking**, **logging**, and **deployment**, especially when integrated with Flask APIs.

## 1. Create a seperate branch
```bash
git checkout -b main-mlflow
```

### MLFLOW SERVER COMMANDS

-- Create a folder on the name artifacts
```bash
mkdir artifacts
```bash

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 1234
```


## ✅ Model Evaluation Criteria

| Metric | Description | Goal |
|--------|-------------|------|
| **MAE (Mean Absolute Error)** | Average absolute difference between predicted and actual values. | 🔽 Lower is better |
| **R² (Coefficient of Determination)** | Indicates how well the model explains the variance in the data. | 🔼 Higher is better |
| **RMSE (Root Mean Squared Error)** | Square root of the average squared differences between predicted and actual values. | 🔽 Lower is better |

---

## 🏆 Best Model Based on Metrics

| Run # | MAE ↓       | R² ↑         | RMSE ↓      | Alpha | l1_ratio |
|-------|-------------|--------------|-------------|--------|----------|
| 🟠 1   | 0.65707707  | 0.00955867   | 0.80452421  | 0.5    | 0.89     |
| ⚫ 2   | 0.65981843  | 0.00838218   | 0.80500189  | 0.88   | 0.89     |
| 🔴 3   | 0.65981843  | 0.00838218   | 0.80500189  | 0.88   | 0.89     |
| 🟡 **4**   | **0.65514628** | **0.01301496** | **0.80311923** | 0.9    | 0.4      |

✅ **Conclusion:**  
**Run #4** outperforms the others across all key metrics — it has the **lowest MAE**, **highest R²**, and **lowest RMSE**.  
Therefore, it is the **best model** among the evaluated runs.
