#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "profile wala page"
print """
<html>
<head>
<link href="css/profile.css" rel="stylesheet" type="text/css"/>
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
 <h1 style="text-align:center;font-family:gabriola;color:#024753;">Doctor's Profile Page</h1>
 <hr/>
 <form action="dcpcode.py" method="post">
 <center>
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
	</center>
 </div>
 <div id="footer"></div>
</div>
</body>
</html>
"""