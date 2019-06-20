def string_sum(a, b):
   return a + " and the second one is " + b

class FilterModule(object):
    def filters(self):
        return {'string_sum': string_sum}
