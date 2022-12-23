# Dependencies

### library to install to run this project

``` shell
pip install PyQt5
pip install pyqt-tools
# if PyQt5 Designer not installed 
pip install PyQt5Designer
# download mysql.connect
pip install mysql.connector
pip3 install bcrypt

#Encrypt password
pip install bcrypt

#Try install package 
python -m pip install <P A C K A G E   N A M E>
#Convert .ui files in .py
# try on Windows
# pyuic5 -m FILE_NAME.ui -o FILE_NAME.py
# work in MAC
pyuic5 FILE_NAME.ui -o FILE_NAME.py

# compile resources - will be contain all assets
pyrcc5 resources.qrc -o resources.py

```