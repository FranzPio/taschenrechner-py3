import wx
import platform

ubuntu_size = (230, 330)
windows_size = (235, 390)
other_os_size = (245, 400)

if platform.system() == "Linux":
    global window_size
    try:
        if platform.linux_distribution()[0] == "Ubuntu":
            window_size = ubuntu_size
        elif platform.linux_distribution()[0] == "debian":
            window_size = windows_size
    except AttributeError:
        window_size = other_os_size
elif platform.system() == "Windows":
    window_size = windows_size
else:
    window_size = other_os_size


class Application(wx.Frame):

    def __init__(self, *args, **kwargs):  # parent, title, style=wx.DEFAULT_FRAME_STYLE):
        super().__init__(*args, **kwargs)  # parent, title=title, size=(225, 500), style=style)
        # self.SetPosition((400, 150))
        self.muldiv_already_pressed = False
        self.to_display = ""
        self.result = 0
        self.numbers = ""
        self.Centre()
        self.menubar()
        self.UI()
        self.Show()

    def menubar(self):
        menubar = wx.MenuBar()

        actions_menu = wx.Menu()
        menubar.Append(actions_menu, "&Aktionen")

        view_menu = wx.Menu()
        menubar.Append(view_menu, "&Ansicht")

        self.showstatusbarbutton = wx.MenuItem(view_menu, wx.ID_ANY, "&Statusleiste anzeigen\tCtrl+A",
                                               "Die Statusleiste wird angezeigt/versteckt.", wx.ITEM_CHECK)
        view_menu.Append(self.showstatusbarbutton)
        view_menu.Check(self.showstatusbarbutton.GetId(), False)
        self.showstatusbarbutton.Enable(False)

        actions_menu.AppendSeparator()

        minimizebutton = wx.MenuItem(actions_menu, wx.ID_ICONIZE_FRAME, "&Minimieren\tCtrl+M",
                                     "Das Fenster wird minimiert.")
        # minimizebutton.SetBitmap(wx.Bitmap(r"resources\wxPythontest\minimizeimage.png"))
        actions_menu.Append(minimizebutton)

        quitbutton = wx.MenuItem(actions_menu, wx.ID_EXIT, "&Schließen\tCtrl+S", "Das Fenster wird geschlossen.")
        # quitbutton.SetBitmap(wx.Bitmap(r"\resources\wxPythontest\quitimage.png"))
        actions_menu.Append(quitbutton)

        self.Bind(wx.EVT_MENU, self.CloseApp, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.MinimizeApp, id=wx.ID_ICONIZE_FRAME)

        self.SetMenuBar(menubar)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.Hide()
        # self.statusbar.SetStatusText("")

    # noinspection PyArgumentList
    def UI(self):
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(30)

        self.display = wx.StaticText(panel, label="0", pos=(5, 5))
        self.display.SetFont(font)

        button1 = wx.Button(panel, label="1", pos=(5, 75), size=(50, 50))
        button2 = wx.Button(panel, label="2", pos=(55, 75), size=(50, 50))
        button3 = wx.Button(panel, label="3", pos=(105, 75), size=(50, 50))
        button4 = wx.Button(panel, label="4", pos=(5, 125), size=(50, 50))
        button5 = wx.Button(panel, label="5", pos=(55, 125), size=(50, 50))
        button6 = wx.Button(panel, label="6", pos=(105, 125), size=(50, 50))
        button7 = wx.Button(panel, label="7", pos=(5, 175), size=(50, 50))
        button8 = wx.Button(panel, label="8", pos=(55, 175), size=(50, 50))
        button9 = wx.Button(panel, label="9", pos=(105, 175), size=(50, 50))
        button0 = wx.Button(panel, label="0", pos=(55, 225), size=(50, 50))
        buttonadd = wx.Button(panel, label="+", pos=(175, 75), size=(50, 50))
        buttonsubtract = wx.Button(panel, label="-", pos=(175, 125), size=(50, 50))
        buttonmultiply = wx.Button(panel, label="*", pos=(175, 175), size=(50, 50))
        buttondivide = wx.Button(panel, label="/", pos=(175, 225), size=(50, 50))
        buttonequals = wx.Button(panel, label="=", pos=(175, 275), size=(50, 50))

        buttonlist = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0,
                      buttonadd, buttonsubtract, buttonmultiply, buttondivide, buttonequals]

        evt_handlers = [self.set1, self.set2, self.set3, self.set4, self.set5, self.set6, self.set7, self.set8,
                        self.set9, self.set0, self.setadd, self.setsubtract, self.setmultiply, self.setdivide,
                        self.setequals]

        for index, button in enumerate(buttonlist):
            button.Bind(wx.EVT_BUTTON, evt_handlers[index])

    def CloseApp(self, evt):
        self.Close()

    def MinimizeApp(self, evt):
        self.Iconize()

    def set1(self, evt):
        self.muldiv_already_pressed = False
        self.number = 1
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set2(self, evt):
        self.muldiv_already_pressed = False
        self.number = 2
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set3(self, evt):
        self.muldiv_already_pressed = False
        self.number = 3
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set4(self, evt):
        self.muldiv_already_pressed = False
        self.number = 4
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set5(self, evt):
        self.muldiv_already_pressed = False
        self.number = 5
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set6(self, evt):
        self.muldiv_already_pressed = False
        self.number = 6
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set7(self, evt):
        self.muldiv_already_pressed = False
        self.number = 7
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set8(self, evt):
        self.muldiv_already_pressed = False
        self.number = 8
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set9(self, evt):
        self.muldiv_already_pressed = False
        self.number = 9
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def set0(self, evt):
        self.number = 0
        self.to_display += str(self.number)
        self.display.SetLabel(self.to_display)

    def setadd(self, evt):
        self.display.SetLabel("+")
        try:
            self.numbers += self.to_display + "+"
        except ValueError:
            pass
        self.to_display = ""

    def setsubtract(self, evt):
        self.display.SetLabel("-")
        try:
            self.numbers += self.to_display + "-"
        except ValueError:
            pass
        self.to_display = ""

    def setmultiply(self, evt):
        if self.muldiv_already_pressed:
            pass
        else:
            self.muldiv_already_pressed = True
            self.display.SetLabel("*")
            try:
                self.numbers += self.to_display + "*"
            except ValueError:
                pass
            self.to_display = ""

    def setdivide(self, evt):
        if self.muldiv_already_pressed:
            pass
        else:
            self.muldiv_already_pressed = True
            self.display.SetLabel("/")
            try:
                self.numbers += self.to_display + "/"
            except ValueError:
                pass
            self.to_display = ""

    def setequals(self, evt):
        try:
            self.numbers += self.to_display
        except ValueError:
            pass
        try:
            self.result = eval(self.numbers)
        except SyntaxError:
            pass
        self.display.SetLabel("= " + str(self.result))
        self.result = 0
        self.to_display = ""
        self.numbers = ""


app = wx.App()
Application(None, title="Rechner", size=window_size,
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX)
app.MainLoop()
