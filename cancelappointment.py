#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_appointment"
cur.execute(q)
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
<p align="center" style="font-size:50px;"><b>Welcome Doctor..!<b></p>
</div>
<br/>
<div id="menu">
<ul>
	<li><a href="view.py">View Appointments</a></li>
	<li><a href="cancelappointment.py">Cancel Appointments</a></li>
	<li><a href="dchangepass.py">Change Password</a></li>
	<li><a href="logout.py">Logout</a></li>
</ul>
 </div>
<div id="content">
<center>
<h1 style="text-align:center;font-family:gabriola;">List Of Booked Appointments</h1>
<hr/>
<table border='1' align="center" padding="15px">
<tr>
<th>App. ID</th>
<th>Doc Id</th>
<th>Patient Name</th>
<th>DOA</th>
<th>Post Date</th>
<th>Status</th>
<th>Update Status</th>
</tr>
"""
for r in res:
 print "<tr>"
 print "<td>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "<td><a href='ups.py?id="+str(r[0])+"&s="+str(r[5])+"'>Update Status</a></td>"
 print "</tr>"

print """
</table>
</center>
</div>
</div>
</body>
</html>
"""




