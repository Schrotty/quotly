import os
import sqlite3

from quotly.Quote import Quote


class Quotly:
    def __init__(self):
        if not os.path.exists('data'):
            os.mkdir('data')

        self.conn = sqlite3.connect('data/quotes.db')

    def store_quote(self, quote, *targets):
        cur = self.conn.cursor()

        t = []
        if len(targets[0]) > 0:
            for targ in targets[0]:
                t.append(targ)

        t.extend([''] * (5 - len(t)))
        cur.execute(
            "insert into quotes (quote, target_one, target_two, target_three, target_four, target_five) "
            "values (?, ?, ?, ?, ?, ?)", (quote, t[0], t[1], t[2], t[3], t[4]))

        self.conn.commit()

    def fetch_quote(self):
        cur = self.conn.cursor()

        cur.execute("select quote, target_one, target_two, target_three, target_four, target_five "
                    "from quotes order by random() limit 1")

        return Quote(cur.fetchone())

    def fetch_quote(self, *targets):
        cur = self.conn.cursor()

        t = list(targets)
        t.extend([''] * (5 - len(targets)))
        cur.execute("select quote, target_one, target_two, target_three, target_four, target_five "
                    "from quotes "
                    "where target_one == (?) "
                    "order by random() limit 1", (t[0]))

        return Quote(cur.fetchone())

    def __del__(self):
        self.conn.close()
