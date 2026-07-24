import re

pattern = r"[A-Z]+yclone"
text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected 
madagascar and Reunion in early March 2018. Dumazile originated from a low-pressure area that formed near Agalega on 27 February. It became
a tropical disturbance on 2 March, and was named the next day after attaining tropical storn status. Dumazile reached its peak intensity
on 5 March, with 10-minute sustained winds of 165 km/h and a central atmospheric presuure of 945 hPa. As it tracked southeastwards, Dumazile
weakened steadily over the next couple of days due to wind shear, and became as post-tropical cyclone on 7 March.
'''

# match = re.search(pattern , text)
# print(match)
matches = re.finditer(pattern , text)
for match in matches:
    print(match.span)
    print(type(match.span()))
    print(text[match.span()[0] : match.span()[1]])