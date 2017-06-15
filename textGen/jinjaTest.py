from jinja2 import Template

templateString ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}

    {# a comment #}
</body>
</html>
"""

layer1 = item{}
item{"hef"} = "blah"
item{"captino"} = "moe blah"

name="josh"

template = Template(templateString)
print template.render(a_variable=name, navigation=layer1, item.href=item['hef'])
