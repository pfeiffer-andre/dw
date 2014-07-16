#! /bin/sh

install -d /usr/lib/kylix3/
install -m 755 libborqt-6.9.0-qt2.3.so /usr/lib/kylix3/libborqt-6.9.0-qt2.3.so

cd /usr/lib/kylix3/
cp -s libborqt-6.9.0-qt2.3.so libborqt-6.9-qt2.3.so

grep -q "^/usr/lib/kylix3\$" /etc/ld.so.conf
if [ $? == 1 ]; then
  echo /usr/lib/kylix3 >> /etc/ld.so.conf
fi

/sbin/ldconfig
