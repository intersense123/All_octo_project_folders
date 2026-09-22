from PySide2.QtCore import QObject, QTimer

class PageStatusManager(QObject):

    def __init__(self, label, stacked):
        super().__init__()

        self.label = label
        self.stacked = stacked

        self.page_index = None

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide)

        self.label.setText("")

        # Make text bold
        font = self.label.font()
        font.setBold(True)
        self.label.setFont(font)

        # Hide status when page changes
        self.stacked.currentChanged.connect(self._on_page_changed)

    def show(self, page_index, message, timeout=2000):
        # print("STATUS:", page_index, message)
        self.page_index = page_index

        # Show only on correct page
        if self.stacked.currentIndex() != page_index:
            return

        self.timer.stop()

        self.label.setText(message)
        

        if timeout > 0:
            self.timer.start(timeout)

    def hide(self):
        self.timer.stop()

        self.label.clear()
        
       

    def _on_page_changed(self, index):
        # Hide message if user leaves that page
        if self.page_index is not None and index != self.page_index:
            self.hide()