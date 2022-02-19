from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.]

topics = [
    {"id": 1, "title": "test1", "body": "test1 is ...."},
    {"id": 2, "title": "test2", "body": "test2 is ...."},
    {"id": 3, "title": "test3", "body": "test3 is ...."},
]


def HTMLTemplate(articleTag):
    global topics
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
                <li> <a href="/delete"> delete </a> </li>
                <li> <a href="/update"> update </a> </li>
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
    article = f"""
    <form action="/create/" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea name="body" placeholder="body" style="resize: none ;"></textarea></p>
        <p><input type="submit"></p>
    </form>
    """
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ""
    for topic in topics:
        if topic["id"] is int(id):
            article = f"""
                <h2>
                    Welcome
                </h2>
                <p>
                    {topic["body"]}
                </p>
            """
        else:
            pass
    return HttpResponse(HTMLTemplate(article))
