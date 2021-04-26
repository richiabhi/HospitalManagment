#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Index wala page"
print """
<html>
<head>
<link href="css/doc.css" rel="stylesheet" type="text/css"/>
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
<form action="doccode.py" method="post">
<h1><em>Doctor's Registration Form</em></u></h1>
<hr/>
<tr>
<td>Doctor's Name</td>
<td><input type="text" name="name" required /></td>
</tr>
<tr>
<td>Father's Name</td>
<td><input type="text" name="fname" required /></td>
</tr>
<tr>
<td>Gender</td>
<td><input type="radio" name="a" value="male"/>Male
<input type="radio" name="a" value="female"/>Female</td>
</tr>
<tr>
<td>Mobile No.</td>
<td><input type="number" name="mob" required /></td>
</tr>
<tr>
<td>Address</td>
<td><textarea name="address" required ></textarea></td>
</tr>
<tr>
<td>Speciality</td>
<td><select name="spec" required >
<option>--Select--</option>
<option>Surgeon</option>
<option>Physician</option>
<option>Cardiologist</option>
<option>Orthologist</option>
<option>Eye Specialist</option>
</select></td>
<tr>
<td>Fees</td>
<td><input type="text" name="fees" required /></td>
</tr>
<tr>
<td>Timing</td>
<td><input type="text" name="timing" required /></td>
</tr>
<tr>
<td>Email</td>
<td><input type="email" name="email" required /></td>
</tr>
<tr>
<td>Password</td>
<td><input type="password" name="password" required /></td>
</tr>
"""
import random 
a=[0,1,2,3,4,5,6,7,8,9]
n1=random.choice(a)
n2=random.choice(a)
sum=n1+n2
print "<tr>"
print "<td>Captcha</td>"
print "<td colspan='2'><input type='hidden' value='"+str(sum)+"' name='sum'/>"
print "<input value='"+str(n1)+"' style='width:20px;' readonly/> + "
print "<input value='"+str(n2)+"' style='width:20px;' readonly/>"
print " = <input type='number' name='t' style='width:40px;' required/>"
print "</td>"
print "</tr>"
print """
<br/>
<tr>
<td></td>
<td><input type="Submit" value="Register" style="width:170px;background-color:#024753;color:white;border:3px solid white;"/></td>
</tr>
</form>
</table>
</div>
<div id="footer">
<hr/>
Copyright &copy; 2014-All Rights Reserved-SGPGI Lucknow<br/>
Designed & Developed By : Abhishek Namdeo<br/>
Softpro India Pvt. Ltd.
</div>
</div>
"""