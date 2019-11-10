# Wheel cutter

This repository is intended to compliment an article written for the Horological Journal (April 2019) and contains the Python source code for a Raspberry Pi to drive a stepper motor connected to a dividing head which in turn is used for wheel cutting.

https://github.com/mbcoder/wheel-cutter/blob/master/April%20HJ%202019%20-%20V14%20-%20Raspberry%20Pi%20-%20V2.pdf

## Shopping List

The following list shows potential suppliers of the parts needed to make your own stepper driver.

 - Raspberry Pi : https://www.modmypi.com/raspberry-pi/raspberry-pi-a-plusb-plus23-1015/rpi3-model-b-plus/raspberry-pi-3-model-b-plus 
 - TB6600 stepper driver - https://www.ebay.co.uk/itm/2pcs-12-48V-Single-Axis-TB6600-4A-2-Phase-Hybrid-Stepper-Motor-Driver-Controller/282459617201?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649
 - Nema 23 stepper motor - https://www.amazon.co.uk/gp/product/B06WVB5L14/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1
 - Mounting bracket - https://www.ebay.co.uk/itm/New-Nema-23-stepper-motor-mount-clamp-aluminum-bracket-Plasma-Cutter-CNC-Milling/112551325177?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649
 - Motor coupling - https://www.ebay.co.uk/itm/Flexible-Shaft-Coupling-CNC-Stepper-Motor-Coupler-Connector-10-Size-for-Choice/152031865795?ssPageName=STRK%3AMEBIDX%3AIT&var=451230027575&_trksid=p2057872.m2749.l2649
 - 5A 12V power supply - https://www.ebay.co.uk/itm/DC-5V-12V-24V-Universal-Power-Supply-Regulated-Switching-LED-Driver-CCTV-2A-40A/352377651874?ssPageName=STRK%3AMEBIDX%3AIT&var=621739419968&_trksid=p2057872.m2749.l2649
 - Patch cables (a more permanent solution may be more desirable) - https://www.ebay.co.uk/itm/40-pcs-Dupont-Cables-M-F-M-M-F-F-Jumper-Breadboard-Wire-GPIO-Ribbon-Pi-Arduino/263021195544?_trkparms=aid%3D222007%26algo%3DSIM.MBE%26ao%3D2%26asc%3D52543%26meid%3D90f3f14fef4341db9ecbf291419a911d%26pid%3D100005%26rk%3D5%26rkt%3D12%26mehot%3Dpp%26sd%3D201000956114%26itm%3D263021195544&_trksid=p2047675.c100005.m1851
 
 ## Setting up the Raspberry Pi

Setting a new out of the box setup (NOOBS) Raspberry Pi is a simple operation achieved by following the instructions on this page: https://www.raspberrypi.org/help/noobs-setup/2/

Now you have a basic functioning Raspberry Pi, you can clone the repository in preparation for running the Python application for controlling the stepper motor.  Start by opening the Terminal window from the black ">_" icon at the top of the Raspberry Pi screen.  How type the following:

```
git clone https://github.com/mbcoder/wheel-cutter.git
```

When you press enter you should see the following happen:

```
Cloning into 'wheel-cutter'...
remote: Counting objects: 44, done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 44 (delta 23), reused 19 (delta 9), pack-reused 0
Unpacking objects: 100% (44/44), done.
pi@raspberrypi:~ $ 
```

Now change to the wheel-cutter directory which contains the application code you have just downloaded.

```
cd wheel-cutter/
```

You now need to run the setup script which will download the python GUI library you need for the application.  Type the following

```
./setup
```

You will see the following on the terminal window:
```
Collecting guizero
  Downloading https://files.pythonhosted.org/packages/87/19/e8d1831fedc1328c39dacf9a9c5342ceed0315cf301aa2284cd09fc91e9e/guizero-0.5.2-py3-none-any.whl
Collecting pillow>=5 (from guizero)
  Downloading https://www.piwheels.org/simple/pillow/Pillow-5.2.0-cp35-cp35m-linux_armv7l.whl (1.1MB)
    100% |████████████████████████████████| 1.1MB 17kB/s 
Installing collected packages: pillow, guizero
Successfully installed guizero-0.5.2 pillow-5.2.0
pi@raspberrypi:~/wheel-cutter $ 
```

Before getting too carried away with cabling up the stepper motor, I would recommend following a phased approach to connecting everythin up which should reduce th risk of frying your Pi!  Take a look at this page: https://github.com/mbcoder/wheel-cutter/wiki/Connecting-it-up

You are now ready to run the wheel cutting application.  The can be run by typing in the following which will start the application:

```
python3 wheelcutter.py
```
