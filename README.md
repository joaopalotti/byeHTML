Bye HTML
======================

Boilerpipe should work only with Python 3.6+, therefore this parser will also only work in Python 3.6+.

Instalation
------------

>> pip install -e .

Usage
-----

    #!/usr/bin/env python
    
    from bywHTML import byeHTML

    bye = byeHTML("<html> <head>This is a simple text. </head> <body> Body </body> </html>", preprocesshtml="justext")

    print bye.get_html()

