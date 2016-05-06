from __future__ import unicode_literals
from cdt import mako_views
from cdt import settings


lookup = mako_views.TemplateRender(
    settings.DEFUALT_TEMPLATE_DIRS[0].get('cdtAction'),
    ['from cdt import views'],
)
