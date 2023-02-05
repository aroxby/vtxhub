FROM python:3

RUN pip install --root-user-action=ignore --upgrade pip

RUN useradd -m app
USER app
WORKDIR /home/app
ENV PATH=/home/app/.local/bin:${PATH}

COPY . .
RUN pip install --user -r requirements.txt


CMD python -m vtxhub
