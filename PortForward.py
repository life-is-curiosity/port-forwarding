#!/usr/bin/python

import time,socket,threading

# Print Log
def log(strLog):
    strs=time.strftime("%Y-%m-%d %H:%M:%S")
    print (strs+"->"+strLog)
 
# TCP Protocol   
class pipethread(threading.Thread):
    
    def __init__(self,source,sink):
        threading.Thread.__init__(self)
        self.source=source
        self.sink=sink
        log("New Pipe create:%s->%s" % (self.source.getpeername(),self.sink.getpeername()))

    def run(self):
        while True:
            try:
                data=self.source.recv(1024)
                if not data: break
                self.sink.send(data)
            except Exception  as ex:
                log("redirect error:"+str(ex))
                break
        self.source.close()
        self.sink.close()

class portmap(threading.Thread):

    def __init__(self,port,newhost,newport,local_ip=''):
        threading.Thread.__init__(self)
        self.newhost=newhost
        self.newport=newport
        self.port=port
        self.local_ip=local_ip
        self.sock=None
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.local_ip,port))
        self.sock.listen(5)
        log("start listen protocol:%s,port:%d " % ('tcp',port))

    def run(self):
        while True:
            fwd=None
            newsock=None
            newsock,address=self.sock.accept()
            log("new connection->protocol:%s,local port:%d,remote address:%s" % ('tcp',self.port,address[0]))
            fwd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                fwd.connect((self.newhost,self.newport))
            except Exception  as ex:
                log("connet newhost error:"+str(ex))
                break

            # Setting on Two Piers : source -> sink 
            
            p1=pipethread(newsock,fwd)
            p1.start()
            p2=pipethread(fwd,newsock)
            p2.start()
            
            
if __name__=='__main__':

    # to=portmap(10061,'10.13.135.31',21)      
    # to.start()