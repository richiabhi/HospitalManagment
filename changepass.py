#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
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
	<li><a href="login.py">Logout</a></li>
	</ul>
	</div>
	<div id="content">
	<center>
	<h1 style="text-align:center;font-family:gabriola;">Enter Your Old as well as New Password</h1>
	<hr/>
   <form action="cpcode.py" method="post">
    <table>
	  <tr>
	     <td>Enter Email Id :</td>
		 <td>
		   <input type="email" name="email" required />
		 </td>
	  </tr>
	  <tr>
	    <td>Enter Old Password :</td>
	    <td>
	  <input type="password" name="oldpass" required />	
		</td>
	  </tr>
	  <tr>
	    <td>Enter New Password :</td>
	    <td>
	<input type="password" name="newpass" required />
		</td>
	  </tr>
	  <tr>
	    <td>Enter Confirm Password :</td>
	    <td>
		<input type="password" name="cpass" required />
		</td>
	  </tr>
	  <tr>
	     <td colspan="2" align="center">
		 <input type="submit" value="Change Password" style="color:white;height:40px;background-color:#024753;"/>
		 </td>
	  </tr>
	</table>
	</form>
	</div>
	</center>
	</div>
   </body>
</html>
"""