import pyorient
import timeit
import random, string

client = pyorient.OrientDB("localhost",2424)
client.connect("root", "incorrect")
client.db_open("GratefulDeadConcerts", "root", "incorrect")


#cluster_id = client.command( "create class KC2 extends V" )


numw=int(raw_input("Enter the number of test writes required:   "))

start = timeit.default_timer()

for i in range(numw):
    fn = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    ln = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    address = ''.join(random.choice(string.ascii_lowercase) for i in range(50))
    client.command( 
    "insert into KC2 ('fn', 'ln', 'address') values("+fn+", "+ln+", "+address+")")

    
print str(i+1) + " writes took " + str(round((timeit.default_timer() - start),3)) + " seconds"



numr=int(raw_input("Enter the number of test reads required:   "))

start = timeit.default_timer()
readresult = client.query("select from KC2", int(numr), '*:0')
print str(numr) + " reads took " + str(round((timeit.default_timer() - start),3)) + " seconds"



print "Database size is now " + str(client.db_count_records()) + " records."
client.db_size()
client.db_close()
