# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import json
import re
import cgi
import operator

class Database(object):
    """
    The idea of this class, is to save to database and retrieve from database any GET / POST request for the API

    Types of API return / request:
    TAG - Specification for a variable.
        Saved / retrieved directly from the table 'tag'.

    FORM - List of TAG that must be filled out together
        Saved / retrieved directly from the table 'form'.

    INSPECTION - A collection of data from all applicable tag specified by the FORM to an specific timestamp / user

    VALUE - The value filled out for an specific tag of a specific INSPECTION

    """
    tag = {}
    form = {}
    inspection = {}
    value = {}

    tag['1'] = {
            'id': 1,
            'name': 'Furnace Temperature',
            'unit': 'Celsius',
            'symbol': 'C',
            'decimal_places': 2
        },
    tag['2'] = {
            'id':2,
            'name':'Furnace Pressure',
            'unit':'Atmosphere',
            'symbol':'atm',
            'decimal_places':2
        }

    form['1'] = {
        'id': 1,
        'name': 'Inspeção do Forno',
        'tag':[tag['1'],tag['2']]
    }

    inspection['1'] = {
            'id':1,
            'form':form['1'],
            'timestamp':'2016/8/1 14:33:12',
            'user':'rsilva'
        }
    inspection['2'] = {
            'id':2,
            'form':form['1'],
            'timestamp':'2/8/2016 13:50:00',
            'user':'admin'
        }

    value['1'] = {
            'id': 1,
            'inspection': inspection['1'],
            'tag': tag['1'],
            'value':1111.3434
        }

    value['2'] = {
            'id': 2,
            'inspection': inspection['1'],
            'tag': tag['2'],
            'value':2222.3434
        }

    value['3'] = {
            'id': 3,
            'inspection': inspection['2'],
            'tag': tag['1'],
            'value':3333.64784
        }

    value['4'] = {
            'id': 4,
            'inspection': inspection['2'],
            'tag': tag['2'],
            'value':4444.22224
        }

    def save(self,record_id, record_type, data):
        """
        On the future, this method will save the data directly on the related table.
        :param record_id:
        :param record_type:
        :param data:
        :return:
        """
        if record_type=="tag":
            self.tag[record_id] = data
        if record_type=="form":
            self.form[record_id] = data
        if record_type=="inspection":
            self.inspection[record_id] = data
        if record_type=="value":
            self.value[record_id] = data

    def get(self,record_id, record_type):
        """
        On the future, this method will get value from related tables.
        :param record_id:
        :param record_type:
        :return:
        """
        if record_type=="tag":
            return self.tag[record_id]
        if record_type=="form":
            return self.form[record_id]
        if record_type=="inspection":
            return self.inspection[record_id]
        if record_type=="value":
            return self.value[record_id]

    def has_key(self,record_id, record_type):
        """
        On the future, this method will get value from related tables.
        :param record_id:
        :param record_type:
        :return:
        """
        if record_type=="tag":
            return self.tag.has_key(record_id)
        if record_type=="form":
            return self.form.has_key(record_id)
        if record_type=="inspection":
            return self.inspection.has_key(record_id)
        if record_type=="value":
            return self.value.has_key(record_id)


    def get_last(self, record_type):
        """
        On the future, this method will get value from related tables.
        :param record_type:
        :return:
        """

        if record_type=="tag":
            return max(self.tag.iteritems(), key=operator.itemgetter(1))[0]
        if record_type=="form":
            return max(self.form.iteritems(), key=operator.itemgetter(1))[0]
        if record_type=="inspection":
            return max(self.inspection.iteritems(), key=operator.itemgetter(1))[0]
        if record_type=="value":
            return max(self.value.iteritems(), key=operator.itemgetter(1))[0]

class HTTPRequestHandler(BaseHTTPRequestHandler):
    API_URL='/api/v1/'
    db = Database()

    def do_POST(self):
        if None != re.search(self.API_URL+'addrecord/*', self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.getheader('content-length'))
                data = cgi.parse_qs(self.rfile.read(length), keep_blank_value=1)
                record_type = self.path.split('/')[-2]
                record_id = self.path.split('/')[-1]
                self.db.save(record_id,record_type,json.loads(data))
                print "record %s is added successfully" % record_id
            else:
                data = {}
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        return

    def do_GET(self):
        if None != re.search(self.API_URL+'getrecord/*', self.path):
            record_id = self.path.split('/')[-1]
            record_type = self.path.split('/')[-2]

            if self.db.has_key(record_id, record_type):
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                result = self.db.get(record_id,record_type)
                self.wfile.write(json.dumps(result))

            else:
                self.send_response(400, 'Bad Request: record does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        else:
          self.send_response(403)
          self.send_header('Content-Type', 'application/json')
          self.end_headers()
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True

    def shutdown(self):
        self.socket.close()
        HTTPServer.shutdown(self)

class SimpleHttpServer():
    def __init__(self, ip, port):
        self.server = ThreadedHTTPServer((ip,port), HTTPRequestHandler)

    def start(self):
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def waitForThread(self):
        self.server_thread.join()

    def addRecord(self, record_id, record_type, jsonEncodedRecord):
        self.db.records[record_type][record_id] = jsonEncodedRecord


    def stop(self):
        self.server.shutdown()
        self.waitForThread()


if __name__=='__main__':
  parser = argparse.ArgumentParser(description='HTTP Server')
  parser.add_argument('port', type=int, help='Listening port for HTTP Server')
  parser.add_argument('ip', help='HTTP Server IP')
  args = parser.parse_args()

  server = SimpleHttpServer(args.ip, args.port)
  print 'HTTP Server Running...........'
  server.start()
  server.waitForThread()