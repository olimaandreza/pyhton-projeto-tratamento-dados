FROM python:3.8

WORKDIR /app

RUN pip install numpy pandas jupyter notebook folium polyline routingpy

RUN git clone https://github.com/jvkersch/pyconcorde
RUN pip install -e ./pyconcorde

COPY ./bigtable.csv /app/data.csv
COPY ./desafioFINAL.ipynb /app/desafioFINAL.ipynb

EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]