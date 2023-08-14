from sklearn.model_selection import train_test_split
import model_evaluation as me
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


class model:

    def __init__(self, train_set, col_list, credit_or_star):
        self.true_model = None
        self.y_pred = None
        self.train_set = train_set
        self.credit_or_star = credit_or_star
        self.col_list = col_list
        self.X_train, self.X_test, \
            self.y_train, self.y_test = train_test_split(train_set[self.col_list],
                                                         train_set[self.credit_or_star + '_level'], test_size=0.3,
                                                         random_state=0)

    def xgboost(self):
        print('XGBoost')
        le = LabelEncoder()
        self.y_train = le.fit_transform(self.y_train)
        self.true_model = xgb.XGBClassifier()
        self.true_model.fit(self.X_train, self.y_train)
        # 预测
        y_predict = self.true_model.predict(self.X_test)
        y_predict = le.inverse_transform(y_predict)
        return y_predict

    def decision_tree(self):
        print('决策树')
        self.true_model = DecisionTreeClassifier(criterion='gini', random_state=0)
        self.true_model.fit(self.X_train, self.y_train)
        # 预测
        y_predict = self.true_model.predict(self.X_test)
        return y_predict

    def random_forest(self):
        print('随机森林')
        self.true_model = RandomForestClassifier()
        self.true_model.fit(self.X_train, self.y_train)
        # 预测
        y_predict = self.true_model.predict(self.X_test)
        return y_predict

    def logistic_regression(self):
        print('逻辑回归')
        self.true_model = LogisticRegression()
        self.true_model.fit(self.X_train, self.y_train)
        # 预测
        y_predict = self.true_model.predict(self.X_test)
        return y_predict

    def train(self):
        print('开始训练')
        # self.y_pred = self.xgboost()
        # self.y_pred = self.decision_tree()
        self.y_pred = self.random_forest()
        # self.y_pred = self.logistic_regression()

    def evaluate(self):
        print('开始评估')
        save_path = 'confusion_matrix_lr.png'
        if self.credit_or_star == 'star':
            class_names = ['1', '2', '3', '4', '5', '6']
            me.plot_confusion_matrix(self.y_test, self.y_pred, class_names, save_path)
        me.count_accuracy_and_more(self.y_test, self.y_pred)

    def predict_test(self, test_set, col_list):
        pred = self.true_model.predict(test_set[col_list])
        pred = pred.astype(int)
        return pred
