#!/bin/bash
echo ""
echo "> INSTALLATION VON 'taschenrechner-py3'"
echo "> ====================================="
echo ""
echo "> ================================"
echo "> Installiere notwendige Pakete..."
echo "> ================================"
echo ""
read -p "> [ENTER] drücken, um fortzufahren: " -n 1  -s
echo ""
sudo apt-get install dpkg-dev build-essential python3.5-dev libwebkitgtk-dev libjpeg-dev libtiff-dev libgtk2.0-dev libsdl1.2-dev libgstreamer-plugins-base0.10-dev libnotify-dev freeglut3 freeglut3-dev
echo ""
echo "> ============================================================="
echo "> Installiere Python-Abhängigkeiten... (kann eine Weile dauern)"
echo "> ============================================================="
echo ""
read -p "> [ENTER] drücken, um fortzufahren: " -n 1  -s
echo ""
sudo apt-get install python3-pip
sudo pip3 install -U setuptools
sudo pip3 install -U --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython_Phoenix
echo ""
echo "> ==================================="
echo "> Installiere 'taschenrechner-py3'..."
echo "> ==================================="
echo ""
read -p "> [ENTER] drücken, um fortzufahren: " -n 1  -s
cp Taschenrechner.py $HOME/Schreibtisch
echo ""
echo "> +---------------------------------------+"
echo "> |INSTALLATION ERFOLGREICH ABGESCHLOSSEN!|"
echo "> +---------------------------------------+"
echo ""
