#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
email=f.getvalue('email')
oldpass=f.getvalue('oldpass')
newpass=f.getvalue('newpass')
cpass=f.getvalue('cpass')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()

st="false"
query="select password from tbl_doctor where email='"+email+"'"

cur.execute(query)
res=cur.fetchall()
p=""
for r in res:
 p=r[0]
 st="true"

if newpass==cpass and oldpass==p and st=="true":
 q="update tbl_doctor set password='"+newpass+"' where email='"+email+"'"
 n=cur.execute(q)
 if n==1:
  print "<script>alert('Your Password Has Been Changed Succesfully');window.location.href='dchangepass.py';</script>"
 else:
  print "<script>alert('Your Password Has Not been Changed');window.location.href='dchangepass.py';</script>"
else:
 print "<script>alert('New Password Or Old Password Does not Match');window.location.href='dchangepass.py';</script>"