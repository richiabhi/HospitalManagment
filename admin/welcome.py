#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "profile wala page"
print """
<html>
<head>
<style>
body
{
	font-family:Calibri;
}
#outer
{
	height:auto;
	width:100%;
}
#header
{
	height:100px;
	width:100%;
	background-color:#024753;
	color:white;
	border-radius:50px 5px 50px 50px;
}
#menu
{
	height:60px;
	width:90%;
	font-size:18px;
}
#menu ul
{
	list-style-type:none;
}
#menu ul li
{
	display:inline;
	background-color:#024753;
	border-radius:50px 5px 50px 50px;
	padding:15px;
	margin:5px;
}
#menu ul li a
{
	color:white;
	text-decoration:none;
}
#menu ul li:hover
{
	font-size:110%;
}
#content
{
	height:250px;
	width:100%;
	background-color:lightyellow;
	color:#024753;
	text-align:center;
}
#footer
{
	height:100px;
	width:100%;
	background-color:black;
	margin-top:5px;
}
</style>
</head>
<body>
<div id="outer">
<div id="header">
<p align="center" style="font-size:50px;"><b>Welcome Admin..!<b></p>
</div>
<br/>
<div id="menu">
<ul>
	<li><a href="vdoctor.py">View All Doctors</a></li>
	<li><a href="vpatient.py">View All Patients</a></li>
	<li><a href="vappointment.py">View All Appointments</a></li>
	<li><a href="vcontact.py">View All Contact Us</a></li>
	<li><a href="logout.py">Logout</a></li>
</ul>
 </div>
 <div id="content">
 <h1 style="text-align:center;font-family:gabriola;color:#024753;">Admin's Panel</h1>
 <hr>
</div>
</div>
</body>
</html>
"""