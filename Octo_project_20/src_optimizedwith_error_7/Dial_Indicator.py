class DialUIManager:
    """
    This class connects Probe UI logic to existing UI labels on Page 26.
    It does NOT create new UI pages – it only maps values to your current labels.
    """

    def __init__(self, win, label_1, label_2, label_3, label_4, channels):
        self.win = win
        self.label_1 = label_1
        self.label_2 = label_2
        self.label_3 = label_3
        self.label_4 = label_4
        self.channels = channels  # 1 or 2 channels

        # Store mapping for easy use
        self.labels = {
            "D1": {
                "value": self.label_1,
                "status": getattr(self.win, "label_status1", None),
                "remark": getattr(self.win, "label_remark1", None),
            },
            "D2": {
                "value": self.label_2,
                "status": getattr(self.win, "label_status2", None),
                "remark": getattr(self.win, "label_remark2", None),
            },
            "D3": {
                "value": self.label_3,
                "status": getattr(self.win, "label_status3", None),
                "remark": getattr(self.win, "label_remark3", None),
            },
            "D4": {
                "value": self.label_4,
                "status": getattr(self.win, "label_status4", None),
                "remark": getattr(self.win, "label_remark4", None),
            },
        }

        # Apply initial layout rules
        self.apply_layout_rules()

    # ==================================================
    # 1/ Center layout for ONE channel
    # ==================================================
    def apply_layout_rules(self):
        if self.channels == "D1":
            self.center_single_channel()
        else:
            self.split_two_channels()

    def center_single_channel(self):
        """Place label_value1 in center for 800x480 design"""

        # MAIN LABEL (D1)
        self.labels["D1"]["value"].setGeometry(300, 150, 200, 60)
        self.labels["D1"]["value"].setStyleSheet("font-size: 24px; font-weight: bold;")

        if self.labels["D1"]["status"]:
            self.labels["D1"]["status"].setGeometry(300, 230, 200, 40)
            self.labels["D1"]["status"].setStyleSheet("background: green; color:white; font-size:18px;")

        if self.labels["D1"]["remark"]:
            self.labels["D1"]["remark"].setGeometry(300, 280, 200, 40)
            self.labels["D1"]["remark"].setStyleSheet("background: yellow; font-size:18px;")

        # Hide D2, D3, D4 for single channel
        for key in ["D2", "D3", "D4"]:
            if self.labels[key]["value"]:
                self.labels[key]["value"].hide()
            if self.labels[key]["status"]:
                self.labels[key]["status"].hide()
            if self.labels[key]["remark"]:
                self.labels[key]["remark"].hide()

    # ==================================================
    # 2/ Split the screen for TWO channels
    # ==================================================
    def split_two_channels(self):
        """
        Left = D1
        Right = D2
        """

        # Channel 1 (Left)
        self.labels["D1"]["value"].setGeometry(100, 150, 200, 60)
        self.labels["D1"]["value"].setStyleSheet("font-size: 24px; font-weight:bold;")

        if self.labels["D1"]["status"]:
            self.labels["D1"]["status"].setGeometry(100, 230, 200, 40)

        if self.labels["D1"]["remark"]:
            self.labels["D1"]["remark"].setGeometry(100, 280, 200, 40)

        # Channel 2 (Right)
        if self.labels["D2"]["value"]:
            self.labels["D2"]["value"].setGeometry(500, 150, 200, 60)
            self.labels["D2"]["value"].setStyleSheet("font-size: 24px; font-weight:bold;")

        if self.labels["D2"]["status"]:
            self.labels["D2"]["status"].setGeometry(500, 230, 200, 40)

        if self.labels["D2"]["remark"]:
            self.labels["D2"]["remark"].setGeometry(500, 280, 200, 40)

        # Hide D3 & D4 (not used)
        for key in ["D3", "D4"]:
            if self.labels[key]["value"]:
                self.labels[key]["value"].hide()
            if self.labels[key]["status"]:
                self.labels[key]["status"].hide()
            if self.labels[key]["remark"]:
                self.labels[key]["remark"].hide()

    # ==================================================
    # PUBLIC METHODS
    # ==================================================

    def update_probe(self, probe_id, value, status=None):
        probe = self.labels.get(probe_id)
        if not probe:
            return

        probe["value"].setText(str(value))

        if probe["status"] and status:
            probe["status"].setText(status)
            style = (
                "background: green; color:white;"
                if status == "OK"
                else "background: yellow; color:black;"
            )
            probe["status"].setStyleSheet(style)

        