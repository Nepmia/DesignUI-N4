from flask import Flask, render_template,request, redirect
from flask_thumbnails import Thumbnail


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='template')


@app.route('/')
def testhome(name=None):
    return print('client connected')

if __name__ == '__main__' : 
    app.run()



# @app.route('/')
# def dsuimain(name=None):
#     url = "https://ui.nepmia.fr/home"
#     if not user_is_dev():
#         return render_template('dm.html')
#     else:
#         return redirect(url, code=302)

# @app.route('/<content>')
# def content(content):
#     if not user_is_dev():
#         return render_template('dm.html')
#     else:
#         url = "https://ui.nepmia.fr/"
#         if content == "home":
#             title="Home"
#             return render_template('base.html', content=content, title=title,url=url)
#         elif content in ['animations','brandings']:
#             if content == "animations":
#                 content_thumbs = os.listdir(os.path.join(
#                                         app.static_folder,
#                                         f'content/{content}/thumbs/'))
#                 title="Animations"
#                 return render_template('base.html',
#                                         content=content, 
#                                         title=title,
#                                         url=url, 
#                                         content_thumbs=content_thumbs)
#             elif content == "brandings":
#                 title="Brandings"
#                 content_images = os.listdir(os.path.join(
#                     app.static_folder,
#                      f'content/brandings/images/'
#                     ))
#                 folder_root = os.path.join(app.static_folder,f'content/brandings/folders/')
#                 folder_dict = {k:v for k, x, v in os.walk(folder_root)}
#                 del folder_dict[folder_root]
#                 return render_template('base.html', 
#                                         content=content, 
#                                         title=title, 
#                                         url=url,
#                                         folder_dict=folder_dict,
#                                         content_images=content_images)
#         else:
#             return render_template('404.html')

# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html'), 404

# def folder_scan(content_folders):
#     for each in content_folders:
#         content_fold_imgs = os.listdir(os.path.join(
#             app.static_folder,
#             f'content/brandings/folders/{each}'
#         ))
#         return content_fold_imgs

# def user_is_dev():
#     uIP = request.environ.get('HTTP_X_FORWARDED_FOR')
#     if not DEVMODE:
#         print('true')
#         return True
#     elif uIP in DEVIP:
#         print('true')
#         return True
#     else:
#         print('false')
#         return False