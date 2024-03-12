# CSRF Token

In Django werden in den settings.py die CSRF Token bereits mitgeliefert. Das einzige, was man seinem Code hinzufügen muss, sind die Tags an der richtigen Stelle:

Bsp.:

```python
<form method="POST">{% csrf_token %}
```

Der Token Tag muss überall dorthin, wo es eine HTTP Methode gibt. 

HTTP Methoden &rarr; Die aktuelle HTTP-Spezifikation sieht acht Methoden vor: OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE und CONNECT.
