import urllib.request

link = "https://intellij-support.jetbrains.com/hc/en-us/articles/360006298560"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)