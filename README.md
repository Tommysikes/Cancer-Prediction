## Breast Cancer Prediction Model
Welcome to the Breast Cancer Prediction Model project, where we delve into the realm of machine learning to classify breast cancer cases as benign or malignant. Additionally, we aim to predict the recurrence and non-recurrence of malignant cases after a certain period. To achieve this, we've harnessed the power of various machine learning classification methods to develop a robust model that predicts discrete class outcomes for new input data.

## Goal
The primary goal of this project is to build a classification model that can accurately predict whether breast cancer cases are benign or malignant. Furthermore, the model aims to forecast the recurrence and non-recurrence of malignant cases within a specific time frame.

## Libraries Used
The project extensively employs the following libraries:

**pandas**: For data manipulation and analysis.
**numpy**: For mathematical operations and array handling.
**matplotlib.pyplot**: For data visualization and plotting.
**sklearn**: For machine learning tasks, including preprocessing, model building, and evaluation.
**seaborn**: For enhanced data visualization and exploratory analysis.
## Project Flow
### Data Preparation:

Data is loaded using pandas.
Necessary preprocessing steps are performed, including data cleaning and handling missing values.
Data is split into features (input) and target (output) variables.
### Data Exploration and Visualization:

matplotlib.pyplot and seaborn are utilized for data visualization.
Exploratory data analysis is conducted to understand the dataset's characteristics and relationships.
### Data Preprocessing:

StandardScaler from sklearn.preprocessing is used to standardize the features, ensuring fair comparison.
### Model Selection and Training:

Two classification algorithms are employed: SVC (Support Vector Classification) and RandomForestClassifier.
Both models are trained on the preprocessed dataset.
### Model Evaluation:

Cross-validation is performed using cross_val_score and KFold to assess the models' performance.
The accuracy score and confusion matrix are used as evaluation metrics.
### Model Deployment:
FrontEnd was created using streamlit and deployed locally
