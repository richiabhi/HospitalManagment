#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "book wala page"
print """
<html>
<head>
<link href="css/profile.css" rel="stylesheet" type="text/css"/>
<style>
</style>
</head>
<body>
<div id="outer">
<div id="header">
<p align="center" style="font-size:50px;"><b>Welcome Patient..!<b></p>
</div>
<br/>
<div id="menu">
<ul>
	<li><a href="book.py">Book Appointment</a></li>
	<li><a href="myappointment.py">My Appointments</a></li>
	<li><a href="changepass.py">Change Password</a></li>
	<li><a href="logout.py">Logout</a></li>
</ul>
 </div>
<div id="content">
<center>
<h1 style="text-align:center;font-family:gabriola;">Book An Appointment</h1>
<hr/>
<form action="bookcode.py" method="post">
<select name="spec" style="width:170px;height:35px;background-color:#024753;color:white;border:3px solid white">
<option value="">Choose Speciality</option>
"""
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select distinct speciality from tbl_doctor"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
for r in res:
 print '<option>'+r[0]+'</option>'
print """
</select>
<br/><br/>
<input type="submit" value="Search Doctor" style="color:white;height:40px;background-color:grey" />
</form>
</div>
</div>
</body>
</html>
"""