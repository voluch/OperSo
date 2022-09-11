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
                            for x in tqdm(self.df.loc[:, 'input'].tolist())]
        else:
            print(self.df.loc[:, 'input'].tolist())
            self.df['X'] = [x.lower() for x in tqdm(self.df.loc[:, 'input'].tolist())]
        return self.df
