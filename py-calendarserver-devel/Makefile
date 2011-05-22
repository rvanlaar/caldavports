# Ports collection makefile for:    py-calendarserver
# Date created:         April 25, 2011
# Whom:                 Roland van Laar <roland@micite.net>
#
# $FreeBSD$
#

PORTNAME=		calendarserver
PORTVERSION=		3.0.r7257
DISTNAME=		calendarserver-trunk\(r7257\)
CATEGORIES=		net python
MASTER_SITES=
PKGNAMEPREFIX=		${PYTHON_PKGNAMEPREFIX}

MAINTAINER=		roland@micite.net
COMMENT=		Calendar and Contacts Server from Apple.

USE_PYTHON=		2.7+
USE_PYDISTUTILS=	easy_install
PYDISTUTILS_PKGNAME=	Calendar_and_Contacts_Server
PYDISTUTILS_PKGVERSION=	trunk._r7257_
PYEASYINSTALL_ARCHDEP=	yes

USE_PGSQL=		yes

RUN_DEPENDS=		bash:${PORTSDIR}/shells/bash
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
	@${REINPLACE_CMD} -e 's|version()|("trunk", "(r7257)")|g' ${WRKSRC}/setup.py
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
