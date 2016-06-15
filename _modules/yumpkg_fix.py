
__virtualname__ = 'yumpkg_fix'

def __virtual__():
    try:
        # yumpkg module in salt 2015.5 is broken on Fedora 23 - tries to
        # check/install python-dnf-plugins-core, while python3-dnf-plugins-core is
        # used. As the package is always installed in Qubes, fake the check
        # until we got newer salt
        __context__['yumpkg.has_repoquery'] = True
    except NameError:
        pass
    # nothing to do
    return False
