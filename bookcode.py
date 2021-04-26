#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Book Code"
import cgi,MySQLdb
data=cgi.FieldStorage()
s=data.getvalue('spec')
#print s
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select * from tbl_doctor where speciality='"+s+"'"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
print """
<html>
<head>
<link href="css/profile.css" rel="stylesheet" type="text/css"/>
<style>
table
{
border-collapse:collapse;
width:90%;
height:30%;
background-color:#024753;
color:white;
font-size:20px;
}
table, th, td
{
border: 1px solid white;
}
table td a 
{
color:white;
}
table td a:hover
{
font-size:110%;
}
td
{
text-align:center;
vertical-align:middle;
}
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
<h1 style="text-align:center;font-family:gabriola;">List Of Doctors</h1>
<hr/>
<table border='1' align="center" padding="15px">
<tr>
<th>Doctor's Name</th>
<th>Speciality</th>
<th>Fees</th>
<th>Timing</th>
<th>Book Now</th>
</tr>
"""

for r in res:
    print "<tr><td>",r[1],"</td>"
    print "<td>",r[6],"</td>"
    print "<td>",r[7],"</td>"  
    print "<td>",r[8],"</td>"
    print "<td><a href='appoint.py?did="+str(r[0])+"'>Book</a></td></tr>"
print """
</table>
</center>
</div>
</div>
"""






