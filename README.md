# kubernetes-data-science
Deploys a data science tool suite to a local Kubernetes distributed compute cluster.

Tool Suite:
  - Apache Spark
  - Jupyterlab notebook interface
  - Python interpreter with Pandas, Scikit-learn, Matplotlib, and Statsmodels
  - R statistics

Tool Suite Add-ons:
  - DataProfiler: Sensitive data detection, equiped with a pre-trained deep learning model identify sensitive data (PII / NPI).
  - DataComPy: Prints out a human-readable report summarizing and sampling differences between two pandas dataframes.
  - DataCompareR: Compare two R datasets and view a report on the similarities and differences.
  - Rubicon-ml: Captures and stores searchable model training and execution information, like parameters and outcomes, and display them in a dashboard. 
  - Synthetic-data: Sample data generation (https://github.com/capitalone/synthetic-data)
  - Jupyterlab templates: (https://github.com/jpmorganchase/jupyterlab_templates)


#

### Machine Learning Operations (MLOps):
- Deployment: single node bare metal (nerdctl)
- Deployment: single node kubernetes (kubectl)
- Deployemnt: cloud service provider kuberenetes: (aws eks / kubectl), (gcloud container clusters / kubectl), (az aks / kubectl)
- Shared notebooks and data access/transfers
- Logging and metrics
- Multi-format data ingest (HL7, SAS, CSV, XLSX, ZIP, TXT, JSON, XML, HTML, Images, HDF, PDF, DOCX, MP3, MP4...)
- Dataset clean-up and type conversion

### Opensource Analytics on Apache Spark:
(https://spark.apache.org/docs/latest/ml-statistics.html)
- Collinearity and covariance
- Boosting: RandomForest & XGBoost (Regressor and Classifier)
- Extracting, transforming and selecting features
- Classification and Regression
- Clustering
- Collaborative filtering
- Frequent Pattern Mining
- Model selection and tuning
- Limited-memory BFGS (L-BFGS)
- Normal equation solver for weighted least squares
- Iteratively reweighted least squares (IRLS)
- Clustering
- Dimensionality reduction
- Feature extraction and transformation
- Frequent pattern mining
- Evaluation metrics
- PMML model export
- Optimization
- Timeseries collection and analyis

##


![jupyterlab](https://user-images.githubusercontent.com/4974054/137600119-bdf4c50b-d649-40cd-89c9-76f2ea596d42.jpg)

![spark-kubernetes-notebook](https://user-images.githubusercontent.com/4974054/137775097-7d7eb98b-114c-4f8d-8c9a-3d849feb4ef0.jpg)

![spark-3 2-shell](https://user-images.githubusercontent.com/4974054/137662534-52214316-d289-43ad-968f-f14aa342d52d.jpg)

![kubernetes](https://user-images.githubusercontent.com/4974054/137600230-bb56dd0c-060f-4b01-b086-ed034d86c851.jpg)

![spark-kubernetes-notebook-images](https://user-images.githubusercontent.com/4974054/137789727-582313c0-df04-4776-aa6f-340363e7631a.jpg)

![kds-container-ui](https://user-images.githubusercontent.com/4974054/137663428-1fc82a4f-2d00-460a-9bd1-22a7ae3afb3c.jpg)
