import win32api, win32con, time, ctypes

# Dictionary to translate characters in to HEX

thisdict = { 'Left mouse button':0x01,'Right mouse button':0x02,
        'Control-break processing':0x03,'Middle mouse button (three-button mouse)':0x04,
'X1 mouse button':0x05,'X2 mouse button':0x06,'BACKSPACE key':0x08,
'TAB':0x09,'CLEAR':0x0C,'ENTER':0x0D,'SHIFT':0x10,
'CTRL':0x11,'ALT':0x12,'PAUSE':0x13,'CAPS LOCK':0x14,
'ESC':0x1B,'SPACEBAR':0x20,'PAGE UP':0x21,'PAGE DOWN':0x22,
'END':0x23,'HOME':0x24,'LEFT ARROW':0x25,'UP ARROW':0x26,
'RIGHT ARROW':0x27,'DOWN ARROW':0x28,'SELECT':0x29,
'PRINT':0x2A,'EXECUTE':0x2B,'PRINT SCREEN':0x2C,'INS':0x2D,
'DEL':0x2E,'HELP':0x2F,'0':0x30,'1':0x31,'2':0x32,
'3':0x33,'4':0x34,'5':0x35,'6':0x36,'7':0x37,'8':0x38,
'9':0x39,'A':0x41,'B':0x42,'C':0x43,'D':0x44,'E':0x45,
'F':0x46,'G':0x47,'H':0x48,'I':0x49,'J':0x4A,'K':0x4B,
'L':0x4C,'M':0x4D,'N':0x4E,'O':0x4F,'P':0x50,'Q':0x51,
'R':0x52,'S':0x53,'T':0x54,'U':0x55,'V':0x56,'W':0x57,
'X':0x58,'Y':0x59,'Z':0x5A,'Numeric keypad 0 key':0x60,
'Numeric keypad 1 key':0x61,'Numeric keypad 2 key':0x62,
'Numeric keypad 3 key':0x63,'Numeric keypad 4 key':0x64,
'Numeric keypad 5 key':0x65,'Numeric keypad 6 key':0x66,
'Numeric keypad 7 key':0x67,'Numeric keypad 8 key':0x68,
'Numeric keypad 9 key':0x69,'Multiply key':0x6A,'Add key':0x6B,
'Separator key':0x6C,'Subtract key':0x6D,'Decimal key':0x6E,'Divide key':0x6F,
'F1 key':0x70,'F2 key':0x71,'F3 key':0x72,'F4 key':0x73,'F5 key':0x74,
'F6 key':0x75,'F7 key':0x76,'F8 key':0x77,'F9 key':0x78,'F10 key':0x79,
'F11 key':0x7A,'F12 key':0x7B,'F13 key':0x7C,'F14 key':0x7D,'F15 key':0x7E,
'F16 key':0x7F,'F17 key':0x80,'F18 key':0x81,'F19 key':0x82,'F20 key':0x83,
'F21 key':0x84,'F22 key':0x85,'F23 key':0x86,'F24 key':0x87,
'NUM LOCK key':0x90,'SCROLL LOCK key':0x91 }

#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)
    

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Keypress Functions

def PressKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def AltTab():

''' ######################################################################
	Task to be done is in the next few lines
''' ######################################################################

    click(1885, 32) # Click on these coordinates
    a_string = "COMMAND"	# the string you wan tto type
	
    for letter in a_string:
        print letter, thisdict[letter]
        x = thisdict[letter]
        print type(x), x
        PressKey(x)
        ReleaseKey(x)
    
    PressKey(0x00D) # Carriage Return
    ReleaseKey(0x00D)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
if __name__ =="__main__":

    AltTab()
