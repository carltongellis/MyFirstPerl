My First Perl project

Contents 
'MyFirstPerlPro' folder
-'pservice' folder
 --dbconn.pm - centralize database connection (contains database script)
 --getappt.cgi - fetch records service
 --saverec.cgi - save record service
 --plsqlite.db - SQLite database file
-'perlproject' folder
 --Home.html - Home page of application
 --ppjquery.js - javascript file

Steps to Deploy Project
1. Place the 'perlproject' folder in the htdocs folder of the Apache server.

2. Place the 'pservice' folder in the cgi-bin folder of the Apache server.

3. I use localhost:8080 for my development, you may need to change occurrence of this before running the project.
   a. In 'pservice/saverec.cgi' at line 26 change localhost:8080 to macth your server.

4. Line 1 of all cgi script contain location to Perl.exe, please update to match your environment.

5. Launch application, database will be created automatically. If there is a problem with the database please delete database file 'plsqlite.db' and run application again.

6. To launch the application goto http://[server name]/perlproject/Home.html


If there is any issues running the application please do not hesitate to contact me at carltongellis@gmail.com
Thank you!

