ARG  CODE_VERSION=1.7.1
FROM apache/nifi:${CODE_VERSION}

ARG CODE_VERSION=1.7.1
ARG NIFI_HOME=/opt/nifi/nifi-${CODE_VERSION}
ARG NIFI_LIB=${NIFI_HOME}/lib/
ARG NIFI_CONF=${NIFI_HOME}/conf/
ARG NIFI_CERTS=/opt/certs/
ARG NIFI_SCRIPTS=/opt/nifi/scripts/

COPY --chown=nifi:nifi nifi-file-identity-provider-nar-1.0.0.nar ${NIFI_LIB}
COPY --chown=nifi:nifi nifi.properties login-identity-providers.xml authorizers.xml login-credentials.xml users.xml authorizations.xml ${NIFI_CONF}
COPY --chown=nifi:nifi nifi-test.jks truststore.jks ${NIFI_CERTS}
COPY --chown=nifi:nifi start.sh configure.py ${NIFI_SCRIPTS}

USER root

RUN apt-get update && apt-get install -y python2.7 python-pip
RUN pip install --upgrade pip
RUN pip install nipyapi

EXPOSE 8443
