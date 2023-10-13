from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
from .tasks import send_async_email  # Import the Celery task
from django.views.decorators.csrf import csrf_exempt


def send_email_view(request):
    subject = 'Hello, Celery Email'
    message = 'This is an email sent asynchronously using Celery.'
    from_email = '61e.hussars.elite@gmail.com'
    recipient_list = ['justin.ypc@gmail.com']

    send_async_email.delay(subject, message, from_email, recipient_list)

@csrf_exempt  # For demonstration purposes; use CSRF protection in production
def send_email_trig(request):
    if request.method == "POST":
        subject = 'test'
        message = 'Does it work?'
        from_email = '61e.hussars.elite@gmail.com'
        recipient_list = [request.POST.get('recipient_list')]
        send_async_email.delay(subject, message, from_email, recipient_list)

    else:
        return JsonResponse({"message": "Invalid request method."}, status=400)
    

def send_email_form(request):
    return render(request, 'send.html')

def save_data(request):
    if request.method == "POST":
        data = request.POST.get('data')  # Get the data from the form
        if data:
            subject = '61e Newsletter'
            message = 'Thank you for signing up for our monthly-ish newsletter, here you will get the newest 61e talk of the town, you can also join our discord if you have not already.'
            recip_list= [data]
            result = send_async_email(subject, message, recip_list)
            
            if result == "Email sent successfully.":
                file_path = 'email_list.txt'
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(data + '\n')  # Append the data to the text file
                    file.close()
                s_msg="You have been successfully added to our mailing list! You should be receiving a confirmation mail soon (check spam).\n"
                s_msg= s_msg + "You will be redirected to the homepage in around 5 seconds!"
                red_url=reverse('home')
                response = HttpResponse(s_msg, content_type='text/html')
                response['refresh'] = f'5;URL={red_url}'
                return response
            else:
                f_msg="Invalid email address (or unable to send to it).\n Redirecting in 3 seconds."
                response = HttpResponse(f_msg, content_type='text/html')
                red_url=reverse('send_email_form')
                response['refresh'] = f'3;URL={red_url}'
                return response
            
    return HttpResponse("Invalid request.")