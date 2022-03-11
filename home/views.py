from django.shortcuts import render
import json
from .models import *
from datetime import datetime
# Create your views here.

def jsonread(data1):
    subject=data1
    # ls = subject[0:15]
    ls = subject
    ls_q = {}

    json_len = len(ls)

    for i in range(json_len):
        ls_q = ls[i]
        obj = jsonModel(**ls_q)
        obj.save()


    # get_all = jsonModel.objects.values('date', 'trade_code','high', 'low','open', 'close','volume')
    # get_all = jsonModel.objects.all()
    # get_all = jsonModel.objects.values('date', 'trade_code','high', 'low','open', 'close','volume')
    # get_all = jsonModel.objects.values_list('date', 'trade_code','high', 'low','open', 'close','volume')
    # ls_get_all = list(get_all)
    # print(type(ls_get_all))
    # ls_dict = dict(ls_get_all[0])

    # n_ls_dict = ls_dict
    # print(n_ls_dict)
    # print(ls)
    # v_ls1=[]
    # v_ls2=[]
    # for k,v in ls_dict.items():
        # if v == datetime():
        #     print(True)
        # print(False)
        # v_ls1.append(v)
    # for k,v in ls.items():
    #     v_ls2.append(v)
    # print(v_ls1)
    # print(v_ls2)


    # print(ls)
    # if ls == ls_get_all:
    #     print(True)
    # else:
    #     print(False)

    # for i in range(json_len):
    #     ls_q = ls[i]
    #     obj = jsonModel(**ls_q)
    #     obj.save()

        # ls_q.update(ls[i])
        # print(ls_q)
    

    # for i in ls:
    #     print(i)
    # ls_q = ls[0]
    # print(ls_q)
    # obj = jsonModel(**ls_q)
    # jsonModel.objects.all().delete()
    

    # ls_new = []
    # tuple_ls = ()
    # for key, value in ls_q.items():
        # ls_new.append(value)
        # print(type(key))
    #     obj = jsonModel(date=value, trade_code=value, high=value, low=value, open=value, close=value, volume=value)
    # obj.save()
    
    # key_ls = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']
    
    

def home(request):
    json_data = open('static/stock_market_data.json')

    data1 = json.load(json_data)
    data2 = json.dumps(data1)
    json_data.close()

    data1 = list(data1)
    
    context = {
        'data1':data1
    }

    # jsonread(data1)

    # b = jsonModel(date='2022-03-17', trade_code='1JANATAMF', high='4.3', low='4.1', open='4.2', close='4.1', volume='2285416')
    # b.save()
    # subject=data1
    # ls = subject[5]

    # print(len(subject))
    
    # for i in ls:
    #     print(i[0])

    # for i in subject:
    #     print(i)

    # for key, value in ls.items():
    #     print(value)


    return render(request, 'home/home.html',context)