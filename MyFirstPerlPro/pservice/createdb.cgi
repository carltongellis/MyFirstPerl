#!C:\Perl64\bin\perl.exe -w

use DBI;
my $dbh = DBI->connect(          
    "DBI:SQLite:dbname=plsqlite.db", 
    "",                          
    "",                          
    { RaiseError => 1 },         
) or die $DBI::errstr;
print "Content-type: text/html; charset=iso-8859-1\n\n";
print "Opened database successfully\n";

my $stmt = qq(CREATE TABLE Appointment
   (
      apptTime datetime not null,
      desc varchar(100) not null
      ););

my $rv = $dbh->do($stmt);
if($rv < 0) {
   print $DBI::errstr;
} else {
   print "Table created successfully\n";
}

#$dbh->do("INSERT INTO Appointment(apptTime,desc) VALUES ( '2018-06-10 10:00:00', 'Barbers Appointment at 5 Star Studio.')");


#my $sth = $dbh->prepare( "SELECT * FROM Appointment" );  
#$sth->execute();
      
#my ($a,$d) = $sth->fetchrow();
#print "$a $d\n";



#$sth->finish();
$dbh->disconnect();