from django.shortcuts import render,redirect
from imageapp.models import Imagemodel
from .forms import ImageForm

# Create your views here.
def imageview(request):
    form=ImageForm()

    # Image Form
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("./")
    # Images
    imageView=Imagemodel.objects.all()   
    context={"forms":form,"view":imageView}
    
    return render(request,"index.html",context)

def Delete(request,id):
    ImageDelete=Imagemodel.objects.get(id=id)
    ImageDelete.delete()
    return redirect("../")

def deleted(requet):
    return redirect("../")
