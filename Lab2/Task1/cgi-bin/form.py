import cgi
from http import cookies
import http.cookies
import os

form = cgi.FieldStorage()

text1 = form.getvalue('text1')
text2 = form.getvalue('text2')

variants = ["croissant", "eclair", "bun", "cookie"]
checked_dessert = []
for dessert in variants:
    if form.getvalue(dessert):
        checked_dessert.append(dessert)
dessert = ", ". join(checked_dessert)

if form.getvalue('cake'):
    cake = form.getvalue('cake')
else:
    cake = "немає"

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

count = cookie.get("count")
if count is None:
    count = 1
    print(f"Set-cookie: count={count} httponly")
else:
    count = int(count.value) + 1
    print(f"Set-cookie: count={count} httponly")

HTML = f'''
<html>
<head>
</head>
<body>
    <form class="form">
        <h2><b>Обробка даних форм!</b></h2>
        <br>
        Перший текст: {text1}
        <br><br>
        Другий текст: {text2}
        <br><br>
        Випічка: {dessert}
        <br><br>
        Тортики: {cake}
            <br><br>
        Кількість заповнених форм: {count}
    </form>
</body>
</html'''
print("Content-type: text/html\r\n\r\n")
print()
print(HTML)