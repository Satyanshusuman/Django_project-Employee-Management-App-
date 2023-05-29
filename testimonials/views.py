from django.shortcuts import render
from .models import Testimonial
from .feedbackform import Feedbackform

# Create your views here.
def home(request):
    testi=Testimonial.objects.all()
    return render(request,"testimonials/testimonial.html",{"testi":testi})

def feedback(request):
    if request.method=="POST":
        form=Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            msg="Thanks for submission"
            return render(request,"testimonials/feedback.html",{"feed":form,"msg":msg})
        else:
            return render(request,"testimonials/feedback.html",{"feed":form})
    
    feed=Feedbackform()
    return render(request,"testimonials/feedback.html",{"feed":feed})

