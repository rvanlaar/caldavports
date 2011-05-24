# Ports collection makefile for:    py-pycalendar
# Date created:         April 23, 2011
# Whom:                 Roland van Laar <roland@micite.net>
#
# $FreeBSD$
#

PORTNAME=			pycalendar
PORTVERSION=		2.0
CATEGORIES=			devel python
MASTER_SITES=
PKGNAMEPREFIX=		${PYTHON_PKGNAMEPREFIX}

MAINTAINER=			roland@micite.net
COMMENT=			An icalendar and vcard support for python

USE_PYTHON=			yes
USE_PYDISTUTILS=	easy_install

post-patch:
	@${REINPLACE_CMD} -e 's|distutils.core|setuptools|g' ${WRKSRC}/setup.py


.include <bsd.port.mk>
