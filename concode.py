#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "hii"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
e=data.getvalue('email')
m=data.getvalue('mob')
mess=data.getvalue('mess')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_contact(name,email,mobile,message,date) values ('"+n+"','"+e+"','"+m+"','"+mess+"',curdate())"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()
print """
<html>
  <head>
   <script>
     function feedback()
	 {
	   window.history.forward();
	   window.setTimeout("window.location.href='conus.py'",5000);
	 }
   </script>
  </head>
  <body onload="feedback()" style="font-family:calibri;text-align:center;">
  <h1>Thank You For Contacting Us,we Will Reach To You Within 24hrs.</h1>
  <p>You will be automatically redirected shortly,if not <a href="conus.py">Click Here</a> 
  </body>
</html>
"""
