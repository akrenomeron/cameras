import threading
#import camsgui
import testProgram
import photosphereSS
#import onecam

camsStream = threading.Thread(target=testProgram.main,)
#camsgui = threading.Thread(target=camsgui.main, args= (),)
screenshot = threading.Thread(target=photosphereSS.main,)

screenshot.start()
camsStream.start()
#camsgui.start()

screenshot.join()
camsStream.join()
#camsgui.join()