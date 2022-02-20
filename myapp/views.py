import imp
from webbrowser import get
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.]

nextId = 4

topics = [
    {"id": 1, "title": "test1", "body": "test1 is ...."},
    {"id": 2, "title": "test2", "body": "test2 is ...."},
    {"id": 3, "title": "test3", "body": "test3 is ...."},
]


def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ""
    if id != None:
        contextUI = f"""
        <li> 
            <form action ="/delete/" method="post">
                <input type="hidden" name="id" value="{id}">
                <input type="submit" value="delete"> 
            </form>
        </li>
        <li> 
            <a href="/update/{id}">update</a>
        </li>
        """
    ol = ""
    for topic in topics:
        ol += f'<li> <a href="/read/{topic["id"]}"> {topic["title"]} </a></li>'
    return f"""
        <html> 
        <body>
            <h1><a href="/">Django </a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}

            <ul>
                <li> <a href="/create"> create </a> </li>
                {contextUI}
            </ul>

        </body>
        </html>
    """


def index(request):
    article = f"""
        <h2>
            Welcome
        </h2>
        <p>
            hello django
        </p>
    """
    return HttpResponse(HTMLTemplate(article))


@csrf_exempt
def create(request):
    if request.method == "GET":
        print("GET")
        article = f"""
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body" style="resize: none ;"></textarea></p>
            <p><input type="submit"></p>
        </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        global nextId
        title = request.POST["title"]
        body = request.POST["body"]
        newTopics = {"id": nextId, "title": title, "body": body}

        topics.append(newTopics)
        url = "/read/" + str(nextId)
        nextId = nextId + 1
        return redirect(url)


def read(request, id):
    global topics
    article = ""
    for topic in topics:
        if topic["id"] is int(id):
            article = f"""
                <h2>
                    {topic["title"]}
                </h2>
                <p>
                    {topic["body"]}
                </p>
            """
        else:
            pass
    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST["id"]
        newTopics = []
        for topic in topics:
            if topic["id"] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect("/")


@csrf_exempt
def update(request, id):
    global topics
    if request.method == "GET":
        for topic in topics:
            if topic["id"] == int(id):
                target_topic = topic
        article = f"""
            <form action="/update/{id}/" method="post">
                <p><input name="title" placeholder="title"  value="{target_topic["title"]} "></p>
                <p><textarea name="body" placeholder="body" style="resize: none ;">{target_topic["body"]}</textarea></p>
                <p><input type="submit"></p>
            </form>
        """
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        for topic in topics:
            if topic["id"] == int(id):
                topic["title"] = title
                topic["body"] = body
        return redirect(f"/read/{id}")
