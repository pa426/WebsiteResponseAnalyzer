
class ResponseObj(object):
    url = ""
    status_code = 0
    content_lenght = 0
    date = ""

def make_student(url, status_code, content_lenght, date ):
    responseObj = ResponseObj()
    responseObj.url = url
    responseObj.status_code = status_code
    responseObj.content_lenght = content_lenght
    responseObj.date = date

    return responseObj