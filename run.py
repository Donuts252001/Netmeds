from WITHOUT_ENTERING.home import Home

with Home(teardown=False) as obj:
    obj.landing()
    obj.fitness()
    obj.filters()
    # obj.lowtohigh()
    obj.products()
    obj.confirm()
    