from config import TARGET_COL

class Data_Preprocessor:
    '''
      Data Cleaning steps are documented in get_clean_dataset()
      Underscore prefix used for internal-access methods
    '''
    def __init__(self, df):
        self.df = df.copy(deep=True)
    
    def get_clean_dataset(self):
        for col in ['customer_status', 'churn_category', 'churn_reason']:
            self.df = self.df.drop(columns = col, errors='ignore')

        if TARGET_COL in self.df.columns:
            self._binarize_column(TARGET_COL)

        return self.df
    
    def _binarize_column(self, col_name):
        def binarize(value):
            if value in ['Yes']:
                return 1
            elif value in ['No']:
                return 0
        self.df[col_name] = self.df[col_name].apply(binarize)