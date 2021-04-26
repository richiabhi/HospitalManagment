#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Patient wala page"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
fn=data.getvalue('fname')
g=data.getvalue('a')
m=data.getvalue('number')
a=data.getvalue('address')
e=data.getvalue('email')
p=data.getvalue('password')
sum=data.getvalue('sum')
total=data.getvalue('t')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_patient(name,fname,gender,mobile,address,email,password,date) values ('"+n+"','"+fn+"','"+g+"','"+m+"','"+a+"','"+e+"','"+p+"',curdate())"
cur=con.cursor()
aif sum==total:
 a=cur.execute(query)
 if a==1:
  print "<script>window.location.href='login.py'</script>"
 else:
  print "<script>window.location.href='patient.py'</script>"
else:
 print "<script>alert('Invalid Captcha');window.location.href='patient.py';</script>"