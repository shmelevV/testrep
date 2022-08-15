# Build:
#   docker build -t elgalu/jenkins .
# Test:
#   docker run --rm -ti elgalu/jenkins chromedriver --version
#   #=> ChromeDriver 2.3.....
FROM jenkins/jenkins:lts

# install system packages
USER root
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-virtualenv

# install chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# install chromedriver
RUN wget "https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip"
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin

# install jenkins add-ons
USER jenkins
RUN /usr/local/bin/install-plugins.sh git workflow-aggregator lockable-resources docker-build-publish parameterized-scheduler robot
