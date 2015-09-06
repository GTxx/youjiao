from flask import request


def check_csrf(csrf):
    def check():
        # if request with form, then use csrf
        # if request with application/json, disable csrf
        if 'application/json' in request.content_type:
            return
        if 'form' in request.content_type:
            csrf.protect()
        return
    return check
