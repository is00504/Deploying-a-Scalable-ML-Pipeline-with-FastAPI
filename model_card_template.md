# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This Random Forest Classification model, trained on 1994 census data, predicts income greater than $50k/yr.

## Intended Use
This model was developed as a part of a academic project. It is used to predict income that exceeds $50k/yr based on socioeconomic and demographic features. 
## Training Data
This model is trained on the Census Income-UCI machine learning repository dataset. It consists of 14 features that make up demographic and socioeconomic attributes, these features include:

- Age
- Work class
- Education
- Education-num
- Marital status
- Occupation
- Relationship
- Race
- Sex
- Capital gain
- Capital loss
- Hours per week
- Native country
- Income (target: >$50K or <=$50K)

## Evaluation Data
The evaluation data is 20% of the dataset, it retains the same feature distribution as the training data. All preprocessing steps applied to the training data are also applied to the evaluation data to ensure consistency. 

## Metrics
These are the metrics used to assess the performance of this model:

Precision: 0.7465 | Recall: 0.6391 | F1: 0.6886


## Ethical Considerations
This model is developed for academic use only. Although the dataset contains real-world data it is outdated and should not be used for any real-time production without a proper ethical review or bias assessment.

## Caveats and Recommendations
The dataset contains historical information from a 1994 census database and is intended for educational purposes only. 