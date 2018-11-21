# #!/bin/python3
from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=itemgetter(k)):
        print(*i)



AutoMLE2E


from pipelineblocksdk.data.spark.SparkConfCustom import SparkConfCustom

t1 = time.time()

spark = SparkConfCustom.get_spark_session(program_arguments)
self.logger.info('Spark Session created...')

spark.sparkContext.setLogLevel('ERROR')

### PRELOAD
from automl.feature_creation import TargetMeanEncoder, PCATransformer, ClusterFeature, WeightOfEvidenceEncoder, \
    FrequencyEncoder
from automl.pipeline.feature_engineering_pipeline import FeatureEngineeringPipeline
from automl.constants.naming_constants import ModelTunerKeys, ModelTunerNamingConvention
from automl.preprocessing import random_sampler
from automl.model_selection import TrainTestValidator_Dev
from automl.communications.comms import AutoMLSession
from automl.model_selection.metrics import Metrics

mtk = ModelTunerKeys()
mt_nc = ModelTunerNamingConvention()
metrics = Metrics()
tme_transformer = TargetMeanEncoder()
pca_transformer = PCATransformer()
cf_transformer = ClusterFeature()
woe_transformer = WeightOfEvidenceEncoder()
fe_transformer = FrequencyEncoder()
steps = [tme_transformer, pca_transformer, cf_transformer, woe_transformer, fe_transformer]
"""data_mapr = {
"adult_income":load_adult_income,
"breast_cancer_wisconsin":load_breast_cancer_wisconsin,
"titanic":load_titanic,
"pima_diabetes":load_pima_diabetes,
}"""

### INPUT JSON
input_json = {
    "url": "http://49.204.93.177:8050/rest",
    "pid": "39f3a6e3-346c-49d9-a805-359e56bef8a1",
    "eid": "1",
    "objective": "accuracy",
    "dataset_name": "boston_house_prices",
    "train_ratio": 0.8,
    "test_ratio": 0.2,
    "num_iter": 10,
    "post": False,
    "stratified": False
}

# INPUT CONFIGURATIONS
post = input_json["post"]
url = input_json["url"]
pid = input_json["pid"]
eid = input_json["eid"]
num_iter = input_json["num_iter"]
train_ratio = input_json["train_ratio"]
test_ratio = input_json["test_ratio"]
objective = input_json["objective"]
stratified = input_json["stratified"]
aml_sess = AutoMLSession(pid, eid, url)

# LOAD DATA
data_path = f'hdfs://bb-workspace-hdfs:9000/hdfs/Data/9eb64173-f341-4640-ab21-7725a0310a94/breast-cancer-wisconsin.csv'

X = spark.read.csv(data_path, header=True, inferSchema=True)
target_col = 'malignant'
prob_type = mtk.bnry_clf
id_cols = []

X_train, X_test = random_sampler(X, train_ratio=train_ratio, test_ratio=test_ratio)

### FEATURE ENGINEERING
fep = FeatureEngineeringPipeline(aml_sess)
fep.fit(steps, X_train, target_col, prob_type, stratified=False, objective=objective, id_cols=id_cols)
X_train_w_fs = fep.transform(X_train, assemble_index=True)
X_test_w_fs = fep.transform(X_test, assemble_index=True)

### MODEL SELECTION
if prob_type in [mtk.bnry_clf, mtk.multi_clf]:
    estimators = [mtk.logistic_clf, mtk.random_forest_clf, mtk.decision_tree_clf]  # , mtk.xgb_clf]
else:
    estimators = [mtk.linear_reg, mtk.random_forest_reg, mtk.decision_tree_reg]  # , mtk.xgb_reg]

ttv = TrainTestValidator_Dev(aml_sess, estimators, prob_type, objective, target_levels=fep.target_levels,
                             input_vector_col=mt_nc.features, nrows=fep.nrows, model_optimizer='auto',
                             num_iter=num_iter, post=post, url=url)
ttv.fit(target_col, X_train_w_fs, X_test_w_fs, validation=None)

t2 = time.time()

self.logger.info('Total time taken to run Logistic, Random and Decision: ' + str(t2 - t1) + 'secs.')

# End of code
