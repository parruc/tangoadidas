from django import template

from allauth.socialaccount import providers


register = template.Library()


@register.simple_tag
def get_missing_social_providers(request):
    """
    Returns a list of social authentication providers the user is
    not connected to.

    Usage: `{% get_missing_social_providers as missing_providers %}`.

    Then within the template context, `missing_providers` will hold
    a list of social providers NOT configured for the current user.
    """
    user = request.user
    missing_providers = providers.registry.get_list()
    for account in user.socialaccount_set.all().iterator():
        for missing_provider in missing_providers:
            if missing_provider.id == account.provider:
                missing_providers.remove(missing_provider)
    for missing_provider in missing_providers:
        login_url = missing_provider.get_login_url(request, process="connect")
        yield {"name": missing_provider.name,
               "url": login_url}
