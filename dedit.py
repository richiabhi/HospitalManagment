#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
e=cgi.FieldStorage().getvalue('id')
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
	<li><a href="viewappointment.py">View Appointments</a></li>
	<li><a href="cancelappointment.py">Cancel Appointments</a></li>
	<li><a href="dchangepass.py">Change Password</a></li>
	<li><a href="logout.py">Logout</a></li>
</ul>
 </div>
<div id="content">
<center>
<h1 style="text-align:center;font-family:gabriola;">Edit Your Profile</h1>
<hr/>
	<form action='deditcode.py' method='post'>
	<table>
	
"""
cur=con.cursor()
q="select * from tbl_doctor where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name :</td><td><input name='name' value='"+r[1]+"' /></td></tr>"
 print "<tr><td>Father Name :</td><td><input name='fname' value='"+r[2]+"' /></td></tr>"
 m=""
 f=""
 if r[3]=="male":
  m="checked"
 if r[3]=="female":
  f="checked"
 print "<tr><td>Gender</td><td><input type='radio' name='gender' value='male' "+m+" />Male <input type='radio' name='gender' value='female' "+f+" />Female</td></tr>"
 print "<tr><td>Mobile No : </td><td><input type='number' name='mobileno' value='"+r[4]+"' /></td></tr>"
 print "<tr><td>Email : </td><td><input name='email' value='"+r[9]+"' readonly /></td></tr>"
 print "<tr><td>Address : </td><td><input name='address' value='"+r[5]+"'/></td></tr>"
 print "<tr><td>Fees : </td><td><input name='fees' value='"+r[7]+"'/></td></tr>"
 print "<tr><td>Timing : </td><td><input name='timing' value='"+r[8]+"'/></td></tr>"
 print "<tr><td colspan='3' align='center'><input type='submit' value='Update' /></td></tr>"
print """
     </table>
     </form>
	 </div>
	 </div>
	</body>
</html>
"""