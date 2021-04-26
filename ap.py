#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
id=data.getvalue('id')
#print id
name=data.getvalue('ptname')
#print name
appdate=data.getvalue('dt')
#print appdate
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_appointment(doc_id,pname,doa,date,status) values('"+id+"','"+name+"','"+appdate+"',curdate(),'y')"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()
print """
<html>
  <head>
   <script>
     function redirect()
	 {
	   window.history.forward();
	   window.setTimeout("window.location.href='book.py'",5000);
	 }
   </script>
  </head>
  <body onload="redirect()">
  <center>
  <h1>Your Booking Is Sucessfull</h1>
  <p>You will be automatically redirected shortly, if not <a href="book.py">Click here</a> 
  </center>
  </body>
</html>
"""








