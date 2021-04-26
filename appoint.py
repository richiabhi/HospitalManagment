#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
id=data.getvalue('did')
#print id
print """
<html>
<head>
<link href="css/profile.css" rel="stylesheet" type="text/css"/>
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
<h1 style="text-align:center;font-family:gabriola;">Enter Patient's Name and Date</h1>
<hr/>
<form action="ap.py" method="post">
Patient Name: <input type="text" name="ptname"/>
<br/><br/>
Appointment date: <input type="date" name="dt"/>
<br/>
"""
print '<input type="hidden" name="id" value="'+id+'"/>'
print """
<br/><input type="submit" value="Book Appointment" style="color:white;height:40px;background-color:#024753;"/>
</form>
</center>
</div>
</div>
</body>
</html>
"""





