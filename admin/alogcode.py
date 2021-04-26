#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
aid=f.getvalue('aid')
pwd=f.getvalue('pass')

con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()

q="select * from tbl_admin where email='"+aid+"'"

cur.execute(q)
res=cur.fetchall()
p=""
for r in res:
 p=r[2]

if pwd==p:
 print "<script>alert('Login Success');window.location.href='welcome.py';</script>"
else:
 print "<script>alert('Invalid Password ');window.location.href='index.html';</script>"













