from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
import socket

# Create your views here.
host = socket.gethostbyname(socket.gethostname())
port = 50008
def client(content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    sock.send(bytes(content,encoding='utf8'))
    reply = (sock.recv(1024)).decode()
    sock.close()
    print('client got:[%s]' % reply)
    return reply

def index(request):
    # t = loader.get_template("index.html")
    # c = Context({})
    # return HttpResponse(t.render(c))
    return render(request,'index.html')

def submit(req):
    # t = loader.get_template("index.html")
    ch_content = ''
    if req.POST:
        if 'ch_content' in req.POST:
            ch_content = req.POST['ch_content']
            print(ch_content)
    summarization = client(ch_content)
    summarization = summarization.replace('BEG','')
    summarization = summarization.split('END')[0]
    response = {'summarization':summarization}
    print(response)
    # return HttpResponse(t.render(c))
    return HttpResponse(json.dumps(response), content_type = 'application/json')
