FROM TeamDynamic/Speedo-USERBOT:latest

#clonning repo 
RUN git clone https://github.com/TeamDynamic/Dynamic-Userbot.git /root/Speedo
#working directory 
WORKDIR /root/Speedo

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Speedo/bin:$PATH"

CMD ["python3","-m","Speedo"]
