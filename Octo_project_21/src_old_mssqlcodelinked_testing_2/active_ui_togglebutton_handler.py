from PySide2.QtWidgets import QGraphicsOpacityEffect, QLabel, QLineEdit, QRadioButton
from PySide2.QtGui import QPixmap

def set_widget_opacity(widget, opacity: float):
    """Set opacity of a widget."""
    effect = QGraphicsOpacityEffect(widget)
    effect.setOpacity(opacity)
    widget.setGraphicsEffect(effect)

def update_angle_toggle(win):
    """
    Updates the angle calculation toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.AngleCalculationSettings_dict.get('ANGLE_CALCULATION_SETTINGS_ON_OFF', 'OFF')

    win.valueObj.activeVariables_dict["AngleCalculationOnOff"] = state
    
    # List all related widgets
    widgets = [
        win.label_angleCalculationMasterAngle,
        win.lineEdit_angleDegree,
        win.lineEdit_angleMinutes,
        win.lineEdit_angleSeconds,
        win.label_positiveTol,
        win.lineEdit_toleranceMin,
        win.lineEdit_toleranceSec,
        win.label_negativeTol,
        win.lineEdit_negativeTolMin,
        win.lineEdit_negativeTolSec,
        win.label_Distance,
        win.lineEdit_distanceMm,
        win.label_distanceInMm,
        win.label_Angle,
        win.radioButton_halfAngle,
        win.radioButton_2_fullAngle,
        win.label_angleDegree,
        win.label_angleMin,
        win.label_angleSec,
        win.label_tolMin,
        win.label_tolSec,
        win.label_tolPositiveMin,
        win.label_tolPositiveSec
    ]

    # Update toggle pixmap
    if state == 'ON':
        win.toggelButton_angleCalculation.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggelButton_angleCalculation.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)

def update_rs232_toggle(win):
    """
    Updates the Rs232 toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.RS232Settings_dict.get('RS232_ON_OFF','OFF')
    
    # Also update activeVariables_dict to stay consistent
    win.valueObj.activeVariables_dict["RS232OnOff"] = state
    
    # List all related widgets
    widgets = [
        win.label_baudRate,win.comboBox_baudRate,
        win.label_dataBits,win.comboBox_dataBits,
        win.label_parity,win.comboBox_parity,
        win.label_stopBits,win.comboBox_stopBits,
        win.label_flowControl,win.comboBox_flowControl,
        win.label_portName,win.lineEdit_portName
    ]
    # Update toggle pixmap
    if state == 'ON':
        win.toggleButton_rs232.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggleButton_rs232.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)


def update_autooffcet_toggle(win):
    """
    Updates the autooffcet toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.AOCSettings_dict.get('AOC_ON_OFF','OFF')
    win.valueObj.activeVariables_dict["AOCOnOff"] = state
    widgets = [
        win.button_cncListAoc,
        win.button_reportsAoc,
        win.label_axis,win.comboBox_axis,
        win.label_offsetNo,win.lineEdit_offsetNo,
        win.label_upperOffsetLimit,win.lineEdit_upperOffcetLimit,
        win.label_lowerOffsetLimit,win.lineEdit_lowerOffsetLimit,
        win.label_machine,win.comboBox_machine,
        win.label_direction,win.comboBox_direction,
        win.label_turretNo,win.lineEdit_turretNo,
        win.label_bufferpartNo,win.lineEdit_bufferPartNo
    ]
    if state == 'ON' :
        win.toggleButton_aoc.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggleButton_aoc.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)   

def update_networkdatabase_toggle(win):
    """
    Updates the Networkdatabase toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.NetworkedDatabaseSettings_dict.get('NETWORKE_BASED_DATABASE_ON_OFF','OFF')
    win.valueObj.activeVariables_dict["NetworkedDatabaseSettingsOnOff"] = state
    widgets = [
        win.label_driverNameDb, win.lineEdit_driverNameDb,
        win.label_serverNameDb,win.lineEdit_serverNameDb,
        win.label_databaseNameDb ,win.lineEdit_databaseNameDb,
        win.label_username_Db,win.lineEdit_usernameDb,
        win.label_passwordDb,win.lineEdit_passwordDb,
        win.label_deviceName,win.lineEdit_deviceName
    ]
    if state == 'ON' :
        win.toggleButton_networkBasedDatabase.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggleButton_networkBasedDatabase.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)   

def update_IOSetting_Buzzer_toggle(win):
    """
    Updates the IoSetting Buzzer toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('BUZZER', {}).get('Enable', '0')
    win.valueObj.activeVariables_dict["BuzzerOnOff"] = state
    
    widgets = [
        win.radioButton_okBuzzer,win.radioButton_reworkNotokBuzzer
    ]
    if state == '1':
        win.toggleButton_buzzer.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggleButton_buzzer.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)

def update_IOSetting_Relay_toggle(win):
    """
    Updates the IoSetting Relay toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('RELAY', {}).get('Enable', '0')    
    win.valueObj.activeVariables_dict["RelayOnOff"] = state
    
    widgets = [
        win.label_relayTime,win.lineEdit_relayTime
    ]
    if state == '1':
        win.toggelButton_relay.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggelButton_relay.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)

def update_IOSetting_CycleStopTimer_toggle(win):
    """
    Updates the IoSetting CycleStopTimer toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('CYCLE_STOP_TIMER', {}).get('Enable', '0')     
    win.valueObj.activeVariables_dict["CycleStopTimer"] = state
    
    widgets = [
        win.label_cycleTime,win.lineEdit_cycleTime
    ]
    if state == '1':
        win.toggelButton_cycleStopTimer.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggelButton_cycleStopTimer.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)

def update_IOSetting_AutosaveReading_toggle(win):
    """
    Updates the IoSetting AutosaveReading toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('AUTO_SAVE_READING', {}).get('Enable', '0')    
    win.valueObj.activeVariables_dict["AutoSaveOnOff"] = state
    
    if state == '1':
        win.toggelButton_autoSaveReading.setPixmap(QPixmap(":/images/Switcher_On.png"))    
    else:
        win.toggelButton_autoSaveReading.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        
        

def update_IOSetting_PartTraceability_toggle(win):
    """
    Updates the IoSetting PartTraceability toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('PART_TRACEABILITY', {}).get('Enable', '0')
    win.valueObj.activeVariables_dict["PartTraceabilityOnOff"] = state
     
    widgets = [
        win.radioButton_manualPartTraceability,win.radioButton_autoPartTraceability
    ]
    if state == '1':
        win.toggelButton_partTraceability.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggelButton_partTraceability.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)


def update_IOSetting_TimetoMasterSet_toggle(win):
    """
    Updates the IoSetting TimetoMasterSet  toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('TIME_TO_MASTER_SET', {}).get('Enable', '0')     
    win.valueObj.activeVariables_dict["TimeToMasterSetOnOff"] = state
    
    widgets = [
        win.lineEdit_timeToMasterSet,win.label_hrs
    ]
    if state == '1':
        win.toggleButtontimeToSetMaster.setPixmap(QPixmap(":/images/Switcher_On.png"))
        for w in widgets:
            w.setEnabled(True)
            set_widget_opacity(w, 1.0)
    else:
        win.toggleButtontimeToSetMaster.setPixmap(QPixmap(":/images/Switcher_OFF.png"))
        for w in widgets:
            w.setDisabled(True)
            set_widget_opacity(w, 0.5)



def update_IOSetting_MasterGrouping_toggle(win):
    """
    Updates the IoSetting MasterGrouping toggle image, enables/disables widgets,
    and sets opacity based on the dictionary value in win.valueObj.
    """
    state = win.valueObj.IOSettings_dict.get('MASTER_GROUPING', {}).get('Enable', '0')     
    win.valueObj.activeVariables_dict["MasterGroupingOnOff"] = state
    
    if state == '1':
        win.toggleButton_masterGrouping.setPixmap(QPixmap(":/images/Switcher_On.png"))    
    else:
        win.toggleButton_masterGrouping.setPixmap(QPixmap(":/images/Switcher_OFF.png"))



       