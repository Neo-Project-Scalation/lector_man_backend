from flask import Flask, send_from_directory
from flask_restful import Resource, Api, abort
from os import scandir, getcwd
from os.path import abspath

app = Flask(__name__)
api = Api(app)


class GetMangaChapter(Resource):
    @staticmethod
    def get(manga, chapter):
        images = []
        for arch in scandir(getcwd() + '\\static\\mangas\\' + manga + '\\' + chapter):
            images.append({"nombre": arch.name, "link": '/static/mangas/'+manga+'/'+chapter+'/'+arch.name})
        return {"manga": manga, "chapter": chapter, "images": images}


api.add_resource(GetMangaChapter, '/<manga>/<chapter>')

if __name__ == '__main__':
    app.run()
