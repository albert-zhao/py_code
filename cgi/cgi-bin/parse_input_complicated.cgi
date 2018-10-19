#! /usr/bin/env python3

import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print("""Content-type: text/html

<html>
<head>
<title>Greeting Page</title>
</head>
<body>
<h1>Hello, {}!</h1>
<form action='parse_input_complicated.cgi'>
Change name <input type='text' name='name' />
<input type='submit' />
</form>
</body>
</html>
""".format(name))

# 在 Change name <input type='text' name='name' /> 中
# name 必须有，没有就没法有http://127.0.0.1:8000/cgi-bin/parse_input_complicated.cgi?name=xilongzhao,
# 'name' 反应在name=xilongzhao, 如果是‘value', 那么将有value=xilongzhao
#