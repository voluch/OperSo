import os
import pandas as pd
import werkzeug
from flask import Flask, Response
from flask import render_template, make_response, redirect, url_for, send_from_directory
from flask_restful import Resource, Api, reqparse
import json
from src.models.clustering import Cluster

Upload = 'upload'
app = Flask(__name__)
api = Api(app)
app.config['uploadFolder'] = Upload
app.static_folder = 'static'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['GET'])
def download():
    uploads = os.path.join(app.root_path, app.config['uploadFolder'])
    return send_from_directory(uploads, 'result.csv', as_attachment=True)


class Result(Resource):
    def __init__(self):

        self.parse = reqparse.RequestParser()
        self.parse.add_argument('csv_file', type=werkzeug.datastructures.FileStorage, location='files', required=True)
        self.parse.add_argument('min_input', default=0, type=int, location='form')
        self.parse.add_argument('check_translate', default=False, type=bool, location='form')
        self.cluster = Cluster('paraphrase-multilingual-mpnet-base-v2')
        # self.cluster = Cluster('distiluse-base-multilingual-cased-v2')

    def get(self):
        return redirect(url_for('index'))

    def post(self):
        args = self.parse.parse_args()
        _input = args['csv_file']
        _min = args['min_input']
        _translate = args['check_translate']
        try:
            df = pd.read_csv(_input)
            result = self.cluster.apply(df, _min, _translate)
            self.cluster.df.to_csv(os.path.join(app.config['uploadFolder'],
                                                f'result.csv'), index=False)
            self.cluster.clear_tags()
            return make_response(render_template('result.html', tags=result), 200)
        except:
            return Response(status=503, response=json.dumps({"message": "Smth wrong"}))


api.add_resource(Result, '/result')

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8090))
    HOST = os.getenv("HOST", "0.0.0.0")
    app.run(port=PORT,
            host=HOST,
            debug=True)
