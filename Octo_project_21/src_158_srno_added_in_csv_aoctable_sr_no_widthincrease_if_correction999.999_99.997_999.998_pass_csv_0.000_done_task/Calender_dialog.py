# calendar_dialog.py

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt, QDate


class AOCDateCalendar(QtWidgets.QDialog):
    """
    Touch-friendly custom date selector for AOC.

    Usage:
        AOCDateCalendar("from", self).exec_()
        AOCDateCalendar("to", self).exec_()

    Updates:
        self.ui.label_fromDate
        self.ui.label_toDate
    """

    # =============================================================
    # INIT
    # =============================================================

    def __init__(self, date_type="from", parent=None):

        super(AOCDateCalendar, self).__init__(parent)

        self.ui = parent
        self.date_type = date_type

        # =========================================================
        # TARGET LABEL
        # =========================================================

        if self.date_type == "from":
            self.target_label = self.ui.label_fromDate
        else:
            self.target_label = self.ui.label_toDate

        # =========================================================
        # CURRENT DISPLAY DATE
        # =========================================================

        self.display_year = 0
        self.display_month = 0
        self.selected_date = QDate.currentDate()

        # =========================================================
        # WINDOW
        # =========================================================

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setWindowModality(
            Qt.ApplicationModal
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        # =========================================================
        # SIZE
        # =========================================================

        if self.ui is not None:

            self.setGeometry(
                self.ui.rect()
            )

        else:

            screen = QtWidgets.QApplication.primaryScreen()

            if screen:

                self.setGeometry(
                    screen.geometry()
                )

        # =========================================================
        # LOAD EXISTING DATE
        # =========================================================

        selected = QDate.fromString(
            self.target_label.text().strip(),
            "dd/MM/yyyy"
        )

        if selected.isValid():

            self.selected_date = selected

        else:

            self.selected_date = QDate.currentDate()

        self.display_year = self.selected_date.year()
        self.display_month = self.selected_date.month()

        # =========================================================
        # STYLE
        # =========================================================

        self._set_style()

        # =========================================================
        # CREATE UI
        # =========================================================

        self._create_ui()

    # =============================================================
    # STYLE
    # =============================================================

    def _set_style(self):

        self.setStyleSheet("""
            /* =====================================================
            DIALOG
            ===================================================== */

            QDialog {
                background: transparent;
            }


            /* =====================================================
            MAIN PANEL
            ===================================================== */

            #calendarPanel {
                background-color: #2b2b2b;
                border: 1px solid #4a4a4a;
                border-radius: 14px;
            }


            /* =====================================================
            TITLE
            ===================================================== */

            #calendarTitle {
                color: #f2f2f2;
                background: transparent;

                font-size: 20px;
                font-weight: bold;

                padding: 0px;
                margin: 0px;
            }


            /* =====================================================
            NAVIGATION BUTTONS
            ===================================================== */

            #monthPrevButton,
            #monthNextButton,
            #yearPrevButton,
            #yearNextButton {

                color: #ffffff;
                background-color: #3d3d3d;

                border: 1px solid #5c5c5c;
                border-radius: 8px;

                font-size: 20px;
                font-weight: bold;
            }


            #monthPrevButton:hover,
            #monthNextButton:hover,
            #yearPrevButton:hover,
            #yearNextButton:hover {

                background-color: #4d4d4d;
            }


            #monthPrevButton:pressed,
            #monthNextButton:pressed,
            #yearPrevButton:pressed,
            #yearNextButton:pressed {

                background-color: #1976d2;
            }


            /* =====================================================
            MONTH / YEAR DISPLAY
            ===================================================== */

            #monthDisplay,
            #yearDisplay {

                color: #ffffff;
                background-color: #353535;

                border: 1px solid #505050;
                border-radius: 8px;

                font-size: 20px;
                font-weight: bold;

                padding: 0px;
                margin: 0px;
            }


            /* =====================================================
            WEEKDAY HEADER - MONDAY TO FRIDAY
            ===================================================== */

            #weekdayHeader {

                background-color: #eeeeee;

                border-right: 1px solid #888888;
                border-bottom: 1px solid #888888;

                color: #000000;

                font-size: 16px;
                font-weight: bold;
            }


            /* =====================================================
            SATURDAY / SUNDAY HEADER
            ===================================================== */

            #saturdayHeader,
            #sundayHeader {

                background-color: #eeeeee;

                border-right: 1px solid #888888;
                border-bottom: 1px solid #888888;

                color: #c40000;

                font-size: 16px;
                font-weight: bold;
            }


            /* =====================================================
            CALENDAR TABLE
            ===================================================== */

            #calendarTable {

                background-color: #303030;

                border: 1px solid #454545;

                gridline-color: #454545;

                outline: none;

                font-size: 18px;
                font-weight: bold;
            }


            #calendarTable::item {

                background-color: #303030;

                border: none;

                padding: 0px;
            }


            #calendarTable::item:selected {

                background-color: #1976d2;

                color: #ffffff;
            }


            /* =====================================================
            SELECTED DATE
            ===================================================== */

            #selectedDateLabel {

                color: #ffffff;

                background-color: #353535;

                border: 1px solid #4a4a4a;
                border-radius: 7px;

                font-size: 17px;
                font-weight: bold;

                padding: 0px;
            }


            /* =====================================================
            CANCEL / OK
            ===================================================== */

            #cancelButton,
            #okButton {

                color: #ffffff;

                background-color: #444444;

                border: 1px solid #666666;
                border-radius: 7px;

                font-size: 15px;
                font-weight: bold;
            }


            #cancelButton:hover,
            #okButton:hover {

                background-color: #505050;
            }


            #cancelButton:pressed,
            #okButton:pressed {

                background-color: #1976d2;
            }
        """)

    # =============================================================
    # CREATE UI
    # =============================================================

    def _create_ui(self):

        # =========================================================
        # PANEL
        # =========================================================

        self.panel = QtWidgets.QFrame(self)

        self.panel.setObjectName(
            "calendarPanel"
        )

        # ALWAYS FIXED SIZE
        self.panel.setFixedSize(
            560,
            420
        )

        # Center panel
        self.panel.move(
            (self.width() - self.panel.width()) // 2,
            (self.height() - self.panel.height()) // 2
        )

        # =========================================================
        # MAIN LAYOUT
        # =========================================================

        layout = QtWidgets.QVBoxLayout(
            self.panel
        )

        layout.setContentsMargins(
            0,
            3,
            0,
            3
        )

        layout.setSpacing(
            1
        )

        # =========================================================
        # TITLE
        # =========================================================

        self.title = QtWidgets.QLabel(
            "Select {} Date".format(
                self.date_type.title()
            )
        )

        self.title.setObjectName(
            "calendarTitle"
        )

        self.title.setAlignment(
            Qt.AlignCenter
        )

        # IMPORTANT:
        # 5px was clipping the title.
        self.title.setFixedHeight(
            27
        )

        layout.addWidget(
            self.title
        )

        # =========================================================
        # SEPARATOR
        # =========================================================

        separator = QtWidgets.QFrame()

        separator.setFrameShape(
            QtWidgets.QFrame.HLine
        )

        separator.setFrameShadow(
            QtWidgets.QFrame.Plain
        )

        separator.setStyleSheet(
            "background-color: #4a4a4a; border: none;"
        )

        separator.setFixedHeight(
            1
        )

        layout.addWidget(
            separator
        )

        # =========================================================
        # MONTH NAVIGATION
        # =========================================================

        month_layout = QtWidgets.QHBoxLayout()

        month_layout.setContentsMargins(
            30,
            2,
            30,
            0
        )

        month_layout.setSpacing(
            10
        )

        self.month_prev_button = QtWidgets.QPushButton(
            "◀"
        )

        self.month_prev_button.setObjectName(
            "monthPrevButton"
        )

        self.month_prev_button.setFixedSize(
            50,
            30
        )

        self.month_display = QtWidgets.QLabel()

        self.month_display.setObjectName(
            "monthDisplay"
        )

        self.month_display.setAlignment(
            Qt.AlignCenter
        )

        self.month_display.setFixedHeight(
            30
        )

        self.month_next_button = QtWidgets.QPushButton(
            "▶"
        )

        self.month_next_button.setObjectName(
            "monthNextButton"
        )

        self.month_next_button.setFixedSize(
            50,
            30
        )

        month_layout.addWidget(
            self.month_prev_button
        )

        month_layout.addWidget(
            self.month_display,
            1
        )

        month_layout.addWidget(
            self.month_next_button
        )

        layout.addLayout(
            month_layout
        )

        # =========================================================
        # YEAR NAVIGATION
        # =========================================================

        year_layout = QtWidgets.QHBoxLayout()

        year_layout.setContentsMargins(
            30,
            0,
            30,
            0
        )

        year_layout.setSpacing(
            10
        )

        self.year_prev_button = QtWidgets.QPushButton(
            "◀"
        )

        self.year_prev_button.setObjectName(
            "yearPrevButton"
        )

        self.year_prev_button.setFixedSize(
            50,
            30
        )

        self.year_display = QtWidgets.QLabel()

        self.year_display.setObjectName(
            "yearDisplay"
        )

        self.year_display.setAlignment(
            Qt.AlignCenter
        )

        self.year_display.setFixedHeight(
            30
        )

        self.year_next_button = QtWidgets.QPushButton(
            "▶"
        )

        self.year_next_button.setObjectName(
            "yearNextButton"
        )

        self.year_next_button.setFixedSize(
            50,
            30
        )

        year_layout.addWidget(
            self.year_prev_button
        )

        year_layout.addWidget(
            self.year_display,
            1
        )

        year_layout.addWidget(
            self.year_next_button
        )

        layout.addLayout(
            year_layout
        )

        # =========================================================
        # WEEKDAY HEADER
        # =========================================================

        weekday_layout = QtWidgets.QHBoxLayout()

        weekday_layout.setContentsMargins(
            0,
            2,
            0,
            0
        )

        weekday_layout.setSpacing(
            0
        )

        weekdays = [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]

        self.weekday_labels = []

        for index, day_name in enumerate(weekdays):

            label = QtWidgets.QLabel(
                day_name
            )

            if index == 5:

                label.setObjectName(
                    "saturdayHeader"
                )

            elif index == 6:

                label.setObjectName(
                    "sundayHeader"
                )

            else:

                label.setObjectName(
                    "weekdayHeader"
                )

            label.setAlignment(
                Qt.AlignCenter
            )

            # USER REQUESTED 40 HEIGHT
            label.setFixedHeight(
                40
            )

            weekday_layout.addWidget(
                label,
                1
            )

            self.weekday_labels.append(
                label
            )

        layout.addLayout(
            weekday_layout
        )

        # =========================================================
        # CUSTOM CALENDAR TABLE
        # =========================================================

        self.calendar_table = QtWidgets.QTableWidget()

        self.calendar_table.setObjectName(
            "calendarTable"
        )

        self.calendar_table.setColumnCount(
            7
        )

        self.calendar_table.setRowCount(
            6
        )

        self.calendar_table.verticalHeader().hide()
        self.calendar_table.horizontalHeader().hide()

        self.calendar_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )

        self.calendar_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectItems
        )

        self.calendar_table.setFocusPolicy(
            Qt.NoFocus
        )

        self.calendar_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )

        self.calendar_table.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.calendar_table.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.calendar_table.setShowGrid(
            True
        )

        self.calendar_table.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )

        horizontal_header = (
            self.calendar_table.horizontalHeader()
        )

        horizontal_header.setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        vertical_header = (
            self.calendar_table.verticalHeader()
        )

        vertical_header.setSectionResizeMode(
            QtWidgets.QHeaderView.Fixed
        )

        vertical_header.setDefaultSectionSize(
            30
        )

        layout.addWidget(
            self.calendar_table
        )

        # =========================================================
        # SELECTED DATE
        # =========================================================

        self.selected_label = QtWidgets.QLabel()

        self.selected_label.setObjectName(
            "selectedDateLabel"
        )

        self.selected_label.setAlignment(
            Qt.AlignCenter
        )

        self.selected_label.setFixedHeight(
            30
        )

        layout.addWidget(
            self.selected_label
        )

        # =========================================================
        # BOTTOM BUTTONS
        # =========================================================

        button_layout = QtWidgets.QHBoxLayout()

        button_layout.setContentsMargins(
            50,
            2,
            50,
            0
        )

        button_layout.setSpacing(
            10
        )

        self.cancel_button = QtWidgets.QPushButton(
            "✕  CANCEL"
        )

        self.cancel_button.setObjectName(
            "cancelButton"
        )

        self.cancel_button.setFixedSize(
            135,
            37
        )

        self.ok_button = QtWidgets.QPushButton(
            "✓  OK"
        )

        self.ok_button.setObjectName(
            "okButton"
        )

        self.ok_button.setFixedSize(
            135,
            37
        )

        button_layout.addStretch()

        button_layout.addWidget(
            self.cancel_button
        )

        button_layout.addWidget(
            self.ok_button
        )

        button_layout.addStretch()

        layout.addLayout(
            button_layout
        )

        # =========================================================
        # SIGNALS
        # =========================================================

        self.month_prev_button.clicked.connect(
            self._previous_month
        )

        self.month_next_button.clicked.connect(
            self._next_month
        )

        self.year_prev_button.clicked.connect(
            self._previous_year
        )

        self.year_next_button.clicked.connect(
            self._next_year
        )

        self.calendar_table.cellClicked.connect(
            self._calendar_cell_clicked
        )

        self.ok_button.clicked.connect(
            self.accept
        )

        self.cancel_button.clicked.connect(
            self.reject
        )

        # =========================================================
        # INITIAL CALENDAR
        # =========================================================

        self._update_calendar()

    # =============================================================
    # UPDATE CALENDAR
    # =============================================================

    def _update_calendar(self):

        # =========================================================
        # MONTH DISPLAY
        # =========================================================

        month_date = QDate(
            self.display_year,
            self.display_month,
            1
        )

        self.month_display.setText(
            month_date.toString(
                "MMMM"
            ).upper()
        )

        self.year_display.setText(
            str(
                self.display_year
            )
        )

        # =========================================================
        # FIRST DAY OF MONTH
        # Monday = 0
        # Sunday = 6
        # =========================================================

        first_date = QDate(
            self.display_year,
            self.display_month,
            1
        )

        first_day_index = (
            first_date.dayOfWeek() - 1
        )

        # =========================================================
        # NUMBER OF DAYS IN MONTH
        # =========================================================

        days_in_month = (
            first_date.daysInMonth()
        )

        # =========================================================
        # REQUIRED ROWS ONLY
        #
        # Example:
        #
        # 31 | 1 | 2 | 3 | 4 | 5 | 6
        #
        # The calendar stops there.
        # No additional empty row.
        # =========================================================

        total_cells = (
            first_day_index +
            days_in_month
        )

        required_rows = (
            (total_cells + 6) // 7
        )

        # Minimum 4 rows
        required_rows = max(
            4,
            required_rows
        )

        self.calendar_table.setRowCount(
            required_rows
        )

        # =========================================================
        # TABLE HEIGHT
        # =========================================================

        row_height = 30

        for row in range(required_rows):

            self.calendar_table.setRowHeight(
                row,
                row_height
            )

        table_height = (
            required_rows * row_height +
            2
        )

        self.calendar_table.setFixedHeight(
            table_height
        )

        # =========================================================
        # CLEAR TABLE
        # =========================================================

        self.calendar_table.clearContents()

        # =========================================================
        # NEXT MONTH
        # =========================================================

        next_month_date = (
            first_date.addMonths(1)
        )

        next_month_day = 1

        # =========================================================
        # FILL CALENDAR
        # =========================================================

        for row in range(required_rows):

            for column in range(7):

                cell_index = (
                    row * 7 +
                    column
                )

                item = QtWidgets.QTableWidgetItem()

                item.setTextAlignment(
                    Qt.AlignCenter
                )

                # =================================================
                # BEFORE CURRENT MONTH
                # =================================================

                if cell_index < first_day_index:

                    item.setText(
                        ""
                    )

                    item.setData(
                        Qt.UserRole,
                        None
                    )

                    item.setFlags(
                        Qt.NoItemFlags
                    )

                # =================================================
                # CURRENT MONTH
                # =================================================

                elif cell_index < (
                    first_day_index +
                    days_in_month
                ):

                    day = (
                        cell_index -
                        first_day_index +
                        1
                    )

                    current_date = QDate(
                        self.display_year,
                        self.display_month,
                        day
                    )

                    item.setText(
                        str(day)
                    )

                    item.setData(
                        Qt.UserRole,
                        current_date
                    )

                    item.setFlags(
                        Qt.ItemIsEnabled |
                        Qt.ItemIsSelectable
                    )

                    # WEEKEND = RED
                    if column >= 5:

                        item.setForeground(
                            QtGui.QColor(
                                "#ff0000"
                            )
                        )

                    # MONDAY TO FRIDAY = WHITE
                    else:

                        item.setForeground(
                            QtGui.QColor(
                                "#ffffff"
                            )
                        )

                    # SELECTED DATE
                    if current_date == self.selected_date:

                        item.setBackground(
                            QtGui.QColor(
                                "#1976d2"
                            )
                        )

                        item.setForeground(
                            Qt.white
                        )

                # =================================================
                # NEXT MONTH
                #
                # Only fill remaining cells in final row.
                # =================================================

                else:

                    next_date = QDate(
                        next_month_date.year(),
                        next_month_date.month(),
                        next_month_day
                    )

                    item.setText(
                        str(
                            next_month_day
                        )
                    )

                    item.setData(
                        Qt.UserRole,
                        next_date
                    )

                    item.setFlags(
                        Qt.ItemIsEnabled |
                        Qt.ItemIsSelectable
                    )

                    # Weekend next month = dim red
                    if column >= 5:

                        item.setForeground(
                            QtGui.QColor(
                                "#cc2222"
                            )
                        )

                    # Weekday next month = dim gray
                    else:

                        item.setForeground(
                            QtGui.QColor(
                                "#aaaaaa"
                            )
                        )

                    next_month_day += 1

                self.calendar_table.setItem(
                    row,
                    column,
                    item
                )

        # =========================================================
        # UPDATE SELECTED DATE LABEL
        # =========================================================

        self._update_selected_date()

    # =============================================================
    # CALENDAR CELL CLICKED
    # =============================================================

    def _calendar_cell_clicked(
        self,
        row,
        column
    ):

        item = self.calendar_table.item(
            row,
            column
        )

        if item is None:
            return

        selected = item.data(
            Qt.UserRole
        )

        if not isinstance(
            selected,
            QDate
        ):
            return

        if not selected.isValid():
            return

        # =========================================================
        # SET SELECTED DATE
        # =========================================================

        self.selected_date = selected

        # =========================================================
        # IF NEXT MONTH DATE CLICKED
        # OPEN THAT MONTH
        # =========================================================

        if (
            selected.year() != self.display_year or
            selected.month() != self.display_month
        ):

            self.display_year = (
                selected.year()
            )

            self.display_month = (
                selected.month()
            )

        self._update_calendar()

    # =============================================================
    # PREVIOUS MONTH
    # =============================================================

    def _previous_month(self):

        current = QDate(
            self.display_year,
            self.display_month,
            1
        )

        previous = current.addMonths(
            -1
        )

        self.display_year = (
            previous.year()
        )

        self.display_month = (
            previous.month()
        )

        self._update_calendar()

    # =============================================================
    # NEXT MONTH
    # =============================================================

    def _next_month(self):

        current = QDate(
            self.display_year,
            self.display_month,
            1
        )

        next_date = current.addMonths(
            1
        )

        self.display_year = (
            next_date.year()
        )

        self.display_month = (
            next_date.month()
        )

        self._update_calendar()

    # =============================================================
    # PREVIOUS YEAR
    # =============================================================

    def _previous_year(self):

        self.display_year -= 1

        self._update_calendar()

    # =============================================================
    # NEXT YEAR
    # =============================================================

    def _next_year(self):

        self.display_year += 1

        self._update_calendar()

    # =============================================================
    # UPDATE SELECTED DATE
    # =============================================================

    def _update_selected_date(self):

        self.selected_label.setText(
            "Selected: {}".format(
                self.selected_date.toString(
                    "dd/MM/yyyy"
                )
            )
        )

    # =============================================================
    # KEEP PANEL CENTERED IF PARENT SIZE CHANGES
    # =============================================================

    def resizeEvent(
        self,
        event
    ):

        super(
            AOCDateCalendar,
            self
        ).resizeEvent(
            event
        )

        if hasattr(
            self,
            "panel"
        ):

            self.panel.move(
                (self.width() - self.panel.width()) // 2,
                (self.height() - self.panel.height()) // 2
            )

    # =============================================================
    # ACCEPT
    # =============================================================

    def accept(self):

        try:

            if not self.selected_date.isValid():

                self.selected_date = (
                    QDate.currentDate()
                )

            self.target_label.setText(
                self.selected_date.toString(
                    "dd/MM/yyyy"
                )
            )

            super(
                AOCDateCalendar,
                self
            ).accept()

        except Exception as e:

            print(
                "Calendar accept error:",
                e
            )

            super(
                AOCDateCalendar,
                self
            ).reject()