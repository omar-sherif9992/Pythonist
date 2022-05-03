def html_decorator(func):
    def wrapper(*args,**kwargs):
        message=str(func(args[0]))
        result=message
        if kwargs['flag']:
            for (key,value) in kwargs.items():
                if key =="flag":
                    continue
                elif (key=="img") and value is True :
                    result=f"{result}<{key} src='{kwargs['src']}'>"
                elif (key=="a") and value is True :
                    result=f"<{key} href='{kwargs['href']}'>{result}</{key}>"
                elif (key=="hr" or key=="br") and value is True:
                    result = f"{result}<{key}>"

                elif value is True :
                    result=f"<{key}>{result}</{key}>"
        return result
    return wrapper
@html_decorator
def html_text(message,flag=True,href="",a=True,div=False,h1=False,h2=False,h3=False,h4=False,p=False,hr=False,br=False,img=False,src=""):
    """you make your tags true from inside to outside
    ex: print(html_text("omar",flag=True,img=True,src="omar.jpeg",a=True,href="google.com",h1=True,br=True))
         ===> <h1><a>omar<img src='omar.jpeg'></a></h1> """
    return message
print(html_text("omar",flag=True,img=True,src="omar.jpeg",a=True,href="google.com",h1=True,br=True))
