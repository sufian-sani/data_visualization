from unittest import result
from django.shortcuts import render, HttpResponseRedirect, reverse
import json
from .models import *
from datetime import datetime
from .forms import *
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
    
def resetdata(request):
    jsonModel.objects.all().delete()
    json_data = open('static/stock_market_data.json')

    data1 = json.load(json_data)
    data2 = json.dumps(data1)
    json_data.close()

    data1 = list(data1)
    jsonread(data1)
    return HttpResponseRedirect(reverse('home:home'))


def home(request):

    # line chart

    get_all_close = jsonModel.objects.values_list('close')
    close_get_all = list(get_all_close)

    get_all_date = jsonModel.objects.values_list('date')
    date_get_all = list(get_all_date)

    res_close = [str(''.join(map(str, idx))) for idx in close_get_all]
    res_date = [str(''.join(map(str, idx))) for idx in date_get_all]

    result_close = []
    for i in res_close:
        i = i.replace(',', '')
        result_close.append(i)

    close_main_get_all = [float(''.join(map(str, idx))) for idx in result_close]
    date_main_get_all = [str(''.join(map(str, idx))) for idx in res_date]

    date_main_get_all.sort()

    # line chart
    # -------------
    # bar chart

    get_all_volume = jsonModel.objects.values_list('volume')
    volume_get_all = list(get_all_volume)

    get_all_date = jsonModel.objects.values_list('date')
    h_date_get_all = list(get_all_date)

    h_res_date = [str(''.join(map(str, idx))) for idx in h_date_get_all]

    res_volume = [str(''.join(map(str, idx))) for idx in volume_get_all]

    result_volume = []
    for i in res_volume:
        i = i.replace(',', '')
        result_volume.append(i)

    volume_main_get_all = [int(''.join(map(str, idx))) for idx in result_volume]

    h_date_main_get_all = [str(''.join(map(str, idx))) for idx in h_res_date]

    # res_date.sort()
    h_date_main_get_all.sort()

    # print(volume_main_get_all[6])
    # context = {'volume_main_get_all':volume_main_get_all, 'h_date_main_get_all':h_date_main_get_all}

    # bar chart

    # json_data = open('static/stock_market_data.json')

    # data1 = json.load(json_data)
    # data2 = json.dumps(data1)
    # json_data.close()

    # data1 = list(data1)

    queryset = jsonModel.objects.order_by('date')
    
    context = {
        'queryset':queryset,
        'close_main_get_all':close_main_get_all,
        'date_main_get_all':date_main_get_all,
        'volume_main_get_all':volume_main_get_all,
        'h_date_main_get_all':h_date_main_get_all,
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

def update_page(request, pk):
    data_info = jsonModel.objects.get(pk=pk)
    # form = forms.MusicianForm(instance=artist_info)
    form = UpdateForm(instance=data_info)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=data_info)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home:home'))
    
    context = {
        'title': 'Update Data',
        'form':form
    }

    return render(request, 'home/update_page.html', context)

def chatshow(request):
    # get_all = jsonModel.objects.values_list('close')
    get_all_close = jsonModel.objects.values_list('close')
    close_get_all = list(get_all_close)

    get_all_date = jsonModel.objects.values_list('date')
    date_get_all = list(get_all_date)

    res_close = [str(''.join(map(str, idx))) for idx in close_get_all]
    res_date = [str(''.join(map(str, idx))) for idx in date_get_all]

    # print(res_date)

    result_close = []
    for i in res_close:
        i = i.replace(',', '')
        result_close.append(i)

    close_main_get_all = [float(''.join(map(str, idx))) for idx in result_close]
    date_main_get_all = [str(''.join(map(str, idx))) for idx in res_date]

    # res_date.sort()
    date_main_get_all.sort()
    # print(date_main_get_all)
    # for i in res_date:
    #     print(type(i))

    # data = [45,98,78,25,1,2,5,4,7,8,9,5]

    context = {'close_main_get_all':close_main_get_all,'date_main_get_all':date_main_get_all}

    # return render(request, 'home/chat_show.html', context)
    return render(request, 'home/chat_show2.html', context)

def bar_chart(request):
    get_all_volume = jsonModel.objects.values_list('volume')
    volume_get_all = list(get_all_volume)

    get_all_date = jsonModel.objects.values_list('date')
    date_get_all = list(get_all_date)

    res_date = [str(''.join(map(str, idx))) for idx in date_get_all]

    res_volume = [str(''.join(map(str, idx))) for idx in volume_get_all]

    result_volume = []
    for i in res_volume:
        i = i.replace(',', '')
        result_volume.append(i)

    volume_main_get_all = [int(''.join(map(str, idx))) for idx in result_volume]

    date_main_get_all = [str(''.join(map(str, idx))) for idx in res_date]

    # res_date.sort()
    date_main_get_all.sort()

    # print(volume_main_get_all[6])
    context = {'volume_main_get_all':volume_main_get_all, 'date_main_get_all':date_main_get_all}

    return render(request, 'home/bar_chart.html', context)

def delete_page(request, pk):
    data_info = jsonModel.objects.get(pk=pk).delete()
    print(pk)
    # form = UpdateForm(instance=data_info)

    # return render(request, 'home/update_page.html')
    return HttpResponseRedirect(reverse('home:home'))

def add_data(request):
    form = UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home:home'))
    
    context = {
        'title': 'Add Data',
        'form':form,
    }

    return render(request, 'home/update_page.html', context)