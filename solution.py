from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = '\r\n My message'
    endmsg = '\r\n.\r\n'

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket=socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    recv=clientSocket.recv(1024).decode()
    #print('STMP TEST:')
    #print(received)
   # print(recv)
   # if recv[:3] != '220':
       # print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')
    # Send MAIL FROM command and print server response.
    mailcommand='MAIL FROM: <pythonmail@johncodes.com>\r\n.'
    clientSocket.send(mailcommand.encode())
    recv2=clientSocket.recv(1024).decode()
   # print(recv2)
    #if recv2[:3] != '250':
       # print('250 reply not received from server.')
# Send RCPT TO command and print server response.
    # Fill in start
    rcptto='RCPT TO: <autograder@gradescope.com>\r\n'
    clientSocket.send(rcptto.encode())
    recv3=clientSocket.recv(1024).decode()
   # print(recv1)
   # if recv3[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end
 # Send DATA command and print server response.
    # Fill in start
    datacommand='DATA\r\n'
    #print('datacommand')
    clientSocket.send(datacommand.encode())
    recv4=clientSocket.recv(1024).decode()
   # if recv4[:3] != '250':
        #print('data 250 reply not received from server.')
    # Fill in end
    
 # Send message data.
    # Fill in start
    clientSocket.send((msg+endmsg).encode())
    recv5=clientSocket.recv(1024).decode()
   # print(recv5)
    #if recv5[:3] != '250':
        #print('data 250 reply not received from server.')
     # Fill in end
# Send QUIT command and get server response.
    # Fill in start
    quitcommand='QUIT\r\n'
    #print(quitcommand)
    clientSocket.send(quitcommand.encode())
    recv6=clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv6[:3] != '250':
       # print('data 250 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
