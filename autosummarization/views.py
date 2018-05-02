from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from socket import socket,AF_INET,SOCK_STREAM

# Create your views here.

def client(content):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('192.168.1.103',50008))
    sock.send(content)
    reply = sock.recv(1024)
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
    print(summarization)
    # summarization = ch_content+'123123123'
    # c = Context({'Summarization': summarization, 'Content':ch_content})
    c = summarization
    # return HttpResponse(t.render(c))
    return HttpResponse(c, content_type = 'application/json')
