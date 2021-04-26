#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Index wala page"
print """
<html>
<head>
<link href="css/login.css" rel="stylesheet" type="text/css"/>
<style>
table
{
color:white;
}
table tr td
{
padding:5px;
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
<center>
<div id="content">
<table>
<form action="logcode.py" method="post">
<h1><em>Login</em></h1>
<hr/>
<tr>
<td>Who you are</td>
<td><select style="width:170px;background-color:#024753;color:white;border:3px solid white" name="who">
<option>--User--</option>
<option>Doctor</option>
<option>Patient</option>
</select></td>
<tr>
<td>Email</td>
<td><input type="email" name="email" required /></td>
</tr>
<tr>
<td>Password</td>
<td><input type="password" name="password" required /></td>
</tr>
<tr>
<td></td>
<td><input type="submit" value="Login" style="color:white;height:30px;background-color:#024753;"/></td>
</tr>
</form>
</table>
</div>
</center>
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