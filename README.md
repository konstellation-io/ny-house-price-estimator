# NY House Price Estimator

## Aim

This is an example repository illustrating the use of KDL on a simple machine learning classification task. 

In this project, the aim is to create an estimator for the price of a rental property in New York. We are using a publicly available dataset containing property attributes such as type of property (house, apartment, etc.), number of bedrooms and bathrooms, neighbourhood, and amenities (such as breakfast, TV, internet, WiFi, etc.). Our aim is to create a classification model that can use the aforementioned attributes to predict whether the rental price of the property falls within the low-, mid-, high- or luxury-priced category. The data are imbalanced, since there are much more low- and mid-priced properties than luxury-priced properties, requiring us to handle class balance in model training.

## Project structure

The project repository has the following directory structure:

```
├── goals         <- Acceptance criteria (typically as automated tests describing desired behaviour)
│
├── lab
│   │
│   ├── analysis  <- Analyses of data, models etc. (notebooks)
│   │
│   ├── lib       <- Importable functions used by analysis notebooks and processes scripts
│   │                (including unit tests)
│   │
│   └── processes           <- Source code for reproducible workflow steps.
│       ├── preprocess_data
│       │   └── main.py
│       ├── train_model
│       │   └── main.py
│       └── config.ini         <- Config for Drone runs
|
├── runtimes      <- Code for generating deployment runtimes (.krt)
│
├── .drone.yml    <- Instructions for Drone runners
├── .env          <- Local environment variables for VScode IDE
├── .gitignore    
└── README.md     <- Main README
```


## Launching experiment runs (Drone)

To enable full tracability and reproducibility, all executions that generate results or artifacts
(e.g. processed datasets, trained models, validation metrics, plots of model validation, etc.)
are run on Drone runners instead of the user's Jupyter or Vscode tools.

Pipeline execuitions are launched by the trigger specified in `.drone.yml` for each pipeline.
An example is shown below:

```yaml
trigger:
  ref:
    - refs/tags/preprocess-data-*
```

With this trigger in place, the pipeline will be executed on Drone agents whenever a tag matching the pattern specified in the trigger is pushed to the remote repository, for example:

```bash
git tag preprocess-data-v0
git push origin preprocess-data-v0
```

Note: When using an external repository (e.g. hosted on Github), a delay in synchronization between Gitea and the mirrored external repo may cause a delay in launching the pipeline on the Drone runners.
This delay can be overcome by manually forcing a synchronization of the repository in the Gitea UI Settings.

## Testing

The repository contains some unit tests, e.g. in `lab/lib/data_processing_test.py`.

To run the tests, you may use the terminal:

```bash
~/repos/ny-house-price-estim$ pytest lab
```

... or the various GUI options provided in VS Code for running tests.