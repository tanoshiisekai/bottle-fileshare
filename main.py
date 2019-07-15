import bottle
import tornado
import os
import urllib.parse


@bottle.route('/upload', method="POST")
def do_upload():
    upload = bottle.request.files.get('upload')
    filespath = os.getcwd()+"/files/"
    filename = upload.raw_filename
    print(filename)
    filestream = upload.file.read()
    if filename:
        fp = open(filespath + filename, "wb")
        fp.write(filestream)
        fp.close()
    bottle.redirect('/')


def getfiles():
    filels = []
    filespath = os.getcwd() + "/files/"
    for files in os.walk(filespath):
        for f in files[2]:
            filels.append(("/files/"+f, f))
    return filels[:]


@bottle.route("/deletefile")
def deletefile():
    fileurl = bottle.request.GET.fileurl
    os.remove(os.getcwd()+fileurl)
    bottle.redirect("/")


@bottle.route("/")
def index():
    files = getfiles()
    files.sort()
    return bottle.template('index', filelist=files)


@bottle.route("/files/<filename>")
def download(filename):
    filespath = os.getcwd() + "/files/"
    filename = urllib.parse.unquote(filename)
    return bottle.static_file(filename, root=filespath, download=filename)




bottle.debug(True)
bottle.run(host="localhost", port=8080, server="tornado", reloader=True)
