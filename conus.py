#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Index wala page"
print """
<html>
<head>
<link href="css/conus.css" rel="stylesheet" type="text/css"/>
<style>
table
{
color:white;
}
table tr td
{
padding:5px;
}
p
{
font-size:20px;
}
</style>
</head>
<body>
<div id="outer">
<div id="header">
<div id="logo">
<img src="images/logo.png" height="200px" width="100%" alt="logo"/>
</div>
<div id="heading">
<p align="center" style="font-size:50px;"><b>Sanjay Gandhi Postgraduate Institute of Medical Sciences<b></p>
</div>
</div>
<div id="menu">
	<ul>
		<li><a href="index.html">Home</a></li>
		<li><a href="about.py">About Us</a></li>
		<li><a href="doc.py">Doctor</a></li>
		<li><a href="patient.py">Patient</a></li>
		<li><a href="login.py">Login</a></li>
		<li><a href="conus.py">Contact Us</a></li>
	</ul>
</div>
<div id="row">
<div id="rowa" style="text-align:center;">
<br/>
<h2>Contact Us</h2>
<hr/>
<br/>
<center>
<table>
<form action="concode.py" method="post">
<tr>
<td>Name</td>
<td><input type="text" name="name"/></td>
</tr>
<tr>
<td>Email</td>
<td><input type="email" name="email"/></td>
</tr>
<tr>
<td>Mobile</td>
<td><input type="number" name="mob"/></td>
</tr>
<tr>
<td>Message</td>
<td><textarea name="mess"></textarea></td>
</tr>
<tr>
<td></td>
<td><input type="submit" value="Send" style="color:white;height:30px;background-color:#024753;"/></td>
</tr>
</form>
</table>
</center>
</div>
<div id="rowb" style="text-align:center;">
<br/>
<h2>Address :</h2>
<hr/>
<br/>
<p align="center">SGPGI Campus,Raebareli Rd, Haibat Mau Mawaiya, Lucknow, Uttar Pradesh 226014</p>
<p align="center">Email us : <u>sgpgi@yahoo.com</u></p>
<p align="center">Phone : 0522 266 8700</p>
</div>
</div>
<div id="map">
<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14234.67795370525!2d80.94821!3d26.88224!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x730fe46201abc68a!2sSoftpro+India!5e0!3m2!1sen!2sin!4v1411887056855" width="100%" height="100%"></iframe>
</div>
<div id="footer">
<hr/>
Copyright &copy; 2014-All Rights Reserved-SGPGI Lucknow<br/>
Designed & Developed By : Abhishek Namdeo<br/>
Softpro India Pvt. Ltd.
</div>
</div>
</body>
</html>
"""