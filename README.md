# libVNCServer: A library for easy implementation of a VNC server.

## Build in Sailfish OS SDK
This is how it works under linux.

* Go to https://sailfishos.org/ and grab the Sailfish OS SDK and install it.

* Check out the code (if not done already)
```
git clone https://github.com/mer-qa/libvncserver.git
```

* Start the Sailfish OS SDK build engine virtual box machine
```
VBoxHeadless -s MerSDK &
```

* Log into the build engine via ssh
```
ssh -p 2222 -i ~/SailfishOS/vmshare/ssh/private_keys/engine/mersdk mersdk@localhost
```

* Navigate to the folder where you have cloned the git repo in step 2. You will find your home directory under ```/home/mersdk/share```.

* Build the RPM package for armv7hl
```
mb2 -t SailfishOS-armv7hl -s ./rpm/libvncserver.spec build
```

* In the new created folder ```RPMS``` you will now find two rpm files

   These RPM files can now be installed in the armv7hl build target of the SDK or on the device (just ```LibVNCServer-0.9.9.29git7b9fc019-1.armv7hl.rpm```, not the -devel package).
```
cd RPMS/
ls -l
total 448
-rw-rw-r-- 1 mersdk 1001 402729 2014-10-21 13:47 LibVNCServer-0.9.9.29git7b9fc019-1.armv7hl.rpm
-rw-rw-r-- 1 mersdk 1001  49429 2014-10-21 13:47 LibVNCServer-devel-0.9.9.29git7b9fc019-1.armv7hl.rpm
```
* install them in the SailfishOS-armv7hl target so it's available to link against for other applications
```
sb2 -t SailfishOS-armv7hl -m sdk-install -R
rpm -ivh LibVNCServer-devel-0.9.9.29git7b9fc019-1.armv7hl.rpm LibVNCServer-0.9.9.29git7b9fc019-1.armv7hl.rpm
exit
```

* Sync your SDK with the target. To do so open in a browser [http://localhost:8080/C/targets/SailfishOS-armv7hl](http://localhost:8080/C/targets/SailfishOS-armv7hl) and click on the button **sync**
