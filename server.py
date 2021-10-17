#gunicorn


from os import path


def render_template(template_name='index.html',path='/', context={}):
    html_Str = ""
    with open (template_name, 'r') as f:
        html_Str = f.read()
        html_Str  = html_Str.format(**context)
    return html_Str



def home(environ):

    return render_template(
        template_name='index.html',
        context={}
    )


def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path == "/": #index / root if the app
        data = home(environ)
    else:
        data = render_template(template_name='404.html', path=path, context={'path':path})

    data = data.encode("utf-8")

    start_response(
        f"200 OK", [
            ("Content-Type", "Text/html"),
            ("Content-Lenght", str(len(data)))

        ]
    )

    return iter([data])