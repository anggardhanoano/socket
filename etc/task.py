from datetime import datetime
import socket
import time
import requests
import json
from socket import gethostname


class Task(object):
    def __init__(self, client, thread, args):
        self.thread = thread
        self.client = client
        self.args = args
        print("task created")

    def work(self):
        pass


class LongTask(Task):

    url = 'http://data.fixer.io/api/latest?access_key=10974ad3908504c118fd3694e8fb8c39'
    rates = {}

    def convert(self, from_currency, to_currency, amount):
        data = requests.get(self.url).json()
        initial_amount = amount

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        return '{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency)

    def work(self):
        try:
            self.client.send(str.encode(
                'Please wait, converting the exchange rate.....'))
            self.client.send(str.encode(self.convert(
                self.args[0].decode().upper(), self.args[1].decode().upper(), int(self.args[2]))))
        except Exception as e:
            self.client.send(str.encode('fail to finish the task :('))
            self.client.send(str.encode(str(e)))
        finally:
            self.client.close()
            self.thread.stop()


class MediumTask(Task):

    def work(self):
        try:
            name, aliases, addresses = socket.gethostbyname_ex(self.args[0])
            self.client.send(str.encode(
                'Please wait, getting your requested host.....'))
            self.client.send(str.encode('Name: ' + name))
            self.client.send(str.encode('Addresses: ' + str(addresses)))
        except Exception as e:
            self.client.send(str.encode('fail to finish the task :('))
            self.client.send(str.encode(str(e)))
        finally:
            self.client.close()
            self.thread.stop()


class ShortTask(Task):

    def work(self):
        try:
            self.client.send(str.encode('The server is getting time....'))
            self.client.send(f'{datetime.now().isoformat()}\n'.encode('utf-8'))
        except Exception as e:
            self.client.send(str.encode('fail to finish the task :('))
            self.client.send(str.encode(str(e)))
        finally:
            self.client.close()
            self.thread.stop()


class PrimeTask(Task):

    def prime(self, n):
        prime_numbers = [2, 3]
        i = 3
        if(0 < n < 3):
            return '{} th Prime Number is :{}'.format(n, prime_numbers[n-1])
        elif(n > 2):
            while (True):
                i += 1
                status = True
                for j in range(2, int(i/2)+1):
                    if(i % j == 0):
                        status = False
                        break
                if(status == True):
                    prime_numbers.append(i)
                if(len(prime_numbers) == n):
                    break
            return '{} th Prime Number is :{}'.format(n, prime_numbers[n-1])
        else:
            return'Please Enter A Valid Number'

    def work(self):
        try:
            self.client.send(str.encode('Wait....'))
            self.client.send(str.encode(str(self.prime(int(self.args[0])))))
        except Exception as e:
            self.client.send(str.encode('fail to finish the task :('))
            self.client.send(str.encode(str(e)))
        finally:
            self.client.close()
            self.thread.stop()
