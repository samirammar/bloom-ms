from django import template
from core.models import TeamMember

register = template.Library()


@register.simple_tag
def get_team_members():
    """Returns active team members ordered by order field"""
    return TeamMember.objects.filter(is_active=True)