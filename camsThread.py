import threading
import onecam
import camsgui
import photosphereSS

camsStream = threading.Thread(target=onecam.main, args = (),)
#camsgui = threading.Thread(target=camsgui.main, args= (),)
#screenshot = threading.Thread(target=photosphereSS.main, args = (),)

#screenshot.start()
camsStream.start()
#camsgui.start()

#screenshot.join()
camsStream.join()
#camsgui.join()