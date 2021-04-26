#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
  <head>
   <script>
     function redirect()
	 {
	   window.history.forward();
	   window.setTimeout("window.location.href='index.html'",2000);
	 }
   </script>
  </head>
  <body onload="redirect()">
  <center>
  <h1>Thank You..!</h1>
  <p>You will be automatically redirected shortly, if not <a href="index.html">Click here</a> 
  </center>
  </body>
</html>
"""