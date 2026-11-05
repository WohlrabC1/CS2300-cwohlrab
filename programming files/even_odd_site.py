#BL
#Bugs introduced AM
#opens numbers.html file
with open("numbers.html", "w") as f:
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    #writes a table of nums 1-50 sorting into odd and even nums into html file
    for i in range(1, 50):
        for j in range(1, 50):
            if i % 2 == 0:
                g.write("<tr><td>{}</td><td></td></tr>\n".format(i))
            if i % 3 == 0:
                g.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    f.write("</table>\n</body>\n</html>")
with open("numbers.html"") as f:
    print(f.read())
    
