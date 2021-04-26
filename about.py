#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Index wala page"
print """
<html>
<head>
<link href="css/about.css" rel="stylesheet" type="text/css"/>
<style>
.row
{
height:300px;
width:100%;
margin-left:120px;
}
.col
{
height:210px;
width:310px;
float:left;
background:white;
margin:20px;
padding:10px;
box-shadow:10px 10px 20px  black;
}
.col:hover
{
transform:scale(1.1);
background:#2a6fcd;
transition:all ease 1s;
}
.col img
{
height:100%;
width:100%;
filter:grayscale(100%);
}
.col img:hover
{
filter:grayscale(0);
transition:all ease 1s;
}
#gallery
{
height:700px;
width:95%;
background:#33b5e5;
margin-left:30px;
border-radius:20px 10px;
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
<div id="content">
<p><font face="gabriola" size="40px">About SGPGI - </font></p>
<hr/>
<ul style="text-align:justify;">
	<li>Sanjay Gandhi Postgraduate Institute of Medical Sciences (SGPGIMS), Lucknow (India) is a University established under State Act in 1983. The Institute is located on a sprawling 550 acres residential campus at Raebareli Road, 15 km away from the main city. The institute offers its own degrees, which are duly recognized by the Medical Council of India. The Institute is rated amongst the top medical institutions in the country, delivering state-of-art tertiary medical care, super-specialty teaching, training and research. Dedicated faculty members endeavor to provide quality education, patient care and research and strive to meet the challenges and needs of the society. The Institute offers DM, MCh, MD, PhD, Post Doctoral Fellowships (PDF) and Post Doctoral Certificate Courses (PDCC), and Senior Residency in various specialties. The peers in the field have recognized the courses offered by the Institute and the candidates obtaining degrees from SGPGIMS have been highly placed both within the country and abroad.</li>
</ul>
<p><font face="gabriola" size="40px">Campus - </font></p>
<hr/>
<ul>
	<li>SGPGIMS campus is spread over an area of 700 acres. Two types of accommodation are available on the campus for student: two hostels that have with single-occupancy rooms and apartments (subject to availability). The campus has an artificial lake, with fountains and walking path around it. Recreational facilities include a swimming pool and sports complex. There is a hobby-centre called "Rang" which also houses the faculty club, a community centre and a large air-conditioned multi-purpose auditorium "Shruti". The campus has a nursery school and a high school up to class X.the campus also features a college of Nursing . With students coming from all over the nation . Most of the students are from Azamgarh,Mau and Jaunpur. The Institute community centre has a branch of State Bank of India and a post Anurag Kumar Yadav and Govind Kumar Yadav</li>
</ul>
</div>
<div id="gallery">
<h1 align="center" style="color:white";><br/><u>Image Gallery</u></h1>
<div class="row">
<div class="col">
<img src="images/sgpgi1.jpg"/>
</div>
<div class="col">
<img src="images/sgpgi2.jpg"/>
</div>
<div class="col">
<img src="images/sgpgi3.jpg"/>
</div>
</div>
<div class="row">
<div class="col">
<img src="images/8.jpg"/>
</div>
<div class="col">
<img src="images/9.jpg"/>
</div>
<div class="col">
<img src="images/10.jpg" />
</div>
</div>
</div>
<div id="footer">
<hr/>
Copyright &copy; 2014-All Rights Reserved-SGPGI Lucknow<br/>
Designed & Developed By : Abhishek Namdeo<br/>
Softpro India Pvt. Ltd.
</div>
</div>
"""