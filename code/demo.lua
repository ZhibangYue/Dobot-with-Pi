err, socket = TCPCreate(false, "192.168.5.2", 8081)
TCPStart(socket, 20)
while true do
 err, recBuf = TCPRead(socket, 30)
 end
TCPDestroy(socket)