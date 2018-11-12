import wx

# class Frame1(wx.Frame):
#     def __init__(self,superior):
#         wx.Frame.__init__(self, parent=superior,
#                            title="Example", pos=(100, 200), size=(350, 200))
#         self.panel = wx.Panel(self)
#         #text1 = wx.TextCtrl(panel, value="Hello, World!", size=(350, 200))
#         self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick)
    
#     def OnClick(self, event):
#         posm = event.GetPosition()
#         wx.StaticText(parent=self.panel, label="Hello, World!",
#                       pos=(posm.x, posm.y))



# if __name__=="__main__":
#     app=wx.App()
#     frame=Frame1(None)
#     frame.Show(True)
#     app.MainLoop()


# import wx


# class Frame1(wx.Frame):
#     def __init__(self, superior):
#         wx.Frame.__init__(self, parent=superior, title="Hello World in wxPython")
#         panel = wx.Panel(self)

#         sizer = wx.BoxSizer(wx.VERTICAL)

#         self.text1 = wx.TextCtrl(panel, value="Hello, World!",
#                          size=(200, 180), style=wx.TE_MULTILINE)

#         sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)

#         button = wx.Button(panel, label="Click Me")

#         sizer.Add(button)
#         panel.SetSizerAndFit(sizer)
#         panel.Layout()
#         self.Bind(wx.EVT_BUTTON, self.OnClick, button)


# def OnClick(self, text):
#     self.text1.AppendText("\nHello, World!")


import wx


class Frame1(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel, value="Hello, World!",
                                 size=(200, 180), style=wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label="Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)
        self.Show(True)

    def OnClick(self, text):
        self.text1.AppendText("\nHello, World!")


if __name__ == '__main__':
        app = wx.App()
        frame = Frame1(None, "Hello World in wxPython")
        app.MainLoop()
