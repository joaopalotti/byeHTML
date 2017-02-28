======================
Bye HTML
======================

Instalation
------------

>> python setup.py install

Usage
-----

    #!/usr/bin/env python
    
    import byeHTML

    bye = byeHTML("<html> <head>This is a simple text. </head> <body> Body </body> </html>", preprocesshtml="justext")

    print bye.get_html()

