#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
id=f.getvalue('id')
s=f.getvalue('s')
if s=='y':
 s='n'
else:
 s='y'

con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="update tbl_appointment set status='"+s+"' where appid='"+id+"'"

a=cur.execute(q)

if a==1:
 print "<script>alert('Status Updated');window.location.href='view.py';</script>"
else:
 print "<script>alert('Status is not updated');window.location.href='view.py';</script>"







