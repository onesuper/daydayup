

class DayDayUpException(Exception):
    code=1
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return unicode(self).encode('utf8')

    def __unicode__(self):
        return 'DayDayUpError: {0}'.format(self.message).decode('utf8')

