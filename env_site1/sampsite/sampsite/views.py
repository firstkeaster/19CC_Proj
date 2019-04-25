from django.http import HttpResponse
## HttpResponse: used to pass info back to view.

import random

def hello_world(request):
    return HttpResponse("Hello World Fu!")

def root_page(request):
    return HttpResponse("Root Home Page")

def random_number(request, max_rand=100):
    ## calc random between 0 to max_rand
    random_num = random.randrange(0, int(max_rand))
    msg = "Random Number Between 0 and {} : {}".\
        format(max_rand, random_num)
    return HttpResponse(msg)