#!C:\Perl64\bin\perl.exe -w
use strict;
use warnings;
use CGI;

use dbconn;

my $cgi = CGI->new();

#get data from submitted form
my $txtDate = $cgi->param('txtDate') . ' ' . $cgi->param('txtTime') . ':00';
my $txtDesc = $cgi->param('txtDesc');

#establish database connection
my $dbh = dbconn::getconn;
#insert record
$dbh->do("INSERT INTO Appointment(apptTime,desc) VALUES ( '$txtDate', '$txtDesc')");

#Free up resources
$dbh->disconnect();
#redirect to Home page
print $cgi->redirect("http://localhost:8080/perlproject/Home.html");