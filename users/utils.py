from django.contrib import messages


def clearCachedMessages(request): 
    storage = messages.get_messages(request)
    storage.used = True    

