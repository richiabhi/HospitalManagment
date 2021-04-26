#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
fname=f.getvalue('fname')
gender=f.getvalue('gender')
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
address=f.getvalue('address')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="update tbl_patient set name='"+name+"',fname='"+fname+"',gender='"+gender+"',mobile='"+mobileno+"',address='"+address+"' where email='"+email+"'"
cur.execute(q)
print "<script>window.location.href='pprofile.py?id="+email+"';</script>"