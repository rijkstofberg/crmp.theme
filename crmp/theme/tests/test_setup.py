from crmp.theme.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_is_crmp_theme_installed(self):
        self.failUnless(self.installer.isProductInstalled('crmp.theme'))

    def test_is_plone_app_theming_installed(self):
        self.failUnless(self.installer.isProductInstalled('plone.app.theming'))

    def test_uninstall(self):
        self.installer.uninstallProducts(['crmp.theme'])
        self.failIf(self.installer.isProductInstalled('crmp.theme'))

    def test_browserlayer(self):
        from crmp.theme.browser.interfaces import ICrmpThemeLayer
        from plone.browserlayer import utils
        self.failUnless(ICrmpThemeLayer in utils.registered_layers())

    def test_css_registry_configured(self):
        css_resources = set(
            getToolByName(self.portal, 'portal_css').getResourceIds())

        self.failUnless(
            '++theme++crmp.theme/css/style.css' in css_resources)

    def test_js_registry_configured(self):
        js_resources = set(
            getToolByName(self.portal, 'portal_javascripts').getResourceIds())

        self.failUnless(
            '++theme++crmp.theme/javascript/libs/modernizr.custom.js'
            in js_resources)

    def test_doctype_configured(self):
        from plone.app.theming.interfaces import IThemeSettings
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility

        settings = getUtility(IRegistry).forInterface(IThemeSettings)
        self.assertEqual(settings.doctype, '<!doctype html>')
