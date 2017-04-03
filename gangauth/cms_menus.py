from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from cms.menu_bases import CMSAttachMenu
from gangauth.forms import UserLoginForm
from gangdev.utils import User


class UserMenu(Menu):
    def get_nodes(self, request):
            return [
                NavigationNode(_("Profil"), "/log/", 1, attr={'visible_for_anonymous': False, 'right': True}),
                NavigationNode(_("Edit"), reverse("user_edit"), 2, 1, attr={'visible_for_anonymous': False, 'right': True}),
                NavigationNode(_("Change Password"), reverse("user_password"), 3, 1, attr={'visible_for_anonymous': False, 'right': True}),
                NavigationNode(_("Log out"), reverse("logout"), 4, 1, attr={'visible_for_anonymous': False, 'right': True}),

                NavigationNode(_("Log in"), '/', 5, attr={'visible_for_authenticated': False, 'right': True, 'login': True, 'login_form': UserLoginForm}),

                NavigationNode(_("Sign up"), reverse("subscribe"), 6, attr={'signup': True, 'right': True, 'visible_for_anonymous': True, 'visible_for_authenticated': False}),
            ]

menu_pool.register_menu(UserMenu)
