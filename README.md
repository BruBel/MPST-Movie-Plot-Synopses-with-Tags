# MPST: Movie Plot Synopses with Tags

This project was developed to solve [MPST: Movie Plot Synopses with Tags](https://www.kaggle.com/rmisra/news-category-dataset) multi-label text classification problem. It's a complex dataset which deal with imbalanced data and 71 differents tags to predict!

Some technnologies of Machine Learning and Data Science used:

## Dealing with imbalanced data

- [Tune class weights](https://www.kaggle.com/eikedehling/exploring-class-imbalance-resampling-and-weights)
- [Up-sampling with sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html)

## Models

- Logistic Regression
- XGBoost Classifier

## API

- FastAPI

### Running

To clone and run this application:

```bash
# Clone this repository
$ git clone https://github.com/BruBel/MPST-Movie-Plot-Synopses-with-Tags

# Go into the repository
$ cd MPST-Movie-Plot-Synopses-with-Tags

# Install dependencies
$ pip install -r requirements.txt

# Go into API repository
$ cd code/api

# Run api
$ uvicorn main:app --host 0.0.0.0 --port 5058
```

Now there are two options:
- Go to http://localhost:5058/docs#/default/predict_category_predict_post
- Click in "Try it out" and fill in the JSON. Execute.

OR

- In terminal:

curl -X POST "http://localhost:5058/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"synopsis\":\"SYNOPSISEHERE\"}"




