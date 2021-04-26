#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "login wala page"
import cgi,MySQLdb
data=cgi.FieldStorage()
w=data.getvalue('who')
e=data.getvalue('email')
p=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
if w=="Doctor":
 query="select * from tbl_doctor where email='"+e+"' and password='"+p+"'"
 cur=con.cursor()
 a=cur.execute(query)
 con.commit()
 con.close()
 if a==1:
  print "<script>alert('Login Successful');window.location.href='dprofile.py?id="+e+"'</script>"
 else:
  print "<script>alert('Login UnSuccessful');window.location.href='login.py'</script>" 
if w=="Patient":
 query="select * from tbl_patient where email='"+e+"' and password='"+p+"'"
 cur=con.cursor()
 b=cur.execute(query)
 con.commit()
 con.close()
 if b==1:
  print "<script>alert('Login Successful');window.location.href='pprofile.py?id="+e+"'</script>"
 else:
  print "<script>alert('Login UnSuccessful');window.location.href='login.py'</script>" 
