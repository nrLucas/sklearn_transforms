from sklearn.base import BaseEstimator, TransformerMixin

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
rm_columns.fit(X=df_data_1)
df_data_2 = pd.DataFrame.from_records(
    data=rm_columns.transform(
        X=df_data_1
    ),
)

rm_columns2.fit(X=df_data_2)
df_data_3 = pd.DataFrame.from_records(
    data=rm_columns2.transform(
        X=df_data_2
  ),
)

rm_columns3.fit(X=df_data_3)
df_data_4 = pd.DataFrame.from_records(
    data=rm_columns3.transform(
        X=df_data_3
   ),
)

rm_columns4.fit(X=df_data_4)
df_data_5 = pd.DataFrame.from_records(
    data=rm_columns4.transform(
        X=df_data_4
   ),
)

rm_columns5.fit(X=df_data_5)
df_data_6 = pd.DataFrame.from_records(
    data=rm_columns5.transform(
        X=df_data_5
   ),
)

rm_columns6.fit(X=df_data_6)
df_data_7 = pd.DataFrame.from_records(
    data=rm_columns6.transform(
        X=df_data_6
   ),
)

rm_columns7.fit(X=df_data_7)
df_data_8 = pd.DataFrame.from_records(
    data=rm_columns7.transform(
        X=df_data_7
   ),
)

rm_columns8.fit(X=df_data_8)
df_data_9 = pd.DataFrame.from_records(
    data=rm_columns8.transform(
        X=df_data_8
   ),
)

rm_columns9.fit(X=df_data_9)
df_data_10 = pd.DataFrame.from_records(
    data=rm_columns9.transform(
        X=df_data_9
   ),
)
