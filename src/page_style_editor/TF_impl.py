from ofjustpy_engine.tracker import trackStub
class StubTag:
    pass


class Stub_HCStatic(StubTag):
    def __init__(self, *args, **kwargs):
        self.target = kwargs.get("target")

    def register_childrens(self):
        # HC are not div elements and do not
        # contain childrens

        pass

    @classmethod
    def is_static(cls):
        # We treat everything as mutable
        return False

    def __call__(self, a, attach_to_parent=True):
        """
        if the both parent and child are static
        then child is already attached at setup/initialized time

        """

        if attach_to_parent:
            # if parent is static then childs are declared
            # during setup/initialization
            a.add_component(self.target)
        self.register_childrens()

        if not self.target.obj_json:
            self.target.build_json()

        return self.target

    
    @property
    def twsty_tags(self):
        return self.target.twsty_tags
    
    @property
    def id(self):
        return "/" + self.key


    
    @property
    def key(self):
        return self.target.key

    @property
    def svelte_safelist(self):
        """
        svelte_safelist is for all the twtags introduced
        during event handler. 
        passive components do not have event handlers
        """
        return []
    
    pass


class Stub_HCPassive(Stub_HCStatic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    @classmethod
    def is_static(cls):
        return True

    def register_childrens(self):
        # HC are not div elements and do not
        # contain childrens

        pass

@trackStub    
def gen_Stub_HCPassive(target, **kwargs):
    print ("====================>     from patched gen_Stub_HCPassive")
    return Stub_HCPassive(target=target)
