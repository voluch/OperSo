from googletrans import Translator


class Preprocessor:
    def __int__(self):
        self.df = None

    def translate(self):
        translator = Translator()
        self.df['X'] = [translator.translate(x, dest='uk').text for x in self.df[0].tolist()]

    def fit(self, df):
        self.df = df
        self.translate()
        return self.df
