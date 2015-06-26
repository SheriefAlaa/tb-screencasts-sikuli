# Globals and settings
myOS = Env.getOS()
Settings.TypeDelay = 0.2

class Mac():
  def openSafari():
    App.focus("Safari")

  def downloadTorBrowser():
    pass

  def installTorBrowser():
    pass

  def cleanTorBrowser():
    pass

class Windows():
  def openIE():
    App.focus("C:\Program Files (x86)\Internet Explorer\iexplore.exe")

  def IEFocusAddressBar():
    type("l", Key.CTRL)

  def downloadTorBrowser():
    pass

  def installTorBrowser():
    pass

  def cleanTorBrowser():
    pass

# Utils
def mouseClick(pos):
  '''pos can be Button.LEFT or Button.RIGHT'''
  mouseDown(pos)
  mouseUp()

def visitTorProject():
  type("https://torproject.org/" + Key.ENTER)

def openBrowser():
  if myOS == OS.WINDOWS:
    App.focus("C:\Program Files (x86)\Internet Explorer\iexplore.exe")
  elif myOS == OS.MAC:
    App.focus("Safari")
  elif myOS == OS.LINUX:
    App.focus("Firefox")


openBrowser()

if myOS == OS.MAC:
  MacObj = Mac()
  MacObj.downloadTorBrowser()

if myOS == OS.WINDOWS:
  WinObj = Windows()
  WinObj.openIE()
  WinObj.IEFocusAddressBar()
  WinObj.downloadTorBrowser()