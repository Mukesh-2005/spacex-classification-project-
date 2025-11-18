# 🚀 Lab 8 Summary: Final Model Evaluation on Falcon 9 Dataset
## 📌 Dataset and Preprocessing
- The dataset contains 83 feature columns (X) and one target column (Class) representing successful (1) or failed (0) Falcon 9 landings.
- Features were standardized before model training.
- The data was split using an 80/20 train-test split, resulting in approximately 18 samples in the test set (Y_test).

# 🧠 Models and Hyperparameter Tuning
 Four classification models were trained and tuned using 10-fold cross-validation via GridSearchCV:
 ## Logistic Regression
- Tuned over regularization strength (C values of 0.01, 0.1, and 1)
- Used L2 penalty with the 'lbfgs' solver
 ## Support Vector Machine (SVM)
- Explored multiple kernels: linear, rbf, poly, and sigmoid
- Tuned over a logarithmic range of C and gamma values
 ## Decision Tree Classifier
- Tuned across multiple criteria (gini, entropy), splitters (best, random), and depths
- Included variations in max_features, min_samples_leaf, and min_samples_split
 ## K-Nearest Neighbors (KNN)
- Tuned over n_neighbors from 1 to 10
- Evaluated different algorithms (auto, ball_tree, kd_tree, brute) and distance metrics (p = 1 for Manhattan, p = 2 for Euclidean)

# 📊 Model Performance on Test Set
| Model  | Accuracy on Unseen Data | 
|----- | -- | 
|Logistic Regression  | 83.33% | 
| SVM |83.33%  | 
| KNN | 83.33% | 
|***Decision Tree***| ***88.89%***|


# ✅ Conclusion
All models performed reasonably well on the unseen test data, achieving over 83% accuracy. However, the Decision Tree Classifier outperformed the others with an accuracy of 88.89%, making it the best-performing model for this classification task.

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: November 2025



