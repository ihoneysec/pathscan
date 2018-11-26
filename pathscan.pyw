#!python34
# -*- coding: utf-8 -*-
# Created by: guo_houtan@topsec.com.cn
# Time: 20160620
#
# Form implementation generated from reading ui file 'pathscan.ui'
# Created by: PyQt4 UI code generator 4.11.4
# WARNING! All changes made in this file will be lost!

import sys
import os
import random
try:
    from urllib import request
except ImportError:
    import urllib2 as request

import requests
import gevent
from gevent.threadpool import ThreadPool
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (
     QDesktopServices,
     QColor,
     QMainWindow,
     QApplication,
     QListWidgetItem,
     QFileDialog,
     QListWidget,
     QTreeWidgetItem,
     QAbstractItemView,
     QCheckBox)
from PyQt4.QtCore import (
     pyqtSlot,
     pyqtSignal,
     Qt,
     QUrl,
     QFile,
     QThread,
     QIODevice,
     QTextStream,
     QCoreApplication)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(556, 535)
        MainWindow.setMinimumSize(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_head = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_head.setObjectName(_fromUtf8("groupBox_head"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_head)
        self.horizontalLayout.setMargin(4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_url = QtGui.QLabel(self.groupBox_head)
        self.label_url.setObjectName(_fromUtf8("label_url"))
        self.horizontalLayout.addWidget(self.label_url)
        self.lineEdit_url = QtGui.QLineEdit(self.groupBox_head)
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.label = QtGui.QLabel(self.groupBox_head)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_start = QtGui.QPushButton(self.groupBox_head)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtGui.QPushButton(self.groupBox_head)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.gridLayout_3.addWidget(self.groupBox_head, 0, 0, 1, 2)
        self.groupBox_result = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_result.setTitle(_fromUtf8(""))
        self.groupBox_result.setObjectName(_fromUtf8("groupBox_result"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_result)
        self.gridLayout_2.setMargin(4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.treeWidget = QtGui.QTreeWidget(self.groupBox_result)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(10)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_result, 1, 0, 3, 1)
        self.groupBox_dict = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_dict.setMaximumSize(QtCore.QSize(171, 16777215))
        self.groupBox_dict.setObjectName(_fromUtf8("groupBox_dict"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_dict)
        self.gridLayout_4.setMargin(4)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.listWidget = QtGui.QListWidget(self.groupBox_dict)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 3)
        self.gridLayout_3.addWidget(self.groupBox_dict, 1, 1, 1, 1)
        self.groupBox_settings = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_settings.setMaximumSize(QtCore.QSize(171, 16777215))
        self.groupBox_settings.setCheckable(False)
        self.groupBox_settings.setObjectName(_fromUtf8("groupBox_settings"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_settings)
        self.gridLayout_5.setMargin(4)
        self.gridLayout_5.setSpacing(4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.spinBox_threads = QtGui.QSpinBox(self.groupBox_settings)
        self.spinBox_threads.setMaximum(1000)
        self.spinBox_threads.setProperty("value", 10)
        self.spinBox_threads.setObjectName(_fromUtf8("spinBox_threads"))
        self.gridLayout_5.addWidget(self.spinBox_threads, 0, 1, 1, 1)
        self.label_timeout = QtGui.QLabel(self.groupBox_settings)
        self.label_timeout.setObjectName(_fromUtf8("label_timeout"))
        self.gridLayout_5.addWidget(self.label_timeout, 0, 2, 1, 1)
        self.label_thread = QtGui.QLabel(self.groupBox_settings)
        self.label_thread.setObjectName(_fromUtf8("label_thread"))
        self.gridLayout_5.addWidget(self.label_thread, 0, 0, 1, 1)
        self.spinBox_timeout = QtGui.QSpinBox(self.groupBox_settings)
        self.spinBox_timeout.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinBox_timeout.setMaximum(100)
        self.spinBox_timeout.setSingleStep(10)
        self.spinBox_timeout.setProperty("value", 5)
        self.spinBox_timeout.setObjectName(_fromUtf8("spinBox_timeout"))
        self.gridLayout_5.addWidget(self.spinBox_timeout, 0, 3, 1, 1)
        self.comboBox_action = QtGui.QComboBox(self.groupBox_settings)
        self.comboBox_action.setEnabled(True)
        self.comboBox_action.setEditable(True)
        self.comboBox_action.setFrame(True)
        self.comboBox_action.setObjectName(_fromUtf8("comboBox_action"))
        self.comboBox_action.addItem(_fromUtf8(""))
        self.comboBox_action.addItem(_fromUtf8(""))
        self.comboBox_action.addItem(_fromUtf8(""))
        self.comboBox_action.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_action, 4, 2, 1, 2)
        self.checkBox_dba = QtGui.QCheckBox(self.groupBox_settings)
        self.checkBox_dba.setObjectName(_fromUtf8("checkBox_dba"))
        self.gridLayout_5.addWidget(self.checkBox_dba, 8, 0, 1, 2)
        self.checkBox_bak = QtGui.QCheckBox(self.groupBox_settings)
        self.checkBox_bak.setChecked(True)
        self.checkBox_bak.setObjectName(_fromUtf8("checkBox_bak"))
        self.gridLayout_5.addWidget(self.checkBox_bak, 8, 2, 1, 2)
        self.comboBox_method = QtGui.QComboBox(self.groupBox_settings)
        self.comboBox_method.setEditable(False)
        self.comboBox_method.setObjectName(_fromUtf8("comboBox_method"))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_method, 3, 2, 1, 2)
        self.label_method = QtGui.QLabel(self.groupBox_settings)
        self.label_method.setObjectName(_fromUtf8("label_method"))
        self.gridLayout_5.addWidget(self.label_method, 3, 0, 1, 2)
        self.label_action = QtGui.QLabel(self.groupBox_settings)
        self.label_action.setObjectName(_fromUtf8("label_action"))
        self.gridLayout_5.addWidget(self.label_action, 4, 0, 1, 2)
        self.checkBox_pxy = QtGui.QCheckBox(self.groupBox_settings)
        self.checkBox_pxy.setObjectName(_fromUtf8("checkBox_pxy"))
        self.gridLayout_5.addWidget(self.checkBox_pxy, 9, 0, 1, 2)
        self.checkBox_for = QtGui.QCheckBox(self.groupBox_settings)
        self.checkBox_for.setObjectName(_fromUtf8("checkBox_for"))
        self.gridLayout_5.addWidget(self.checkBox_for, 9, 2, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_settings, 2, 1, 1, 1)
        self.groupBox_status = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_status.setMaximumSize(QtCore.QSize(171, 84))
        self.groupBox_status.setObjectName(_fromUtf8("groupBox_status"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_status)
        self.gridLayout.setMargin(4)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_status)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 2)
        self.checkBox_200 = QtGui.QCheckBox(self.groupBox_status)
        self.checkBox_200.setChecked(True)
        self.checkBox_200.setObjectName(_fromUtf8("checkBox_200"))
        self.gridLayout.addWidget(self.checkBox_200, 0, 0, 1, 1)
        self.checkBox_403 = QtGui.QCheckBox(self.groupBox_status)
        self.checkBox_403.setChecked(False)
        self.checkBox_403.setTristate(False)
        self.checkBox_403.setObjectName(_fromUtf8("checkBox_403"))
        self.gridLayout.addWidget(self.checkBox_403, 3, 0, 1, 1)
        self.checkBox_302 = QtGui.QCheckBox(self.groupBox_status)
        self.checkBox_302.setObjectName(_fromUtf8("checkBox_302"))
        self.gridLayout.addWidget(self.checkBox_302, 3, 1, 1, 1)
        self.checkBox_500 = QtGui.QCheckBox(self.groupBox_status)
        self.checkBox_500.setChecked(True)
        self.checkBox_500.setObjectName(_fromUtf8("checkBox_500"))
        self.gridLayout.addWidget(self.checkBox_500, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_status, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "玛德制杖 - By道长且阻", None))
        self.label_url.setText(_translate("MainWindow", "地址", None))
        self.pushButton_start.setText(_translate("MainWindow", "开始", None))
        self.pushButton_stop.setText(_translate("MainWindow", "停止", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "状态", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "路径", None))
        self.groupBox_dict.setTitle(_translate("MainWindow", "字典选择", None))
        self.groupBox_settings.setTitle(_translate("MainWindow", "扫描设置", None))
        self.label_timeout.setText(_translate("MainWindow", "超时", None))
        self.label_thread.setText(_translate("MainWindow", "线程", None))
        self.comboBox_action.setItemText(0, _translate("MainWindow", "PHP", None))
        self.comboBox_action.setItemText(1, _translate("MainWindow", "ASP", None))
        self.comboBox_action.setItemText(2, _translate("MainWindow", "ASPX", None))
        self.comboBox_action.setItemText(3, _translate("MainWindow", "JSP", None))
        self.checkBox_dba.setToolTip(_translate("MainWindow", "<html><head/><body><p>用于已知网站使用程序的情况下</p></body></html>", None))
        self.checkBox_dba.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.checkBox_dba.setText(_translate("MainWindow", "源码比对", None))
        self.checkBox_bak.setText(_translate("MainWindow", "备份扫描", None))
        self.comboBox_method.setItemText(0, _translate("MainWindow", "HEAD", None))
        self.comboBox_method.setItemText(1, _translate("MainWindow", "POST", None))
        self.comboBox_method.setItemText(2, _translate("MainWindow", "GET", None))
        self.comboBox_method.setItemText(3, _translate("MainWindow", "PUT", None))
        self.comboBox_method.setItemText(4, _translate("MainWindow", "OPTIONS", None))
        self.label_method.setText(_translate("MainWindow", "请求方法", None))
        self.label_action.setText(_translate("MainWindow", "网站类型", None))
        self.checkBox_pxy.setText(_translate("MainWindow", "自动代理", None))
        self.checkBox_for.setText(_translate("MainWindow", "递归扫描", None))
        self.groupBox_status.setTitle(_translate("MainWindow", "结果筛选", None))
        self.checkBox_200.setText(_translate("MainWindow", "200", None))
        self.checkBox_403.setText(_translate("MainWindow", "403", None))
        self.checkBox_302.setText(_translate("MainWindow", "302", None))
        self.checkBox_500.setText(_translate("MainWindow", "500", None))
        self.action.setText(_translate("MainWindow", "复制", None))
        self.action_2.setText(_translate("MainWindow", "保存", None))
###########################################################################################################3
class EventHandler(QMainWindow,Ui_MainWindow):
    @pyqtSlot(QTreeWidgetItem,int)
    def on_treeWidget_itemDoubleClicked(self,item,i):
        self.open_url(item.text(1))

    @pyqtSlot(bool)
    def on_checkBox_dba_clicked(self,event):
        if event:
            folder = QFileDialog.getExistingDirectory(None,u"选择源码所在的文件夹")
            if folder:
                self.settings['folder'] = folder
                self.updatestatus(self.settings['folder'])
            else:
                self.checkBox_dba.setCheckState(False)
        else:
            self.settings['folder'] = None

    @pyqtSlot(bool)
    def on_checkBox_pxy_clicked(self,event):
        if event:
            folder = QFileDialog.getOpenFileName(None,u"选择代理地址文件",self.dictpath,"*.proxy")
            if folder:
                self.settings['proxies'] = open(folder,'r').readlines()
                self.scan.setup(proxies=self.settings['proxies'])
                self.updatestatus(folder)
            else:
                self.checkBox_pxy.setCheckState(False)
        else:
            self.settings['proxies'] = []

    @pyqtSlot(bool)
    def on_checkBox_for_clicked(self,event):
        if event:
            self.settings['autofor'] = True
        else:
            self.settings['autofor'] = False

    @pyqtSlot(int)
    def on_spinBox_timeout_valueChanged(self,event):
        self.settings['timeout'] = event
        self.scan.setup(timeout=event)

    @pyqtSlot(int)
    def on_spinBox_threads_valueChanged(self,event):
        self.settings['threads'] = event
        self.scan.setup(threads=event)

    @pyqtSlot(str)
    def on_comboBox_method_currentIndexChanged(self,event):
        self.settings['method'] = getattr(requests,str(event).lower())
        self.scan.setup(handler=getattr(requests,str(event).lower()))

    def checkstatus(self,event,status):
        if event:
            if status not in self.status_list:
                self.status_list.append(status)
        else:
            if status in self.status_list:
                self.status_list.remove(status)

    @pyqtSlot(bool)
    def on_checkBox_200_clicked(self,event):
        self.checkstatus(event,200)

    @pyqtSlot(bool)
    def on_checkBox_301_clicked(self,event):
        self.checkstatus(event,302)

    @pyqtSlot(bool)
    def on_checkBox_403_clicked(self,event):
        self.checkstatus(event,403)

    @pyqtSlot(bool)
    def on_checkBox_500_clicked(self,event):
        self.checkstatus(event,500)

    @pyqtSlot(bool)
    def on_pushButton_start_clicked(self,event):
        self.URL = str(self.lineEdit_url.text())
        if not self.URL or self.URL[:4].lower()!='http':
           self.updatestatus(u"请输入有效的地址")
           return
        if self.URL[-1]!='/':
           self.URL += '/'
        if self.pushButton_start.text()==u"开始":
           self.pushButton_start.setText(u"暂停")
           self.treeWidget.clear()
           self.start(self.URL)
           self.lenthmax = len(self.pathlist)
           self.progressBar.setRange(0,self.lenthmax)
           self.updatestatus(u"开始扫描")
        elif self.pushButton_start.text()==u"暂停":
           self.pushButton_start.setText(u"继续")
           self.scan.pause()
           self.updatestatus(u"暂停扫描")
        elif self.pushButton_start.text()==u"继续":
           self.pushButton_start.setText(u"暂停")
           self.scan.pause()
           self.updatestatus(u"继续扫描~")

    @pyqtSlot(bool)
    def on_pushButton_stop_clicked(self,event):
        self.scan.stop()
        self.pushButton_start.setText(u"开始")
        if event:
            self.updatestatus(u"扫描完成。")
            self.progressBar.setValue(self.lenthmax)
        else:
            self.updatestatus(u"中断扫描,WTF?")

###########################################################################################

class GeventThread(QThread):
    """使用异步方式"""
    signal = pyqtSignal(bool)
    signal_event = pyqtSignal(int,str)
    def __init__(self):
        QThread.__init__(self)
        self.Queue   = []
        self.threads = 10
        self.timeout = 10
        self.__FLAG  = True   #stop
        self.__STAT  = False  #pause
    def recv(self,url):
        headers = {'Referer':url}
        headers.update({'User-Agent':random.choice(self.headers).strip()})
        proxies = None
        if self.proxies:
            ips = random.choice(self.proxies).strip()
            proxies = {'http':ips,'https':ips}
        status = self.handler(url=url,headers=headers,proxies=proxies).status_code
        self.signal_event.emit(status,url)
    def run(self):
        if self.Queue and self.handler:
            self.__FLAG  = True
            self.__STAT  = False
            pool = ThreadPool(self.threads)
            Queue = iter(self.Queue)
            while self.__FLAG:
                if self.__STAT:
                    self.sleep(1)
                    continue
                try:
                    data = next(Queue)
                    pool.spawn(self.recv, data)
                except StopIteration:
                    self.__FLAG = False
                    break
            gevent.wait(timeout=self.timeout)
        self.signal.emit(True)
    def stop(self):
        self.__FLAG = False
        self.__STAT = False
    def pause(self):
        self.__STAT = not self.__STAT
    def setup(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

class QIterThread(QThread):
    """使用多线程方式"""
    class QHandlerThread(QThread):
        """具体处理事务的子线程"""
        def setup(self,handler,**kwargs):
            self.handler = handler
            self.kwargs = kwargs
        def run(self):
            try:
                result = self.handler(**self.kwargs)
                status = result.status_code
                #lenth = len(result.content)
                self.signal_event.emit(status,self.kwargs['url'])
            except Exception as e:
                self.signal_event.emit(500,str(e))

    signal = pyqtSignal(bool)
    signal_event = pyqtSignal(int,str)
    def __init__(self):
        QThread.__init__(self)
        self.Queue   = []
        self.threads = 10
        self.timeout = 10
        self.event   = None
        self.__FLAG  = True   #stop
        self.__STAT  = False  #pause
    def run(self):
        if self.Queue and self.signal and self.event and self.handler:
            self.__FLAG  = True
            self.__STAT  = False
            self.Queue = iter(self.Queue)
            while self.__FLAG:
                __ = []
                if self.__STAT:
                    self.sleep(1)
                    continue
                for _ in range(self.threads):
                    try:
                        data = next(self.Queue)
                    except StopIteration:
                        self.__FLAG = False
                        break
                    _Q = self.QHandlerThread()
                    _Q.setup(self.handler,url=data,headers=headers,proxies=proxies,timeout=self.timeout)
                    __.append(_Q)
                    self.signal_event.connect(self.event)
                for _ in __:
                    _.start()
                for _ in __:
                    _.wait()
        self.signal.emit(True) #biu! biu! biu!
    def stop(self):
        self.__FLAG = False
        self.__STAT = False
    def pause(self):
        self.__STAT = not self.__STAT
    def setup(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
######################################################################################################
class ScanHandler(EventHandler):
    session = requests.Session()
    def __init__(self):
        super(EventHandler, self).__init__()
        self.setupUi(self)
        self.PATH = os.getcwd()
        self.URL = ''
        self.dictpath = self.PATH + '/data/'
        self.agents_path = self.dictpath + 'user-agents.txt'
        self.dicttype = '.dic'
        self.settings = {}  #选项字典
        self.siteinfo = {}  #网站信息
        self.filelist = []  #字典文件列表
        self.pathlist = []  #字典路径列表
        self.lenthmax = 0   #字典列表总长
        self.current  = 0   #当前字典位数
        self.load_filelist(self.dictpath,self.dicttype)
        self.scan = GeventThread()
        self.scan.signal.connect(self.on_pushButton_stop_clicked)
        self.scan.signal_event.connect(self.handlerThread_Event)
        self.status_list = [200,500]
        self.settings['proxies'] = []
        self.updatestatus(u"准备就绪~")

    def start(self,url):
        self.URL = url
        self.pathlist = []
        self.load_settings()
        self.scan.setup(
            Queue = self.pathlist,
            handler = self.settings['method'],
            threads = self.settings['threads'],
            timeout = self.settings['timeout'],
            headers = self.settings['headers'],
            proxies = self.settings['proxies'])
        self.scan.start()

    def load_filelist(self,dictpath,dicttype='.dic'):
        """载入字典文件"""
        if not os.path.isdir(dictpath):
           os.mkdir(dictpath)
        files = os.listdir(dictpath)
        for name in files:
            #print(name)
            filepathname = dictpath+name
            if not os.path.isdir(filepathname) and filepathname.lower().endswith(dicttype):
               item = QListWidgetItem(name)
               item.setCheckState(Qt.Checked)
               self.listWidget.addItem(item)

    def load_pathlist(self):
        """载入字典内容"""
        pathlist = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState():
               inFile = QFile(self.dictpath + item.text())
               if inFile.open(QIODevice.ReadOnly):
                   stream = QTextStream(inFile)
                   while not stream.atEnd():
                       line = stream.readLine()
                       pathlist.append(line)
        return pathlist

    def load_settings(self):
        self.current = 0
        self.pathlist = []
        self.pathlist += self.load_pathlist()
        self.settings['threads'] = int(self.spinBox_threads.value())
        self.settings['timeout'] = int(self.spinBox_timeout.value())
        self.settings['headers'] = open(self.agents_path,'r').readlines()
        self.settings['autofor'] = False
        self.settings['action'] = str(self.comboBox_action.currentText()).strip().lower()
        self.settings['method'] = getattr(self.session,str(self.comboBox_method.currentText()).strip().lower())
        self.load_siteinfo(self.URL)
        if self.checkBox_dba.checkState():
             self.pathlist += self.load_folder(self.settings['folder'])
        pathlist = []
        for url in self.pathlist:
            pathlist.append(self.URL+request.quote(self.load_url(str(url))))
        self.pathlist = pathlist
        if self.checkBox_dba.checkState():
           self.pathlist = self.makebak(self.pathlist,self.settings['action'])

    def makebak(self,pathlist,url,action=None):
        pathlist = []
        for url in pathlist:
            if url.lower().endswith('.'+action):
                name = '.'.join(url.split('/')[-1].split('.')[:-2])
                real = '/'.join(url.split('/')[:-1])
                pathlist.append(url+'.bak')
                pathlist.append(real+'/'+name+'.bak')
                pathlist.append(url+'~')
                pathlist.append(real+'/'+name+'~')
                pathlist.append(real+'/.'+name+'.'+action+'.swp')
        return pathlist

    def load_folder(self,folder):
        """载入文件夹下所有文件"""
        filelist = []
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                filelist.append(("%s/%s"%(dirpath,filename)).replace(folder,'').replace('\\','/'))
        return filelist

    def load_url(self,url):
        url = url.replace("{TYPE}",self.siteinfo['TYPE'])
        url = url.replace("{NAME}",self.siteinfo['NAME'])
        url = url.replace("{DOMAIN}",self.siteinfo['DOMAIN'])
        return url

    def load_siteinfo(self,url):
        """
        {TYPE} 网页类型
        {NAME} 网站名称
        {DOMAIN} 网站域名
        """
        domain = 'www'
        if '://' in url:
            head,urlpath = url.split('://')
            if '/' in urlpath:
                domain = urlpath.split('/')[0]
            else:
                domain = urlpath
        self.siteinfo['NAME'] = self.siteinfo['DOMAIN'] = domain
        self.siteinfo['TYPE'] = self.settings['action']

    def updatestatus(self,msg):
        """更新状态栏"""
        self.progressBar.setValue(self.current)
        self.statusBar.showMessage(u"  共 %d 条 | 第 %d 条| %s"%(self.lenthmax,self.current,msg))

    def open_url(self,url):
        QDesktopServices.openUrl(QUrl(url))

    def handlerThread_Event(self,status,url):
        """线程响应事件"""
        self.current += 1
        self.updatestatus(url)
        if status in self.status_list:
            item = QTreeWidgetItem()
            item.setText(0,str(status))
            item.setText(1,str(url))
            if status == 200:
                item.setTextColor(0,QColor("#00ff00"))
                item.setTextColor(1,QColor("#00ff00"))
            elif status == 500:
                item.setTextColor(0,QColor("#ff0000"))
                item.setTextColor(1,QColor("#ff0000"))
            else:
                item.setTextColor(0,QColor("#0000ff"))
                item.setTextColor(1,QColor("#0000ff"))
            self.treeWidget.addTopLevelItem(item)

###########################################################################

def main():
    app = QApplication(sys.argv)
    mainWindow = ScanHandler()
    mainWindow.show()
    sys.exit(app.exec_())

main()

