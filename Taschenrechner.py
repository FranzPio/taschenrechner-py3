#!/usr/bin/env python3
import wx
import platform
import fractions
from collections import OrderedDict


class Application(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.muldiv_already_pressed = False
        self.shift_already_pressed = False
        self.buttondict = OrderedDict()
        self.displaying = ""
        self.result = 0
        self.numbers = ""

        self.menubar()
        self.UI()

        self.SetMinSize((303, 400))
        self.Centre()
        if ostype != "Linux":
            self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.SetFocus()
        self.Show()

    def menubar(self):
        menubar = wx.MenuBar()

        actions_menu = wx.Menu()
        menubar.Append(actions_menu, "&Aktionen")

        minimize = wx.MenuItem(actions_menu, wx.ID_ICONIZE_FRAME, "&Minimieren\tCtrl+M",
                               "Das Fenster wird minimiert.")
        actions_menu.Append(minimize)

        close = wx.MenuItem(actions_menu, wx.ID_EXIT, "&Schließen\tCtrl+S", "Das Fenster wird geschlossen.")
        actions_menu.Append(close)

        self.Bind(wx.EVT_MENU, self.CloseApp, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.MinimizeApp, id=wx.ID_ICONIZE_FRAME)

        self.SetMenuBar(menubar)

    # noinspection PyArgumentList
    def UI(self):
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DFACE))
        # seems to work on Windows (almost exactly like the default frame colour)
        # but on Linux? maybe this will be better:
        #
        # self.SetBackgroundColour(wx.NullColour)
        #

        if platform.system() == "Windows":
            font = wx.Font(pointSize=25, family=wx.FONTFAMILY_DEFAULT, style=wx.FONTSTYLE_NORMAL,
                           weight=wx.FONTWEIGHT_BOLD)
        else:
            font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
            font.SetPointSize(30)

        buttonfont = wx.Font(pointSize=12, family=wx.FONTFAMILY_DEFAULT, style=wx.FONTSTYLE_NORMAL,
                             weight=wx.FONTWEIGHT_NORMAL)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)

        self.display = wx.StaticText(self, label="0", pos=(5, 5))
        self.display.SetFont(font)
        hbox1.Add(self.display, 1, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox1, 1, wx.EXPAND | wx.ALL, 0)
        vbox.Add((-1, 10))

        buttonlabels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "x/y", ",", "+", "-", "*", "/", "="]
        for label in buttonlabels:
            if label != ")" and label != "(":
                self.buttondict["button" + label] = wx.Button(self, label=label, size=(50, 50))
            else:
                self.buttondict["button" + label] = wx.Button(self, label=label, size=(20, 50))

        hbox2.Add(self.buttondict["button1"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox2.Add(self.buttondict["button2"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox2.Add(self.buttondict["button3"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox2.Add(self.buttondict["button+"], 2, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        vbox.Add((-1, 3))

        hbox3.Add(self.buttondict["button4"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox3.Add(self.buttondict["button5"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox3.Add(self.buttondict["button6"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox3.Add(self.buttondict["button-"], 2, wx.EXPAND)
        vbox.Add(hbox3, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        vbox.Add((-1, 3))

        hbox4.Add(self.buttondict["button7"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox4.Add(self.buttondict["button8"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox4.Add(self.buttondict["button9"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox4.Add(self.buttondict["button*"], 2, wx.EXPAND)
        vbox.Add(hbox4, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        vbox.Add((-1, 3))

        hbox5.Add(self.buttondict["button0"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox5.AddStretchSpacer(2)
        hbox5.Add(self.buttondict["button/"], 2, wx.EXPAND)
        vbox.Add(hbox5, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        vbox.Add((-1, 3))

        hbox6.Add(self.buttondict["button("], 1, wx.EXPAND | wx.RIGHT, 2)
        hbox6.Add(self.buttondict["button)"], 1, wx.EXPAND | wx.RIGHT, 5)
        hbox6.Add(self.buttondict["buttonx/y"], 2, wx.EXPAND | wx.RIGHT, 5)
        hbox6.Add(self.buttondict["button,"], 2, wx.EXPAND | wx.RIGHT, 5)
        hbox6.Add(self.buttondict["button="], 4, wx.EXPAND)
        vbox.Add(hbox6, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        vbox.Add((-1, 5))

        self.SetSizer(vbox)

        buttonlist = self.buttondict.values()
        evt_handlers = [self.set0, self.set1, self.set2, self.set3, self.set4, self.set5, self.set6, self.set7,
                        self.set8, self.set9, self.setopenbracket, self.setclosebracket, self.setfraction,
                        self.setdecimalmark, self.setadd, self.setsubtract, self.setmultiply, self.setdivide,
                        self.setequals]

        index = 0
        for button in buttonlist:
            button.Bind(wx.EVT_BUTTON, evt_handlers[index])
            if ostype == "Linux":
                button.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
            button.SetFont(buttonfont)
            index += 1

    def CloseApp(self, evt):
        self.Close()

    def MinimizeApp(self, evt):
        self.Iconize()

    def OnKeyDown(self, evt):
        key = evt.GetKeyCode()
        numpaddict = {"324": "0", "325": "1", "326": "2", "327": "3", "328": "4", "329": "5", "330": "6", "331": "7",
                      "332": "8", "333": "9", "388": "add", "390": "subtract", "387": "multiply", "392": "divide",
                      "370": "equals", "389": "decimalmark", "391": "decimalmark"}
        operatordict = {"43": "add", "45": "subtract", "10": "equals", "13": "equals", "44": "decimalmark",
                        "46": "decimalmark"}
        shiftoperatordict = {"43": "multiply", "55": "divide", "56": "openbracket", "57": "closebracket",
                             "48": "equals"}
        if not self.shift_already_pressed:
            if str(key) == "306":
                self.shift_already_pressed = True
            else:
                try:
                    number = int(chr(key))
                    eval("self.set" + str(number) + "(wx.EVT_BUTTON)")
                except ValueError:
                    if str(key) in numpaddict.keys():
                        eval("self.set" + numpaddict[str(key)] + "(wx.EVT_BUTTON)")
                    if str(key) in operatordict.keys():
                        eval("self.set" + operatordict[str(key)] + "(wx.EVT_BUTTON)")
        else:
            if str(key) in shiftoperatordict.keys():
                eval("self.set" + shiftoperatordict[str(key)] + "(wx.EVT_BUTTON)")
            self.shift_already_pressed = False

    def set1(self, evt):
        self.muldiv_already_pressed = False
        value = "1"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set2(self, evt):
        self.muldiv_already_pressed = False
        value = "2"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set3(self, evt):
        self.muldiv_already_pressed = False
        value = "3"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set4(self, evt):
        self.muldiv_already_pressed = False
        value = "4"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set5(self, evt):
        self.muldiv_already_pressed = False
        value = "5"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set6(self, evt):
        self.muldiv_already_pressed = False
        value = "6"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set7(self, evt):
        self.muldiv_already_pressed = False
        value = "7"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set8(self, evt):
        self.muldiv_already_pressed = False
        value = "8"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set9(self, evt):
        self.muldiv_already_pressed = False
        value = "9"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def set0(self, evt):
        self.muldiv_already_pressed = False
        value = "0"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setopenbracket(self, evt):
        value = "("
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setclosebracket(self, evt):
        value = ")"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setfraction(self, evt):
        try:
            fraction = str(fractions.Fraction(self.result).limit_denominator())
            if self.result != 0:
                self.display.SetLabel(fraction)
        except ValueError:
            pass
        self.SetFocus()

    def setdecimalmark(self, evt):
        value = "."
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setadd(self, evt):
        value = "+"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setsubtract(self, evt):
        value = "-"
        self.numbers += value
        self.displaying += value
        self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setmultiply(self, evt):
        if self.muldiv_already_pressed:
            pass
        else:
            self.muldiv_already_pressed = True
            value = "*"
            self.numbers += value
            self.displaying += value
            self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setdivide(self, evt):
        if self.muldiv_already_pressed:
            pass
        else:
            self.muldiv_already_pressed = True
            value = "/"
            self.numbers += value
            self.displaying += value
            self.display.SetLabel(self.displaying)
        self.SetFocus()

    def setequals(self, evt):
        self.result = 0
        try:
            self.result = eval(self.numbers)
        except ZeroDivisionError:
            self.result = "Math. Fehler"
        except (SyntaxError, TypeError):
            if self.numbers:
                self.result = "Syntaxfehler"
        self.display.SetLabel("= " + str(self.result))
        self.displaying = ""
        self.numbers = ""
        self.SetFocus()


ostype = platform.system()

app = wx.App()
Application(None, title="Rechner", size=(325, 400),
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.RESIZE_BORDER)
app.MainLoop()
