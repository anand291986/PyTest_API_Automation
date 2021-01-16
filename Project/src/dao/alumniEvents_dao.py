class AlumniEventsDao(object):

    def get_eventid(session, eventid):
        """
        :arg
        session : DB Session
        eventid : integer
        :return: dict
        Dictionary of database result
        """

        sql = f'''SELECT * FROM ER_COMMON.Event
                  WHERE event_id = {eventid}'''
        row = session.execute(sql).first()
        if row is not None:
            output = dict(zip(row.keys(), row))
            return output
        else:
            raise Exception("Matching EventID not found in database")
