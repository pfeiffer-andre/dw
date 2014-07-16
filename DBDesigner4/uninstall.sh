#!/bin/sh

rm -f /usr/lib/kylix3/libborqt-6.9-qt2.3.so
rm -f /usr/lib/kylix3/libborqt-6.9.0-qt2.3.so

find /usr/lib/kylix3/* >/dev/null 2>&1
if [ $? == 1 ]; then
  mv /etc/ld.so.conf /etc/ld.so.conf.old
  grep -v "^/usr/lib/kylix3\$" /etc/ld.so.conf.old > /etc/ld.so.conf
fi
/sbin/ldconfig
rm -f /etc/ld.so.conf.old
