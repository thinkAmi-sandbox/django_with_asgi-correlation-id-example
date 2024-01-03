"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from asgi_correlation_id import CorrelationIdMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

# add asgi-correlation-id middleware
# デフォルト設定のまま起動したい場合
# application = CorrelationIdMiddleware(application)

# オプションを追加
# バリデーションをしない (validator=None) : バリデーションをする場合、X-Request-IDがあっても不適切な値の場合は再生成する
application = CorrelationIdMiddleware(application, validator=None)
