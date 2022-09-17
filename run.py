from WITHOUT_ENTERING.home import Home

with Home(teardown=False) as obj:
    obj.landing()
    # obj.preq()
    obj.searching()
    obj.collecting()
    # obj.adding()
    # obj.carting()
    # obj.proceeding()