#!C:\Perl64\bin\perl.exe -w

package dbconn;
use DBI;
sub getconn{
   #create/open database 
    my $dbh = DBI->connect(          
        "DBI:SQLite:dbname=plsqlite.db", 
        "",                          
        "",                          
        { RaiseError => 1 },         
    ) or die $DBI::errstr;
    
    my $stmt = qq(CREATE TABLE IF NOT EXISTS Appointment 
   (
	  ID integer primary key autoincrement,
      apptTime datetime not null,
      desc varchar(100) not null
      ););

    #create table if not exist
    my $rv = $dbh->do($stmt);
    if($rv < 0) {
       print $DBI::errstr;
    } else {
       #print "Table created successfully\n";
    }
    return $dbh;
}

1;