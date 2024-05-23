FROM python:3

RUN mkdir /opt/python
COPY helloworld.py /opt/python/
RUN chmod +x /opt/python/helloworld.py


ARG DD_SERVICE=PythonApp
ARG DD_ENV=dev
ARG DD_VERSION=0.1

ENV DD_APM_ENABLED=true
ENV DATADOG_TRACE_ENABLED=true
ENV DD_LOGS_INJECTION=true
ENV DD_TRACE_ANALYTICS_ENABLED=true

RUN pip install flask
RUN pip install flask_restful
RUN pip install ddtrace 
RUN pip install requests

WORKDIR /opt/python

EXPOSE 80

ENTRYPOINT [ "/bin/bash", "-c", "ddtrace-run python helloworld.py" ]