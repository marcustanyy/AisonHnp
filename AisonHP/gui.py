
import streamlit as st
import datetime as dt
import socket, json
from streamlit_autorefresh import st_autorefresh

PROCESS_IDLE = "IDLE"
PROCESS_START = "OPERATING"
PROCESS_END = "END"
PROCESS_STOP = "STOP"
har1_Status = {"temp" : "30 °C", "status" : PROCESS_IDLE}

def Display_GUI():
    
    st_autorefresh(interval = 3000, key = "refresh")
    har1_Status = Send_Packet("update")
    st.header("Aison Harvester Packager Controls")

    harv1 = st.container()
    harv2 = st.container()
    harv3 = st.container()

    with harv1:
        st.subheader("Harvester 1")
        if st.button("Start 1"):
            har1_Status = Send_Packet(PROCESS_START)

        if st.button("Stop 1"):
            har1_Status = Send_Packet(PROCESS_END)

        with st.expander("Harvester 1 Status"):
            now = dt.datetime.now()
            st.write("Current Date & Time :")
            st.write(now.strftime("%Y-%m-%d   %H:%M:%S"))
            temp1, status1 = st.columns(2)
            temp1.metric("Temperature", "30 °C")
            status1.metric("Status", har1_Status["status"])
        

    with harv2:
        st.subheader("Harvester 2")
        if st.button("Start 2"):
            currProcess = PROCESS_START

        if st.button("Stop 2"):
            currProcess = PROCESS_STOP
        
        with st.expander("Harvester 2 Status"):
            st.write("Invalid")
    
    with harv3:
        st.subheader("Harvester 3")   
        if st.button("Start 3"):
            currProcess = PROCESS_START

        if st.button("Stop 3"):
            currProcess = PROCESS_STOP
        
        with st.expander("Harvester 3 Status"):
            st.write("Invalid")

def Send_Packet(packet):
    TCP_IP = socket.gethostname()
    TCP_PORT = 8000
    BUFFER_SIZE = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, TCP_PORT))
    server.send(packet.encode())
    data = server.recv(BUFFER_SIZE)
    object = json.loads(data.decode())
    print(har1_Status["temp"] + " " + object["status"])
    server.close()
    return object