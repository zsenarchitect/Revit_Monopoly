"""Prints calculated hash values for each extension."""
#pylint: disable=import-error,invalid-name,broad-except,superfluous-parens


__title__ = 'Open\nPanel'
__context__ = 'zero-doc'


from pyrevit import forms, UI


test_panel_uuid = "6b59123c-e13a-43d4-a98d-11c19cd00577"

#print UI.GetDockablePane(test_panel_uuid)


forms.open_dockable_panel("6b59123c-e13a-43d4-a98d-11c19cd00577")
