FROM python 
ADD . /main 
WORKDIR /main
CMD [ "python","terminal.py"]