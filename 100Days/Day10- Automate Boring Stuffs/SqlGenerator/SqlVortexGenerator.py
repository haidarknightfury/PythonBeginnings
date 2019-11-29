from datetime import timedelta
import datetime
import json


class SqlGenerator(object):
    def __init__(self, id, start_date, map_values, default_amount = 10):
        self._id = id
        self._start_date = start_date
        self._map_val = map_values
        self._default_amnt = default_amount

    @property
    def id(self):
        """id of the contract"""
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @staticmethod
    def generate_sql(id, dt, amount):
        """generate the sql for the insertion in the tables"""
        generated_sql_st = 'INSERT INTO S#ING_VORTEX_CCRD_IMPAYE VALUES({}, \'{}\', {});'.format(id, dt, amount)
        return generated_sql_st

    @property
    def map_vals(self):
        return self._map_val

    @map_vals.setter
    def map_vals(self, map_val):
        self._map_val = map_val

    def generate(self):
        generated_sqls = []
        cur_date = self._start_date
        default_amount = self._default_amnt

        for day in range(1, 30):
            if day in self._map_val:
                default_amount = self._map_val[day]
            sql = self.generate_sql(self._id, cur_date.strftime('%d/%m/%Y'), default_amount)
            generated_sqls.append(sql)
            cur_date = cur_date + timedelta(days=1)
        return  generated_sqls


if __name__ == '__main__':

    with open('generator.conf.json', 'r') as conf_file:
        conf = json.load(conf_file)
        result = map(lambda dayish: {dayish['day'] : dayish['amount']}, conf['params'])
        conf_result = {}
        for map_item in list(result):
            for key in map_item.keys():
                conf_result[key] = map_item[key]
        print(conf_result)

        sql_gen = SqlGenerator(conf['id'], datetime.date.fromisoformat(conf['startDate']),  conf_result)
        output_file = open('generated.sql','w+')
        for sql in sql_gen.generate():
            output_file.write(sql +'\n')
