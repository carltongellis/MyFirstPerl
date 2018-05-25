#!C:\Perl64\bin\perl.exe -w
use strict;
use warnings;
use JSON;
use CGI;

use dbconn;
#establish database connection
my $dbh = dbconn::getconn;

my $cgi = CGI->new();
#set header
print $cgi->header( -type => 'application/json' );

#get search criteria
my $searchString = $cgi->param('searchString');

#create whre clause
if($searchString){  $searchString = "where desc like '%$searchString%'"; } else{$searchString = '';}

#retrieve results from DB
my $sth = $dbh->prepare( "SELECT apptTime, desc FROM Appointment $searchString" );  
$sth->execute();

my $JSONstring = '';
my $apptTime = '';
my $desc = '';
my $count =0;

#convert results to JSON format
while(($apptTime, $desc) = $sth->fetchrow()){
    if($count > 0){
        $JSONstring .=',';
    }
    $JSONstring = $JSONstring ."{\"Appt\":\"$apptTime\",\"Desc\":\"$desc\"}";
    $count++;
}

print '['. $JSONstring . ']';

#Free up resources
$sth->finish();
$dbh->disconnect();
