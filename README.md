# *One click* kubernetes-data-science
One click deploys a data science tool suite to a local Kubernetes distributed compute cluster by helping to integrate a broad spectrum of high quality opensource software.  Each tool is made available depending on use case, without requiring the end user to seek out, individually install, configure, update, and integrate disparate tooling into new or existing analysis workflows. 

Each component dependency is pulled from each respective upstream project and/or docker repository, and no upstream code is ever modified. Different industries and user roles have varied needs; as such the platform is fully customizable in that analytic containers can be added, removed, or rolled back to earlier versions depending on host infrastructure and the applicable template.

Use on-prem Kubernetes or Okteto Cloud: Managed Kubernetes service designed for developers. Free developer accounts. The apps sleep after 24 hours of inactivity.
Details: https://okteto.com/docs/cloud

### *Browser navigate to unique link generated under "Endpoints:"*

#
![kubernetes-datascience-launcher](https://user-images.githubusercontent.com/4974054/138598007-ecfa1e11-0418-45a2-b3ad-4027995eb406.jpg)
#
### R Spreadsheet Analytics (Jamovi):

  - Opensource alternative to SPSS, MATLAB, Statistica, and SAS.

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/alexander-manley/kubernetes-jamovi-launcher)

#

### Jupyter-Spark Tool Suite:
  - Apache Spark
  - Jupyterlab notebook interface
  - Python interpreter with Pandas, Scikit-learn, Matplotlib, and Statsmodels
  - R statistics

Launch, startup can take up to 10 minutes:

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/alexander-manley/kubernetes-datascience-launcher)

#

### Dataiku Data Science Studio (DSS):
  - Free edition
  - Data preparation and model management

Launch, startup can take up to 10 minutes:

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/alexander-manley/kubernetes-data-science-dataiku-dss-launcher)

#

### RAPIDS/DASK Distributed Machine Learning:

  - Distributed python clustering and regression algorithms

Launch, startup can take up to 10 minutes, requires account upgrade for sufficient compute resource allocation:

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/alexander-manley/kubernetes-data-science-dask-rapids-launcher)

#

### MLFlow:

- Track experiments to record & compare parameters and results (MLflow Tracking).

- Packaging ML code in a reproducible form to share with data scientists or transfer to production (MLflow Projects).

- Manage and deploy models from a variety of ML libraries to a variety of model serving and inference platforms (MLflow Models).

- Provide a central model store to collaboratively manage the full lifecycle of an MLflow Model, including model versioning, stage transitions, and annotations (MLflow Model Registry).

[![Launch MLFlow Now](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/alexander-manley/kubernetes-mlflow-launcher)

#

### Tensorflow Notebook:

  - Training and inference of deep neural networks

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/alexander-manley/kubernetes-tensorflow-launcher)

#

### Additional Opensource ML Platforms:

Seldon: https://github.com/SeldonIO/seldon-core
(https://github.com/SeldonIO/seldon-core/tree/master/helm-charts/seldon-core-operator)

Generic Kubeflow via Kustomize manifests: https://github.com/kubeflow/manifests

Polyaxon: https://github.com/polyaxon/polyaxon

DVC: https://github.com/iterative/dvc

ClearML: https://github.com/allegroai/clearml/

Guild AI: https://github.com/guildai/guildai

Sacred: https://github.com/IDSIA/sacred

Tensorboard: https://github.com/tensorflow/tensorboard


### SaaS Enterprise Alternatives:

AWS Sagemaker

Azure ML Studio

Google Vertex AI

Neptune AI (Warsaw)

Comet (Tel Aviv, NY)

Pachyderm (San Francisco)

Weights & Biases (San Francsico)

#

### Tool Suite Add-ons:
  - DataProfiler: Sensitive data detection, equiped with a pre-trained deep learning model identify sensitive data (PII / NPI).
  - DataComPy: Prints out a human-readable report summarizing and sampling differences between two pandas dataframes.
  - DataCompareR: Compare two R datasets and view a report on the similarities and differences.
  - Rubicon-ml: Captures and stores searchable model training and execution information, like parameters and outcomes, and display them in a dashboard. 
  - Synthetic-data: Sample data generation (https://github.com/capitalone/synthetic-data)
  - Jupyterlab templates: (https://github.com/jpmorganchase/jupyterlab_templates)

### Kubeflow (K3ai) Add-ons:
- argo-workflow:                  Argo Workflow plugin
- h2o-single:                     H2O.ai
- jupyter-minimal:                Minimal Jupyter Configuration
- katib:                          Kubeflow Katib
- kf-pipelines-tekton:            Kubeflow Pipelines based on Tekton
- kubeflow-pipelines:             Kubeflow Pipelines platform agnostic
- mpi-op:                         MPI-Operator
- nvidia-gpu:                     Nvidia GPU support
- pytorch-op:                     Pytorch op
- tekton:                         Kubeflow Pipelines based on Tekton
- tensorflow-op:                  Kubeflow Tensorflow

### Pipeline Integration:

- Apache Airflow
- Luigi
- Prefect
- Argo
- KubeFlow
- MLFlow

- Modin backend: https://github.com/ray-project/ray

#

### Machine Learning Operations (MLOps):
- Deployment: single node bare metal (nerdctl)
- Deployment: single node kubernetes (kubectl)
- Deployemnt: cloud service provider kuberenetes: (aws eks / kubectl), (gcloud container clusters / kubectl), (az aks / kubectl)
- Shared notebooks and data access/transfers
- Logging and metrics
- Multi-format data ingest (HL7, SAS, CSV, XLSX, ZIP, TXT, JSON, XML, HTML, Images, HDF, PDF, DOCX, MP3, MP4...)
- Dataset clean-up and type conversion
- Lifecycle management (https://github.com/mlflow/mlflow/releases)

![kubeflow-katib](https://user-images.githubusercontent.com/4974054/139364088-afbfed2f-35a9-40a7-a41c-ee0ccc289b88.jpg)

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
- Interpretability (https://github.com/interpretml/interpret/releases)
- Dashboarding (https://github.com/apache/superset/releases)

### Data layer
- Trino (PrestoSQL) multi-source database ingest
- Pixie Kubernetes metrics (https://docs.px.dev/installing-pixie/install-guides/self-hosted-pixie)
- FastAPI, Django, and Flask endpoints
- Text indexing and search (Elasticsearch) (https://github.com/opensearch-project/OpenSearch/releases)
- ETL / singer formater (https://pypi.org/project/meltano/#history)
- External data versioning and rollback (https://github.com/treeverse/lakeFS/releases)
- Spark versioning and rollback (https://github.com/delta-io/delta/releases)

##

## ML Model Monagement

![jupyterlab](https://user-images.githubusercontent.com/4974054/137600119-bdf4c50b-d649-40cd-89c9-76f2ea596d42.jpg)

![spark-kubernetes-notebook](https://user-images.githubusercontent.com/4974054/137775097-7d7eb98b-114c-4f8d-8c9a-3d849feb4ef0.jpg)

![spark-3 2-shell](https://user-images.githubusercontent.com/4974054/137662534-52214316-d289-43ad-968f-f14aa342d52d.jpg)

![kubeflow](https://user-images.githubusercontent.com/4974054/138380876-38345266-c31b-4c32-8eb0-3f22d84f03e8.jpg)

## K3S Kubernetes Container Image Management

![kubernetes](https://user-images.githubusercontent.com/4974054/137600230-bb56dd0c-060f-4b01-b086-ed034d86c851.jpg)

![spark-kubernetes-notebook-images](https://user-images.githubusercontent.com/4974054/137789727-582313c0-df04-4776-aa6f-340363e7631a.jpg)

![k3s-images](https://user-images.githubusercontent.com/4974054/139365312-9c07c716-0c0c-4525-8fc5-a6307d6b7c8a.jpg)

### CI/CD

![kds-container-ui](https://user-images.githubusercontent.com/4974054/137663428-1fc82a4f-2d00-460a-9bd1-22a7ae3afb3c.jpg)
