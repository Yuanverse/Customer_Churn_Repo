from sklearn.metrics import roc_auc_score, precision_score, \
    recall_score, f1_score
from sklearn.model_selection import train_test_split
from config import TEST_SIZE, RANDOM_SEED


class ModelEvaluator:
    '''
        Model-agnostic & metric-agnostic evaluator.
        Currently supports AUC, precision, recall, and F1 score
    '''
    supported_metrics = ['auc', 'precision', 'recall', 'f1']

    def __init__(self, model, X, y):
        self.model = model
        self.X = X
        self.y = y

    def evaluate(self, metric_list):

        X_train, X_test, y_train, y_test = \
            train_test_split(self.X, self.y, test_size=TEST_SIZE, random_state=RANDOM_SEED)
        self.model.train(X_train, y_train)

        metrics_dict = {}
        for metric in metric_list:
            if metric == 'auc':
                y_pred = self.model.predict_proba(X_test)
            else:
                y_pred = self.model.predict(X_test)
            metrics_dict[metric] = self._calculate(metric, y_test, y_pred)

        return metrics_dict

    def _calculate(self, metric, true_labels, pred_labels):
        assert metric in self.supported_metrics
        metric_map = {
            'auc': roc_auc_score,
            'precision': precision_score,
            'recall': recall_score,
            'f1': f1_score
        }
        # To minimize code repetition, use dict to map metric to sklearn fn
        return metric_map[metric](true_labels, pred_labels)