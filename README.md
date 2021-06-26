# vr408_pyqt_gui

A python GUI for the ALLBOT VR408 robot using PyQT5. The graphical interface was created using QT designer, then the `pyuic5` compiler was used to autogenerate the files.

The files are as follows:

assignservodialog.ui -- designer file for the Assign servo channels to the legs of VR408

assignservodialog.py -- generated from `pyuic5`

dialogservoconfig.ui -- PCA9685 configuration -- bus id, address, etc.

dialogservoconfig.py -- generated from `pyuic5`

vr408mainwindow.ui -- Main window GUI

vr408mainwindow.py -- generated from `pyuic5`

vr408mainwin.py -- GUI for the VR408. PCA9685 interfacing is disabled in order to be tested on a local computer without error handling.

# Testing

To test the GUI just run `python3 vr408mainwin.py`. Keep in mind that the instructions for interfacing the VR408 functions are commented. However the GUI is functional by outputing the result in the log.

# Known issues:

The settings parser is not yet complete, that is, save & load configuration does not work.
