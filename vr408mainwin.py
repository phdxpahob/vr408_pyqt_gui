from PyQt5 import QtWidgets, uic
import sys
#import vr408 as VR408

class RosBotWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RosBotWindow, self).__init__()
        uic.loadUi('vr408mainwindow.ui', self)
        
        self.Button_backward.clicked.connect(self.moveBackward)
        self.Button_left.clicked.connect(self.moveLeft)
        self.Button_right.clicked.connect(self.moveRight)
        self.Button_forward.clicked.connect(self.moveForward)

        self.Button_zminus.clicked.connect(self.RotateCW)
        self.Button_zplus.clicked.connect(self.RotateCCW)
        
        self.speedSlider.valueChanged.connect(self.onSliderChange)
        
        self.Button_waveFLeft.clicked.connect(self.waveFLeft)
        self.Button_waveFRight.clicked.connect(self.waveFRight)
        self.Button_waveRLeft.clicked.connect(self.waveRLeft)
        self.Button_waveRRight.clicked.connect(self.waveRRight)
        
        self.Button_leanLeft.clicked.connect(self.leanLeft)
        self.Button_leanRight.clicked.connect(self.leanRight)
        self.Button_leanForward.clicked.connect(self.leanForward)
        self.Button_leanBackward.clicked.connect(self.leanBackward)
        
        self.Button_animate.clicked.connect(self.onScaredClicked)
        self.Button_play.clicked.connect(self.onChirpClicked)
        
        self.action_About.triggered.connect(lambda: QtWidgets.QMessageBox.about(self, "About RosBotGui", "A simple GUI for controlling the Velleman VR408 robot or similar."))
        self.action_Contents.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, "RosBotGui Help Contents", "Help is not yet available."))
        
        self.actionOpen_configuration.triggered.connect(self.OpenCfg)
        self.actionSave_configuration.triggered.connect(self.SaveCfg)
        self.actionExit.triggered.connect(app.quit)
        
        self.actionServo_configuration.triggered.connect(self.ServoCfg)
        self.actionJoint_configuration.triggered.connect(self.JointCfg)
        
        self.show()
    
    def moveForward(self):
        #VR408.walkforward(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Step Forward.")
    
    def moveBackward(self):
        #VR408.walkbackward(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Step Backward.")
    
    def moveLeft(self):
        #VR408.walkleft(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Step Left.")
    
    def moveRight(self):
        #VR408.walkright(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Step Right.")
    
    def RotateCW(self):
        #VR408.turnright(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Rotate Clockwise.")
    
    def RotateCCW(self):
        #VR408.turnleft(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Rotate Counterclockwise.")
    
    def waveFLeft(self):
        #VR408.wavefrontleft(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Wave Front Left.")
    
    def waveFRight(self):
        #VR408.wavefrontright(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Wave Front Right.")
    
    def waveRLeft(self):
        #VR408.waverearleft(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Wave Rear Left.")
    
    def waveRRight(self):
        #VR408.waverearright(1, self.speedSlider.value()/1000)
        self.textBrowser_log.append("Wave Rear Right.")
    
    def leanLeft(self):
        #VR408.leanleft(self.speedSlider.value()/1000)
        self.textBrowser_log.append("Lean Left.")
    
    def leanRight(self):
        #VR408.leanright(self.speedSlider.value()/1000)
        self.textBrowser_log.append("Lean Right.")
    
    def leanForward(self):
        #VR408.leanforward(self.speedSlider.value()/1000)
        self.textBrowser_log.append("Lean Forward.")
    
    def leanBackward(self):
        #VR408.leanbackward(self.speedSlider.value()/1000)
        self.textBrowser_log.append("Lean Backward.")
    
    def onScaredClicked(self):
        if self.spinBox_shakes.value() == 0:
            self.textBrowser_log.append('Cannot animate scared with 0 shakes...')
        else:
            #Python 2: self.textBrowser_log.append('Animate scared with ' + str(self.spinBox_shakes.value()) + ' shakes and ' + str(self.beeps_spinBox.value()) + ' beeps')
            self.textBrowser_log.append('Animate scared with {} shakes and {} beeps'.format(self.spinBox_shakes.value(), self.beeps_spinBox.value()))
            #VR408.scared(self.spinBox_shakes.value(), self.beeps_spinBox.value())
    
    def onChirpClicked(self):
        if self.spinBox_beeps.value() == 0:
            self.textBrowser_log.append('Cannot chirp with 0 beeps...')
        elif self.spinBox_beeps.value() == 1:
            self.textBrowser_log.append('Chirp with 1 beep.')
        else:
            #Python 2: self.textBrowser_log.append('Chirp with ' + str(self.spinBox_beeps.value()) + ' beeps.')
            self.textBrowser_log.append('Chirp with {} beeps.'.format(self.spinBox_beeps.value()))
    
    def onSliderChange(self, value):
        #global animateSpeed
        #print('slider value is now: {}'.format(value))
        #animateSpeed = (value if value != 0 else value)/1000
        self.textBrowser_log.append('Animation speed is now: {} ms'.format(value/1000))
    
    def OpenCfg(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Load configuration', '', "INI Files (*.ini);;All Files (*.*)")
        #print(fileName)
        if fileName[0] != "":
            self.textBrowser_log.append("Load configuration from file: " + fileName[0])
    
    def SaveCfg(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save configuration', '', "INI Files (*.ini);;All Files (*.*)")
        #print(fileName)
        if fileName[0] != "":
            self.textBrowser_log.append("Save configuration to file: " + fileName[0])
    
    def ServoCfg(self):
        scfg = ServoConfigDialog(self)
        if scfg.exec_():
            self.textBrowser_log.append("Servo configuration dialog accepted.")
            
        else:
            self.textBrowser_log.append("Servo configuration dialog rejected.")
    
    def JointCfg(self):
        scfga = AssignServoDialog(self)
        #temp QFE:
        servoList = [0, 1, 4, 5, 8, 9, 12, 13]
        scfga.combo_hfLeft.setCurrentIndex(servoList[0])
        scfga.combo_hfRight.setCurrentIndex(servoList[4])
        scfga.combo_hrLeft.setCurrentIndex(servoList[1])
        scfga.combo_hrRight.setCurrentIndex(servoList[5])
        scfga.combo_kFLeft.setCurrentIndex(servoList[2])
        scfga.combo_kFRight.setCurrentIndex(servoList[6])
        scfga.combo_kRLeft.setCurrentIndex(servoList[3])
        scfga.combo_kRRight.setCurrentIndex(servoList[7])
        # step2
        #scfga.combo_hfLeft.setCurrentIndex(VR408.hipFrontLeft.pin)
        #scfga.combo_hfRight.setCurrentIndex(VR408.hipFrontRight.pin)
        #scfga.combo_hrLeft.setCurrentIndex(VR408.hipRearLeft.pin)
        #scfga.combo_hrRight.setCurrentIndex(VR408.hipRearRight.pin)
        #scfga.combo_kFLeft.setCurrentIndex(VR408.kneeFrontLeft.pin)
        #scfga.combo_kFRight.setCurrentIndex(VR408.kneeFrontRight.pin)
        #scfga.combo_kRLeft.setCurrentIndex(VR408.kneeRearLeft.pin)
        #scfga.combo_kRRight.setCurrentIndex(VR408.kneeRearRight.pin)
        
        #scfga.flip_hfLeft.setChecked(VR408.hipFrontLeft.flipped)
        #scfga.flip_hfRight.setChecked(VR408.hipFrontRight.flipped)
        #scfga.flip_hrLeft.setChecked(VR408.hipRearLeft.flipped)
        #scfga.flip_hrRight.setChecked(VR408.hipRearRight.flipped)
        #scfga.flip_kfLeft.setChecked(VR408.kneeFrontLeft.flipped)
        #scfga.flip_kfRight.setChecked(VR408.kneeFrontRight.flipped)
        #scfga.flip_krLeft.setChecked(VR408.kneeRearLeft.flipped)
        #scfga.flip_krRight.setChecked(VR408.kneeRearRight.flipped)
        if scfga.exec_():
            # first check duplicati...
            # step2
            #VR408.hipFrontLeft.pin = scfga.combo_hfLeft.currentIndex()
            #VR408.hipFrontRight.pin = scfga.combo_hfRight.currentIndex() 
            #VR408.hipRearLeft.pin = scfga.combo_hrLeft.currentIndex()
            #VR408.hipRearRight.pin = scfga.combo_hrRight.currentIndex()
            #VR408.kneeFrontLeft.pin = scfga.combo_kFLeft.currentIndex()
            #VR408.kneeFrontRight.pin = scfga.combo_kFRight.currentIndex()
            #VR408.kneeRearLeft.pin = scfga.combo_kRLeft.currentIndex()
            #VR408.kneeRearRight.pin = scfga.combo_kRRight.currentIndex()
            
            #VR408.hipFrontLeft.flipped = scfga.flip_hfLeft.isChecked()
            #VR408.hipFrontRight.flipped = scfga.flip_hfRight.isChecked() 
            #VR408.hipRearLeft.flipped = scfga.flip_hrLeft.isChecked()
            #VR408.hipRearRight.flipped = scfga.flip_hrRight.isChecked()
            #VR408.kneeFrontLeft.flipped = scfga.flip_kfLeft.isChecked()
            #VR408.kneeFrontRight.flipped = scfga.flip_kfRight.isChecked()
            #VR408.kneeRearLeft.flipped = scfga.flip_krLeft.isChecked()
            #VR408.kneeRearRight.flipped = scfga.flip_krRight.isChecked()
            servoList[0] = scfga.combo_hfLeft.currentIndex()
            servoList[4] = scfga.combo_hfRight.currentIndex() 
            servoList[1] = scfga.combo_hrLeft.currentIndex()
            servoList[5] = scfga.combo_hrRight.currentIndex()
            servoList[2] = scfga.combo_kFLeft.currentIndex()
            servoList[6] = scfga.combo_kFRight.currentIndex()
            servoList[3] = scfga.combo_kRLeft.currentIndex()
            servoList[7] = scfga.combo_kRRight.currentIndex()
            #VR408.reset_spider()
            self.textBrowser_log.append("Joint configuration dialog accepted.")
        else:
            self.textBrowser_log.append("Joint configuration dialog rejected.")

class ServoConfigDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("dialogservoconfig.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

class AssignServoDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("assignservodialog.ui", self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RosBotWindow()
    #VR408.initPWM()
    #VR408.configurejoints()
    #VR408.reset_spider()
    app.exec_()
    #VR408.resetPWM()
