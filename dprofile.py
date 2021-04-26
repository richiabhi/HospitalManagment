#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "profile wala page"
print """
<html>
<head>
<link href="css/profile.css" rel="stylesheet" type="text/css"/>
<style>
table
{
border-collapse:collapse;
width:50%;
height:50%;
background-color:#024753;
color:white;
font-size:20px;
}
table, th, td
{
border:1px solid white;
}
table td a 
{
color:white;
text-decoration:none;
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
 <h1 style="text-align:center;font-family:gabriola;color:#024753;">Doctor Profile Page</h1>
 <hr/>
 <center>
 <table>
"""
import cgi,MySQLdb
e=cgi.FieldStorage().getvalue('id')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_doctor where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name :</td><td>",r[1],"</td></tr>"
 print "<tr><td>Father Name :</td><td>",r[2],"</td></tr>"
 print "<tr><td>Gender :</td><td>",r[3],"</td></tr>"
 print "<tr><td>Mobile No :</td><td>",r[4],"</td></tr>"
 print "<tr><td>Address :</td><td>",r[5],"</td></tr>"
 print "<tr><td>Speciality :</td><td>",r[6],"</td></tr>"
 print "<tr><td>Fees :</td><td>",r[7],"</td></tr>"
 print "<tr><td>Timing :</td><td>",r[8],"</td></tr>"
 print "<tr><td>Email :</td><td>",r[9],"</td></tr>"
 print "<tr><td>Reg. Date :</td><td>",r[11],"</td></tr>"
 print "<tr><td colspan='2'><a href='dedit.py?id="+e+"'><em>Update Profile</em></a></td></tr>"

print """
</table>
</center>
</div>
</div>
</body>
</html>
"""