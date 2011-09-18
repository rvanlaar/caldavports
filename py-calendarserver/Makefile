# Ports collection makefile for:    py-calendarserver
# Date created:         April 25, 2011
# Whom:                 Roland van Laar <roland@micite.net>
#
# $FreeBSD$
#

PORTNAME=		calendarserver
PORTVERSION=		3.0.r7517
DISTNAME=		calendarserver-trunk\(r7517\)
CATEGORIES=		net python
MASTER_SITES=		https://github.com/rvanlaar/caldavports/raw/master/
PKGNAMEPREFIX=		${PYTHON_PKGNAMEPREFIX}

MAINTAINER=		roland@micite.net
COMMENT=		Calendar and Contacts Server from Apple.

# USE_RC_SUBR

USE_PYTHON=		2.7+
USE_PYDISTUTILS=	easy_install
PYDISTUTILS_PKGNAME=	Calendar_and_Contacts_Server
PYDISTUTILS_PKGVERSION=	trunk._r7517_
PYEASYINSTALL_ARCHDEP=	yes

USE_PGSQL=		yes
USE_TWISTED_RUN=	mail web words
WANT_PGSQL_VER=		90
USE_OPENLDAP=		yes

RUN_DEPENDS=		bash:${PORTSDIR}/shells/bash \
			memcached>=1.4.5:${PORTSDIR}/databases/memcached \
			postgresql-server>=9.0.4:${PORTSDIR}/databases/postgresql90-server \
			${PYTHON_PKGNAMEPREFIX}xattr>=0.5:${PORTSDIR}/devel/py-xattr \
			${PYTHON_PKGNAMEPREFIX}xml>=0.8.4:${PORTSDIR}/textproc/py-xml \
			${PYTHON_PKGNAMEPREFIX}openssl>=0.11:${PORTSDIR}/security/py-openssl \
			${PYTHON_PKGNAMEPREFIX}dateutil>=1.5:${PORTSDIR}/devel/py-dateutil \
			${PYTHON_PKGNAMEPREFIX}PyGreSQL>=4.0,1:${PORTSDIR}/databases/py-PyGreSQL \
			${PYTHON_PKGNAMEPREFIX}ldap2>=2.3.13:${PORTSDIR}/net/py-ldap2 \
			${PYTHON_PKGNAMEPREFIX}vobject>=0.8.1b:${PORTSDIR}/deskutils/py-vobject \
                        ${PYTHON_SITELIBDIR}/_sqlite3.so:${PORTSDIR}/databases/py-sqlite3 \
			${PYTHON_PKGNAMEPREFIX}sqlparse>=0:${PORTSDIR}/databases/py-sqlparse \
			${PYTHON_PKGNAMEPREFIX}pycalendar>=0:${PORTSDIR}/devel/py-pycalendar \
			${PYTHON_PKGNAMEPREFIX}kerberos>=0:${PORTSDIR}/security/py-kerberos

DBDIR=			/var/db/caldavd
LOGDIR=			/var/log/caldavd
SHAREDIR=		${PREFIX}/share/caldavd

DOCSDIR=	   	${PREFIX}/share/doc/${PKGNAMEPREFIX}${PORTNAME}
CONFIGDIR=		${PREFIX}/etc/caldavd
MAN8=			caladmin.8 \
			caldavd.8 \
			carddavd.8 \
			calendarserver_bootstrap_database.8 \
			calendarserver_command_gateway.8 \
			calendarserver_export.8 \
			calendarserver_manage_principals.8 \
			calendarserver_migrate_resources.8 \
			calendarserver_monitor_notifications.8 \
			calendarserver_purge_attachments.8 \
			calendarserver_purge_events.8 \
			calendarserver_purge_principals.8


post-patch:
	@${REINPLACE_CMD} -e 's|version()|("trunk", "(r7517)")|g' ${WRKSRC}/setup.py
	@${REINPLACE_CMD} -e 's|distutils.core|setuptools|g' ${WRKSRC}/setup.py
	@${REINPLACE_CMD} -e 's|bin/bash|usr/bin/env bash|' ${WRKSRC}/bin/caldavd
	@${REINPLACE_CMD} -e 's|errno.ENODATA, 93|93,|' ${WRKSRC}/twext/web2/dav/xattrprops.py
	@${REINPLACE_CMD} -e 's|is "darwin"|== "freebsd8"|' ${WRKSRC}/txdav/base/propertystore/xattr.py
	@${REINPLACE_CMD} -e 's|/usr/bin|/usr/local/bin|g' ${WRKSRC}/calendarserver/tools/bootstrapdatabase.py
	@${REINPLACE_CMD} -e 's|/usr/share/caldavd/lib/python/txdav/common/datastore|${SHAREDIR}|' ${WRKSRC}/calendarserver/tools/bootstrapdatabase.py
	@${REINPLACE_CMD} -e 's|"_postgres"|"pgsql"|' ${WRKSRC}/calendarserver/tools/bootstrapdatabase.py

post-install:
	${MKDIR} ${DBDIR}
	${MKDIR} ${CONFIGDIR}
	${MKDIR} ${LOGDIR}
	${MKDIR} ${SHAREDIR}
	${CP} -p ${WRKSRC}/conf/caldavd.plist ${CONFIGDIR}/caldavd.plist.sample
	${CP} -p ${WRKSRC}/txdav/common/datastore/sql_schema_v1.sql ${SHAREDIR}

	${INSTALL_MAN} ${WRKSRC}/doc/*.8 ${PREFIX}/man/man8

.if !defined(NOPORTDOCS)
	${MKDIR} ${DOCSDIR}
	cd ${WRKSRC}/doc && \
	for i in `ls |${GREP} -v '.8'`; do \
		${MKDIR} ${DOCSDIR}/$${i} && \
		${INSTALL_MAN} ${WRKSRC}/doc/$${i}/* ${DOCSDIR}/$${i}; done
.endif


.include <bsd.port.mk>
