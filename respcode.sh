awk 'BEGIN { count=0;}
$10 ~ /404/ { count++; }
END { print "No. of 404 response codes:",count;}' $1

echo 'Count RC'

awk '{print $10}' $1 | sort -n | uniq -c

