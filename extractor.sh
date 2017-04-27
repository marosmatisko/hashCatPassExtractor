#!bin/bash

username="$1";
rm -rf $username.plist;
rm -rf shadowhash;
rm -rf entropy;
cp /var/db/dslocal/nodes/Default/users/$username.plist $username.plist;
chmod 777 $username.plist;
plutil -convert xml1 $username.plist;
python shadowHashData.py $username;
file shadowhash;
plutil -convert xml1 shadowhash;
file shadowhash;
python entropy.py;
file entropy;
xxd -ps entropy entropy2;
file salt;
xxd -ps salt salt2;
python final.py;
cat hash.txt;
echo;
exit 0;
