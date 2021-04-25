from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import numpy as np



def home(request):
    return render(request,'home.html')

def brainForm(request):
    return render(request,'brainForm.html')

def tbForm(request):
    return render(request,'tbForm.html')

def pueForm(request):
    return render(request,'pueForm.html')

def breastForm(request):
    return render(request,'breastForm.html')

#detecting brain tumor
def resulttumor(request):
    fileobj = request.FILES['braintumor']
    name = request.POST.get('name',0)
    age = request.POST.get('age',0)
    gender = request.POST.get('gender',0)
    #print(name)
    fs  = FileSystemStorage()
    filepathname = fs.save(fileobj.name,fileobj)
    filepathname = fs.url(filepathname)
    mriImage = "."+filepathname
    classifier = load_model('./brainTumorModel.h5',compile=False)
    imgpred = image.load_img(mriImage,target_size=(64,64))
    imgpred = image.img_to_array(imgpred)
    imgpred = np.expand_dims(imgpred,axis=0)
    result = classifier.predict(imgpred)
    if result[0][0]==1:
        message = "Healthy Brain"
    if result[0][1]==1:
        message = "Having Tumor"
    dict = {'filepathname':filepathname,'message':message,'age':age,'name':name,'gender':gender}
    return render(request,'resulttumor.html',dict)

#detecting pnuemonia
def resultpnu(request):
    fileobj = request.FILES['pnuemonia']
    name = request.POST.get('name',0)
    age = request.POST.get('age',0)
    gender = request.POST.get('gender',0)
    fs = FileSystemStorage()
    filepathname = fs.save(fileobj.name,fileobj)
    filepathname = fs.url(filepathname)
    pnuImage = "."+filepathname
    classifier = load_model('./pnuemonia.h5',compile=False)
    imgpred = image.load_img(pnuImage,target_size=(64,64))
    imgpred = image.img_to_array(imgpred)
    imgpred = np.expand_dims(imgpred,axis=0)
    result = classifier.predict(imgpred)
    if result[0][0]==1:
        message = "NORMAL"
    if result[0][1]==1:
        message = "VIRUS DETECTED"
    dict =   {'filepathname':filepathname,'message':message,'name':name,'age':age,'gender':gender}
    return render(request,'resultpnu.html',dict)

#detecting Tuberculosis

def resulttb(request):
    fileobj = request.FILES['tuberculosis']
    name = request.POST.get('name',0)
    age = request.POST.get('age',0)
    gender = request.POST.get('gender',0)
    fs = FileSystemStorage()
    filepathname = fs.save(fileobj.name,fileobj)
    filepathname = fs.url(filepathname)
    tbimg = "."+filepathname
    classifier = load_model('./tuberclosis.h5',compile=False)
    imgpred = image.load_img(tbimg,target_size=(64,64))
    imgpred = image.img_to_array(imgpred)
    imgpred = np.expand_dims(imgpred,axis=0)
    result = classifier.predict(imgpred)
    if result[0][0]==1:
        message = "NORMAL"
    if result[0][1]==1:
        message = "TB DETECTED"
    dict =   {'filepathname':filepathname,'message':message,'name':name,'age':age,'gender':gender}
    return render(request,'resulttb.html',dict)

#detecting Breast Cancer
def resultbreast(request):
    fileobj = request.FILES['breastcancer']
    name = request.POST.get('name',0)
    age = request.POST.get('age',0)
    fs = FileSystemStorage()
    filepathname = fs.save(fileobj.name,fileobj)
    filepathname = fs.url(filepathname)
    breastimg = "."+filepathname
    classifier = load_model('./tuberclosis.h5',compile=False)
    imgpred = image.load_img(breastimg,target_size=(64,64))
    imgpred = image.img_to_array(imgpred)
    imgpred = np.expand_dims(imgpred,axis=0)
    result = classifier.predict(imgpred)
    if result[0][0]==1:
        message = "BENING"
    if result[0][1]==1:
        message = "MELIGANT"
    dict =   {'filepathname':filepathname,'message':message,'name':name,'age':age}    
    return render(request,'resultbreast.html',dict)
