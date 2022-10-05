FROM konstellation/kre-py:2.1.5

ENV PYTHONPATH=/kre/.local/lib/python3.9/site-packages/

WORKDIR /tmp

USER kre

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv --clear install --system --deploy && \
    pip uninstall protobuf -y && \
    pip install protobuf==3.20.1 --no-cache-dir

WORKDIR /kre
