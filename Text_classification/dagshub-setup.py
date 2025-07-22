import dagshub
dagshub.init(repo_owner='Gauti22',repo_name='Text_classification',mlflow=True)

import mlflow
mlflow.set_tracking_uri('https://dagshub.com/Gauti22/Text_classification.mlflow')
with mlflow.start_run():
    mlflow.log_param('parameter_value','name')
    mlflow.log_metric('metric name',1)