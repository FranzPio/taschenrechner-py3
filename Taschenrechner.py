#!/usr/bin/env python3
import wx
import platform
import fractions

ubuntu_size = (230, 360)
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
        self.displaying = ""
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
        font.SetPointSize(25)

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
        buttonopenbracket = wx.Button(panel, label="(", pos=(5, 275), size=(25, 50))
        buttonclosebracket = wx.Button(panel, label=")", pos=(30, 275), size=(25, 50))
        buttonfraction = wx.Button(panel, label="x/y", pos=(55, 275), size=(50, 50))
        buttondecimalmark = wx.Button(panel, label=".", pos=(105, 275), size=(50, 50))
        buttonadd = wx.Button(panel, label="+", pos=(175, 75), size=(50, 50))
        buttonsubtract = wx.Button(panel, label="-", pos=(175, 125), size=(50, 50))
        buttonmultiply = wx.Button(panel, label="*", pos=(175, 175), size=(50, 50))
        buttondivide = wx.Button(panel, label="/", pos=(175, 225), size=(50, 50))
        buttonequals = wx.Button(panel, label="=", pos=(175, 275), size=(50, 50))

        buttonlist = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0,
                      buttonopenbracket, buttonclosebracket, buttonfraction, buttondecimalmark, buttonadd,
                      buttonsubtract, buttonmultiply, buttondivide, buttonequals]

        evt_handlers = [self.set1, self.set2, self.set3, self.set4, self.set5, self.set6, self.set7, self.set8,
                        self.set9, self.set0, self.setopenbracket, self.setclosebracket, self.setfraction,
                        self.setdecimalmark, self.setadd, self.setsubtract, self.setmultiply, self.setdivide,
                        self.setequals]

        for index, button in enumerate(buttonlist):
            button.Bind(wx.EVT_BUTTON, evt_handlers[index])

    def CloseApp(self, evt):
        self.Close()

    def MinimizeApp(self, evt):
        self.Iconize()

    def set1(self, evt):
        self.muldiv_already_pressed = False
        value = "1"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set2(self, evt):
        self.muldiv_already_pressed = False
        value = "2"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set3(self, evt):
        self.muldiv_already_pressed = False
        value = "3"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set4(self, evt):
        self.muldiv_already_pressed = False
        value = "4"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set5(self, evt):
        self.muldiv_already_pressed = False
        value = "5"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set6(self, evt):
        self.muldiv_already_pressed = False
        value = "6"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set7(self, evt):
        self.muldiv_already_pressed = False
        value = "7"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set8(self, evt):
        self.muldiv_already_pressed = False
        value = "8"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set9(self, evt):
        self.muldiv_already_pressed = False
        value = "9"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def set0(self, evt):
        self.muldiv_already_pressed = False
        value = "0"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def setopenbracket(self, evt):
        value = "("
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def setclosebracket(self, evt):
        value = ")"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def setfraction(self, evt):
        fraction = str(fractions.Fraction(self.result).limit_denominator())
        if self.result != 0:
            self.display.SetLabel(fraction)

    def setdecimalmark(self, evt):
        value = "."
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def setadd(self, evt):
        value = "+"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def setsubtract(self, evt):
        value = "-"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)

    def setmultiply(self, evt):
        if self.muldiv_already_pressed:
            pass
        else:
            self.muldiv_already_pressed = True
            value = "*"
            self.numbers += value
            self.displaying += value
            self.display.SetLabel(self.displaying)

    def setdivide(self, evt):
        if self.muldiv_already_pressed:
            pass
        else:
            self.muldiv_already_pressed = True
            value = "/"
            self.numbers += value
            self.displaying += value
            self.display.SetLabel(self.displaying)

    def setequals(self, evt):
        self.result = 0
        try:
            self.result = eval(self.numbers)
        except ZeroDivisionError:
            self.result = "Math. Fehler"
        except SyntaxError:
            self.result = "Syntaxfehler"
        self.display.SetLabel("= " + str(self.result))
        self.displaying = ""
        self.numbers = ""


app = wx.App()
Application(None, title="Rechner", size=window_size,
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX)
app.MainLoop()
