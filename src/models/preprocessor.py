from googletrans import Translator
from tqdm import tqdm


class Preprocessor:
    def __init__(self):
        self.df = None
        self.translator = Translator()

    def apply(self, df, _translate):
        self.df = df.copy()
        if _translate:
            self.df['X'] = [self.translator.translate(x.lower(), dest='uk').text
                            for x in tqdm(self.df.iloc[:, 0].tolist())]
        else:
            self.df['X'] = [x.lower() for x in tqdm(self.df.iloc[:, 0].tolist())]
        return self.df
