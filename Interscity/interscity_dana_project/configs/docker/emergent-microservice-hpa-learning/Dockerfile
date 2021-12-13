FROM ubuntu:18.10

COPY ./dana ./home/roberto/dana 
COPY ./interscity_dana_project ./home/roberto/interscity_dana_project
ENV DANA_HOME=/home/roberto/dana/
ENV PATH="${PATH}:/home/roberto/dana/"
WORKDIR /home/roberto/interscity_dana_project/pal/

ENTRYPOINT ["/bin/bash", "./../scripts/bash/hpa-learning.sh"]
