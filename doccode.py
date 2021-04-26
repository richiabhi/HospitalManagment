#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Index wala page"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
fn=data.getvalue('fname')
g=data.getvalue('a')
m=data.getvalue('mob')
a=data.getvalue('address')
s=data.getvalue('spec')
fe=data.getvalue('fees')
t=data.getvalue('timing')
e=data.getvalue('email')
p=data.getvalue('password')
sum=data.getvalue('sum')
total=data.getvalue('t')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_doctor(docname,fname,gender,mobile,address,speciality,fees,timing,email,password,date) values ('"+n+"','"+fn+"','"+g+"','"+m+"','"+a+"','"+s+"','"+fe+"','"+t+"','"+e+"','"+p+"',curdate())"
cur=con.cursor()
if sum==total:
 a=cur.execute(query)
 if a==1:
  print "<script>window.location.href='login.py'</script>"
 else:
  print "<script>window.location.href='doc.py'</script>"
else:
 print "<script>alert('Invalid Captcha');window.location.href='doc.py';</script>"