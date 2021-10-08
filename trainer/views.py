from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from .models import Trainer

from .forms import TrainerForm

#takes model trainer from database and sends it to template in a context
#when they are no registrations in the model trainer, sends a message to the tempplate

def all_trainer(request):
    trainer_list = Trainer.objects.all()
    context = {}

    if trainer_list.exists():
        context ={
            'trainers': trainer_list
            }
    else:
        context['message'] = 'There are no Trainers'

    return render(request, 'trainer/in_base.html', context )

#takes the id of the specific trainer model from database and sends it to template in a context so it is possible to read the details

def trainer_details(request, id):
    
    trainer = get_object_or_404(Trainer, id=id)
    
    return render(request, 'trainer/trainer_details.html', {'trainer': trainer})

#takes the id of the specific trainer model from database and sends it to template in a context so it can be deleted   
#a verification message is being send
def delete_trainer(request, id):
    trainers = Trainer.objects.get(id=id)
    trainers.delete()

    message = 'You have successfully deleted trainer: ' + trainers.first_name
    return HttpResponseRedirect('/trainer/success/'+message+'/')



#takes the id of the specific trainer model from database and sends it to template in a context so it can be updated
#a verification message is being send
def update_trainer(request, id):
    trainer = Trainer.objects.get(id=id)

    if request.method == 'POST':
        message = 'You have successfully edited trainer: ' + trainer.first_name 

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        object = request.POST.get('object')
        description = request.POST.get('description')


        trainer.first_name = first_name
        print(last_name)
        print(object)
        if last_name != None:
            trainer.last_name = last_name
        if object != None: 
            trainer.object = object  
        if description  != None: 
            trainer.description  = description      

        trainer.save()
        return HttpResponseRedirect('/trainer/success/'+message+'/')
    else:
        context = {
            'trainer': trainer,
            
        }

    return render(request, 'trainer/update_trainer.html', context)


#a new trainer is being created with details given by the client to the form
#a verification message is being send

def add_trainer(request):
    if request.method == 'POST':
        trainer_form = TrainerForm(request.POST)
        if trainer_form.is_valid():
            trainer_form.save()

            msg = 'Trainer successfully added!'
            return HttpResponseRedirect('/trainer/success/'+msg+'/')
    else:
        trainer_form = TrainerForm()

    return render(request, 'trainer/add_trainer.html', {'form': trainer_form})





#a verification message is being send        
def success(request, message):
    return render(request, 'trainer/success.html', {'message': message})        
    

   
